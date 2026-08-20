---
type: source-note
status: active
created: 2026-08-19
updated: 2026-08-20
vendor: "Waves"
product: "NS1"
tags:
  - music-production
  - plugin-source
---

# NS1 资料

- 对应知识卡：[[notes/音乐制作/插件/Waves/NS1|NS1]]
- 本机版本范围：12.7.0.209
- 访问日期：2026-08-20

## 来源记录

### Waves NS1 Noise Suppressor User Guide

- 类型：official-manual
- URL：https://www.waves.com/1lib/pdf/plugins/ns1-noise-suppressor.pdf
- 版本适用：NS1 通用；本机 Waves v12.7
- 可信度：high
- 支持的事实：实时自适应工作方式、单 Fader、Attenuation Meter 与 Mono/Stereo 组件。

### NS1 Noise Suppressor

- 类型：official-product
- URL：https://www.waves.com/plugins/ns1-noise-suppressor
- 版本适用：当前产品概览
- 可信度：medium-high
- 支持的事实：适用场景、实时自适应定位和官方手册入口。

## 证据边界

- 官方资料用于确认功能和控制语义；参数起点与信号链位置属于条件化工作流，必须在 S4 实测。
- 当前安装版本可能早于在线文档；任何新版专属功能在未回读本机界面前不得写成已验证。

## S4 本机验证

- Waves NS1 Stereo 12.7.0.209 VST3 在 Ableton Live 11.3.43 / 48 kHz 真实加载；A: Default Preset，Suppression 0/50/100，宿主 0 samples。
- 50 对固定人声整体约 -0.271 dB，对脉冲/稳定多音约 -2.808/-1.978 dB；100 对固定人声约 -13.141 dB，确认推子是内容自适应强度而非 dB 衰减读数。
- 报告：[[projects/p1-plugin-knowledge-base/validation/reports/29b6d9504a55--Waves-NS1|NS1 L3 验证]]；量化：`projects/p1-plugin-knowledge-base/validation/results/29b6d9504a55--composite-ns1-suppression.json`。
- Composite 没有专门叠加已知噪声；本轮不声称白/粉/风扇噪声改善量，也不声称 0% 逐比特透明。
- 未验证 Mono、VST2、其它采样率、内部左右联动、压缩前后顺序或盲听。

## 反向链接

- [[projects/P1 插件适配知识库]]
