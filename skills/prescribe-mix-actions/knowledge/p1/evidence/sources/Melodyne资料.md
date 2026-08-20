---
type: source-note
status: active
created: 2026-08-19
updated: 2026-08-20
vendor: "Celemony"
product: "Melodyne"
tags:
  - music-production
  - plugin-source
---

# Melodyne 资料

- 对应知识卡：[[notes/音乐制作/插件/Celemony/Melodyne|Melodyne]]
- 本机版本范围：5.4.1
- 访问日期：2026-08-19

## 来源记录

### Melodyne 5 Reference Guide

- 类型：official-manual
- URL：https://helpcenter.celemony.com/M5/pdf/melodyneEditor5/en?env=dawsWithoutAra
- 版本适用：Melodyne 5；本机 5.4.1
- 可信度：high
- 支持的事实：Detection、算法、Pitch/Timing/Formant/Amplitude 工具、Note Inspector 与编辑边界。

### Correct Pitch Macro

- 类型：official-help
- URL：https://helpcenter.celemony.com/M5/doc/melodyneStudio5/en/M5tour_MacroPitch?env=dawsWithAra
- 版本适用：Melodyne 5，具体 Edition 可能限制功能
- 可信度：high
- 支持的事实：Pitch Center 与 Pitch Drift 的独立宏控制及手工编辑保护逻辑。

### Working with ARA

- 类型：official-help
- URL：https://helpcenter.celemony.com/M5/doc/melodyneStudio5/en/M5tour_WorkingWithARA
- 版本适用：Melodyne 5 + ARA DAW，包括 Studio One 示例
- 可信度：high
- 支持的事实：ARA 无需 Transfer、跟随 DAW 片段与 Track/Clip 工作流。

## 证据边界

- 官方资料用于确认功能和控制语义；参数起点与信号链位置属于条件化工作流，必须在 S4 实测。
- 当前安装版本可能早于在线文档；任何新版专属功能在未回读本机界面前不得写成已验证。

## 本机 S4 证据

- 2026-08-20 在 Ableton Live 11.3.43 / 48 kHz 中加载 Melodyne 5.4.1 VST3；界面明确显示 `melodyne studio`，宿主报告 0 samples。
- 完成约 7 秒实时 Transfer、全部音符选择和 Correct Pitch Macro：Pitch Center 100%、Pitch Drift 0%、Snap to chord scale Off；工程快照与量化见 [[projects/p1-plugin-knowledge-base/validation/reports/394f47cfa81e--Celemony-Melodyne|Melodyne L3 验证]]。
- 本轮没有 ARA；官方 ARA 工作流仍是文档事实。自动检测 D Minor 未用于吸附，不能把调性建议或外部 F0 指标写成旋律正确性。

## 反向链接

- [[projects/P1 插件适配知识库]]
