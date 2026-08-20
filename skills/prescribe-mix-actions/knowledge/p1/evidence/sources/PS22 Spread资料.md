---
type: source-note
status: active
created: 2026-08-20
updated: 2026-08-20
vendor: "Waves"
product: "PS22 Spread"
tags: [music-production, plugin-source]
---

# PS22 Spread 资料

- 对应知识卡：[[notes/音乐制作/插件/Waves/PS22 Spread|PS22 Spread]]
- 本机版本范围：12.7.0.209
- 访问日期：2026-08-20

## 来源记录

### PS22 Stereo Maker 产品页

- 类型：official-product
- URL：https://www.waves.com/plugins/ps22-stereo-maker
- 版本适用：PS22 产品家族；本机 V12
- 可信度：high
- 支持的事实：Mono-to-Stereo、Stereo 增强与声像重平衡定位；家族包含 Spread 与 Split。

### PS22 Stereo Maker User Guide

- 类型：official-manual
- URL：https://assets.wavescdn.com/pdf/plugins/ps22-stereo-maker.pdf
- 版本适用：PS22 用户指南；与本机 V12 控件名称实测一致
- 可信度：high
- 支持的事实：Spread 0–1.2；Freq 32 Hz–16 kHz；LFSpread 低频相对宽度；标准版 Sweeps 2–22、(10) 版 2–10；FCenter/FDensity/Tweak；低 Sweeps 定位、高 Sweeps 扩散；高 Sweeps/FDensity/Spread 的梳状染色风险；Width/Rotation；M/S 表头；Spread=0.6 时 Mono 频响波纹约 ±0.67 dB；线性、非时变、高阶低 Q IIR 交叉馈送和避免时间延迟型伪立体声的设计目标。

## 本机宿主观察

- 搜索结果：Split、Spread、Spread(10)、XSplit 各有 Mono/Stereo 与 Stereo 组件。
- 本轮选标准 `PS22 Spread Stereo`，不是低 DSP 的 `(10)` 或更戏剧化的 Split/XSplit。
- 默认：Input 0.0、Width 1.00、Rotation 0.0、L/R、No Clip、Spread 0.60、Freq 251、LFSpread 1.50、FCenter 724、FDensity 0、Tweak 0、Sweeps 16；Preset=`3-multitone_48k`。
- Ableton 48 kHz：`Latency: 2 samples (0.042 ms)`。
- 快照：`validation/host/snapshots/0072a637f389--FabFilter-Saturn-2 Project/2035ec8dd8df--Waves-PS22-Spread.als`。
- 渲染/量化/报告：`validation/renders/2035ec8dd8df--impulse--default-spread-full.wav`；`validation/results/2035ec8dd8df--impulse-default-spread.json`；`validation/reports/2035ec8dd8df--Waves-PS22-Spread.md`。

## 证据边界

- 官方资料确认算法、控制、变体与工作流；本机参数、组件与 PDC 来自 GUI 实测。
- 默认脉冲只覆盖 48 kHz、VST3 Stereo、当前默认状态和三个宽带脉冲，不直接复现稳态 Mono 频响波纹，也不覆盖连续人声、其它参数、VST2/Mono 或不同采样率。
- 实测 Mono Fold RMS -0.677117 dB 与手册 Spread=0.6 的 ±0.67 dB 数值接近，但定义不同，不能写成直接验证了官方频响波纹。

## 反向链接

- [[projects/P1 插件适配知识库]]

