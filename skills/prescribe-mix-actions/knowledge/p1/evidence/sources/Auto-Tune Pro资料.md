---
type: source-note
status: active
created: 2026-08-19
updated: 2026-08-20
vendor: "Antares"
product: "Auto-Tune Pro"
tags:
  - music-production
  - plugin-source
---

# Auto-Tune Pro 资料

- 对应知识卡：[[notes/音乐制作/插件/Antares/Auto-Tune Pro|Auto-Tune Pro]]
- 本机版本范围：10.0.0
- 访问日期：2026-08-19

## 来源记录

### Auto-Tune Pro X User Guide 10.0

- 类型：official-manual
- URL：https://antares-web-frontend.sfo3.cdn.digitaloceanspaces.com/documentation/pdfs/Auto-Tune_Pro_X_User_Guide_10.0.pdf
- 版本适用：Auto-Tune Pro X 10.0，与本机 10.0.0 直接对应
- 可信度：high
- 支持的事实：Auto/Graph Mode、Key/Scale、Retune Speed、Flex-Tune、Humanize、MIDI 与视图的官方定义。

### AutoTune 2026 FAQ

- 类型：official-support
- URL：https://help.antarestech.com/hc/en-us/articles/42855736822932-AutoTune-2026-FAQ
- 版本适用：新版工作流参考；不得把新版专属功能写回 v10
- 可信度：medium
- 支持的事实：自然与明显调音的参数关系、Humanize 与 Flex-Tune 的条件化使用顺序。

## 证据边界

- 官方资料用于确认功能和控制语义；参数起点与信号链位置属于条件化工作流。
- 当前安装版本可能早于在线文档；任何新版专属功能在未回读本机界面前不得写成已验证。

## 本机 L3 验证

- 宿主/实例：Ableton Live 11.3.43，48 kHz，Auto-Tune Pro 10.0.0 VST3。
- 固定状态：Auto/Modern、Alto-Tenor、C Chromatic、Tracking 50、Flex-Tune/Humanize/Natural Vibrato 0、Formant 100、Mix 100；单变量 Retune Speed 20→0。
- 491 个共同有声帧：距最近半音绝对偏差中位 `6.115`（旁路）/`4.160`（Retune20）/`0.844 cents`（Retune0）；±5 cents比例 `40.1%/63.7%/88.0%`。
- 宿主延迟：`2670 samples / 55.6 ms`；固定人声段三态 RMS 约 -25.94 dBFS。
- 证据：[[projects/p1-plugin-knowledge-base/validation/reports/7b4d8c94b025--Antares-Auto-Tune-Pro|Auto-Tune Pro L3 验证]]、[结果 JSON](../../../../projects/p1-plugin-knowledge-base/validation/results/7b4d8c94b025--fixed-vocal-chromatic-retune-speed.json)。
- 边界：Chromatic 最近半音不是歌曲目标音；未测 Flex-Tune、Humanize、Tracking、Classic、Graph、Formant/Throat、低延迟选项或其它采样率。

## 反向链接

- [[projects/P1 插件适配知识库]]
