---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: a094b33b301c
product: Scheps Omni Channel
evidence_level: L3
test_id: multitone-channel-strip-pre-saturation
---

# Waves Scheps Omni Channel：Full Reset 中性与 HEAVY Drive 单变量验证

## 结论

本机 Waves `Scheps Omni Channel Stereo` V12（文件系统版本 12.7.0.209）已在 Ableton Live 11.3.43、48 kHz 中真实加载；该实例是原版 Scheps Omni Channel，不是 Omni Channel 2。设备栏报告 `Latency: 0 samples`。`A: Full Reset` 实见 Pre Drive 0.0、Pre Saturation Off、Gate Threshold -144 dB、两段 DS² Threshold -48 dB、四段 EQ Gain 0 dB、Compressor VCA/Threshold -50 dB/Ratio 1:1、Input/Output 0 dB、Limiter Off。

`Full Reset` 对旁路的最佳整数偏移为 0 samples、相关系数 1.0、电平与峰值差均为 0 dB；互差 RMS -141.483962 dBFS、峰值 -132.453198 dBFS，落在两次独立 24-bit Triangular dither 的底噪量级。因此它可作为本机原版实例的近似中性起点，但该结论只覆盖当前状态、采样率和输入。

选择 `HEAVY` 后，即使 Drive 仍为 0.0，也相对 Full Reset 增加 0.504912 dB RMS 和 0.501807 dB Peak；十个测试音增益均约 +0.505 dB，非输入音调能量比从 -81.352696 dB 升到 -77.675508 dB。故 `HEAVY Drive 0` 不是中性旁通，比较饱和模式前必须先做输出等响。

在 HEAVY 模式中只把 Drive 从 0.0 改为 3.2 后，RMS 再增加 0.105300 dB、Peak 再增加 0.099415 dB，十个测试音均约增加 0.105 dB；非输入音调能量比升至 -70.455203 dB，即相对 Drive 0 增加 7.220305 dB。该低电平、低驱动结果支持“Drive 增加了可测非线性成分”，但八度相关多音会让谐波落回既有测试频率，不能据此分离谐波阶数、THD 或别名。

## 固定状态与量化

- 插件：Waves `Scheps Omni Channel Stereo` V12，文件系统版本 12.7.0.209，VST3 Stereo。
- 宿主：Ableton Live 11.3.43；160 BPM；48 kHz；观测设备栏 0 samples。
- 夹具：12 s 双单声道十音 `multitone_48k.wav`，两端 0.5 s fade。
- 导出：Master、48 kHz/24-bit WAV、Normalize Off、Triangular dither。
- 基线：`A: Full Reset`，全部可见处理模块处于中性/旁通语义状态。
- 模式变体：Full Reset → HEAVY，Drive 保持 0.0。
- 有效单变量：HEAVY Drive 0.0 → 3.2；其余可见控制固定。
- 工程快照：`validation/host/snapshots/0072a637f389--FabFilter-Saturn-2 Project/a094b33b301c--Waves-Scheps-Omni-Channel.als`。

| 比较 | 延时 | 相关 | RMS 电平差 | Peak 差 | 互差 RMS | 非输入音调能量比 |
|---|---:|---:|---:|---:|---:|---:|
| Full Reset vs 旁路 | 0 samples | 1.000000000 | -0.000000 dB | 0.000000 dB | -141.483962 dBFS | -81.352696 dB |
| HEAVY Drive 0 vs 旁路 | 0 samples | 0.999999994 | +0.504912 dB | +0.501807 dB | -45.252090 dBFS | -77.675508 dB |
| HEAVY Drive 3.2 vs 旁路 | 0 samples | 0.999999953 | +0.610212 dB | +0.601222 dB | -43.553502 dBFS | -70.455203 dB |
| HEAVY Drive 3.2 vs HEAVY Drive 0 | 0 samples | 0.999999980 | +0.105300 dB | +0.099415 dB | -58.562684 dBFS | +7.220305 dB 相对变化 |

| 频率 | HEAVY Drive 0 vs Full Reset | Drive 3.2 vs Drive 0 |
|---:|---:|---:|
| 55 Hz | +0.504865 dB | +0.105210 dB |
| 110 Hz | +0.504948 dB | +0.105370 dB |
| 220 Hz | +0.505032 dB | +0.105529 dB |
| 440 Hz | +0.505032 dB | +0.105529 dB |
| 880 Hz | +0.505032 dB | +0.105529 dB |
| 1760 Hz | +0.505032 dB | +0.105529 dB |
| 3520 Hz | +0.504865 dB | +0.105210 dB |
| 7040 Hz | +0.504781 dB | +0.105051 dB |
| 12000 Hz | +0.504669 dB | +0.104839 dB |
| 16000 Hz | +0.504697 dB | +0.104892 dB |

所有测试音相位差在本次精度内约为 0°；处理态 L-R 残差约 -141.48 dBFS，只支持当前双单声道夹具下左右一致，不能替代 Stereo/M/S/Duo 路由测试。

## 操作观察与工作流

- 从 `Full Reset` 建立可解释基线，再一次只启用一个模块或一种饱和模式。不要从全开预设反推每个模块的贡献。
- 比较 ODD/EVEN/HEAVY 时，先把 Output 匹配到旁路；本机 HEAVY 在 Drive 0 已自带约 +0.5 dB 宽带抬升，未等响 A/B 会偏向更响的一侧。
- 调 Drive 时同时观察输入余量、输出峰值和非输入频谱。低电平下 0→3.2 已能测到非线性成分上升；高电平或更大 Drive 不能按本轮数值线性外推。
- 模块顺序改变会同时改变下游 Compressor、DS²、Gate 和 Pre 的驱动。每次只移动一个模块，重新校准阈值和输出，再比较音节、齿音与峰值。
- `Full Reset` 是本机验证基线，不是所有预设的“零处理保证”；载入任意预设后都应重新回读饱和、阈值、EQ、压缩比、Limiter 和 Input/Output。
- 本机原版可见 PRE/GATE/DS²/EQ/COMP、可重排模块、Insert、Stereo/M/S/Duo 控制；Omni Channel 2 的 CRUSH、SOFT、24 dB Filter 与第三方 VST3 Host 不属于本实例。

## 边界与未验证项

- L3 只覆盖本机原版 V12 VST3 Stereo、Full Reset、HEAVY Drive 0.0 与 3.2、一个输入电平、48 kHz 和 0-sample 宿主报告。
- 未验证 ODD/EVEN、HEAVY 高驱动、Thump、Filters、Gate/Expander、DS²、四段 EQ、VCA/FET/OPT Compressor、Limiter、模块顺序、Insert、Stereo/M/S/Duo、VST2/Mono、其它采样率、自动化、CPU 或连续人声盲听。
- 多音频率呈八度关系；非输入音调能量包含 dither、泄漏和未落在测试频点的非线性成分，不能解释为标准 THD、谐波阶数或 aliasing 指标。
- Ableton 长导出曾因导出起点字段不同产生 10.5 s（160 BPM 下 7 bars）时间线偏移；四个正式 12 s 文件均由确定性窗口恢复并校验相同夹具，不把原始长文件起点差异解释为插件延迟。

## 证据

- 旁路 SHA-256：`bb9b5ef9d4f729e63f943134619a3357a14bd521e164d6f2d9a139f3faf29de3`。
- Full Reset SHA-256：`4e043d9aab31aa4a399e5430335fe971471d6597dfc772fad38e594ab3062921`。
- HEAVY Drive 0 SHA-256：`b2e84af97c9a9419863762d2dd2c4e7326b5182fa2c875cb1210d018ed2ac740`。
- HEAVY Drive 3.2 SHA-256：`72392042cdbde234e2a033b87de83c1e1d12f83c9a11b140ba694d7f7f57636e`。
- 工程快照 SHA-256：`779525251461297c58e20c279168945e03bc5ab2596175018ec470fa77c818b0`。
- 量化：`validation/results/a094b33b301c--channel-strip-pre-saturation.json`。
- 裁切脚本：`validation/scripts/crop_scheps_multitone.py`。
- 测量脚本：`validation/scripts/analyze_channel_strip.py`。

