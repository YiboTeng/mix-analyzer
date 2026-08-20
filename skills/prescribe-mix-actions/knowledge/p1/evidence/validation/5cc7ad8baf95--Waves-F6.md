---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: 5cc7ad8baf95
product: F6
evidence_level: L3
test_id: composite-dynamic-eq-static-and-range
---

# Waves F6：Full Reset、静态 Bell 与向下动态段验证

## 结论

本机 Waves `F6 Stereo` V12（文件系统版本 `12.7.0.209`）已在 Ableton Live 11.3.43、48 kHz 中真实加载，宿主报告 `0 samples` 延迟。`A: Full Reset` 回读为六段平直、Mix `100`、Output `0.0 dB`、Stereo、Internal sidechain、Split；它与同一编排共享旁路在三个主区域均约 `0.000000 dB`，相关系数约 `1.0`，残差约 `-141.4 dBFS`，可视为本夹具中的中性起点。

静态单段设为 Bell、`1736 Hz`、Q `1.0`、Gain `+3.7 dB`、Range `0 dB`。稳定十音段整体增加 `0.260271 dB`，夹具最接近中心的 `1760 Hz` 增加 `1.528927 dB`，并出现频率相关相位变化。它证明静态路径有效，但十个同时输入的谐波相关音调会发生相位/叠加交互，不能把每个频点的 FFT 幅度直接当单独正弦扫频的理想 Bell 曲线，也不能从 `+3.7 dB` 面板值推断输出一定增加同样幅度。

向下动态单段保持 `1736 Hz`、Q `1.0`、Gain `0 dB`，设 Range `-4.3 dB`、Threshold `-53.6 dB`、Attack `16 ms`、Release `160 ms`、Internal、Split。稳定十音整体降低 `0.106428 dB`，`1760/3520 Hz` 分别约 `-0.671908/-0.672974 dB`；三个低电平稀疏短事件仅约 `-0.000119` 至 `-0.000265 dB`。这证明当前动态段不是固定静态削减：是否动作取决于带内检测电平与时间历史，Range 是最大动态边界而不是必然发生的增益变化。

66–72 秒动态区域整体只有 `-0.012161 dB`；高电平稳定窗约 `-0.01481 dB`，极低电平尾部因滤波器状态/相位叠加出现最高约 `+0.060894 dB` 的局部差。当前夹具并非专为 1736 Hz 单频阶梯设计，不能据此反推精确 Ratio、Knee 或 Attack/Release 时间常数。

## 可执行工作流

- 先用静态 Gain 或 Solo 定位问题频率，再把 Gain 归零、用 Range 规定“最多允许动多少”；Threshold 只降到问题音素稳定触发，不能把 Range 当目标 GR。
- 对 2–5 kHz 人声硬度，先用约 1–3 dB 的负 Range、Q 约 0.7–2、Attack 5–30 ms、Release 60–200 ms 起步；以正常元音基本不动、刺耳音素刚退后为停止条件。
- 若 Threshold 很低而目标仍不动作，先检查频点、SC Source、Split/Wide、输入电平与带内能量，而不是继续堆深 Range。本轮 `-28.8 dB` 的探索态几乎未动作，降到 `-53.6 dB` 后才在稳定多音上得到明确衰减。
- 静态与动态 A/B 都要做外部等响；中心频率附近之外的同时多音读数可能受相位叠加影响，不要把一个分析器频点当成完整听感。
- 外部侧链让位时先核对 DAW 路由与 SC Source，再听主唱进入/离开时伴奏是否泵动；M/S 或侧边处理必须额外检查 Mono Fold-down。

## 边界与未验证项

- L3 只覆盖本机 VST3 Stereo V12、48 kHz、Full Reset、一个 1736 Hz/Q1 静态 Bell，以及一个 Internal/Split 向下动态设置。
- 共享旁路来自同一编排、加载 F6 前的独立导出；Ableton PDC 已对齐，Triangular dither 使逐比特空差不成立，约 -141 dBFS 残差属于预期边界。
- 未测外部侧链路由、M/S 与通道 Link、其它 Band/滤波形状、向上扩展、RTA、Solo、Global Release ARC/MNL、Wide 模式、自动化、CPU、Mono、VST2、其它采样率/版本或真实人声盲听。
- 十个谐波相关音调同时存在；频点传输不是单独正弦扫频，也不支持把 220 Hz 的正变化解释为固定 Boost。

## 证据

- 共享旁路 SHA-256：`38a74287a951ad7a62a6abeb219aa91afdd0e4f2abde062b972361851e0de16f`。
- Full Reset SHA-256：`36d50c8e3e5b96ca40dccf884228332e58d8ed3869e23bde466c2d471c2161ce`。
- 静态 Bell SHA-256：`67f718a8fa689b43ddc1cd94a5659114087d089b146fcf193fbbcbc2ba408bbd`。
- 动态 Down SHA-256：`3b3515c2d07efc5b54f875e1116fb6f69d72cfab41117789bdc308bd1293046a`。
- 工程快照 SHA-256：`ec92b1689464ebd4517907083b10eb7ffca505687b016728f56084aef080f619`。
- 量化：`validation/results/5cc7ad8baf95--composite-dynamic-eq.json`。
- 测量脚本：`validation/scripts/analyze_dynamic_eq.py`。

