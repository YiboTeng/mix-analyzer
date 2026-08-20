---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: 47e12f69eb3c
product: CLA-76
evidence_level: L3
test_id: dynamics-steps-compressor-attack
---

# Waves CLA-76：Start Me Up 动态曲线与 Attack 3→7 单变量验证

## 结论

本机 Waves `CLA-76 Stereo` V12（文件系统版本 12.7.0.209）VST3 已在 Ableton Live 11.3.43、48 kHz 中真实加载，宿主设备栏报告 `Latency: 0 samples`。本机旧版面板没有新版在线资料中的 Mix/Trim；实见控制是 Input、Output、Attack、Release、Ratio、Meter、Analog 与 Bluey/Blacky Revision。

默认宿主预置 `A: Start Me Up` 为 Bluey、Input 30、Output 18、Attack 3、Release 4、Ratio 4:1、Meter GR、Analog Off。对五档 220 Hz 阶梯，默认处理相对旁路的稳态增益从低到高依次为 +6.269、+6.275、+5.579、+0.882、-4.184 dB；最低到最高档的增益变化为 -10.454 dB，输出对输入回归斜率 0.5616。它清楚显示 Input 驱动固定阈值结构：低档主要得到 Output 回补，高档则产生越来越强的净衰减。

仅把 Attack 从 3 改到 6.99（名义 7）后，低两档稳态几乎不变，高三档稳态只再低 0.044–0.147 dB；但五个隔离瞬态相对 Attack 3 的峰值进一步降低 0.882、1.707、1.637、1.644、1.653 dB，全文件峰值由 -1.424 降到 -2.306 dBFS。由此可直接确认本机版本的 Attack 数字越大越快，主要改变字头捕获，而不是简单整体降音量。

## 固定状态与量化

- 插件：Waves `CLA-76 Stereo` V12，文件系统 12.7.0.209，VST3。
- 宿主：Ableton Live 11.3.43；48 kHz；报告延迟 0 samples。
- 固定面板：`A: Start Me Up`、Bluey、Input 30、Output 18、Release 4、4:1、Meter GR、Analog Off。
- 单变量：Attack 3.00 → 6.99（按名义刻度 7 记录）。
- 导出：Master、42.1.1–50.1.1、12 s、48 kHz/24-bit WAV、Normalize Off、Triangular dither。
- 夹具：`dynamics_steps_48k.wav`；Ableton 自动 Warp 为 160 BPM 下 8 bars/12 s，因此全部窗口以导出的旁路控制为准。
- 工程快照：`validation/host/snapshots/0072a637f389--FabFilter-Saturn-2 Project/47e12f69eb3c--Waves-CLA-76.als`。

| 输入峰值 | 旁路 RMS | Attack 3 输出 RMS | Attack 3 稳态增益 | Attack 7 输出 RMS | Attack 7 稳态增益 |
|---:|---:|---:|---:|---:|---:|
| -30 dBFS | -33.011 | -26.742 | +6.269 dB | -26.742 | +6.269 dB |
| -24 dBFS | -27.011 | -20.736 | +6.275 dB | -20.736 | +6.275 dB |
| -18 dBFS | -21.011 | -15.432 | +5.579 dB | -15.476 | +5.534 dB |
| -12 dBFS | -15.023 | -14.141 | +0.882 dB | -14.288 | +0.736 dB |
| -6 dBFS | -9.011 | -13.195 | -4.184 dB | -13.327 | -4.316 dB |

| 静态指标 | Attack 3 vs 旁路 | Attack 7 vs 旁路 |
|---|---:|---:|
| 输出对输入斜率 | 0.561571 | 0.554723 |
| 由斜率得到的局部有效比率 | 1.7807:1 | 1.8027:1 |
| 最低到最高档增益变化 | -10.4536 dB | -10.5857 dB |
| 全文件 RMS 差 | -1.2488 dB | -1.3907 dB |
| 全文件峰值差 | +1.4297 dB | +0.5477 dB |

> “局部有效比率”只是在这五档、这个 Input/Output/4:1 预置上的回归描述，不等同面板标称 Ratio，也不能外推到完整传递曲线。

| 隔离瞬态 | Attack 3 峰值增益 vs 旁路 | Attack 7 峰值增益 vs 旁路 | Attack 7 vs Attack 3 |
|---:|---:|---:|---:|
| 1 | +1.430 dB | +0.548 dB | -0.882 dB |
| 2 | -0.435 dB | -2.142 dB | -1.707 dB |
| 3 | -0.441 dB | -2.078 dB | -1.637 dB |
| 4 | -0.378 dB | -2.022 dB | -1.644 dB |
| 5 | -0.327 dB | -1.979 dB | -1.653 dB |

两个处理态的 L-R 残差约 -141.49 dBFS。夹具本身是双单声道，这支持“当前输入下左右处理一致”，但不是独立左右不等电平、相位或 Stereo Link 行为的充分证明。

## 操作观察与工作流

- 先选 Ratio/Revision/Attack/Release，再用 Input 把响句推到目标 GR；最后用 Output 对旁路做等响。Input 不是可与阈值分开的普通输入增益。
- 本轮 `Start Me Up` 在 -30/-24 dBFS 档主要给约 +6.27 dB 净增益，到 -6 dBFS 已变为 -4.18 dB；只看输出响度会把回补与压缩混在一起。
- Attack 3 保留更多瞬态，Attack 7 对重复脉冲再压低约 1.6 dB。主唱字头太硬、后级被峰值触发时向 7 推；辅音变钝、咬字后退时向 3–4 回。
- 由于本机 v12 无 Mix/Trim，All-buttons 并行应在 DAW Aux 完成；Analog Off 先建立无噪声基线，50/60 Hz 只在明确需要硬件底噪时开启。
- Release 仍应按节奏判断：过快会在低频/元音处喘振或失真，过慢会让后续音节持续被压。本轮固定 Release 4，未把恢复时间写成已验证。
- Bluey/Blacky、4/8/12/20/All 必须分别等响比较；不能把硬件修订名或比例标签直接当作音质结论。

## 边界与未验证项

- L3 只覆盖本机 v12 VST3 Stereo、Bluey、`Start Me Up`、4:1、Release 4、Analog Off 与 Attack 3→6.99。
- 未验证 Release 1/7、Blacky、其它 Ratio、All-buttons、Analog 50/60、Mono/Stereo 链接、VST2、其它采样率、CPU、自动化或连续主唱等响盲听。
- 夹具被 Warp 到 12 s；测量窗口全部来自独立导出的旁路控制。结果不能用于宣称未 Warp 源文件下的绝对微秒级硬件 Attack 时间。
- 瞬态 1 在长静音后出现，Attack 3 输出峰值一度高于旁路；后续脉冲受 Release/检测器记忆影响。两者差值仍可靠描述同一序列中 Attack 改变，但不能把单个脉冲当完全无历史的静态阈值测试。

## 证据

- 旁路 SHA-256：`fcff440c44e4d32b5327c9cc2c60a4b258e1117da28d5104c39cafe3b4508689`。
- 默认 Attack 3 SHA-256：`186a34a33a1da931725fc043d001e889b4684ff4063dcd29a85f3ca6f64ae6c3`。
- Attack 6.99 SHA-256：`ef6da88a7fbabbeac669681da0bf70bcc96dbd0c945bb337529eda450f18a263`。
- 工程快照 SHA-256：`f0b6ccc30c6023099277a71d15c1adcada94960cc02cf87a861e1faefbb372b7`。
- 量化：`validation/results/47e12f69eb3c--dynamics-compressor.json`。
- 测量脚本：`validation/scripts/analyze_compressor.py`。
