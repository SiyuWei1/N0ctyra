---
name: 所有文件/记忆需备份到 MacClaude
description: 所有新建或更新的文件（包括 memory）都要同步备份到 N0ctyra 仓库的 MacClaude 目录
type: feedback
originSessionId: fbd8f6f3-9043-478b-8ad7-c3805081202e
---
每次在本地创建、修改任何文件（包括 `~/.claude/projects/-Users-n0cytra/memory/` 下的 memory 文件），都要同步备份一份到 `/Users/n0cytra/OneDrive - The Pennsylvania State University/SIyu W/N0ctyra/MacClaude/` 对应位置，并 `git commit/push` 推到远程仓库。

- memory 文件 → 备份到 `MacClaude/memory_backup/`
- 其他新建文件 → 直接放到 `MacClaude/` 下（按需分类建子文件夹）

**Why:** 用户希望通过 git 仓库保留 Claude 产出的所有内容和记忆状态，便于跨设备同步、版本追踪、防丢失。

**How to apply:**
1. 任何写文件操作后，检查是否已同步到 MacClaude。
2. memory 文件有更新（新增/修改/删除）时，同步覆盖 `MacClaude/memory_backup/`。
3. 操作完成后执行 `cd <repo> && git add . && git commit -m "..." && git push`。
4. 首次初始化备份已于 2026-04-15 完成。
