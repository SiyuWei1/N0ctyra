# N0ctyra

Personal repository for managing Claude agent configurations, memory backups, and project files across devices.

## Structure

```
N0ctyra/
├── MacClaude/        # macOS Claude (Tyra) working directory
│   ├── memory_backup/   # Persistent memory & session backups
│   └── SiyuW_backup/    # Additional file backups
├── WinClaude/        # Windows Claude configuration & project files
│   ├── MEMORY.md
│   ├── user_profile.md
│   ├── project_ist140_concepts.md
│   └── project_meteo1n.md
└── hermes agent/     # Hermes agent configuration
```

## Overview

### MacClaude
The working directory for Tyra (Claude) on macOS. All files created or updated locally are backed up here and synced to git for cross-device access and version history.

**Default save path:** `~/N0ctyra/MacClaude/`

**Memory backup:** Files in `~/.claude/projects/-Users-n0cytra/memory/` are synced to `MacClaude/memory_backup/` on every change.

### WinClaude
Windows-side Claude configuration, user profiles, and project files (IST 140 concepts, Meteo1n project, etc.).

### Hermes Agent
Configuration files for the Hermes agent runtime.

## Sync Policy

> **Important:** This repo is the source of truth for cross-device sync and disaster recovery.

- All new/modified files are committed and pushed after creation or change
- Memory files are backed up on every update
- Only write to `MacClaude/` — other directories are read-only

## Git Workflow

```bash
cd ~/N0ctyra
git add .
git commit -m "describe changes"
git push
```

## Contact

Maintained by **N0ctyra** — reach out on Discord or WeChat.
