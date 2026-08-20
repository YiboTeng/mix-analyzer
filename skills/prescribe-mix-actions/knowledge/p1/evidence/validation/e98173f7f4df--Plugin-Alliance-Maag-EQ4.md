---
type: plugin-validation-report
status: passed-l3
created: 2026-08-20
updated: 2026-08-20
family_id: e98173f7f4df
vendor: "Plugin Alliance"
product: "Maag EQ4"
evidence_level: L3
---

# Plugin Alliance Maag EQ4：20 kHz Air Band 与余量验证

## 结论

本机旧版 Maag EQ4 VST3 已在 Ableton Live 11.3.43、48 kHz 中真实加载。界面只有固定的 SUB、40 Hz、160 Hz、650 Hz、2.5 kHz、Air 频率、Air Gain 与 Level Trim，没有把当前在线新版附加功能倒灌到本机结论。Ableton 报告 `0 samples` 延迟。

在所有固定频段增益为 0、Level Trim 不变的基线之上，把 Air 频率选为 20 kHz、Air Gain 设为 +3 dB，会产生从低频到高频逐渐增加的宽缓提升：十个同时输入的稳定音调相对零增益基线约为 `+0.208/+0.231/+0.119/+0.163/+0.153/+0.160/+0.170/+0.206/+0.265/+0.325 dB`（55 Hz 至 16 kHz），整段稳定多音约 `+0.163 dB`，峰值由 `-1.678` 升至 `-0.898 dBFS`。这支持“20 kHz 选择仍会影响可听频段”，但这些数值来自谐波相关多音同时输入，不等于单独正弦扫频的静态曲线。

同样状态把 Air Gain 推到 +5 dB 时，渲染峰值达到约 `0 dBFS`；其频点与区域结果已经受端点削顶影响，只作为余量风险证据，不作为干净传输曲线。实务上先从 +1 至 +3 dB 开始，以 Level Trim 或后级增益做等响，并同时检查齿音、底噪、峰值和后级动态处理是否被额外触发。

## 固定条件

- 宿主：Ableton Live 11.3.43；48 kHz；VST3；文件系统版本族 `1.3.0.0 | 1.9.0.0`，加载实例未显示可独立确认的精确 build。
- 输入：72 秒确定性复合夹具；8–20 秒为十音稳定多音，66–72 秒为分级动态区域。
- 导出：Master，48 kHz、Stereo、24-bit WAV、Normalize Off、Triangular dither；Ableton PDC 对齐。
- 状态：零增益基线；Air 20 kHz/+3 dB；Air 20 kHz/+5 dB；其它增益为 0，Level Trim 不变。
- 工程快照 SHA256：`f34f0329fa12a7a435e184450e308f6e64ecc449314d6cdc2920b546f6dcbed5`。快照链中保留了测试期间的停用实例；最右侧 EQ4 是最终启用的 20 kHz/+3 dB 实例。

## 关键测量

| 状态 | Peak | RMS | 稳定多音相对零增益 | 16 kHz 相对零增益 |
|---|---:|---:|---:|---:|
| 所有增益 0 | -1.678 dBFS | -21.379 dBFS | 基线 | 基线 |
| Air 20 kHz / +3 dB | -0.898 dBFS | -21.174 dBFS | +0.163 dB | +0.325 dB |
| Air 20 kHz / +5 dB | 约 0 dBFS | -20.683 dBFS | +0.540 dB | +1.055 dB；已触顶 |

零增益基线与较早独立导出的共享旁路在三个主区域存在约 `+0.262/+0.019/+0.026 dB` 差异，最佳整数偏移为 0 samples。由于共享旁路不是同一即时切换渲染、两次导出都含独立三角抖动，并且本机旧 build 可能存在固定路径差异，不能把它写成逐比特透明或把微小差异完全归因于 EQ 曲线；本报告的主结论使用同一插件零增益基线与 Air 变体的相对比较。

## 使用判断

- 选择器必须离开 `OFF`；Air Gain 有数值而频率仍为 OFF 时不会得到预期空气感。
- 20/40 kHz 不是“可听范围之外所以安全”；宽缓曲线会延伸进可听高频。
- 从 +1 至 +3 dB 起步；一边补偿输出，一边看峰值。+5 dB 在当前夹具中已经失去余量。
- 放在去齿之后可做最终光泽；若又把 S/T/CH 推出来，可在其后再做轻度去齿。放在压缩前会改变检测器输入，放在压缩后更接近色彩收尾。
- 固定带是宽幅音乐性塑形，不用于窄共振手术；多个宽频段相加时必须重新匹配响度。

## 边界

未测试 SUB/40/160/650/2.5 kHz 单独曲线、Air 2.5/5/10/40 kHz、Level Trim 精确标定、单音/扫频、真实人声齿音与底噪、VST2、其它采样率、自动化、CPU、Mono/Stereo 组件差异或盲听偏好。+5 dB 结果已削顶，不能用于推导线性增益比例。

## 证据

- [分析结果](../results/e98173f7f4df--composite-air20k-gain-headroom.json)
- [分析脚本](../scripts/analyze_fixed_air_eq.py)
- [工程快照](<../host/snapshots/0072a637f389--FabFilter-Saturn-2 Project/e98173f7f4df--Plugin-Alliance-Maag-EQ4.als>)

