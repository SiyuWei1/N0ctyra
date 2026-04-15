## 自建VPN详细教程

---

### 第一步：购买VPS服务器

**推荐服务商（按易用性排序）：**

| 服务商            | 最低价      | 优点          |
| -------------- | -------- | ----------- |
| Vultr          | $3.5/月   | 按小时计费，随时换IP |
| Bandwagon（搬瓦工） | $49.99/年 | CN2线路，对中国优化 |
| DigitalOcean   | $4/月     | 界面简洁，稳定     |
| Racknerd       | $10+/年   | 便宜          |

**购买时的选择：**
- **系统**：Ubuntu 22.04 或 Debian 12（教程最多）
- **配置**：最低档就够（1核 512MB-1GB内存）
- **地区**：美西（洛杉矶/圣何塞）延迟较低；日本/新加坡也不错
- 付款后你会收到 **IP地址、root密码、SSH端口**

---

### 第二步：连接到服务器

**macOS 自带终端就行：**

```bash
ssh root@你的服务器IP
```

输入密码（输入时不会显示字符，正常现象），回车即可登录。

首次连接会问 `Are you sure you want to continue connecting?`，输入 `yes`。

---

### 第三步：选择协议并安装

以下介绍三种主流方案，**任选其一**：

---

#### 方案A：WireGuard（推荐新手，最简单）

```bash
# 下载一键安装脚本
curl -O https://raw.githubusercontent.com/angristan/wireguard-install/master/wireguard-install.sh

# 给执行权限
chmod +x wireguard-install.sh

# 运行安装
./wireguard-install.sh
```

安装过程中会问你几个问题，**全部按回车用默认值就行**，最后会：
- 生成一个配置文件（如 `wg0-client-phone.conf`）
- 终端上显示一个**二维码**

**客户端使用：**
- macOS/iOS/Android：下载 **WireGuard** 官方App
- 手机：直接扫二维码导入
- 电脑：把配置文件下载到本地，导入WireGuard客户端

```bash
# 把配置文件下载到本地（在本地终端运行，不是服务器上）
scp root@你的服务器IP:~/wg0-client-phone.conf ~/Downloads/
```

**添加更多设备：**
```bash
./wireguard-install.sh
# 选 "Add a new client"
```

---

#### 方案B：Xray (VLESS + Reality)（推荐，抗封锁最强）

```bash
# 安装 Xray
bash -c "$(curl -L https://github.com/XTLS/Xray-install/raw/main/install-release.sh)" @ install
```

然后编辑配置文件：

```bash
nano /usr/local/etc/xray/config.json
```

写入以下内容（替换标注部分）：

```json
{
  "inbounds": [
    {
      "port": 443,
      "protocol": "vless",
      "settings": {
        "clients": [
          {
            "id": "替换成你的UUID",
            "flow": "xtls-rprx-vision"
          }
        ],
        "decryption": "none"
      },
      "streamSettings": {
        "network": "tcp",
        "security": "reality",
        "realitySettings": {
          "dest": "www.microsoft.com:443",
          "serverNames": ["www.microsoft.com"],
          "privateKey": "替换成你的私钥",
          "shortIds": ["abcd1234"]
        }
      }
    }
  ],
  "outbounds": [
    {
      "protocol": "freedom"
    }
  ]
}
```

**生成所需的UUID和密钥：**

```bash
# 生成 UUID
xray uuid

# 生成密钥对（会输出 PrivateKey 和 PublicKey）
xray x25519
```

把生成的值填入配置文件，然后：

```bash
# 启动 Xray
systemctl restart xray
systemctl enable xray

# 检查是否运行正常
systemctl status xray
```

**客户端：**
- iOS：Shadowrocket（$2.99，需美区Apple ID）
- macOS：V2rayU 或 V2rayN
- Android：v2rayNG

客户端添加 VLESS 节点，填入：地址、端口443、UUID、flow选vision、security选reality、SNI填 www.microsoft.com、公钥填你生成的 PublicKey。

---

#### 方案C：Shadowsocks（经典方案）

```bash
# 一键安装
bash <(curl -sL https://raw.githubusercontent.com/teddysun/shadowsocks_install/master/shadowsocks-all.sh)
```

- 选 **shadowsocks-libev**
- 设置密码
- 端口默认或自定义
- 加密方式选 **aes-256-gcm** 或 **chacha20-ietf-poly1305**

安装完成后会显示连接信息。

---

### 第四步：防火墙放行端口

```bash
# 查看防火墙状态
ufw status

# 放行端口（根据你选的方案）
ufw allow 51820/udp    # WireGuard 默认端口
ufw allow 443/tcp      # Xray
ufw allow 你的SS端口    # Shadowsocks

# 启用防火墙
ufw enable
```

也要去VPS服务商的网页控制面板检查安全组/防火墙规则，确保端口开放。

---

### 第五步：基础安全加固（建议做）

```bash
# 更新系统
apt update && apt upgrade -y

# 开启 BBR 加速（提升速度）
echo "net.core.default_qdisc=fq" >> /etc/sysctl.conf
echo "net.ipv4.tcp_congestion_control=bbr" >> /etc/sysctl.conf
sysctl -p

# 验证 BBR 是否开启
lsmod | grep bbr
```

---

### 常见问题

**Q：IP被封了怎么办？**
- Vultr：删掉服务器，重新创建一个（换IP）
- 搬瓦工：后台有换IP功能（可能收费 $8）

**Q：速度慢？**
- 开启 BBR（上面已写）
- 换节点地区（美西/日本通常更快）
- 升级VPS配置

**Q：怎么判断搭建成功？**
```bash
# 在服务器上检查端口是否监听
ss -tlnp | grep 你的端口
```

---

### 方案对比总结

| | WireGuard | Xray VLESS | Shadowsocks |
|--|-----------|------------|-------------|
| 难度 | 最简单 | 中等 | 简单 |
| 抗封锁 | 一般 | 最强 | 中等 |
| 速度 | 最快 | 快 | 快 |
| 适合 | 海外用户/轻度使用 | 中国大陆用户 | 通用 |

**如果你在中国大陆使用，强烈推荐方案B（Xray VLESS + Reality）**，抗封锁能力最好。其他地区用 WireGuard 最省事。
