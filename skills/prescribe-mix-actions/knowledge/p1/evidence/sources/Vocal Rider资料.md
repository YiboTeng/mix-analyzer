---
type: source-note
status: active
created: 2026-08-19
updated: 2026-08-20
vendor: "Waves"
product: "Vocal Rider"
tags:
  - music-production
  - plugin-source
---

# Vocal Rider 资料

- 对应知识卡：[[notes/音乐制作/插件/Waves/Vocal Rider|Vocal Rider]]
- 本机版本范围：12.7.0.209
- 访问日期：2026-08-19

## 来源记录

### Waves Vocal Rider User Guide

- 类型：official-manual
- URL：https://assets.wavescdn.com/pdf/plugins/vocal-rider.pdf
- 版本适用：Vocal Rider 通用；本机 v12.7
- 可信度：high
- 支持的事实：Target、Sensitivity、Attack、Music Sensitivity、Range、Idle、Sidechain 与 Automation。

### Vocal Rider In Depth

- 类型：official-deep-dive
- URL：https://www.waves.com/vocal-rider-in-depth
- 版本适用：Vocal Rider Automation 工作流
- 可信度：high
- 支持的事实：写入、读取和编辑 Rider Automation 的步骤与警告。

### Dynamics Processing Techniques for Better Vocals

- 类型：official-tutorial
- URL：https://www.waves.com/dynamics-processing-techniques-for-better-vocals
- 版本适用：当前官方工作流
- 可信度：medium-high
- 支持的事实：Target、Fast/Slow 与 Range 的条件化使用及避免过度动作。

## 证据边界

- 官方资料用于确认功能和控制语义；参数起点与信号链位置属于条件化工作流，必须在 S4 实测。
- 当前安装版本可能早于在线文档；任何新版专属功能在未回读本机界面前不得写成已验证。

## 本机 S4 证据

- 2026-08-20 在 Ableton Live 11.3.43 / 48 kHz 中加载 Waves `Vocal Rider Stereo` 12.7.0.209 VST3；宿主报告 0 samples。
- 默认可见状态与 Fast/Slow 独立导出、工程快照和 50 ms 窗电平轨迹保存在 [[projects/p1-plugin-knowledge-base/validation/reports/b6c750f3ccec--Waves-Vocal-Rider|Vocal Rider L3 验证]]。
- 默认与显式 Slow 音频近似重合，确认默认开关为 Slow；Fast 相邻动作更大。无音乐侧链、Automation Off，因此官方的 Sidechain 与 Write/Read 工作流仍只算文档事实，未算本机实测。

## 反向链接

- [[projects/P1 插件适配知识库]]
