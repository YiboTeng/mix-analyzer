---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: ad123c8856d3
product: DeBreath
evidence_level: L3
test_id: composite-debreath-default-voice-and-monitor-breath
---

# Waves DeBreath：加载、Mono 折叠、延迟与检测边界验证

## 结论

本机 Waves `DeBreath Mono` 12.7.0.209 VST3 已在 Ableton Live 11.3.43 / 48 kHz 中真实加载，控制可改、工程可保存，宿主回读 35248 samples / 734.3 ms，与 Waves 当前在线延迟表的 48 kHz 数值一致。

当前 Composite 没有人工标注呼吸。Default（Breath 50、Energy -30 dBFS）与 Stress（Breath 89.5、Energy -57 dBFS）在 `Reduction -Inf` 下的 Breath Monitor 都只有约 -144.5 dBFS 的数值噪声底；两个 Voice 输出也相同到测量精度。本轮不能证明呼吸检出或移除效果，反而明确证明这个夹具对 DeBreath 是无效检测夹具。

本轮最强且可重复的结果是格式边界：只加载了 Mono 组件。它把立体声输入折为 Mid 并复制到左右，整段 Voice 的左右相关约 1.0、Side 约 -147.5 dBFS；旁路 Side 为 -30.85 dBFS。稳定多音区域因左右内容差异而相对旁路低 2.508 dB，固定人声区域只低 0.00278 dB。此差异不是呼吸衰减，不能拿来评价算法质量。

按项目 L3 口径，本报告提供本机真实加载、版本/格式、控制状态、宿主延迟、隔离渲染、量化、快照和明确负结果边界；它不把未触发的夹具写成成功呼吸识别。DeBreath 可作为 RX 10 Breath Control 无法加载后的可操作替代，但后续处方必须标记“效果证据待真实标注呼吸补测”。

## 固定状态

- 插件：Waves `DeBreath Mono` 12.7.0.209 VST3。
- 宿主：Ableton Live 11.3.43；48 kHz；35248 samples（734.3 ms）。
- Default：A: Default/Full Reset；Breath 50；Energy -30 dBFS；Reduction -Inf；Fade Out/In 5/5 ms；Room Tone Off。
- Stress：Breath 89.5；Energy -57 dBFS；其余同 Default。
- 隔离：DeBreath 条件启用；NS1、Pro-G、Melodyne 和所有更早链上设备停用；旁路条件连 DeBreath 也停用。

## 量化

| Composite 区域 | Default Voice vs bypass | Default Breath Monitor vs bypass | Stress Voice vs bypass | Stress Breath Monitor vs bypass |
|---|---:|---:|---:|---:|
| 0–6 s 脉冲列 | +0.000001 dB | -89.691 dB | +0.000001 dB | -89.688 dB |
| 8–20 s 稳定多音 | -2.507727 dB | -125.005 dB | -2.507727 dB | -125.006 dB |
| 21–42 s 固定人声 | -0.002778 dB | -118.553 dB | -0.002778 dB | -118.555 dB |
| 45–57 s 空间夹具 | 0.000000 dB | -123.706 dB | 0.000000 dB | -123.697 dB |
| 60–72 s 动态夹具 | 0.000000 dB | -127.298 dB | 0.000000 dB | -127.299 dB |

整段结果：

- bypass：L -21.324、R -21.555、相关 0.7714、Side -30.853、Mid -21.966 dBFS。
- Default Voice：L/R 均 -21.966、相关 ≈1.0、Side -147.506 dBFS。
- Stress Voice：L/R 均 -21.966、相关 ≈1.0、Side -147.503 dBFS。
- Default/Stress Breath Monitor：约 -144.5 dBFS，未得到可用检测分量。

## 解释与工作流

- 先用真实单声道人声，切到 Breath Monitor，再调 Breath 与 Energy；没有听到明确目标呼吸前，不要把 Reduction 变化当作有效处理。
- Breath Monitor 应只有呼吸、没有有音高内容；Voice 还应保留自然句间节奏。若两者不能同时满足，个别事件改用 Clip Gain。
- 当前 Mono 组件只能用于本来就应是单声道的主唱；立体声和声/FX Stem 插入会摧毁 Side。
- 35248 samples 延迟使它不适合实时监听；应在录音后编辑阶段使用，自动化前确认宿主补偿。

## 边界与未验证项

- 没有真实标注呼吸，未验证检出率、误检率、Reduction 曲线、Fade 边缘、Room Tone 或 Voice+Breath 重构。
- 未验证 Stereo 组件、VST2、其它采样率、其它宿主、自动化、盲听和压缩前后顺序。
- Stress 的阈值变化未触发检测，只能说明夹具/条件组合无检出，不能说明 DeBreath 无效。

## 证据

- 旁路 SHA-256：`e2dfde5d5dc081d2df466c94f100a8fed79f864ed720eb9e398221f275aecdda`。
- Default Voice SHA-256：`1674852720fae64acc2aa4cacb643390a7ba415006624e7c9b8cdae554fd4782`。
- Default Breath Monitor SHA-256：`285da5e073487e960148b5e0a108fc9fbe89bde58a1d571a95e9c1da13931af2`。
- Stress Voice SHA-256：`81c09dc81a8e412a44a5c70b664e38a461cf6ed6f427d1078bedeB69b92d3048`。
- Stress Breath Monitor SHA-256：`4fba147bb4904e543259d0ca96ddc0533287b6c63746abaec483741ff6d08725`。
- 工程快照 SHA-256：`8a8a6c166527186d4319f94e5403e22fe856349b749644bb11314c792387230d`。
- 量化：`validation/results/ad123c8856d3--composite-debreath.json`（SHA-256 `8f5f3a7852d7f520b5d9b60eb3e253f36d60da170ad486c7fb0a7fe821659177`）。
- 脚本：`validation/scripts/analyze_debreath.py`（SHA-256 `a51c604b95a97130cc2d88ca59b2f1465048965a370a32b17c432666eded38d7`）。
