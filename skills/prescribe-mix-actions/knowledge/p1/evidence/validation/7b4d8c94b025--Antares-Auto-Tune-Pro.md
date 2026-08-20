---
type: plugin-validation-report
status: passed-l3
created: 2026-08-20
updated: 2026-08-20
family_id: 7b4d8c94b025
vendor: "Antares"
product: "Auto-Tune Pro"
evidence_level: L3
---

# Antares Auto-Tune Pro：Chromatic Retune Speed 验证

## 结论

本机 Auto-Tune Pro 10.0.0 VST3 已在 Ableton Live 11.3.43、48 kHz 中真实加载。默认 Auto/Modern、Alto-Tenor、C Chromatic、Tracking 50、Retune Speed 20、Flex-Tune 0、Humanize 0、Natural Vibrato 0、Formant 100、Transpose 0、Detune 440 Hz、Mix 100%；Ableton 报告 `2670 samples / 55.6 ms` 延迟。

在复合夹具的 21–42 秒固定人声段，用 120 ms 自相关帧测量 491 个三态共同有声帧。旁路 F0 距最近十二平均律半音的绝对偏差中位数为 `6.115 cents`；默认 Retune 20 降至 `4.160 cents`，Retune 0 再降至 `0.844 cents`。落在 ±5 cents 内的帧比例从旁路 `40.1%` 提升到 Retune 20 的 `63.7%`、Retune 0 的 `88.0%`。

Retune 20 相对旁路在 `68.6%` 的共同帧上更接近最近半音，中位改善 `1.884 cents`；Retune 0 为 `87.2%`、中位改善 `4.862 cents`。Retune 0 相对 Retune 20 仍在 `82.1%` 帧上更接近半音，中位改善 `2.776 cents`。这验证了本机实例中更低 Retune Speed 会更快、更紧地吸附到目标音，但不表示旋钮数字是毫秒，也不代表旋律目标音正确。

## 固定条件

- 宿主：Ableton Live 11.3.43；48 kHz；VST3；本机版本 `10.0.0`。
- 模式：Auto、Modern、Alto-Tenor、C Chromatic、Tracking 50、Flex-Tune 0、Humanize 0、Natural Vibrato 0、Formant 100、Transpose 0、Detune 440 Hz、Mix 100%。
- 单变量：Retune Speed 20 → 0；Key/Scale 与其它控件不变。
- 输入：72 秒复合夹具；Pitch 统计只用 21–42 秒固定人声段。
- 导出：Master，48 kHz、Stereo、24-bit WAV、Normalize Off、Triangular dither；Ableton PDC 对齐。
- 工程快照 SHA256：`f6a7de8bd80d94e01b0e078021fcda4215844a6ef1bba55ca58bb037ddd0d914`；保存状态为 Retune Speed 0。

## 关键测量

| 状态 | 绝对偏差中位 | P90 | ±5 cents | ±10 cents | 帧间移动中位 |
|---|---:|---:|---:|---:|---:|
| 旁路 | 6.115 cents | 9.435 | 40.1% | 92.3% | 8.254 cents |
| Retune 20 | 4.160 cents | 7.698 | 63.7% | 93.3% | 6.295 cents |
| Retune 0 | 0.844 cents | 5.951 | 88.0% | 93.1% | 1.337 cents |

固定人声段 RMS 为旁路/Retune20/Retune0 `-25.938/-25.940/-25.938 dBFS`，因此当前 Pitch 统计不是由整体响度差驱动。Retune 0 的帧间移动中位数大幅下降，符合更强平台化；但 P90 仍约 194 cents，主要包含音符转换、滑音与可能的 F0 倍频/半频跳变，不能当成校正错误率。

## 使用判断

- 先确认 Input Type、Key 与 Scale；本报告用 Chromatic 只验证“趋近最近半音”，不验证歌曲调性或旋律正确性。
- 自然校音可从 Retune 20 附近开始，听短音稳定度；需要明确机器感时再向 0 降低。
- Retune 0 把 ±5 cents 内帧比例推到约 88%，同时帧间细微移动中位数从 8.25 降至 1.34 cents。若滑音、颤音或咬字意图被吸平，先回慢 Retune，再按需要增加 Flex-Tune。
- Humanize 用于快速 Retune 下的长音，不用于修复错误 Key/Scale；本轮没有验证其量化效果。
- 固定 55.6 ms 插件延迟不适合无预算的现场监听链；录音时需使用宿主低延迟策略或另选实时方案，并单独验证实际路由。

## 边界

F0 为 120 ms 自相关帧，只比较三态都被判为有声的 491 帧；无声辅音、复音泄漏、Clip Warp、倍频/半频误判和帧选择会影响统计。Chromatic 最近半音不是歌曲目标音，不能评价旋律正确性、音符边界自然度、听感质量或 lisp。未测试 Key/Scale 错配、Flex-Tune、Humanize、Tracking、Classic、Graph、Formant/Throat、MIDI、低延迟选项、Mono、其它采样率、自动化、CPU 或盲听。

## 证据

- [分析结果](../results/7b4d8c94b025--fixed-vocal-chromatic-retune-speed.json)
- [分析脚本](../scripts/analyze_pitch_correction.py)
- [工程快照](<../host/snapshots/0072a637f389--FabFilter-Saturn-2 Project/7b4d8c94b025--Antares-Auto-Tune-Pro.als>)
