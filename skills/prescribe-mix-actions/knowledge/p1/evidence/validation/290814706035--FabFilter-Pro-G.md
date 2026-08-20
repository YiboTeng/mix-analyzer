---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: 290814706035
product: Pro-G
evidence_level: L3
test_id: composite-pro-g-vocal-expander-lookahead
---

# FabFilter Pro-G：Range 地板、Attack 与 Lookahead 验证

## 结论

本机 FabFilter Pro-G 1.3.1.0 VST3 Stereo 已在 Ableton Live 11.3.43 / 48 kHz 中真实加载。固定 Classic、Threshold -30.00 dB、Ratio 3.01:1、Range 11.94 dB、Attack 4.894 ms、Hold 60.10 ms、Release 148.5 ms、Knee 0 dB、Oversampling Off、内部侧链、侧链滤波关闭、Left/Right 模式，只切换 Lookahead 模块。

Lookahead 关闭时宿主报告 0 samples；开启后界面回读 9.951 ms，宿主报告 480 samples / 10.0 ms。Ableton 导出由 PDC 对齐，因此两份渲染的时间轴仍一致，但这不等于录音监听没有延迟。

零 Lookahead 条件把 0–6 秒单样本脉冲列整体降低 11.748791 dB，接近 11.94 dB Range 地板；Lookahead 条件对同一区域仅 -0.000001 dB。五个 35 ms 瞬态在零 Lookahead 下前 5 ms 分别降低约 2.14–2.20 dB，前 20–50 ms仍约 1.78–1.83 dB；开启 Lookahead 后全部约 0.000 dB。反之，五档稳定阶梯在充分稳定后，两条件对旁路均约 0.000 dB。这把三个语义分开：Range 是最大衰减上限，Attack 决定检测后打开速度，Lookahead 通过预开门保留 Attack 可能漏掉的短事件。

该参数组不是通用人声预设。固定人声区域恰好使检测器保持打开，两条件均约 0 dB；这只证明当前输入下活跃语音可中性通过，不证明对所有弱字尾、呼吸或噪声床都安全。

## 固定状态与宿主延迟

- 插件：FabFilter Pro-G 1.3.1.0，VST3 Stereo；Style Classic。
- 核心：Threshold -30.00 dB；Ratio 3.01:1；Range 11.94 dB；Knee 0 dB。
- 时间：Attack 4.894 ms；Hold 60.10 ms；Release 148.5 ms。
- 路由：Internal side-chain；HP/LP filters Off；Left/Right；Oversampling Off。
- 条件 A：Lookahead 模块 Off；宿主 0 samples。
- 条件 B：Lookahead On、9.951 ms；宿主 480 samples / 10.0 ms。
- 隔离：Pro-G 以外的 Melodyne 和更早链上设备全部停用；工程快照保存为条件 A。

| 区域 | 零 Lookahead vs 旁路 | 9.951 ms Lookahead vs 旁路 |
|---|---:|---:|
| 0–6 s 单样本脉冲列 | -11.748791 dB | -0.000001 dB |
| 8–20 s 稳定十音 | -0.000256 dB | 0.000000 dB |
| 21–57 s 固定人声 | -0.000378 dB | -0.000009 dB |
| 60–66 s 空间夹具 | -0.000043 dB | -0.000033 dB |
| 66–72 s 动态阶梯/瞬态 | -0.042030 dB | -0.000004 dB |

## Onset 与稳定段

| 事件窗口 | 零 Lookahead | 9.951 ms Lookahead |
|---|---:|---:|
| -30 dB 档前 5 ms | -11.851304 dB | -4.388565 dB |
| -30 dB 档前 10 ms | -3.386247 dB | -0.256067 dB |
| -30 dB 档前 20 ms | -0.564597 dB | -0.056349 dB |
| -24 dB 档前 5 ms | -9.258563 dB | -0.161242 dB |
| -18 dB 档前 5 ms | -3.241161 dB | 约 0 dB |
| 五个 35 ms 瞬态前 5 ms | -2.201 至 -2.137 dB | 约 0 dB |
| 五个 35 ms 瞬态前 20–50 ms | -1.830 至 -1.779 dB | 约 0 dB |

五档稳定音（名义峰值 -30、-24、-18、-12、-6 dBFS）在稳定后均约 0.000 dB。阈值判断是检测器与节目时间行为，不能直接拿名义峰值或区域 RMS 代替内部 detector level。零 Lookahead 与 Lookahead 整体相关 0.999205，互差 RMS -49.422288 dBFS；差异集中于开门前沿，而不是持续段音色。

## 工作流解释

- 先用最弱有效字尾确定 Threshold，再把 Range 限在只需的衰减量。当前约 12 dB Range 已足以让未预开的脉冲到达地板；继续加深会让句间更像数字切断。
- 先让 Hold 跨过音节内短停顿，再用 Release 保留自然尾部；若门在噪声床附近来回颤动，优先调整阈值、侧链滤波和时间常数，而不是只加 Ratio。
- 当词头被 Attack 吞掉时，Lookahead 是“提前打开”，不是高频增强。它能保留短事件，但本机代价为 480 samples；录音监听或并联路径必须显式检查延迟。
- 当前固定人声段几乎中性，说明稳定打开时不会因这组参数持续降电平；它不能替代带标签的弱辅音、呼吸、尾音和噪声床测试。
- 对照时分别看活跃语音、句尾与静音，不用全段 LUFS 掩盖门限只在部分时间动作的事实。

## 边界与未验证项

- L3 只覆盖本机 1.3.1.0 VST3 Stereo、48 kHz、Classic、内部侧链、Left/Right、OS Off 和上述固定参数。
- 未验证其它 Style、外部侧链、侧链 HP/LP/Audition、M/S、Stereo Link、MIDI Trigger、Oversampling、Mono、其它格式/采样率、自动化、真实人声噪声床标注或盲听。
- 稳定阶梯全部通过不证明 -30 dB 是普适人声阈值，也不证明最弱有效词尾安全；只描述当前 detector/时间历史下的结果。
- PDC 对齐后的导出不能用于声称 Lookahead 没有实时延迟。

## 证据

- 旁路 SHA-256：`38a74287a951ad7a62a6abeb219aa91afdd0e4f2abde062b972361851e0de16f`。
- 零 Lookahead SHA-256：`81bd8641fb3fb4aa044da37e03821707ba9636192ca29f3a1d34099a4bb60384`。
- 9.951 ms Lookahead SHA-256：`937e34481a8c119e258631f5605d2285203bf25e8466a6e3ebb3ef3dfed56153`。
- 工程快照 SHA-256：`d674bfaa0223698d5c992680ddfd6be526357ead63e83f0493b49ca257935609`。
- 量化：`validation/results/290814706035--composite-pro-g-vocal-expander-lookahead.json`（SHA-256 `ed8f2635b7ce42ee1ea67d1ef2f4ac109c29920e676648fded01cd23789caeb5`）。
- 测量脚本：`validation/scripts/analyze_gate.py`。
