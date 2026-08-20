---
type: source-note
status: active
created: 2026-08-20
updated: 2026-08-20
vendor: "Waves"
product: "CLA-76"
tags:
  - music-production
  - plugin-source
---

# CLA-76 资料

- 对应知识卡：[[notes/音乐制作/插件/Waves/CLA-76|CLA-76]]
- 本机版本范围：12.7.0.209
- 访问日期：2026-08-20

## 来源记录

### Waves CLA-76 User Guide

- 类型：official-manual
- URL：https://www.waves.com/1lib/pdf/plugins/cla-76-compressor-limiter.pdf
- 版本适用：CLA-76 核心与现代扩展；Mix/Trim 只按新版资料记录，不外推到本机 v12
- 可信度：high
- 支持的事实：控制范围、Bluey/Blacky、Analog、比例，以及新版 Mix/Trim 的版本边界。

### 4 Tips to Mix Aggressive Rap Vocals

- 类型：official-guide
- URL：https://www.waves.com/tips-mix-aggressive-rap-vocals
- 版本适用：条件化 Rap 工作流
- 可信度：medium
- 支持的事实：快速 Attack 6–7 的官方应用示例。

## 证据边界

- 官方资料用于确认功能和控制语义；参数起点与信号链位置属于条件化工作流，必须在 S4 实测。
- 本机 12.7.0.209 `CLA-76 Stereo` VST3 已在 Ableton Live 11.3.43 回读：面板只有 Input、Output、Attack、Release、Ratio、Meter、Analog 与 Revision；没有新版 Mix/Trim。任何新版专属功能不得写成当前实例功能。
- 本机默认宿主预置 `A: Start Me Up` 实见 Bluey、Input 30、Output 18、Attack 3、Release 4、4:1、GR、Analog Off；宿主在 48 kHz 报告 0 samples。
- S4 只把 Attack 3 改为 6.99（名义 7）；五个隔离瞬态相对 Attack 3 进一步削低约 0.88–1.71 dB，支持“高数字更快”的方向性，但不是绝对硬件时间标定。

## 本机可复现证据

- 工程快照：`projects/p1-plugin-knowledge-base/validation/host/snapshots/0072a637f389--FabFilter-Saturn-2 Project/47e12f69eb3c--Waves-CLA-76.als`
- 旁路、默认与 Attack 7 渲染：`projects/p1-plugin-knowledge-base/validation/renders/47e12f69eb3c--dynamics--*.wav`
- 量化结果：`projects/p1-plugin-knowledge-base/validation/results/47e12f69eb3c--dynamics-compressor.json`
- 测量脚本：`projects/p1-plugin-knowledge-base/validation/scripts/analyze_compressor.py`
- 验证报告：[[projects/p1-plugin-knowledge-base/validation/reports/47e12f69eb3c--Waves-CLA-76|CLA-76 L3 验证]]

## 反向链接

- [[projects/P1 插件适配知识库]]
