---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: 06fad1aad9d8
product: Vocal Bender
evidence_level: L3
test_id: fixed-vocal-pitch-minus12-formant0
---

# Waves Vocal Bender：-12 半音与默认时间响应验证

## 结论

本机 Waves `Vocal Bender Stereo` V12（文件系统版本 12.7.0.209）已在 Ableton Live 11.3.43 中真实加载。默认状态为 Pitch 0、Formant 0、Pitch/Formant 联动开启、Flatten 与 Fine 关闭、Mix 100%，宿主设备栏报告 `Latency: 0 samples`。

在解除 Pitch/Formant 联动后，将 Pitch 精确设为 -12 semitones、Formant 保持 0，以固定人声渲染。加权中位 F0 从 173.771698 Hz 降至 86.945707 Hz，频率比 0.500344463；测得 -1198.808 cents（-11.98808 semitones），相对目标 -1200 cents 的绝对误差为 1.192 cents。这个结果足以确认本机实例能稳定执行低八度命令，但不等于透明变调或听感质量评分。

默认脉冲渲染说明“zero latency”只应按宿主 PDC 语义理解。三次局部攻击峰值偏移为 0/0/1 samples，符合零或近零起音；但整段最佳相关偏移为 105 samples / 2.1875 ms、最佳相关仅 0.693373，三档峰值分别被压低 -5.256/-5.089/-4.805 dB，并出现可测短时扩散。因此它没有固定可补偿延迟，却也不是时间域透明旁通。

## 固定状态与量化

- 插件：Waves `Vocal Bender Stereo` V12，文件系统版本 12.7.0.209，VST3。
- 默认界面：Pitch 0、Formant 0、Link 开启、Flatten/Fine 关闭、Mix 100；底部可见 M1、M2、AM、PT 调制入口，PT 为默认亮起状态；Preset=`Full Reset`。
- 处理状态：关闭 Link；Pitch=-12 semitones；Formant=0；Mix=100；其余保持默认。
- 人声输入：`fixed_vocal_reference.wav`；Arrangement 从 14.1.1 开始，固定导出 16.0.0（24 s）。
- 脉冲输入：`impulse_train_48k.wav`；从 2.1.1 开始，导出 4.0.0（6 s）。
- 导出：Master、48 kHz/24-bit WAV、Triangular dither、Normalize 关闭。
- 工程快照：`validation/host/snapshots/0072a637f389--FabFilter-Saturn-2 Project/06fad1aad9d8--Waves-Vocal-Bender.als`。

| Pitch 指标 | 结果 |
|---|---:|
| Reference 加权中位 F0 | 173.771698 Hz |
| Candidate 加权中位 F0 | 86.945707 Hz |
| 中位频率比 | 0.500344463 |
| 实测移调 | -1198.808 cents / -11.98808 st |
| 目标移调 | -1200.000 cents / -12.00000 st |
| 绝对误差 | 1.192 cents |
| Reference/Candidate 有声帧 | 652 / 492 |
| Reference/Candidate 平均置信度 | 0.938469 / 0.824220 |

| 默认脉冲指标 | 结果 |
|---|---:|
| 宿主报告插件延迟 | 0 samples |
| 三次局部攻击峰值偏移 | 0 / 0 / 1 samples |
| 整段最佳相关偏移 | 105 samples / 2.187500 ms |
| 整段直接相关 / 最佳偏移相关 | -0.000009577 / 0.693372791 |
| RMS 电平差 | -2.006200 dB |
| 三档峰值增益 | -5.255929 / -5.088792 / -4.805299 dB |
| 峰值增益范围 | 0.450630 dB |
| 左右输出相关 | 0.999999998303 |

## 操作观察与工作流

- 做低八度层时，先关闭 Pitch/Formant Link，再把 Pitch 设为 -12、Formant 保持 0；这样可把音高与角色共振的判断分开。确认八度准确后，再用 Formant 约 ±1–3 的小步偏移塑造角色。
- 推荐复制轨或 100% Wet Aux：主唱核心保持干声与中心定位，低八度层高通并降低电平，只补重量或角色。调整时重点听爆破、低频颗粒、辅音颤动、元音塑料感和贝斯遮蔽。
- 先在 Solo 中把效果身份做清楚，再回到全混音按 Active RMS 匹配；当处理层开始覆盖咬字、改变主唱中心或吞掉贝斯时停止增加 Blend。
- Flatten 适合机器人或硬效果，不宜替代透明校音；M1/M2/AM/PT 调制应一次只开一个源，以深度、速度和节奏清晰度为停止条件。
- 宿主的 0 samples 只表示无需固定 PDC。对瞬态敏感的并行层仍需用实际人声检查梳状感和辅音纹理，不能仅凭“zero latency”判断可透明叠加。

## 边界与未验证项

- F0 分析比较两条文件的加权中位自相关分布，没有逐帧对齐；不同采样率、不同长度、Ableton Clip Warp、无声辅音、倍频/半频误判和 Formant 处理均可能影响中位值。本轮只把 1.192 cents 误差用于确认八度级命令。
- 未测试 +12 semitones、Formant ±3 单变量、Flatten、Fine、M1/M2/AM/PT 调制、Mono/VST2、其它采样率、自动化、CPU 或盲听质量。
- 默认脉冲候选仅导出 6 s，而参考为 8 s；共同前 6 s用于分析。Triangular dither 会贡献极低噪声，但不能解释明显的峰值变化或短响应扩散。
- 105-sample 最佳相关偏移描述整体形状匹配，不是固定延迟；局部攻击峰值为 0/0/1 samples，二者不可互相替代。
- 固定人声夹具为本地测试资产，不在知识库之外分发。

## 证据

- 固定人声 SHA-256：`0027fe37914eb6558ee55dfd2f6af4af8d012372437daf9eddd601197a104701`。
- Pitch 候选渲染 SHA-256：`c8fd7db1a212e8b3ab41c02f5a695cd987ed67bb6f7401fedac923ad94c942c8`。
- 脉冲候选渲染 SHA-256：`e2bd187f094ed69a10db30406580ec4ea786033a97e161dab580c5bc7025d56d`。
- 工程快照 SHA-256：`9bcd5f623e381ce28b39969c6185ce30cb68df8f01441182797c160a35b933e9`。
- Pitch 量化：`validation/results/06fad1aad9d8--fixed-vocal-pitch-minus12-formant0.json`。
- 默认脉冲量化：`validation/results/06fad1aad9d8--impulse-neutral.json`。
- 测量脚本：`validation/scripts/analyze_pitch_shift.py` 与 `validation/scripts/analyze_saturation.py`。

