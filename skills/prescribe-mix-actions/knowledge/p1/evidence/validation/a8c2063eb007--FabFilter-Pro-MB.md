---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: a8c2063eb007
product: Pro-MB
evidence_level: L3
test_id: composite-multiband-single-band-lookahead
---

# FabFilter Pro-MB：单频段压缩与全局 Lookahead 验证

## 结论

本机 FabFilter Pro-MB `1.2.8.0` VST3 Stereo 已在 Ableton Live 11.3.43、48 kHz 中真实加载。`Default Setting` 回读为无频段、Dynamic Phase、Oversampling Off、全局 Lookahead On、Analyzer Pre+Post、Mix 100%、Output 0 dB。虽没有频段，Ableton 仍报告 `960 samples / 20 ms` 延迟；其音频对共享旁路在三个主区域均约 0 dB、相关约 1.0、残差约 `-141.5 dBFS`。这说明当前默认态音频近似中性，但全局 Lookahead 仍预留完整延迟。

建立一个中心 `1720.8 Hz` 的 Compress 频段，固定 Threshold `-32.10 dB`、Range `-6.00 dB`、Ratio `4.00:1`、Knee `24.00 dB`、Attack/Release `20.0%`、Output `0.00 dB`、band Lookahead `1.000 ms`。全局 Lookahead On 时，三个 50 ms 稀疏短事件相对默认分别约 `-0.228266/-0.148266/-0.030818 dB`；全局 Off 时约 `-0.000001/-0.000001/-0.000006 dB`。它直接证明全局开关会改变短事件捕获，而非只有延迟标签变化。

稳定十音区域整体变化很小：Lookahead On/Off 相对默认约 `-0.001676/-0.000919 dB`；但频点结果存在频率相关正负变化。十个谐波相关音调同时进入一个动态、多段滤波器，不能把这些 FFT 点当成单独正弦扫频或静态分频曲线。66–72 秒动态区整体约 `-0.003272/-0.004455 dB`，局部高电平窗 On/Off 约最低 `-0.108/-0.148 dB`；当前固定 Threshold 与夹具只产生轻度动作，不代表 Range `-6 dB` 必然达到。

全局 Lookahead On 时 Ableton 始终报告 `960 samples / 20 ms`，即使 band Lookahead 仅显示 `1.000 ms`；关闭全局 Lookahead 后宿主报告 `0 samples`，频段 Lookahead 控件同时灰显。全局延迟预算、每段预读数值和实际动态动作必须分别记录。

## 可执行工作流

- 先创建一个必要频段，用 Solo/频谱定位，再以 Range 规定最多动作量；Threshold 只降到问题音素稳定触发。Range 不是目标 GR。
- 录音监听或低延迟场景先检查顶部全局 Lookahead 开关与 DAW 报告延迟；只把 band Lookahead 旋到 1 ms 并不会把本机全局延迟从 20 ms 降到 1 ms。
- 捕捉快速齿音、爆发或硬辅音时对同一状态 A/B 全局 Lookahead On/Off；本轮短事件只有 On 明显动作。若要保留字头，可关闭或减少预读，并重新校准 Threshold、Attack 与 Range。
- 动态相位作为常规起点；只有相位叠加、离线线性相位或最低延迟有明确需求时，再单变量比较 Linear/Minimum Phase。
- 比较时做外部等响，并同时看问题音素、正常元音和无声/呼吸区；不要依据某个多音 FFT 点或面板 Range 推断完整听感。

## 边界与未验证项

- L3 只覆盖本机 `1.2.8.0` VST3 Stereo、48 kHz、无频段默认态、一个 1720.8 Hz Compress 频段和全局 Lookahead On/Off。
- 共享旁路来自同一编排、加载 Pro-MB 前的独立导出；Ableton PDC 已对齐，Triangular dither 使逐比特空差不成立。
- 未测频段边界的精确传输、专用单音扫频、Expand/向上模式、外部侧链、Minimum/Linear Phase、Oversampling、Stereo Link/M/S、自动化、CPU、Mono、其它格式/采样率或真实人声等响盲听。
- 当前固定 Threshold 在动态区只产生轻度动作；不能据此反推完整 Ratio、Knee、Attack/Release 曲线，也不能把 `-6 dB` Range 写成实际 GR。

## 证据

- 共享旁路 SHA-256：`38a74287a951ad7a62a6abeb219aa91afdd0e4f2abde062b972361851e0de16f`。
- 无频段默认 SHA-256：`b4117392811b1aaec185e0e59edc807dfe0e2717ca25f82084685f66ccdb9e7a`。
- 单频段 / 全局 Lookahead On SHA-256：`0359eb74f5898f833e8f03ef2709e3f0b9f79567a0c3324f6f4eb0b75688dc8d`。
- 单频段 / 全局 Lookahead Off SHA-256：`218d701e831909a78c50008b9a75bf4c10c2cec2af0ceeb68b65692a4df71502`。
- 工程快照 SHA-256：`9da2aa84339d4b789c20613620cfe187ef4376b1778f0ce1d67d2d6d4bd84fef`。
- 量化：`validation/results/a8c2063eb007--composite-multiband-lookahead.json`。
- 测量脚本：`validation/scripts/analyze_multiband_dynamics.py`。

