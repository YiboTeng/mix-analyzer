---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: 0072a637f389
product: Saturn 2
evidence_level: L3
test_id: impulse-default-warm-tape
---

# FabFilter Saturn 2：默认 Warm Tape 单段脉冲传输验证

## 结论

本机 FabFilter Saturn 2 2.0.8 VST3 在 Ableton Live 11.3.43 的真实默认实例中为单频段 `Warm Tape`，`Linear Phase` 与 `High Quality` 均未启用，Global Mix 100%，Output 0.0 dB；宿主设备栏报告 `Latency: 0 samples`。固定三电平脉冲经 6 秒离线导出后，最佳整数延迟仍为 0 samples，但峰值传输呈明确电平依赖：输入 -1.938/-6.021/-12.041 dBFS 时，输出峰值为 -8.530/-10.371/-15.424 dBFS，相应峰值增益 -6.591/-4.351/-3.382 dB，三档范围 3.209 dB。这说明默认 Warm Tape 已在零 Drive 显示位置下对强瞬态产生逐级更明显的软化，不能把“默认/Drive 中心”当作中性旁通。

全局直接相关 0.673004，RMS 电平差 -2.272077 dB，残差 RMS -57.351078 dBFS；每个脉冲峰值位置均保持 0 samples 偏移，左右输出相关 0.999999975770。强、中、弱三次脉冲后 85.3 ms 窗内，核心九样本以外的能量占 2.507%、1.867%、1.668%，证明默认模型同时产生短时响应扩展；这些数字只描述本固定脉冲，不等价于稳态 THD、磁带噪声或听感优劣。

## 固定状态与量化

- 插件：FabFilter Saturn 2，本机文件清单版本 2.0.8.0，真实实例标题 `Saturn 2`，VST3。
- 默认界面：单频段 `Warm Tape`；Linear Phase 关闭；High Quality 关闭；Global Mix 100%；Output 0.0 dB；未增加 Band、调制源或反馈。
- 输入：实际使用 `impulse_train_48k.wav`，不是轨道名称中残留的 `multitone`；夹具位于 2.1.1，Host 160 BPM，Warp 关闭。
- 导出：Master、2.1.1 起、4.0.0 长（6 s）、48 kHz/24-bit WAV、Triangular dither、Normalize 关闭。
- 工程快照：`validation/host/snapshots/0072a637f389--FabFilter-Saturn-2.als`。

| 全局指标 | 结果 |
|---|---:|
| 宿主报告插件延迟 | 0 samples |
| 最佳整数延迟 | 0 samples / 0.000000 ms |
| 直接相关系数 | 0.673004248642 |
| RMS 电平差 | -2.272077 dB |
| 残差 RMS | -57.351078 dBFS |
| 左右输出相关 | 0.999999975770 |
| 三档峰值增益范围 | 3.209055 dB |

| 脉冲输入 | 输出峰值 | 峰值增益 | 峰值偏移 | 核心外能量占比 |
|---:|---:|---:|---:|---:|
| -1.938333 dBFS | -8.529749 dBFS | -6.591416 dB | 0 samples | 2.5071% |
| -6.020600 dBFS | -10.371353 dBFS | -4.350753 dB | 0 samples | 1.8670% |
| -12.041200 dBFS | -15.423561 dBFS | -3.382361 dB | 0 samples | 1.6675% |

## 操作观察与工作流

- 默认 Warm Tape 已显著压低大瞬态，且输入越强衰减越大；因此实际人声上应先从默认单段开始，匹配处理前后 Active RMS/LUFS，再判断“更密、更稳”是否来自谐波/包络而不是单纯降峰或电平变化。
- 当前默认无宿主延迟，适合先做低风险实时 Insert 基线；这不证明 Good 8x、Superb 32x、Linear Phase、多段分频或调制仍为零延迟。
- 单段已经产生可量化的瞬态软化和短响应尾。只有当某一频带确实需要独立 Drive/Tone/Dynamics 时才增加 Band；否则多段会把分频、相位、OS 与电平变量同时引入。
- Global Mix 100% 让本次传输归因于处理路径。人声实用起点可保持全湿、低 Drive 后用 Output 等响；若需并行，优先复制轨/Aux 或明确记录 Global Mix，避免把内部并行与外部 Send 混写。
- 本次强脉冲峰值下降 6.59 dB，说明默认状态对爆破、硬辅音和已接近满幅的峰值并非温和。真实主唱应先给足前级余量，并在饱和后复查齿音、字头与后级压缩触发。

## 边界与未验证项

- 本轮使用脉冲而非原矩阵建议的 multitone；它足以验证默认瞬态传输、延迟与短响应，但未测稳态谐波阶次、THD、别名或频响。因此只将“默认 Warm Tape 单段主行为”判定 L3，不宣称全部 Saturn 2 模式已经校准。
- 未量化 Style 切换、Drive 曲线、Tone、Dynamics、Feedback、Band Mix、M/S、调制、双段/六段分频、Good 8x、Superb 32x、Linear Phase、CPU 或自动化。
- 源文件为 8 秒 PCM16，候选渲染为 6 秒 PCM24；分析只使用共同前 6 秒。独立 Triangular dither 会贡献极低随机底噪，但不能解释 3.209 dB 的电平依赖峰值传输。
- `Latency: 0 samples` 只覆盖本机 VST3 默认 HQ/Linear 关闭状态；不得外推到其它质量模式、采样率、宿主或 Studio One。
- 本轮没有进行等响盲听；量化结果不构成 Warm Tape 优于其它 Style 的判断。

## 证据

- Saturn 2 渲染 SHA-256：`7bfa940dfdae7bff937b5e318433892874499941a3c340db298db4421489fab9`。
- 固定脉冲 SHA-256：`aafbd0a42ee57fde77b79aae591d54f87383b391e76803af9405757f92e3cf2e`。
- 量化：`validation/results/0072a637f389--impulse-default-warm-tape.json`。
- 测量脚本：`validation/scripts/analyze_saturation.py`。
