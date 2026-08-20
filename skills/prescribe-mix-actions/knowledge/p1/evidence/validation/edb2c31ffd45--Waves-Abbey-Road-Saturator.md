---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: edb2c31ffd45
product: Abbey Road Saturator
evidence_level: L3
test_id: impulse-default-tg
---

# Waves Abbey Road Saturator：默认 TG 路径脉冲传输验证

## 结论

本机 Waves Abbey Road Saturator 12.7.0.209 `Abbey Road Saturator Stereo` VST3 在 Ableton Live 11.3.43 的真实默认实例中加载为 `A: Default Preset`，Saturator 选择 TG、Saturator Mix 100%，Pre EQ 与 Post EQ 均启用且增益旋钮保持中心；宿主设备栏报告 `Latency: 49 samples (1.02 ms)`，与 Waves 对 44.1/48 kHz 的官方 49-sample 声明一致。

固定三电平脉冲经 6 秒离线导出后，峰值传输呈强烈电平依赖：输入 -1.938/-6.021/-12.041 dBFS 时，输出峰值为 -11.243/-10.887/-11.804 dBFS，相应峰值增益 -9.305/-4.866/+0.237 dB，三档范围 9.542 dB。默认 TG 路径因此不是线性增益或中性旁通；高电平瞬态被明显压平，而较低电平脉冲接近保持并略有提升。

全局直接相关 0.121423，RMS 电平差 -2.020908 dB；最佳整数相关偏移为 -2 samples，但三次局部峰值分别位于 -1/0/+1 samples，均落在约 ±0.021 ms 内。这一算法相关对齐结果不能替代宿主 PDC 数值：宿主显示的 49 samples 是插件延迟声明，导出音频已经过宿主补偿。左右输出相关 0.999999998260，说明这组左右相同输入在默认 Stereo/TG 状态下仍基本保持同相。

## 固定状态与量化

- 插件：Waves Abbey Road Saturator 12.7.0.209，真实实例 `Abbey Road Saturator Stereo`，VST3。
- 默认界面：`A: Default Preset`；ST 输入、OUT 计量；Pre EQ 与 Post EQ 开启且各增益旋钮保持中心；Compander Ratio 视觉约 2.5、Blend 视觉接近 100%；Saturator 选 TG、Gain 视觉约中位、Mix 显示 100.0。视觉未显示精确数字的旋钮只作为界面观察，不写成精确参数值。
- 输入：实际使用 `impulse_train_48k.wav`，不是轨道名称中残留的 `multitone`；夹具位于 2.1.1，Host 160 BPM，Warp 关闭。
- 导出：Master、2.1.1 起、4.0.0 长（6 s）、48 kHz/24-bit WAV、Triangular dither、Normalize 关闭。
- 工程快照：`validation/host/snapshots/edb2c31ffd45--Waves-Abbey-Road-Saturator.als`。

| 全局指标 | 结果 |
|---|---:|
| 宿主报告插件延迟 | 49 samples / 1.02 ms |
| 最佳整数相关偏移 | -2 samples / -0.041667 ms |
| 直接相关系数 | 0.121423364644 |
| RMS 电平差 | -2.020908 dB |
| 残差 RMS | -54.565594 dBFS |
| 左右输出相关 | 0.999999998260 |
| 三档峰值增益范围 | 9.541966 dB |

| 脉冲输入 | 输出峰值 | 峰值增益 | 局部峰值偏移 | 核心外能量占比 |
|---:|---:|---:|---:|---:|
| -1.938333 dBFS | -11.242864 dBFS | -9.304531 dB | -1 sample | 38.8002% |
| -6.020600 dBFS | -10.886988 dBFS | -4.866388 dB | 0 samples | 24.8594% |
| -12.041200 dBFS | -11.803764 dBFS | +0.237435 dB | +1 sample | 10.3594% |

## 操作观察与工作流

- 默认 TG 已对强瞬态做非常明显的电平依赖压平；把它用于主唱 Insert 时，先保证输入峰值余量，再用 Output 做等响。若不等响，峰值下降与 RMS 变化会掩盖真正的谐波/密度收益。
- 默认 Saturator Mix 为 100%，因此本次结果描述完整处理路径。实际主唱若只需质感，可先用 10–30% 内部 Mix 或全湿 Aux，再按 Active RMS/LUFS-S 与干声匹配；并行返回要高通低频、复查齿音和爆破。
- Pre/Post EQ 均参与默认路径；本次没有把中心旋钮位置当作精确 0 dB。做精细调校时应先固定 TG/REDD、Compander 与 Mix，再一次只改变一个 EQ 或 Gain 控制。
- 49 samples 是宿主报告的 PDC 延迟，不等同于波形中某个峰值的局部偏移；离线导出已被宿主补偿。实时录音监听、并行外部路由或其它宿主仍应重新核对。
- 强脉冲核心外能量占 38.8%，明显高于较弱脉冲的 10.4%，说明默认链不仅削峰，还产生电平相关的短时响应扩展；在人声上需重点听辅音拖尾、砂砾和低中频堆积。

## 边界与未验证项

- 本轮使用三电平脉冲而非原矩阵建议的 multitone。它验证了默认 TG 的瞬态传输、宿主延迟、短响应和通道一致性，但未测稳态谐波阶次、THD、别名、频响或噪声底。
- 未量化 REDD、Saturator Off、Compander Off/Ratio/Blend、上下 crossover、Input/Output、Pre/Post EQ 单变量、自动化、CPU 或连续人声盲听；L3 只覆盖真实默认 TG 主行为及其主要副作用。
- 源文件为 8 秒 PCM16，候选渲染为 6 秒 PCM24；分析只使用共同前 6 秒。独立 Triangular dither 会贡献极低随机底噪，但不能解释 9.542 dB 的电平依赖峰值范围。
- 左右相关接近 1 只覆盖左右相同输入和默认 Stereo 实例，不证明所有不对称输入、Mono/Stereo 组件或宽化路由都完全一致。
- 本轮没有等响音乐素材盲听；量化结果不构成 TG 优于 REDD 或优于其它饱和器的判断。

## 证据

- 候选渲染 SHA-256：`f31397ebe55c3035de5ab4906ea48d77584c756320cc5345e833fa0bdac48766`。
- 固定脉冲 SHA-256：`aafbd0a42ee57fde77b79aae591d54f87383b391e76803af9405757f92e3cf2e`。
- 工程快照 SHA-256：`96aa887d08d405a34d1b885f1e504a72b3ff2fcce4a01609231cfff63b72f0ef`。
- 量化：`validation/results/edb2c31ffd45--impulse-default-tg.json`。
- 测量脚本：`validation/scripts/analyze_saturation.py`。
