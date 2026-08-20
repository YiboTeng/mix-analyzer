---
type: source-note
status: active
created: 2026-08-20
updated: 2026-08-20
vendor: "Plugin Alliance"
product: "Maag EQ4"
tags:
  - music-production
  - plugin-source
---

# Maag EQ4 资料

- 对应知识卡：[[notes/音乐制作/插件/Plugin Alliance/Maag EQ4|Maag EQ4]]
- 本机版本范围：1.3.0.0 | 1.9.0.0
- 访问日期：2026-08-20

## 来源记录

### Brainworx Maag EQ4 Manual

- 类型：official-manual
- URL：https://files.plugin-alliance.com/products/maag_eq4/maag_eq4_manual.pdf
- 版本适用：EQ4 核心固定频段与 Air Band；旧版界面边界需本机回读
- 可信度：high
- 支持的事实：固定频段、Air 频率、Level Trim 与频段交互。

### Plugin Alliance Maag EQ4

- 类型：official-product
- URL：https://www.plugin-alliance.com/products/eq4
- 版本适用：当前产品页；仅用于核心设计，不向旧版本倒灌新附加功能
- 可信度：medium
- 支持的事实：Air Band 定位、固定频段和音乐性用途。

## 证据边界

- 官方资料用于确认功能和控制语义；参数起点与信号链位置属于条件化工作流，必须在 S4 实测。
- 当前安装版本可能早于在线文档；任何新版专属功能在未回读本机界面前不得写成已验证。

## 本机验证补充

- Ableton Live 11.3.43 / 48 kHz 中真实加载的旧版 VST3 界面只有固定五段、Air 频率、Air Gain 与 Level Trim；未见 TMT、Mono Maker 等新版附加项。
- 宿主报告 0 samples。Air 20 kHz/+3 dB 相对所有增益为 0 的实例，在稳定多音上呈随频率总体上升的宽缓提升；+5 dB 已使当前夹具峰值触及约 0 dBFS。
- 本机测量与适用边界见 [[projects/p1-plugin-knowledge-base/validation/reports/e98173f7f4df--Plugin-Alliance-Maag-EQ4|Maag EQ4 L3 验证]]。它补充安装实例行为，不替代官方手册，也不外推到其它版本。

## 反向链接

- [[projects/P1 插件适配知识库]]
