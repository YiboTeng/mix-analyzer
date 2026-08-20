---
type: plugin-validation-report
status: passed-l3
created: 2026-08-20
updated: 2026-08-20
family_id: 0c0769036773
vendor: "Slate Digital"
product: "Fresh Air"
evidence_level: L3
---

# Slate Digital Fresh Air：Mid/High Air 隔离验证

## 结论

本机 Fresh Air 1.1.1 VST3 已在 Ableton Live 11.3.43、48 kHz 中真实加载。界面回读确认 `Mid Air`、`High Air`、两旋钮 Link、`Trim`、Power、Peak/RMS 表；Ableton 报告 `0 samples` 延迟。Link 在本报告中保持关闭，不能从当前结果推断声道联动或两旋钮联动的精确比例。

相对同一实例的 Mid/High 均为 0、Trim 0 基线，`Mid Air 21% / High Air 0%` 使稳定多音整体增加 `+0.651 dB`，55 Hz 至 16 kHz 十个频点约增加 `+0.72/+0.69/+0.71/+0.65/+0.61/+0.58/+0.55/+0.72/+0.75/+0.80 dB`；全文件峰值从 `-1.918` 升至 `-0.708 dBFS`。这说明当前多音/动态夹具下 Mid Air 并不是一个可按旋钮百分比解释的固定窄带或固定 dB Shelf。

`Mid Air 0% / High Air 21%` 使稳定多音整体增加 `+0.911 dB`，12/16 kHz 分别约 `+1.57/+2.34 dB`，而 7040 Hz约 `+0.31 dB`；全文件峰值达到 `-0.000001 dBFS`。虽没有样本精确等于 1.0，但它已耗尽当前夹具的数字余量，因此 21% 是风险端点，不是推荐起点。实务上先从 5–10% 小步上推，以 Trim 或后级增益等响，并同时检查 S/T/CH、点击、底噪与后级去齿/压缩触发。

## 固定条件

- 宿主：Ableton Live 11.3.43；48 kHz；VST3；本机文件系统版本 `1.1.1`。
- 输入：72 秒确定性复合夹具；8–20 秒包含十音稳定多音，66–72 秒为分级动态区域。
- 导出：Master，48 kHz、Stereo、24-bit WAV、Normalize Off、Triangular dither；Ableton PDC 对齐。
- 状态：中性 0/0；Mid 21%/High 0%；Mid 0%/High 21%；三态均 Trim 0、Power On，单变量态 Link Off。
- 工程快照 SHA256：`a3cec6e09b6cb863a271d5db25d3ce1382c39835d6614c18c947f405d27fc5f6`；最终保存状态为 Mid 0% / High 21%。

## 关键测量

| 状态 | Peak | RMS | 稳定多音相对中性 | 12 kHz | 16 kHz |
|---|---:|---:|---:|---:|---:|
| Mid 0 / High 0 | -1.918 dBFS | -21.417 dBFS | 基线 | 基线 | 基线 |
| Mid 21 / High 0 | -0.708 dBFS | -20.598 dBFS | +0.651 dB | +0.75 dB | +0.80 dB |
| Mid 0 / High 21 | -0.000001 dBFS | -20.413 dBFS | +0.911 dB | +1.57 dB | +2.34 dB |

两种处理态相对中性基线的最佳整数偏移均为 0 samples，稳定区相关分别为 `0.9999947` 与 `0.9999986`。中性实例相对较早独立导出的共享旁路全文件 Peak/RMS 约高 `0.021/0.021 dB`；因为不是同一次插件旁通切换并含独立三角抖动，本报告不把它写成精确中性偏置或逐比特透明结论。

十音拟合后的残差/音调比在中性、Mid 21、High 21 三态约为 `17.090/17.086/17.090 dB`。该指标没有显示当前稳态多音下明显新增的非拟合残差比例，但十音彼此存在谐波关系，动态处理的产物可能落回已有频点，因此它只是筛查，不是 THD/混叠证明。

## 使用判断

- 先分别调整 Mid 与 High；找出刺耳、齿音、底噪或余量边界后再考虑 Link。
- Mid Air 从 5–10% 起，目标是补咬字/前景感；若 2–5 kHz 变硬或主体变薄，立即回退。
- High Air 从 5–10% 起，优先监测 12–16 kHz、S/T/CH、口水音与噪声。当前 21% 已把测试峰值推到数字上限附近。
- 每次用 Trim 或后级增益匹配旁通响度和 Peak/RMS；旋钮百分比不是 dB，整体增益变化也不是纯高频曲线。
- 常见位置是清理、压缩和第一阶段去齿之后；若激励后重新冒出齿音，可在其后补非常轻的去齿，而不是用重度去齿抵消过量 Air。

## 边界

未测试 Trim 精确标定、Link 联动比例、Power/插件旁通即时空差、单音/扫频、真实人声音素、噪声与点击专用夹具、瞬态-only 行为、VST2/VST3 一致性、其它采样率、自动化、CPU、Mono/Stereo 通道行为或盲听偏好。High 21% 已到端点附近，不用于推导更高百分比的线性比例。

## 证据

- [分析结果](../results/0c0769036773--composite-mid-high-air.json)
- [分析脚本](../scripts/analyze_dual_band_exciter.py)
- [工程快照](<../host/snapshots/0072a637f389--FabFilter-Saturn-2 Project/0c0769036773--Slate-Digital-Fresh-Air.als>)
