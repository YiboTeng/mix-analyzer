---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: 1994a7f7d443
product: Black Box Analog Design HG-2
evidence_level: L3
test_id: impulse-default
---

# Plugin Alliance Black Box HG-2：旧版默认路径脉冲传输验证

## 结论

本机 Plugin Alliance Black Box Analog Design HG-2 1.3.0.0 VST3 在 Ableton Live 11.3.43 中真实加载为原版 HG-2，而不是 HG-2MS。默认界面可见 Calibration、Density、Input、Mix、Saturation、Pentode、Triode、Output、Air Amount，以及 FLAT 校准位置、Alt Tube、Air、Bypass 等控制；宿主设备栏报告 `Latency: 32 samples (0.67 ms)`。

固定三电平脉冲经 6 秒离线导出后，三次局部峰值均保持 0-sample 对齐。输入 -1.938/-6.021/-12.041 dBFS 时，输出峰值为 -3.109/-6.946/-12.830 dBFS，对应峰值增益 -1.170/-0.925/-0.789 dB，三档范围 0.381 dB。默认旧版路径因此不是透明旁通：高电平瞬态被略多压低，但其电平依赖远小于本批次默认 Saturn 2 Warm Tape 与 Abbey Road Saturator TG。

直接相关为 0.972700，最佳整数偏移 0 samples，RMS 电平差 -0.839411 dB，残差 RMS -67.166254 dBFS；左右输出相关 0.999999998701。强/中/弱脉冲核心外能量占比约 0.724%/0.704%/0.693%，说明默认实例产生轻微、随电平变化的短时管式响应，但在左右相同输入下未产生可测的声像偏移。

## 固定状态与量化

- 插件：Plugin Alliance Black Box Analog Design HG-2 1.3.0.0，VST3；本轮不是 HG-2MS。
- 默认界面：Calibration 处于 `FLAT`；Saturation、Pentode、Triode、Output 与 Air Amount 旋钮视觉约中位，Density/Input/Mix 保持默认；未把没有数字显示的旋钮位置写成精确值。
- 可见开关：On/Off、In/Out、Alt Tube、Air、Bypass；A/B/C/D 与 Copy/Paste/Reset 状态保持默认，未做切换。
- 输入：实际使用 `impulse_train_48k.wav`；轨道名称仍残留 `multitone`，不作为夹具证据。Clip 位于 2.1.1，Host 160 BPM，Warp 关闭。
- 导出：Master、2.1.1 起、4.0.0 长（6 s）、48 kHz/24-bit WAV、Triangular dither、Normalize 关闭。
- 工程快照：`validation/host/snapshots/1994a7f7d443--Plugin-Alliance-Black-Box-HG-2.als`。

| 全局指标 | 结果 |
|---|---:|
| 宿主报告插件延迟 | 32 samples / 0.67 ms |
| 最佳整数相关偏移 | 0 samples / 0.000000 ms |
| 直接相关系数 | 0.972700208840 |
| RMS 电平差 | -0.839411 dB |
| 残差 RMS | -67.166254 dBFS |
| 残差峰值 | -19.474977 dBFS |
| 左右输出相关 | 0.999999998701 |
| 三档峰值增益范围 | 0.380995 dB |

| 脉冲输入 | 输出峰值 | 峰值增益 | 局部峰值偏移 | 核心外能量占比 |
|---:|---:|---:|---:|---:|
| -1.938333 dBFS | -3.108614 dBFS | -1.170281 dB | 0 samples | 0.7236% |
| -6.020600 dBFS | -6.945506 dBFS | -0.924906 dB | 0 samples | 0.7036% |
| -12.041200 dBFS | -12.830486 dBFS | -0.789286 dB | 0 samples | 0.6930% |

## 操作观察与工作流

- 默认旧版 HG-2 已有温和的削峰与短时响应；用于主唱或 Vocal Bus 时应先记录输入峰值和 Active RMS，再用 Output 等响。不能因密度感或平均响度变化直接判定音质提升。
- 原版 HG-2 的 Pentode/Triode 是串联管级，Saturation/Alt Tube 是并行角色，Density 又会联动主级；精调时一次只改变一类控制。推荐先固定 FLAT、Air 关闭或默认状态，以 Pentode 或 Triode 单变量找到主体，再小幅加 Density。
- Mix 适合在全湿识别角色后回到约 10–40% 作为起点；若做更重并行，使用 Aux 并在返回轨检查爆破、齿音、低中频拥挤与 Mono 折叠。
- Air 是 10 kHz 以上光泽控制，不能代替去齿或高频平衡。开启或推高后要重新量化 5–12 kHz 齿音事件，而不是只听整体“更亮”。
- 宿主报告的 32 samples 是插件延迟声明；本次离线导出经过 PDC 后为 0-sample 对齐。实时监听、跨宿主或外部并行路由仍须重新确认。

## 边界与未验证项

- 本轮以三电平脉冲替代原矩阵的 multitone，验证默认路径的瞬态传输、宿主延迟、短响应与通道一致性；未测稳态谐波阶次、THD、别名、频响或噪声底。
- 未量化 Pentode、Triode、Density、Saturation、Alt Tube、Calibration、Air、Input、Mix 与 Output 的单变量消融，也未验证旧版每个旋钮的精确数值范围。
- 未测试 VST2、其它采样率、Mono 组件、自动化、CPU、连续人声等响盲听或 HG-2MS；L3 只覆盖本机 1.3.0.0 VST3 原版默认主行为及主要副作用。
- 独立 24-bit Triangular dither 会贡献极低随机底噪，但不能解释 0.381 dB 的电平依赖峰值范围或约 -19.47 dBFS 的残差峰值。
- 左右相关接近 1 只适用于左右相同输入和当前默认 Stereo 路径，不证明不对称素材、并行声部或所有版本都保持相同相关性。

## 证据

- 候选渲染 SHA-256：`4f168d74e1eeea931ed3ed0b2ead71c15c40454ea95de660e4f2f4117103292a`。
- 固定脉冲 SHA-256：`aafbd0a42ee57fde77b79aae591d54f87383b391e76803af9405757f92e3cf2e`。
- 工程快照 SHA-256：`5a74ccbdec4422040b2a6db3131aa7437bb47e31a028b51c4fef1a702d6f39bc`。
- 量化：`validation/results/1994a7f7d443--impulse-default.json`。
- 测量脚本：`validation/scripts/analyze_saturation.py`。

