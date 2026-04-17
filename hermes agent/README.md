# Hermes Agent

Multi-platform AI agent bot — connects Discord and WeChat, powered by Claude.

## Platforms

| Platform | Status | Details |
|----------|--------|---------|
| Discord  | ✅ Connected | Home channel configured |
| WeChat   | ✅ Connected | iLink Bot API (`b28b5525a78d@im.bot`) |

## Architecture

- **Runtime:** Python bot running on a Hong Kong VPS (Linux)
- **Brain:** Claude API (MiniMax-M2.7 provider)
- **Voice:** Faster-Whisper STT + `discord.py[voice]` / native TTS
- **Deployment:** `tmux` session for persistent uptime

## Key Files

- `run_agent.py` — Main bot logic (on VPS, not in this repo)
- Config: `config.yaml` — STT settings, API keys, platform tokens

## Message Delivery Rules

### WeChat
- Single message limit: **2000 characters**
- Burst sending risk: Platform rate limits can silently drop messages
- **Rule:** Keep replies to 2–3 consolidated messages max; never flood

### Discord
- Standard message limits apply
- Supports media attachments, voice messages

## Operational Notes

- Bot runs independently of Mac — no local presence required
- Files stored on VPS at `~/hermes/files/`
- WeChat messages flow through iLink Bot API bridge
- STT uses faster-whisper for voice recognition in Discord voice channels

## Related

- **Repository:** [SiyuWei1/N0ctyra](https://github.com/SiyuWei1/N0ctyra)
- **Owner:** N0ctyra
