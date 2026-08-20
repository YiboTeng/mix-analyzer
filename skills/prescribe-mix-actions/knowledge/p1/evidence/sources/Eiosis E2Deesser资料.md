---
type: source-note
status: active
created: 2026-08-20
updated: 2026-08-20
vendor: "Eiosis"
product: "Eiosis E2Deesser"
tags:
  - music-production
  - plugin-source
---

# Eiosis E2Deesser 资料

- 对应知识卡：[[notes/音乐制作/插件/Eiosis/Eiosis E2Deesser|Eiosis E2Deesser]]
- 本机版本范围：1.0.9.3
- 访问日期：2026-08-20

## 来源记录

### Eiosis E2Deesser User Guide

- 类型：official-manual
- URL：https://downloads.eiosis.com/E2Deesser/Eiosis_E2Deesser_User_Guide.pdf
- 版本适用：E2Deesser 核心版本；重定向和当前文档状态需留档
- 可信度：high
- 支持的事实：Mode 用途与禁忌、Auto、Smooth、Gain、Dry/Wet 和检测工作流。

## 证据边界

- 官方资料用于确认功能和控制语义；参数起点与信号链位置属于条件化工作流。
- 当前安装版本可能早于在线文档；任何新版专属功能在未回读本机界面前不得写成已验证。

## 本机 L3 验证

- 宿主/实例：Ableton Live 11.3.43，48 kHz，E2Deesser 1.0.9.3 VST3。
- UI 回读：Solo Vocal、Back Vocals、Voice Over、Guitar Squeaks、Overheads、Stereo/M-S/Mid Mastering；Sensitivity、Amount、Auto、Smooth、Gain、Dry/Wet、Voiced/Sibilants EQ、Bypass。
- 默认值：Sensitivity、Amount、Auto、Smooth、Dry/Wet 均 50%，Gain 0 dB；宿主延迟 `720 samples / 15 ms`。
- 受控结果：Solo 默认对三个稀疏事件约 -2.449 dB；Voice Over 相对 Solo 再低 -0.676 dB；Auto 50→100（Smooth 固定 50）约 +0.063 dB；Smooth 50→100（Auto 固定 50）约 -0.316 dB。
- 证据：[[projects/p1-plugin-knowledge-base/validation/reports/0188bc583c26--Eiosis-E2Deesser|E2Deesser L3 验证]]、[结果 JSON](../../../../projects/p1-plugin-knowledge-base/validation/results/0188bc583c26--composite-e2deesser-mode-auto-smooth.json)。
- 边界：夹具不是带音素标签的真实语音语料；默认 Dry/Wet 50%；未测 Back Vocals/M-S、Idle Threshold、多档曲线、VST2 或其它采样率。

## 反向链接

- [[projects/P1 插件适配知识库]]
