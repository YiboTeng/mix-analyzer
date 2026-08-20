---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: 497c2536aeff
product: Pro-Q 3
evidence_level: L3
test_id: multitone-parametric-eq-phase-modes
---

# FabFilter Pro-Q 3：默认透明性、Bell 传递与三种相位模式验证

## 结论

本机 FabFilter Pro-Q 3 VST3 已在 Ableton Live 11.3.43、48 kHz 中真实加载。About 界面回读为 `FabFilter Pro-Q 3 version 3.23 (64-bit), June 29, 2023`；文件系统产品族记录为 3.2.3.0。`Default Setting` 实见无频段、Output `0.0 dB`、Analyzer `Pre+Post+SC`、全局 `Zero Latency`，宿主设备栏报告 `Latency: 0 samples`。

默认平直态对独立旁路导出直接相关 `1.0`、最佳整数偏移 `0 samples`、RMS/峰值差均约 `0 dB`；十个输入频点的增益和相位均为 `0.000 dB / 0°`，残差约 `-141.481 dBFS`。因此本机当前默认态在该 24-bit+dither 测试分辨率内可视为透明控制；这不是所有隐藏状态、格式、采样率或自动化路径的逐位证明。

建立一个 Stereo Bell，界面回读 `1763.0 Hz / +6.00 dB / Q 1.000`。夹具最近输入音为 1760 Hz，中心偏差 3 Hz（0.17%）；三种模式在 1760 Hz 实测分别为 `+5.999963`、`+6.000002`、`+5.999889 dB`。半频 880 Hz 约 `+2.821–2.822 dB`，倍频 3.52 kHz 约 `+2.826–2.838 dB`，证明当前 Bell 的中心增益与 Q=1 宽度方向符合界面设定。

Zero Latency 与 Natural Phase 都呈频率相关相位：Zero 在 880/1760/3520 Hz 为 `+19.467/+0.284/-18.994°`，Natural 为 `+19.373/+0.098/-19.379°`。Natural 相对 Zero 的幅度差在十个频点最大约 `0.022 dB`，但高频相位继续分离，到 16 kHz 为 `-2.451°`；它不是“零延迟同一算法的改名”。Linear Phase Medium 的十个频点相位均在约 `±0.000005°` 内，同时保留同一幅度曲线。

宿主报告延迟为 Zero `0 samples`、Natural `320 samples (6.7 ms)`、Linear Phase Medium `5120 samples (106.7 ms)`。Ableton PDC 后，所有处理态对旁路的最佳整数偏移仍为 `0 samples`。Linear 的全段峰值只比旁路高 `+1.303 dB`，低于 Zero 的 `+1.865 dB`，说明时间域峰值被重新分布；本轮没有脉冲/扫频，不能仅凭此宣称前振铃可闻。

## 固定状态与量化

- 插件：FabFilter Pro-Q 3 3.23 (64-bit; June 29, 2023)，VST3 Stereo。
- 宿主：Ableton Live 11.3.43；160 BPM；48 kHz。
- 默认：`Default Setting`、无频段、Output 0.0 dB、Analyzer Pre+Post+SC、Zero Latency。
- 单变量：建立 Stereo Bell `1763.0 Hz / +6.00 dB / Q 1.000`；仅切换全局 Zero Latency、Natural Phase、Linear Phase Medium。
- 导出：Master、32.1.1–40.1.1、12 s、48 kHz/24-bit WAV、Normalize Off、Triangular host dither。
- 夹具：`multitone_48k.wav`，双单声道 55/110/220/440/880/1760/3520/7040/12000/16000 Hz。
- 工程快照：`validation/host/snapshots/0072a637f389--FabFilter-Saturn-2 Project/497c2536aeff--FabFilter-Pro-Q-3.als`。

| 全局指标 | 默认 vs 旁路 | Bell Zero vs 旁路 | Bell Natural vs 旁路 | Bell Linear Medium vs 旁路 |
|---|---:|---:|---:|---:|
| 宿主报告延迟 | 0 samples | 0 samples | 320 samples | 5120 samples |
| PDC 后最佳整数偏移 | 0 | 0 | 0 | 0 |
| RMS 电平差 | -0.000 dB | +1.863880 dB | +1.869503 dB | +1.869500 dB |
| 峰值差 | 0.000 dB | +1.865195 dB | +1.894595 dB | +1.302784 dB |
| 直接相关 | 1.000000000000 | 0.952212851660 | 0.951180956622 | 0.970550707970 |
| 残差 RMS | -141.481 dBFS | -28.345 dBFS | -28.271 dBFS | -29.631 dBFS |
| L-R 残差 RMS | -141.481 dBFS | -141.486 dBFS | -141.462 dBFS | -141.482 dBFS |

| 频率 | Zero 增益 / 相位 | Natural 增益 / 相位 | Linear Medium 增益 / 相位 |
|---:|---:|---:|---:|
| 55 Hz | +0.013 dB / +1.785° | +0.013 dB / +1.779° | +0.013 dB / 0.000° |
| 110 Hz | +0.050 dB / +3.556° | +0.050 dB / +3.544° | +0.050 dB / 0.000° |
| 220 Hz | +0.201 dB / +7.001° | +0.201 dB / +6.977° | +0.201 dB / 0.000° |
| 440 Hz | +0.783 dB / +13.124° | +0.783 dB / +13.077° | +0.783 dB / 0.000° |
| 880 Hz | +2.821 dB / +19.467° | +2.822 dB / +19.373° | +2.822 dB / 0.000° |
| 1.76 kHz | +6.000 dB / +0.284° | +6.000 dB / +0.098° | +6.000 dB / 0.000° |
| 3.52 kHz | +2.826 dB / -18.994° | +2.838 dB / -19.379° | +2.838 dB / 0.000° |
| 7.04 kHz | +0.767 dB / -12.171° | +0.788 dB / -13.114° | +0.788 dB / 0.000° |
| 12 kHz | +0.257 dB / -6.397° | +0.277 dB / -8.148° | +0.277 dB / 0.000° |
| 16 kHz | +0.144 dB / -3.739° | +0.157 dB / -6.189° | +0.157 dB / 0.000° |

## 操作观察与工作流

- 常规单轨修正先用 Zero Latency：当前实例不增加宿主延迟，且静态 Bell 的幅度目标准确；先在 Solo/频谱中定位，再回全混音确认，不以峰值图替代听感。
- Natural Phase 的幅度曲线与 Zero 很接近，但宿主增加 320 samples，且高频相位并不完全相同。只有低频/高 Q 或并行相位确有问题时才值得 A/B，不应把标签理解成“免费升级”。
- Linear Phase Medium 在稳态十音上保持近零相位，但增加 5120 samples；适合必须保持跨频率相位对齐的离线/总线问题验证，不适合作为实时追踪或普通人声修正默认值。
- 比较不同模式时必须让 DAW PDC 开启并等响。当前三种 Bell 的整段 RMS 约高 1.87 dB；若直接旁通，更响会偏向处理态。
- 动态 EQ、外部侧链、M/S 与 per-band placement 是 Pro-Q 3 的主要价值，但本轮只验证静态 Stereo Bell；实际去齿/共振应从小 Range 开始，并单独观察触发范围、音素稳定性与单声道。
- 线性相位的峰值变化不能只看稳态频响解释。要评估前振铃，需用脉冲/短字头、不同 Linear 分辨率和等响盲听；本轮只固定了 Medium 的延迟与稳态相位。

## 边界与未验证项

- L3 只覆盖本机 VST3 Stereo 3.23、48 kHz、Default Setting，以及一个 1763 Hz/+6 dB/Q1 Bell 的三种全局模式。
- Bell 中心与夹具 1760 Hz 相差 3 Hz；实测中心增益仍为 +6.000 dB，但不把它伪写成完全同频设定。
- 未测 Dynamic Range/Threshold/Auto、外部侧链、Band Solo、Spectrum Grab、Collision、M/S/L/R placement、其它 filter shape/slope/Q/gain、per-band phase、Auto Gain、输出 Trim 或自动化。
- 未做脉冲、扫频、非八度多音、aliasing、CPU、其它 Linear Phase 分辨率、其它采样率、Mono/VST2/AU/AAX 或真实人声等响盲听。
- Linear steady-state 近零相位不等于“听感必然更好”；5120 samples 与可能的前振铃是独立代价，本轮未量化其可闻性。

## 证据

- 旁路 SHA-256：`aaf2513cd42bfa3f79a3223ae0a627c0660b8dbab4d9c18cba365fb6ba9a65ed`。
- 默认 SHA-256：`67e6a6718e2883521a6a4f2a3b093195411b91ea0624d5038b51475da3a975c0`。
- Bell Zero SHA-256：`bbe3fc1103d99233acfc5c65d680aab2e75826483de7e3c872e04948503ca0a4`。
- Bell Natural SHA-256：`f8ead09b53aa7d4e025f35e4c4a33cd77057fa56b2fba6c8235de30c109628a4`。
- Bell Linear Medium SHA-256：`feb2c94d78a8cdc4b5cd985cbcc63039b1daf78416eba24a60d17021e2b7e071`。
- 工程快照 SHA-256：`438daae42ecbf5763cbbf1ae3bd5fd590f9e6bcbc29a2d375eaae49d9a12bc89`。
- 量化：`validation/results/497c2536aeff--multitone-parametric-eq-phase-modes.json`。
- 测量脚本：`validation/scripts/analyze_eq.py`。
