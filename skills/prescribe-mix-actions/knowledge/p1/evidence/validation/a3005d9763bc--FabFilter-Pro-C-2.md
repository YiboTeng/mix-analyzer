---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: a3005d9763bc
product: Pro-C 2
evidence_level: L3
test_id: dynamics-steps-compressor-attack-and-host-mapping
---

# FabFilter Pro-C 2：默认 Clean 曲线、Attack 单变量与 Lookahead 宿主映射验证

## 结论

本机 FabFilter Pro-C 2 2.1.7.0 VST3 Stereo 已在 Ableton Live 11.3.43、48 kHz 中真实加载，默认与变体状态的设备栏均显示 `Latency: 0 samples`。`Default Setting` 的宿主回读为 Clean、Threshold -18.00 dB、Ratio 4.00:1、Attack 0.255 ms、Release 209.2 ms、Knee +18.00 dB、Range +60.00 dB、Hold 0.000 ms、Auto Release Off、Output/Wet Gain 0.00 dB、Mix 100%、Oversampling Off、插件 UI Lookahead Off。Auto Gain 在 UI 中为黄色启用态；低于阈值的档位出现约 +4.8 dB 回补也与此一致。

默认态对五档 220 Hz 阶梯的稳态增益依次为 +4.836、+4.735、+3.440、+0.687、-3.282 dB，输出对输入回归斜率 0.66185。它不是“4:1 就得到 0.25 斜率”的简单硬拐点：+18 dB Knee、Auto Gain、有限测试范围与程序相关包络共同影响本次局部结果。默认瞬态列五次达到约 0 dBFS，说明直接套用默认 Auto Gain 会把峰值推到满幅附近，不能作为透明电平匹配起点。

在插件 UI 中只把 Attack 从 0.255 ms 改为 75.19 ms 后，五档稳态增益变为 +0.539、+0.480、-0.456、-2.684、-6.097 dB；五个隔离瞬态相对默认态低 2.325–2.345 dB，全文件峰值从约 0 dBFS 降到 -2.325 dBFS。这个方向不能被解读为“慢 Attack 一定更压字头”：本轮保留默认 Auto Gain，Attack 改变同时触发了明显的整体回补差异，正好证明比较 Attack/Style 前必须关闭 Auto Gain 并重新等响。

Lookahead 另发现宿主映射异常：Ableton 暴露参数可从 0.000 推到 20.00 ms，但 Pro-C 2 面板仍显示 `Lookahead: Off`，对应渲染与默认态互差 RMS 仅 -141.48 dBFS、峰值 -132.45 dBFS、相关系数 1.0，且估计延时 0 samples。此项只证明当前 Ableton/VST3 实例的该宿主参数调整没有传播到插件 DSP，不能用来声明 Pro-C 2 的 20 ms Lookahead 音效或真实延迟。

## 固定状态与量化

- 插件：FabFilter Pro-C 2 2.1.7.0，VST3 Stereo。
- 宿主：Ableton Live 11.3.43；48 kHz；观测设备栏 0 samples。
- 默认：Clean、Threshold -18 dB、Ratio 4:1、Attack 0.255 ms、Release 209.2 ms、Knee +18 dB、Range +60 dB、Hold 0 ms、Auto Release Off、Auto Gain On、Output/Wet Gain 0 dB、Mix 100%、OS Off、UI Lookahead Off。
- 有效单变量：插件 UI Attack 0.255 → 75.19 ms；其余可见插件控制固定。
- 负向集成探针：Ableton 暴露 Lookahead 0.000 → 20.00 ms；插件 UI 未改变且音频实质空差。
- 导出：Master、42.1.1–50.1.1、12 s、48 kHz/24-bit WAV、Normalize Off、Triangular dither。
- 夹具：`dynamics_steps_48k.wav`；Ableton 自动 Warp 为 160 BPM 下 8 bars/12 s，全部窗口以导出旁路控制为准。
- 工程快照：`validation/host/snapshots/0072a637f389--FabFilter-Saturn-2 Project/a3005d9763bc--FabFilter-Pro-C-2.als`。

| 输入峰值 | 旁路 RMS | 默认输出 RMS | 默认稳态增益 | Attack 75.19 输出 RMS | Attack 75.19 稳态增益 |
|---:|---:|---:|---:|---:|---:|
| -30 dBFS | -33.011 | -28.175 | +4.836 dB | -32.472 | +0.539 dB |
| -24 dBFS | -27.011 | -22.276 | +4.735 dB | -26.531 | +0.480 dB |
| -18 dBFS | -21.011 | -17.570 | +3.440 dB | -21.466 | -0.456 dB |
| -12 dBFS | -15.023 | -14.336 | +0.687 dB | -17.707 | -2.684 dB |
| -6 dBFS | -9.011 | -12.293 | -3.282 dB | -15.107 | -6.097 dB |

| 静态指标 | 默认 vs 旁路 | Attack 75.19 vs 旁路 |
|---|---:|---:|
| 输出对输入斜率 | 0.661850 | 0.725999 |
| 局部有效比率（仅回归描述） | 1.5109:1 | 1.3774:1 |
| 最低到最高档增益变化 | -8.1179 dB | -6.6360 dB |
| 全文件 RMS 差 | -1.3713 dB | -4.1857 dB |
| 全文件峰值差 | +2.8537 dB | +0.5285 dB |

| 隔离瞬态 | 默认峰值 | Attack 75.19 峰值 | Attack 75.19 vs 默认 |
|---:|---:|---:|---:|
| 1 | ~0.000 dBFS | -2.345 dBFS | -2.345 dB |
| 2 | ~0.000 dBFS | -2.326 dBFS | -2.326 dB |
| 3 | ~0.000 dBFS | -2.325 dBFS | -2.325 dB |
| 4 | ~0.000 dBFS | -2.325 dBFS | -2.325 dB |
| 5 | ~0.000 dBFS | -2.325 dBFS | -2.325 dB |

## 操作观察与工作流

- 先关 Auto Gain，再做 Threshold/Ratio/Knee/Range/Attack/Release 的因果判断；最后以 Output/Wet Gain 对旁路匹配响度。本机默认态低档被回补约 4.8 dB且瞬态触顶，是最直接的反例。
- Clean 作为可解释基线。先用 Range 限定最大压缩量，再用 Threshold 获得目标 GR；Ratio 只定义曲线的一部分，不能脱离 Knee、Style 和电平范围读成实际输出斜率。
- Attack 以字头和后级峰值为目标调节。若想比较 0.255 与 75 ms，必须在 Auto Gain Off、输出等响后再听辅音、鼓点和峰值；本轮默认 Auto Gain On 的结果只用于证明混杂风险。
- Release 209.2 ms/Auto Release Off 是本机默认。实际主唱从音节恢复和节奏泵动判断；太快可能喘振或失真，太慢会让后续字持续被压。
- Sidechain HP/LP/Bell 只改变检测器，不直接 EQ 主信号。低频误触发时先 Audition 检查，再最小量过滤；不要用高通把应当受控的胸腔能量完全绕过。
- Lookahead 与 OS 必须同时回读插件 UI、宿主延迟和音频差分。当前 Ableton 暴露 Lookahead 的数值不可信，不能据宿主旋钮 alone 建立工作流。
- Stereo Link/M/S、Dry/Wet 并行和外部侧链要用独立夹具验证；本轮双单声道左右残差约 -141.5 dBFS只支持当前输入下左右一致。

## 边界与未验证项

- L3 只覆盖本机 2.1.7.0 VST3 Stereo、Default Setting/Clean、默认 Auto Gain On、Attack 0.255→75.19 ms、UI Lookahead Off 与一次失败的 Ableton Lookahead 映射探针。
- 未验证其它七种 Style、Auto Gain Off 的等响 Attack 曲线、Auto Release、Range 限幅、侧链滤波/外部侧链、Stereo Link/M/S、Dry/Wet 并行、2x/4x OS、真实插件 UI Lookahead、其它采样率/格式、CPU 或连续主唱盲听。
- 夹具被 Warp 到 12 s；结果不是绝对模拟攻击/释放时间标定。默认态瞬态触到 0 dBFS，不能外推为无削顶工作流。
- `Lookahead 20 ms` 文件名保留实验意图；报告和 JSON 已明确其内部仍为 Off，只可作为宿主映射失败证据。

## 证据

- 旁路 SHA-256：`5261897d7fcba3a600162969b2a2c55fcc20d3023f3fa1701110c409c0a6bf91`。
- 默认 SHA-256：`169dd9a9a1b8d6afb190929b49135b2e7e50f73823e59e0c0f65eef307fa7ce8`。
- Lookahead 宿主映射探针 SHA-256：`ccaa34a4ef08c6c56473127ca5599ff4e26949aaaa79b4aa00a14732f60da5d2`。
- Attack 75.19 ms SHA-256：`1c641fc699775b300d433382ea5029da4860b0d1145d9fe932c4076978a5aef2`。
- 工程快照 SHA-256：`c9e2286261282163b1c4268a58ea942ed4be6398ecf6681c6747212a35663718`。
- 量化：`validation/results/a3005d9763bc--dynamics-compressor-lookahead.json`。
- 测量脚本：`validation/scripts/analyze_compressor_lookahead.py`。
