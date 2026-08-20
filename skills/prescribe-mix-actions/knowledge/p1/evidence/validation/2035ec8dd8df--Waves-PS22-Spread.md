---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: 2035ec8dd8df
product: PS22 Spread
evidence_level: L3
test_id: ps22-default-spread-impulse-v1
---

# Waves PS22 Spread：默认频率相关宽化验证

## 结论

本机 Waves `PS22 Spread Stereo` V12（12.7.0.209）已在 Ableton Live 11.3.43 中真实加载。默认界面为 Input 0 dB、Width 1、Rotation 0、Spread 0.60、Freq 251 Hz、LFSpread 1.50、FCenter 724 Hz、FDensity 0、Tweak 0、Sweeps 16；宿主报告 2 samples / 0.042 ms PDC。

三个宽带脉冲的 0–100 ms 响应具有稳定线性比例：L/R 相关均值 0.711395513，Side/Mid RMS -7.728248 dB，Mono Fold 相对每通道 Stereo RMS -0.677117 dB；左右峰值到达中位数均 5 samples / 0.104167 ms，通道间峰值差 0。左、右三档峰值增益约 -5.887 dB 与 -5.276 dB，未随输入电平改变，符合官方所述线性、非时变处理。

结果支持“默认状态产生可测全频 Side，同时保留较强 Mid，Mono 变化温和但不为零”。官方称 Spread=0.6 的 Mono 频响波纹约 ±0.67 dB；本轮 -0.677117 dB 是宽带 RMS 折叠差，定义不同，数值接近不构成直接复现。

## 固定状态与量化

- 插件：`PS22 Spread Stereo` V12，VST3。
- 默认参数：Input 0.0 dB；Width 1.00；Rotation 0.0；L/R；No Clip；Spread 0.60；Freq 251 Hz；LFSpread 1.50；FCenter 724 Hz；FDensity 0；Tweak 0；Sweeps 16。
- 输入：`impulse_train_48k.wav`；导出：Master、48 kHz/24-bit WAV、Normalize 关闭。
- 分析窗口：42 s 完整渲染的前 5 s，包含三个干净脉冲且早于固定人声；候选事件独立检测并按顺序与夹具配对。
- 快照：`validation/host/snapshots/0072a637f389--FabFilter-Saturn-2 Project/2035ec8dd8df--Waves-PS22-Spread.als`。

| 指标 | 结果 |
|---|---:|
| 宿主延迟 | 2 samples / 0.042 ms |
| 脉冲数 | 3 |
| 左/右峰值到达中位数 | 5 / 5 samples |
| 通道间峰值差 | 0 samples |
| L/R 相关均值 | 0.711395513112 |
| Side/Mid RMS | -7.728248 dB |
| Mono Fold RMS Delta | -0.677117 dB |
| Mono 峰值 Delta | 约 -0.300352 dB |
| 左峰值增益 | -5.886980 / -5.886976 / -5.886976 dB |
| 右峰值增益 | -5.275515 / -5.275516 / -5.275512 dB |

Hann 窗会压低响应起点的直接 Mid 峰值，因此窗口化频域侧/中比与全响应时间域侧/中比不同。三个脉冲在 20–200、200–2000、2000–20000 Hz 的尾部 Side/Mid 大致为 -0.36、-0.55、-0.85 dB；它只说明滤波尾部的 Side 能量遍布频谱，不能替代稳态多音 Mono 频响测量。

## 操作观察与工作流

- 先决定 Spread 或 Split：Spread 平滑、近似正弦式分布；Split 更接近方波式左右分割。
- 先选 Sweeps：2–4 定位，约 8 折中，12–22 扩散；再定 Spread/LFSpread、FCenter/FDensity，最后 Tweak 居中。
- 宽 Stereo 先把 Width 降到约 0.6–0.7，再以 Spread 0.25–0.5 起步。越过图中 L/R 线代表反相超宽，应结合扬声器、耳机和 Mono 判断。
- 主唱核心保留干 Mid；PS22 层以复制轨/Aux 混回并按需高通、去齿和 Duck。它不是 Doubler，也没有 Delay 控制。

## Spread 与 Spread(10)

本机同时暴露标准 Spread 与 Spread(10) 的 Mono/Stereo、Stereo 组件。官方确认两者控制体系相同，主要差异是标准版 Sweeps 可到 22，`(10)` 只到 10、DSP 更低；不能把 `(10)` 写成另一套 Mono 兼容算法。CPU 差值未测。

## 边界与未验证项

- 只测 48 kHz、VST3 Stereo、默认 `Spread=0.60 / Sweeps=16 / LFSpread=1.50 / FDensity=0`；未测 VST2、Mono/Stereo、自动化、其它采样率或 CPU。
- 完整 42 s 导出继承旧 2.1.1–28.0.0 选区；分析器只用前 5 s，固定人声不参与。
- 5-sample 峰值位置来自 0.005 阈值事件后的局部峰值，不等同 2-sample PDC。
- 未做 Spread、Sweeps、LFSpread、FDensity 单变量，也未完成连续人声盲听和稳态多音 Mono 波纹复现。

## 证据

- 参考 SHA-256：`aafbd0a42ee57fde77b79aae591d54f87383b391e76803af9405757f92e3cf2e`。
- 候选 SHA-256：`2a8659961423c9529756fc9a15093d7783e912d5d40861d09ef43e90572a292e`。
- 快照 SHA-256：`4b7a1ef68e13fffb737919d4e39dbf845f847fde5c6d39cb404ec1c786f94796`（渲染后再次保存，已固化仅 PS22 启用的隔离状态）。
- 结果：`validation/results/2035ec8dd8df--impulse-default-spread.json`。
- 脚本：`validation/scripts/analyze_spatial.py`。
- 官方产品页：https://www.waves.com/plugins/ps22-stereo-maker
- 官方手册：https://assets.wavescdn.com/pdf/plugins/ps22-stereo-maker.pdf
