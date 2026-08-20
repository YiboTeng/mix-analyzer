---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: 98d9ac6060f6
product: Pro-L 2
evidence_level: L3
test_id: dynamics-steps-pro-l-2-gain-drive
---

# FabFilter Pro-L 2：默认透明性与 +6 dB 驱动验证

## 结论

本机 FabFilter Pro-L 2 `2.21 (64-bit, June 29 2023)` VST3 Stereo 已在 Ableton Live 11.3.43、48 kHz 中真实加载。默认 `Default Setting` 的可见固定状态为 Gain `0.00 dB`、Output `0.0 dBTP`、True Peak Limiting On、Oversampling Off、Dither Off；宿主报告 `3115 samples / 64.9 ms` 延迟。

默认态对旁路的五档稳态增益都在 `-0.000001 dB`，峰值差为 `0 dB`、直接相关 `1.0`，只剩约 `-141.483 dBFS` 的独立宿主抖动残差。这支持“本机默认 Gain 0 在未触发限制时电平与波形中性”，但不代表插件零延迟：导出已由 Ableton PDC 对齐。

驱动态面板主读数显示 `+6.0 dB`，高精度悬停读回为 `+5.96 dB`。五档持续音的 RMS 与峰值均增加 `+5.9632 dB`，最高持续音样本峰值到 `-0.0373 dBFS`，说明前四档与最高稳态基本仍是线性驱入，不能只凭“已插入限制器”推断所有段落都在压。五个隔离瞬态相对旁路只增加约 `+1.699 dB`，相对线性 +5.96 dB 参考被削减约 `4.261 dB`，输出样本峰值约 `-1.155 dBFS`；这清楚证明当前默认算法会在尖峰处动作，而不会把持续音一律压到同一响度。

整段驱动态 RMS 比旁路高 `+5.900 dB`、样本峰值高 `+2.816 dB`，直接相关仍为 `0.998713`。因此“更响”是主要比较偏差；实际人声总线必须以插件后级 Trim 或 Unity Gain 做等响 A/B，并分别看持续音、短峰、Sample Peak 与 dBTP。WAV 的样本峰值不是独立 True Peak 证明，本轮不把 `0.0 dBTP` 面板设定误写为发布平台安全结论。

## 固定状态与量化

- 插件：FabFilter Pro-L 2 `2.21 (64-bit; June 29, 2023)`，VST3 Stereo。
- 宿主：Ableton Live 11.3.43；160 BPM；48 kHz；报告延迟 3115 samples / 64.9 ms。
- 预设：`Default Setting`。
- 固定：Output `0.0 dBTP`、True Peak Limiting On、Oversampling Off、Dither Off。
- 单变量：插件内部 Gain `0.00 dB` → 主读数 `+6.0 dB`；悬停高精度读回 `+5.96 dB`。
- 导出：Master、42.1.1–50.1.1、12 s、48 kHz/24-bit WAV、Normalize Off、Triangular host dither。
- 夹具：`dynamics_steps_48k.wav`；Ableton 自动 Warp 为 160 BPM 下 8 bars/12 s。
- 工程快照：`validation/host/snapshots/0072a637f389--FabFilter-Saturn-2 Project/98d9ac6060f6--FabFilter-Pro-L-2.als`。

| 输入峰值 | 旁路 RMS | 驱动态 RMS | 实测 RMS 增益 | 驱动态峰值 | 相对线性 +5.96 dB 的峰值变化 |
|---:|---:|---:|---:|---:|---:|
| -30 dBFS | -33.011 | -27.048 | +5.963 dB | -24.039 dBFS | +0.003 dB |
| -24 dBFS | -27.011 | -21.047 | +5.963 dB | -18.039 dBFS | +0.003 dB |
| -18 dBFS | -21.011 | -15.048 | +5.963 dB | -12.037 dBFS | +0.003 dB |
| -12 dBFS | -15.023 | -9.060 | +5.963 dB | -6.037 dBFS | +0.003 dB |
| -6 dBFS | -9.011 | -3.047 | +5.963 dB | -0.037 dBFS | +0.003 dB |

持续音 Crest Factor 变化在 `-0.000019` 至 `-0.000001 dB`，支持这些稳态窗口基本未受限制。五个隔离瞬态的结果高度一致：旁路峰值约 `-2.854 dBFS`、驱动态约 `-1.155 dBFS`、实测峰值增益约 `+1.699 dB`，相对线性驱入削减约 `4.261 dB`。驱动态整段共有 0 个样本达到 `-0.01 dBFS` 以上、9048 个样本达到 `-0.10 dBFS` 以上；这只描述离散样本，不替代 dBTP 仪表或过采样真峰值测量。

## 操作观察与工作流

- 先设 Output/True Peak，再推 Gain；不要先推响后才寻找安全 Ceiling。本轮 `0.0 dBTP` 只为测量，不是推荐发布值。
- 不用单一 GR 峰值代表整句。本轮持续音几乎完全线性通过，而隔离瞬态约被削去 4.26 dB；应同时观察典型 GR、最大 GR 与动作持续时间。
- 人声总线从 1–3 dB 偶发峰值限制起步。若主体持续被压、齿音变硬或尾字下沉，先回退 Gain，再处理前级 Clip Gain/压缩，而不是换 Style 继续追响度。
- 比较 Style、Lookahead 或 Oversampling 时，固定 Output、Gain 与输入，使用 Unity Gain/后级 Trim 等响；否则算法差异会被约 +6 dB 的响度偏差淹没。
- True Peak Limiting 已开启仍需区分 Sample Peak、dBTP 与编码后峰值。本轮最高样本峰值 `-0.037 dBFS` 不等于已证明 0.0 dBTP 的全部发布安全性。
- Dither 只在最终位深转换一次；本轮插件 Dither Off，文件中的 Triangular dither 来自宿主导出设置。

## 边界与未验证项

- L3 仅覆盖本机 Pro-L 2 2.21 VST3 Stereo、Default Setting、Output 0.0 dBTP、TP On、OS Off、Dither Off，以及 Gain 0 与界面 +6.0 dB（高精度 +5.96 dB）三态。
- Ableton 导出使用 PDC；3115 samples / 64.9 ms 是宿主报告，不是从已对齐 WAV 反推的裸延迟。
- WAV 分析只测 sample peak；未独立测量 dBTP/ISP、编码后峰值、其它 Output ceiling 或平台交付目标。
- 未验证八种 Style、Lookahead、Attack、Release、Channel Link、2–32x Oversampling、Unity Gain、Audition、Loudness meter、Dither、Mono、其它格式/采样率/版本、自动化、CPU 或盲听。
- 本轮最高持续音未明显受限；结论重点是默认未触发透明性与短峰动作，不把它外推为所有高 GR 节目下的失真/泵动表现。

## 证据

- 旁路 SHA-256：`a6008c02065b3079ec40f84584f28ac23f486eb297c66ab1a4d640b5668adaae`。
- 默认 SHA-256：`b3d5448538145d4340eb00be38ea9fc25c7d65facf0e78d77a4086219aa412e7`。
- Gain +6 显示态 SHA-256：`0619beac820ee595070a06bd1bd36cf4138894a396112a26288a2a171417bac3`。
- 工程快照 SHA-256：`d6661b6287a0b83b21d01ed80d364aaba7b8c93c628cc1830efc7d4786536c57`。
- 量化：`validation/results/98d9ac6060f6--dynamics-pro-l-2.json`。
- 测量脚本：`validation/scripts/analyze_limiter.py`。

