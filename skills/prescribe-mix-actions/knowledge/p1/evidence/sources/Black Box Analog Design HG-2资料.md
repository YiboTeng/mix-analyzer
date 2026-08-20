---
type: source-note
status: active
created: 2026-08-20
updated: 2026-08-20
vendor: "Plugin Alliance"
product: "Black Box Analog Design HG-2"
tags:
  - music-production
  - plugin-source
---

# Black Box Analog Design HG-2 资料

- 对应知识卡：[[notes/音乐制作/插件/Plugin Alliance/Black Box Analog Design HG-2|Black Box Analog Design HG-2]]
- 本机版本范围：1.3.0.0
- 访问日期：2026-08-20

## 来源记录

### Black Box HG-2 Manual

- 类型：official-manual
- URL：https://files.plugin-alliance.com/products/black_box_analog_design_hg-2/black_box_analog_design_hg-2_manual.pdf
- 版本适用：HG-2 核心；本机旧版需回读
- 可信度：high
- 支持的事实：串/并联管级和控制。

### Plugin Alliance HG-2

- 类型：official-product
- URL：https://www.plugin-alliance.com/products/hg-2
- 版本适用：当前页，仅核核心设计
- 可信度：medium
- 支持的事实：Pentode/Triode、Density、Parallel、Calibration、Air、Mix。

## 证据边界

- 官方资料用于确认功能和控制语义；参数起点与信号链位置属于条件化工作流，必须在 S4 实测。
- 当前安装版本可能早于在线文档；任何新版专属功能在未回读本机界面前不得写成已验证。

## S4 本机复核

- 真实宿主：Ableton Live 11.3.43；本机组件为 HG-2 1.3.0.0 VST3 原版，不是 HG-2MS。
- 默认界面实际可见 Calibration/FLAT、Density、Input、Mix、Saturation、Pentode、Triode、Output、Air Amount、Alt Tube、Air 与 Bypass；无数字显示的旋钮只记录视觉默认位置。
- 宿主报告延迟 32 samples / 0.67 ms；固定三电平脉冲默认渲染的峰值增益为 -1.170/-0.925/-0.789 dB，三次局部峰值均 0-sample 对齐。
- 量化结果与完整边界见 [[projects/p1-plugin-knowledge-base/validation/reports/1994a7f7d443--Plugin-Alliance-Black-Box-HG-2|HG-2 默认路径 L3 验证]]；本机复核只证明旧版默认行为，不证明当前在线产品页的所有新功能。

## 反向链接

- [[projects/P1 插件适配知识库]]
