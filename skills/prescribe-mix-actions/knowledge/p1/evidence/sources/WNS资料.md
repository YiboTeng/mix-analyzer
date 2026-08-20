---
type: source-note
status: active
created: 2026-08-20
updated: 2026-08-20
vendor: "Waves"
product: "WNS"
tags:
  - music-production
  - plugin-source
---

# WNS 资料

- 对应知识卡：[[notes/音乐制作/插件/Waves/WNS|WNS]]
- 本机版本：12.7.0.209 VST3 Stereo
- 访问日期：2026-08-20

## 来源记录

### Waves WNS Noise Suppressor User Guide

- 类型：official-manual
- URL：https://assets.wavescdn.com/pdf/plugins/wns-noise-suppressor.pdf
- 可信度：high
- 支持事实：六段动态抑制、无需 Noise Print、Threshold/Gain/Smoothing/频带边界、Suggest、零延迟、置于其它动态之前。

### WNS Noise Suppressor Product Page

- 类型：official-product
- URL：https://www.waves.com/plugins/wns-noise-suppressor
- 可信度：medium-high
- 支持事实：对白宽带降噪定位和实时工作流。

### Waves Plugin Latency

- 类型：official-support
- URL：https://www.waves.com/support/tech-specs/plugin-latency
- 可信度：high
- 支持事实：当前 Native 宿主延迟表；本机 Ableton 另回读 0 samples。

## S4 本机验证

- WNS Stereo 12.7.0.209 VST3 在 Ableton Live 11.3.43 / 48 kHz 加载，0 samples。
- 默认六段 0 dB 电平中性；宽带压力状态对固定人声约 -13.91 dB，证明过量会移除有效节目。
- 报告：[[projects/p1-plugin-knowledge-base/validation/reports/6756edefac77--Waves-WNS|WNS L3 验证]]。
- 本轮无校准噪声床，不声称 SNR 改善；WNS 不覆盖专用 De-plosive。

## 反向链接

- [[projects/P1 插件适配知识库]]

