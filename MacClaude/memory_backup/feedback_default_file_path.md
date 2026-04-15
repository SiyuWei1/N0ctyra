---
name: 文件默认保存路径
description: 用户要求创建的文件默认保存到 N0ctyra 仓库的 MacClaude 文件夹
type: feedback
originSessionId: fbd8f6f3-9043-478b-8ad7-c3805081202e
---
创建文件时默认保存到 `/Users/n0cytra/N0ctyra/MacClaude/`（即 `SiyuWei1/N0ctyra` 仓库的 `MacClaude/` 目录）。

**Why:** 用户已将本地仓库从 OneDrive 的 `SIyu W/` 移到 `/Users/n0cytra/N0ctyra/`，并删除了原 `SIyu W/` 文件夹（2026-04-15）。所有文件通过 git 仓库管理和同步。

**How to apply:** 除非用户指定其他路径，所有新建文件放到 `/Users/n0cytra/N0ctyra/MacClaude/` 下（可按需建子文件夹分类）。创建后执行 `cd /Users/n0cytra/N0ctyra && git add . && git commit -m "..." && git push` 同步到远程。
