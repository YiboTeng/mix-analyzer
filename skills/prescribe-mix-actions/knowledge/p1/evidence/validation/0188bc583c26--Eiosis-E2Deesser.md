---
type: plugin-validation-report
status: passed-l3
created: 2026-08-20
updated: 2026-08-20
family_id: 0188bc583c26
vendor: "Eiosis"
product: "Eiosis E2Deesser"
evidence_level: L3
---

# Eiosis E2Deesser：Mode、Auto 与 Smooth 受控验证

## 结论

本机 E2Deesser 1.0.9.3 VST3 已在 Ableton Live 11.3.43、48 kHz 中真实加载。界面回读确认 Solo Vocal、Back Vocals、Voice Over、Guitar Squeaks、Overheads、Stereo/M-S/Mid Mastering 模式，以及 Sensitivity、Amount、Auto、Smooth、Gain、Dry/Wet、Voiced EQ、Sibilants EQ 和 Bypass。Ableton 报告固定 `720 samples / 15 ms` 延迟。

默认 Solo Vocal（Sensitivity/Amount/Auto/Smooth/Dry-Wet 均 50%、Gain 0 dB）相对共享旁路，在三个稀疏源事件上均约降低 `2.449 dB`；8–20 秒稳定多音与 66–72 秒动态区整体约 `+0.010/+0.003 dB`，说明当前动作高度依赖内容，而不是全程固定衰减。

只把 Mode 改为 Voice Over 后，三个源事件相对 Solo Vocal 再降低 `0.676 dB`；7–14 kHz 和 14 kHz 以上分别再低约 `0.63/1.06 dB`，而稳定多音和晚段动态区约为 0 dB 差。它支持“Voice Over 更敏感”的本机局部结论，但不能外推为所有旁白都应优先使用。

只把 Auto 从 50% 增至 100%、Smooth 固定 50% 时，源事件整体仅 `+0.063 dB`；只把 Smooth 从 50% 增至 100%、Auto 固定 50% 时，源事件整体 `-0.316 dB`，7–14 kHz约 `-0.41 dB`。Auto 100/Smooth 0 与 Auto 0/Smooth 100 的组合端点相差 `1.061 dB`，但组合端点不是两个控件的独立传递函数。实务上先选 Mode 与 Sensitivity/Amount，再分别微调 Auto、Smooth，并对齿音事件做等响/峰值复查。

## 固定条件

- 宿主：Ableton Live 11.3.43；48 kHz；VST3；本机 Inventory 版本 `1.0.9.3`。
- 输入：72 秒确定性复合夹具；0–6 秒含三个稀疏源事件，8–20 秒为稳定多音，66–72 秒为动态区。
- 导出：Master，48 kHz、Stereo、24-bit WAV、Normalize Off、Triangular dither；Ableton PDC 对齐。
- 公共设置：Sensitivity 50%、Amount 50%、Gain 0 dB、Dry/Wet 50%、Voiced EQ On、Sibilants EQ On。
- 状态：Solo 默认；Voice Over 默认；Solo Auto 100/Smooth 50；Solo Auto 50/Smooth 100；另保留 Auto 100/Smooth 0 与 Auto 0/Smooth 100 组合端点。
- 工程快照 SHA256：`fd159e51d20de2662559e8cd69896434d468bcf814b217bacfd2f0759ecd4e58`；快照保存状态为 Solo Vocal、Auto 0%、Smooth 100%。

## 关键测量

| 比较 | 0–6 秒整体 | <7 kHz | 7–14 kHz | >14 kHz | 事件 Peak |
|---|---:|---:|---:|---:|---:|
| Solo 默认 vs 旁路 | -2.449 dB | -2.55 dB | -2.51 dB | -2.34 dB | -2.47 dB |
| Voice Over vs Solo 默认 | -0.676 dB | -0.20 dB | -0.63 dB | -1.06 dB | -0.69 dB |
| Auto 100 / Smooth 50 vs 默认 | +0.063 dB | +0.03 dB | +0.06 dB | +0.09 dB | +0.06 dB |
| Auto 50 / Smooth 100 vs 默认 | -0.316 dB | -0.22 dB | -0.41 dB | -0.32 dB | -0.33 dB |
| Auto100/Smooth0 vs Auto0/Smooth100 | +1.061 dB | +0.65 dB | +1.16 dB | +1.28 dB | +1.08 dB |

三个稀疏事件的结果在每个状态内几乎一致，且事件相关系数显示到 12 位小数仍接近 1.0；这说明本夹具下主要表现为稳定的事件电平/频带重塑，不能据此证明对真实连续辅音不存在更复杂的时间变化。全文件处理态 Peak 接近 0 dBFS，来自夹具其它高电平段，因此听感 A/B 之前仍需做外部增益匹配与余量复查。

## 使用判断

- 干主唱先用 Solo Vocal；只有旁白/说唱在同一 Sensitivity 下漏检时，才试 Voice Over，并同时监测呼吸、F/H、底噪和 Idle 误触发。
- 先用 Sensitivity 找检测边界，再用 Amount 定总处理量；不要用 Auto/Smooth 代替检测阈值与总量控制。
- Auto 从默认 50% 附近单独微调；当前 50→100% 对测试事件只产生约 +0.06 dB，说明它不是简单的“更多去齿”旋钮。
- Smooth 从默认 50% 附近缓慢增加；当前 50→100% 对 7–14 kHz约多压 0.41 dB。若齿音变钝、沙哑或主体咬字被带走，回退。
- 默认 Dry/Wet 为 50%；若要校准最大处理，可暂时提高 Wet，但返回工作比例后必须重新检查事件峰值、整体响度和旁通差。
- 录音监听需为固定 15 ms 插件延迟留预算；当前 UI 未见可关闭的 Lookahead 控件，不要把它当零延迟去齿器。

## 边界

当前夹具不是带音素标签的真实语音语料，不能给出检测精确率、召回率或 lisp 偏好。未测试 Sensitivity/Amount 曲线、Idle Threshold 的完整交互、自定义 Voiced/Sibilants EQ、Back Vocals 左右独立检测、Stereo/M-S/Mid Mastering、其它模式、自动化、CPU、VST2/VST3 一致性、其它采样率或盲听。默认 Dry/Wet 50%，所测衰减不是全湿上限。

## 证据

- [分析结果](../results/0188bc583c26--composite-e2deesser-mode-auto-smooth.json)
- [分析脚本](../scripts/analyze_e2deesser.py)
- [工程快照](<../host/snapshots/0072a637f389--FabFilter-Saturn-2 Project/0188bc583c26--Eiosis-E2Deesser.als>)
