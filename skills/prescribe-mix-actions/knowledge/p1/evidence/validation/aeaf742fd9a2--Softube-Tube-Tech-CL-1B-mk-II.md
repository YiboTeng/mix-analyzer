---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: aeaf742fd9a2
product: Tube-Tech CL 1B mk II
evidence_level: L3
test_id: dynamics-steps-cl1b-mode
---

# Softube Tube-Tech CL 1B mk II：Fix/Man 与 Fixed 模式验证

## 结论

本机 Softube `Tube-Tech CL 1B mk II` 2.5.x VST3 Stereo 已在 Ableton Live 11.3.43、48 kHz 中真实加载，宿主设备栏报告 `Latency: 4 samples (0.083 ms)`。本轮保持 Threshold -20 dB、Gain 0 dB、Parallel 100%、Sidechain Low Cut Off 与其余可见旋钮不变，只比较 Fix/Man 与 Fixed。

五档稳态阶梯显示两种模式都会随输入升高而增加衰减，但 Fix/Man 在本轮持续音上更深：从 -24 到 -6 dBFS 四档，其稳态输出比 Fixed 再低 1.459、1.881、2.146、2.279 dB。Fix/Man 的输出对输入斜率为 0.2315，Fixed 为 0.3086；这只是当前五档与当前状态下的局部曲线，不等同面板 Ratio 的绝对校准。

模式差异在字头更明显。Fixed 对五个隔离脉冲均把峰值压低约 2.64 dB；Fix/Man 的首个脉冲比旁路高 0.589 dB，后四个高约 1.863 dB。因脉冲位于前段持续压缩之后，结果同时包含检测器/释放记忆、模拟电路与模式包络，不能把它简化成“Fix/Man 没有快 Attack”。它能可靠说明：在这组输入历史下，Fixed 明显更强地约束短峰，而 Fix/Man 对持续音形成更深的后续稳态衰减。

## 固定状态与量化

- 插件：Softube `Tube-Tech CL 1B mk II` 2.5.x，VST3 Stereo。
- 宿主：Ableton Live 11.3.43；160 BPM；48 kHz；报告延迟 4 samples / 0.083 ms。
- 固定控制：Threshold -20 dB、Gain 0 dB、Parallel 100%、Sidechain Low Cut Off；其余可见旋钮保持加载默认。
- 单变量：Time-control mode `Fix/Man` → `Fixed`。
- 官方语义：Fixed 为约 1 ms Attack / 50 ms Release；Fix/Man 使用固定快 Attack，并按节目在快释放与手动 Release 之间过渡，Attack 旋钮在该模式控制转入手动释放的延迟。
- 导出：Master、42.1.1–50.1.1、12 s、48 kHz/24-bit WAV、Normalize Off、Triangular dither。
- 夹具：`dynamics_steps_48k.wav`；Ableton 自动 Warp 为 160 BPM 下 8 bars/12 s，全部窗口以独立旁路导出为准。
- 工程快照：`validation/host/snapshots/0072a637f389--FabFilter-Saturn-2 Project/aeaf742fd9a2--Softube-Tube-Tech-CL-1B-mk-II.als`。

| 输入峰值 | 旁路 RMS | Fix/Man RMS | Fix/Man 稳态增益 | Fixed RMS | Fixed 稳态增益 |
|---:|---:|---:|---:|---:|---:|
| -30 dBFS | -33.011 | -33.337 | -0.326 dB | -33.026 | -0.015 dB |
| -24 dBFS | -27.011 | -31.757 | -4.746 dB | -30.298 | -3.288 dB |
| -18 dBFS | -21.011 | -30.420 | -9.409 dB | -28.538 | -7.528 dB |
| -12 dBFS | -15.023 | -29.101 | -14.078 dB | -26.955 | -11.932 dB |
| -6 dBFS | -9.011 | -27.721 | -18.710 dB | -25.442 | -16.431 dB |

| 静态指标 | Fix/Man vs 旁路 | Fixed vs 旁路 |
|---|---:|---:|
| 输出对输入斜率 | 0.231520 | 0.308584 |
| 由斜率得到的局部有效比率 | 4.3193:1 | 3.2406:1 |
| 最低到最高档增益变化 | -18.3839 dB | -16.4162 dB |
| 全文件 RMS 差 | -11.2380 dB | -13.1548 dB |
| 全文件峰值差 | +1.8634 dB | -2.6407 dB |

> “局部有效比率”只描述本轮五档回归；光学检测、Knee、时间积分与固定模式共同影响结果，不能据此反推硬件完整传递曲线或面板 Ratio。

| 持续音起点 | Fix/Man 达到稳态 ±1 dB | Fixed 达到稳态 ±1 dB |
|---:|---:|---:|
| -24 dBFS | 122.92 ms | 83.69 ms |
| -18 dBFS | 111.04 ms | 57.00 ms |
| -12 dBFS | 109.71 ms | 30.40 ms |
| -6 dBFS | 171.88 ms | 55.27 ms |

| 隔离脉冲 | Fix/Man 峰值增益 vs 旁路 | Fixed 峰值增益 vs 旁路 | Fixed vs Fix/Man |
|---:|---:|---:|---:|
| 1 | +0.589 dB | -2.643 dB | -3.232 dB |
| 2 | +1.863 dB | -2.641 dB | -4.504 dB |
| 3 | +1.863 dB | -2.641 dB | -4.504 dB |
| 4 | +1.863 dB | -2.641 dB | -4.504 dB |
| 5 | +1.863 dB | -2.641 dB | -4.504 dB |

两种处理态的 L-R 残差约 -141.48 dBFS。夹具是双单声道，这只支持当前输入下左右处理一致，不能替代不等电平、相位或 Stereo Link 测试。

## 操作观察与工作流

- 主唱电平整理优先从 Manual 或 Fix/Man、低至中等 Ratio 开始，用 Threshold 把响句调到约 3–5 dB GR，再以 Gain 做旁路等响；不要照抄 Threshold 数值，因为它取决于输入标定。
- Fixed 是明确的快速控制模式。本轮它比 Fix/Man 对重复短峰多压约 4.5 dB；爆破、硬辅音或后级仍被尖峰触发时可试，但字头变钝就退回 Fix/Man/Manual 或减少 GR。
- Fix/Man 不是普通“手动 Attack”。Attack 旋钮控制从固定快释放过渡到手动 Release 的延迟；Release 旋钮决定长事件的恢复。持续元音更稳但句尾被拖住时，应先检查 Release 与累积 GR。
- Sidechain Low Cut 只改变检测侧链。爆破或胸腔低频过度触发时从 Off 逐步升高，并对比低音响句是否反而穿出；本轮未验证其频率选择性。
- Parallel 会同时改变感知响度与相位条件。先全湿设好压缩，再回混并做 Active RMS 等响；本轮只验证 100% wet。
- 串联 CLA-76 时让两级分工：CLA-76 先削少量瞬态，CL 1B 再平滑宏动态；不要让两级都持续深压。

## 边界与未验证项

- L3 只覆盖本机 VST3 Stereo、48 kHz、Threshold -20 dB、默认其余控制、Fix/Man 与 Fixed、一个阶梯/脉冲历史和 4-sample 宿主报告。
- 未验证 Manual、Attack/Release 端点、Ratio 扫描、Gain 非线性、Sidechain Low Cut、外部侧链、Parallel Null、Mono、VST2、Stereo Link、其它采样率、CPU、自动化或连续主唱等响盲听。
- 官方 1 ms/50 ms 是模式定义；表中 30–84 ms 的持续音“进入稳态”包含检测、光学包络、窗函数和输入历史，不是对 1 ms Attack 的否定或直接硬件时间测量。
- Fix/Man 隔离脉冲高于旁路是当前渲染的可重复测量事实，但本轮没有把模拟级过冲、相位响应与释放记忆分离；不能把 +1.863 dB 泛化为所有音频或预设。

## 证据

- 旁路 SHA-256：`3ca5a7a96c90f301020bbf1c4d9f895086e6767b6b8cd150caa75e4c6959856c`。
- Fix/Man SHA-256：`6f516cb79f638db1fb84bd543fa94b8e78104593c283a102add0eb344ba5d68f`。
- Fixed SHA-256：`65c02689cef7894714af07a8879e544bbb5093d94a6956b327b7c6dd25850c45`。
- 工程快照 SHA-256：`a5636c0cefa2d058ad099166d19faf2673d04185f13ea3b96347afa72ac9ec37`。
- 量化：`validation/results/aeaf742fd9a2--dynamics-cl1b-mode.json`。
- 测量脚本：`validation/scripts/analyze_tubetech_cl1b.py`。

