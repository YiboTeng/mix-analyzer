---
type: source-note
status: active
created: 2026-08-20
updated: 2026-08-20
vendor: "Waves"
product: "DeBreath"
tags:
  - music-production
  - plugin-source
---

# DeBreath 资料

- 对应知识卡：[[notes/音乐制作/插件/Waves/DeBreath|DeBreath]]
- 本机版本范围：12.7.0.209
- 访问日期：2026-08-20

## 来源记录

### Waves DeBreath User Manual

- 类型：official-manual
- URL：https://assets.wavescdn.com/pdf/plugins/debreath.pdf
- 版本适用：DeBreath 通用；本机 Waves v12.7
- 可信度：high
- 支持的事实：模板匹配检测；Breath/Energy 双阈值；Reduction、Fade In/Out、Room Tone、Voice/Breath Monitor；Voice 与 Breath 路径相加应等于原始源；官方逐段监听与调阈工作流。
- 版本提示：PDF 在延迟段把 44.1/48 kHz 都写为 32384 samples，与当前 Waves 延迟表及本机 48 kHz 回读不一致；延迟事实采用当前表和本机回读。

### DeBreath Vocal Plugin

- 类型：official-product
- URL：https://www.waves.com/plugins/debreath
- 版本适用：当前产品概览
- 可信度：medium-high
- 支持的事实：用于声乐、旁白与多媒体中的呼吸控制，并可在衰减处加入 Room Tone。

### Waves Plugin Latency

- 类型：official-support
- URL：https://www.waves.com/support/tech-specs/plugin-latency
- 版本适用：当前在线延迟表
- 可信度：high
- 支持的事实：DeBreath Native 44.1 kHz 为 32384 samples，48 kHz 为 35248 samples；本机 Ableton 48 kHz 回读 35248 samples，与当前表一致。

## 证据边界

- 官方资料用于确认设计意图和控制语义；不能替代本机检测准确率、伪检/漏检和声音质量验证。
- 本机仅成功加载 Waves `DeBreath Mono` VST3。当前复合夹具没有人工标注呼吸事件，默认与高敏感度压力条件都未产生高于数值噪声底的 Breath 监听分量，因此本轮不声称已经验证呼吸移除效果。
- Mono 组件在立体声轨道上会将输入折为双单声道；任何对 Stereo 组件的结论均未验证。

## S4 本机验证

- Ableton Live 11.3.43 / 48 kHz；DeBreath Mono 12.7.0.209 VST3；宿主回读 35248 samples（734.3 ms）。
- Default：Breath 50、Energy -30 dBFS、Reduction -Inf、Fade In/Out 5 ms、Room Tone Off；Stress：Breath 89.5、Energy -57 dBFS，其余不变。
- Default/Stress 的 Breath Monitor 均约 -144.5 dBFS，说明夹具未触发检测；Voice 路径等于折叠后的 Mid 并复制到左右，整个文件 Side 从 -30.85 dBFS 降到约 -147.5 dBFS。
- 报告：[[projects/p1-plugin-knowledge-base/validation/reports/ad123c8856d3--Waves-DeBreath|DeBreath L3 验证]]；量化：`projects/p1-plugin-knowledge-base/validation/results/ad123c8856d3--composite-debreath.json`。

## 反向链接

- [[projects/P1 插件适配知识库]]
