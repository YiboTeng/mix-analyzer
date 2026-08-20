---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: fb4b55cbf4ec
product: ADPTR MetricAB
evidence_level: L3
test_id: neutral-metric-source
---

# ADPTR MetricAB 1.0：Metric 源中性与参考工作流验证

## 结论

本机 ADPTR MetricAB 1.0 VST3 在 Ableton Live 11.3.43 中、默认 `Metric`（蓝色 A）源、Gain 0.0 dB、Loudness Match 关闭时，对固定脉冲夹具没有可测得的时移或电平改变。与独立旁通渲染相比，最佳整数延迟为 0 samples，直接相关系数 0.999999998926，RMS 电平差 -0.000000 dB；残差 RMS -141.486632 dBFS、峰值 -132.453198 dBFS，符合两次独立 24-bit Triangular dither 导出的随机抖动底噪边界。

## 固定状态与量化

- 插件：Plugin Alliance / ADPTR MetricAB，本机观测版本 1.0.0 / 1.0.0.0，VST3。
- 状态：Default；蓝色 `A | B` 选择器位于 `METRIC`；Gain 0.0 dB；Loudness Match 关闭；Filter 默认 High 22050 Hz、Low 10 Hz；其余保持默认。
- 输入：固定 `impulse_train_48k.wav`；Master 渲染 6 s、48 kHz/24-bit WAV、Triangular dither。
- 对照：共享旁通 `a0c159c0ffd1--impulse--bypass.wav`，同一夹具与导出规格、独立渲染。
- 工程快照：`validation/host/snapshots/fb4b55cbf4ec--ADPTR-MetricAB.als`。

| 指标 | 结果 |
|---|---:|
| 最佳整数延迟 | 0 samples / 0.000000 ms |
| 直接相关系数 | 0.999999998926 |
| 最佳延迟相关系数 | 0.999999999462 |
| RMS 电平差 | -0.000000 dB |
| 残差 RMS | -141.486632 dBFS |
| 残差 Peak | -132.453198 dBFS |
| 最大绝对样本误差 | 2.384185791015625e-07 |

## 操作观察与工作流

- 大型 `A | B` 选择器的蓝色 `METRIC` 是宿主输入，橙色 B 是内部参考；做最终导出前必须确认回到蓝色 A，否则会输出参考槽而不是工程总线。
- 第一参考槽菜单可见 `Load Audio File`、`Show In Explorer`、`Remove Audio File`、`Clear Track Settings`；本轮通过 Windows 文件对话框走通本地 WAV 载入路径，并观察到槽位切换状态。
- Playback 页可见 Latch、Loop、1–4 定位槽、前后跳转以及 1/2、2x 速度；Filter 页提供 12 dB、High/Low 截止与 Low Mid/Mid/High/Sub/Bass/Reset 快捷监听。
- 顶部分析页包括 Playback、Spectrum、Correlation、Stereo Image、Dynamics、Loudness。它们应作为定位与复核工具，不能把单一图形差异直接当成音色优劣。
- Metric 源中性验证通过，说明它可放在监控链末端做只读比较；但是否被错误写入最终导出仍取决于 A/B 当前源，工作流必须保存源状态截图或快照。

## 边界与未验证项

- 两份对照均使用 Triangular dither，随机抖动使逐样本 bit-identical 不成立；因此以零延迟、近 1 相关、零电平差和约 -141.5 dBFS 残差作为中性证据。
- 本轮未量化内部参考播放的样本对齐、Cue/Sync/PDC、Loudness Match 误差、各分析器读数准确度、自动化或多参考槽上限。
- 已走通参考 WAV 的载入入口并观察 A/B 状态，但稀疏脉冲文件在槽位缩略波形中不易视觉确认；不把这一步记为参考播放的量化通过。
- 结论只覆盖本机 1.0 VST3 与 Ableton；不外推当前 1.4 手册新增行为、VST2 或 Studio One。

## 证据

- Metric 源渲染 SHA-256：`df0eafe6c9be1c027ad023b4968959f7dc35c26d95d874c07523c839ca5ee24f`。
- 独立旁通 SHA-256：`0123293a90801b37bbabd43e59492875ca3c319b9420363a653a2629903f92fc`。
- 量化：`validation/results/fb4b55cbf4ec--neutral-metric-source.json`。
- 测量脚本：`validation/scripts/analyze_neutral.py`。
