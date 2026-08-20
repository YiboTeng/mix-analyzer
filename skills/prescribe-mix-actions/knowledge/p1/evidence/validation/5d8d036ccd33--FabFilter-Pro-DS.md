---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: 5d8d036ccd33
product: Pro-DS
evidence_level: L3
test_id: composite-deesser-wide-split-lookahead
---

# FabFilter Pro-DS：Single Vocal、Wide/Split 与 Lookahead 验证

## 结论

本机 FabFilter Pro-DS VST3 已在 Ableton Live 11.3.43、48 kHz 中真实加载。About 界面回读为 `FabFilter Pro-DS version 1.21 (64-bit), June 29, 2023`；默认预设为 `Default Setting`，可见状态为 Threshold `-36.00 dB`、Range `6.00 dB`、Single Vocal、Wide Band、侧链约 `7–14 kHz`、Stereo Link `100% / MID`、Lookahead `12.00 ms`、Oversampling Off、输入/输出 `0 dB`。

在 72 秒复合夹具中，Single Vocal + Wide + 12 ms Lookahead 对 0.50、2.50、4.50 秒三个短促源事件分别降低 `1.158`、`0.992`、`0.747 dB`，0–6 秒区域整体降低 `1.086 dB`。Split + 12 ms 对同三事件分别降低 `1.022`、`0.877`、`0.662 dB`，区域整体降低 `0.957 dB`。当前夹具下两者都只在 1037 个高于 -70 dBFS 的 50 ms 活跃窗中有 3 个窗达到至少 0.05 dB 衰减，证明 Single Vocal 检测不是对所有高频/电平持续动作。

8–20 秒稳定十音多频区域中，Wide 与 Split 的区域 RMS 差均约 `0.000 dB`；这是一项有用的负结果：非语音稳定多音没有被当前 Single Vocal 默认阈值当作齿音。它不能外推为对真实 S/T/CH 的漏检率。

关闭 Lookahead 模块后，三个短事件相对旁路仅为 `-0.000001 / 0.000000 / +0.000002 dB`，1037 个活跃窗没有一个达到 0.05 dB 衰减；在这个短事件夹具与默认阈值下，Lookahead 是检测并处理起始瞬态的必要条件。该结论只适用于本轮状态，不意味着所有人声必须启用 12 ms。

宿主延迟边界比旋钮数字更重要：Wide + 12 ms Lookahead + OS Off 报告 `720 samples / 15.0 ms`；Split 同状态为 `1232 samples / 25.7 ms`。把 Lookahead 旋钮转到 `0.000 ms` 但保留模块启用，宿主仍报告 `720 samples`；只有真正关闭 Lookahead 模块，Wide + OS Off 才为 `0 samples`。Lookahead Off 时 2x/4x Oversampling 分别为 `34 / 40 samples`（`0.71 / 0.83 ms`）。因此实时链路要检查模块开关和宿主回读，不能只看 Lookahead 数字。

## 固定状态与量化

- 插件：FabFilter Pro-DS 1.21 (64-bit; June 29, 2023)，VST3 Stereo。
- 宿主：Ableton Live 11.3.43；48 kHz。
- 默认：`Default Setting`、Threshold -36.00 dB、Range 6.00 dB、Single Vocal、Wide、约 7–14 kHz、Stereo Link 100%/MID、Lookahead 12.00 ms、OS Off、I/O 0 dB。
- 单变量：Wide→Split；以及 Wide 下关闭 Lookahead 模块。延迟另探测 OS Off/2x/4x。
- 导出：Master、Start 2.1.1、Length 48.0.0、实际 72 s、48 kHz/24-bit stereo WAV、Normalize Off、Triangular host dither。
- 夹具：同一 Arrangement 的复合导出；0–6 秒为短促源事件，8–20 秒为稳定十音多频，66–72 秒为末段动态事件。
- 工程快照：`validation/host/snapshots/0072a637f389--FabFilter-Saturn-2 Project/5d8d036ccd33--FabFilter-Pro-DS.als`。

| 指标 | Wide + LA 12 ms | Split + LA 12 ms | Wide + LA Off |
|---|---:|---:|---:|
| 宿主报告延迟 | 720 samples | 1232 samples | 0 samples |
| 0–6 s 区域电平差 | -1.086260 dB | -0.957434 dB | -0.000000 dB |
| 0.50 s 短事件 | -1.158393 dB | -1.022176 dB | -0.000001 dB |
| 2.50 s 短事件 | -0.992285 dB | -0.876841 dB | -0.000000 dB |
| 4.50 s 短事件 | -0.747308 dB | -0.661717 dB | +0.000002 dB |
| 8–20 s 稳定多音 | -0.000000 dB | -0.000000 dB | -0.000000 dB |
| ≥0.05 dB 衰减的活跃 50 ms 窗 | 3/1037 | 3/1037 | 0/1037 |

## 操作观察与工作流

- 单主唱先以 `Single Vocal + Wide` 作基线：先听检测是否只抓目标辅音，再决定是否换 Split；本轮 Wide 比 Split 多约 0.09–0.14 dB 的整体短事件衰减，但没有足够的频谱/盲听证据宣称哪一个更自然。
- 用 Trigger/Sidechain Audition 调检测范围，而不是先把 Threshold 压到底。稳定多音不触发说明 Single Vocal 有内容分类；测试它应使用真实或标注过的语音事件，不应只依赖扫频/多音。
- Range 与 Threshold 分工：Threshold 决定何时动作，Range 限制最深衰减。实际主唱先从 Range 2–4 dB、Lookahead 5–10 ms 开始，最坏 S 仍跳出再逐步增加；这些是工作流起点，不是本轮实测最优值。
- 若辅音起始漏过，先检查 Lookahead 模块是否真正启用，再增加时间。当前实例中旋钮 0 ms 与模块 Off 不是同一延迟状态。
- Split 会额外增加 512 samples 延迟。若目的只是“保住低频主体”，要在宿主 PDC、等响和句首/句尾上下文中 A/B；不要把 Split 当作免费透明升级。
- 在 Air EQ/Exciter 前先做轻度去齿；若后级又制造出尖锐边缘，可在链尾第二阶段只削 1–2 dB。多级 Pro-DS、动态 EQ 和 soothe 叠加时要逐个旁通，防止 lisp 与整体暗化。

## 边界与未验证项

- L3 只覆盖本机 VST3 Stereo 1.21、48 kHz、默认 Threshold/Range、Single Vocal、Wide/Split、Lookahead 12 ms/Off 与少量 Oversampling 延迟探针。
- 复合夹具不是标注语料库；短事件没有逐音素 S/T/CH 标签，不能计算真实人声的 Precision/Recall，也不能评判 lisp、自然度或可懂度。
- Wide/Split 的本轮频带 FFT 在稀疏短窗中受窗函数与底噪影响，不作为“全频衰减”或“只衰减高频”的独立量化证明；两模式的语义仍以官方资料和界面定义为 L2 来源。
- 未测 Allround、Threshold/Range 扫描、侧链 HP/LP 精确标度、Trigger/Sidechain Audition 输出、外部侧链、Mid/Side/Stereo Link 单变量、Mono、自动化、CPU、其它格式/采样率/版本或真实主唱等响盲听。
- 导出区间是复合 Arrangement，文件名沿用 `multitone` 前缀；报告明确披露实际区域，避免把整段结果误称为纯多音测试。

## 证据

- 旁路 SHA-256：`75d2b8e2b10b567ec407e3fd7da2ed53d4f58885df768c58ddd69c526ecec5ce`。
- Wide + Lookahead 12 ms SHA-256：`0e664b38c41f885d8a4546d7f452b1b19508ff350e02c037ecf4f1dd78e2809c`。
- Split + Lookahead 12 ms SHA-256：`a509ba26fee7a063306b6d3bc8939659038d8b2a22db65933afad7dd614cc198`。
- Wide + Lookahead Off SHA-256：`dc0e357a7bcd05503cb7957e8c05b1a7bd4eabbf9172f7a0c10d56888b16fecc`。
- 工程快照 SHA-256：`24674094d6f8a0f741e6abdd46e2e9caef3328369a28c4364ddb69fae0212f3d`。
- 量化：`validation/results/5d8d036ccd33--composite-deesser-wide-split-lookahead.json`。
- 测量脚本：`validation/scripts/analyze_deesser.py`。
