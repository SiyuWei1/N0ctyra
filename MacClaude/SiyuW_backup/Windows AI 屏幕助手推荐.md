# Windows 上类似 Clicky 的 AI 屏幕助手

原项目 [farzaa/clicky](https://github.com/farzaa/clicky) 只支持 macOS（Swift 原生）。以下是 Windows 上可用的替代方案。

## 最接近 Clicky 的（直接移植版）

- **[tekram/clicky-windows](https://github.com/tekram/clicky-windows)** — 社区做的 Windows 版 Clicky，Electron 实现。功能一致：
  - 截屏 + Claude Vision 看屏幕
  - 按键说话（push-to-talk）+ 实时转录
  - TTS 语音回复（ElevenLabs 或 Windows SAPI）
  - 动画光标叠加层，指向 Claude 提到的 UI 元素
  - 推荐先试这个

## 其他类似的开源屏幕 AI 助手（都支持 Windows）

- **[PyGPT](https://pygpt.net/)** — 跨平台桌面 AI 助手，支持视觉、语音、Agent
- **[Screenpipe](https://github.com/screenpipe/screenpipe)** — Rust 写的，持续录屏 + AI 记忆，100% 本地运行
- **[Jarvis Voice Assistant](https://github.com/Julian-Ivanov/jarvis-voice-assistant)** — Claude Vision + 语音 + 屏幕截图，双击启动
- **[pywinassistant](https://github.com/a-real-ai/pywinassistant)** — 用自然语言操控 Windows GUI
- **[Windows-Use](https://github.com/CursorTouch/Windows-Use)** — AI Agent 直接操作 Windows 界面

## 建议

- 想要 Clicky 那种"cursor 旁边的 AI 老师"体验 → 装 `tekram/clicky-windows`
- 想要更强的屏幕理解 + 本地隐私 → 用 Screenpipe
