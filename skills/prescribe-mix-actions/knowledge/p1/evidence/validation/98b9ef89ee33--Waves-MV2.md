---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: 98b9ef89ee33
product: MV2
evidence_level: L3
test_id: dynamics-steps-mv2-level-controls
---

# Waves MV2：Low / High Level 动态收敛验证

## 结论

本机 Waves `MV2 Stereo` 12.7.0.209 VST3 已在 Ableton Live 11.3.43、48 kHz 中真实加载；宿主报告 `64 samples / 1.3 ms` 延迟。本轮保持 Output `0.0`，分别比较旁路、Low/High 均为 `0.0`、Low Level `+26.2` 与 High Level `-12.0`。

Low/High 均为 0 时相对旁路直接相关 1.0、五档稳态增益 0 dB，可作为本机实例的中性控制。Low `+26.2` 不是统一 Makeup：相对中性，五档稳态增益从最低档的 +20.726 dB 递减到最高档的 +6.541 dB，输出对输入斜率为 0.402948；它把电平跨度显著压窄，并把最高持续音峰值推到 0 dBFS。这个状态足以证明 Low 会优先抬高低电平内容，也量化了噪声、呼吸和房间尾音随弱字一同前冲的风险。

High `-12.0` 在本机 v12 与本夹具上也不是简单的“把响处衰减 12 dB”：相对中性，五档仍分别增加 +11.289、+10.557、+9.271、+7.176、+4.087 dB，输出对输入斜率 0.703470。也就是说，它同样令动态向上方收敛，但低档增益大于高档；最高隔离脉冲达到 -0.794 dBFS。可把该结果安全地写成“High 控制当前版本的上方收敛/峰值约束量，同时伴随内部回补”，不能把面板负数直接当作最终输出衰减或纯 GR。

两种深度都会显著改变整体响度：全文件 RMS 分别增加 +8.797 dB 与 +5.404 dB。实际使用必须在 MV2 后用 Output 或下游增益做等响和峰值复查；本轮没有执行 Output 单变量，因此不声称其标度精度。

## 固定状态与量化

- 插件：Waves `MV2 Stereo` 12.7.0.209，VST3。
- 宿主：Ableton Live 11.3.43；160 BPM；48 kHz；报告延迟 64 samples / 1.3 ms。
- 中性：Low Level `0.0`、High Level `0.0`、Output `0.0`。
- 单变量 A：Low Level `0.0` → `+26.2`，High Level 与 Output 固定 0。
- 单变量 B：High Level `0.0` → `-12.0`，Low Level 与 Output 固定 0。
- 导出：Master、42.1.1–50.1.1、12 s、48 kHz/24-bit WAV、Normalize Off、Triangular dither。
- 夹具：`dynamics_steps_48k.wav`；Ableton 自动 Warp 为 160 BPM 下 8 bars/12 s。
- 工程快照：`validation/host/snapshots/0072a637f389--FabFilter-Saturn-2 Project/98b9ef89ee33--Waves-MV2.als`。

| 输入峰值 | 中性 RMS | Low +26.2 相对中性 | Low +26.2 峰值 | High -12 相对中性 | High -12 峰值 |
|---:|---:|---:|---:|---:|---:|
| -30 dBFS | -33.011 | +20.726 dB | -9.281 dBFS | +11.289 dB | -18.713 dBFS |
| -24 dBFS | -27.011 | +17.652 dB | -6.360 dBFS | +10.557 dB | -13.447 dBFS |
| -18 dBFS | -21.011 | +13.988 dB | -4.023 dBFS | +9.271 dB | -8.732 dBFS |
| -12 dBFS | -15.023 | +10.204 dB | -1.805 dBFS | +7.176 dB | -4.829 dBFS |
| -6 dBFS | -9.011 | +6.541 dB | 0.000 dBFS | +4.087 dB | -1.920 dBFS |

| 静态指标 | Low +26.2 vs 中性 | High -12 vs 中性 |
|---|---:|---:|
| 输出对输入斜率 | 0.402948 | 0.703470 |
| 当前五档局部有效比率 | 2.481712:1 | 1.421524:1 |
| 最低到最高档增益变化 | -14.184427 dB | -7.202713 dB |
| 全文件 RMS 差 | +8.796920 dB | +5.403528 dB |
| 全文件峰值差 | +2.853701 dB | +2.059502 dB |
| 直接相关 | 0.929099428 | 0.974730231 |

> “局部有效比率”只来自五档稳态回归，用于描述本夹具中的动态收敛；它不是 MV2 隐藏固定 Ratio 的反推。

Low `+26.2` 的四个持续音进入稳态 ±1 dB 约需 28.15–81.56 ms，High `-12.0` 约需 27.40–76.17 ms。五个隔离脉冲相对中性分别增加约 +2.854 dB 与 +2.060 dB，且脉冲位于持续音之后，包含处理历史；这些数字不能改写为 Attack/Release 常数。三个处理态的 L-R 残差约 -139.86 至 -139.99 dBFS，只支持当前双单声道夹具下左右输出一致，不能代替 Stereo Link 测试。

## 操作观察与工作流

- 先完成降噪、呼吸和嘴部杂音整理，再从很浅的 Low Level 开始；+26.2 是刻意放大的测量状态，不是推荐起点。
- 用弱字可懂度与句间噪声共同决定 Low 的停止点。弱字已稳定而继续增加主要抬升底噪、房间或呼吸时立即回退。
- High 的负数不等于最终衰减量。本机 -12 状态仍增加全文件 RMS 5.4 dB；以 Cut 表和峰值表观察动作，但用通道峰值与等响 A/B 决定是否安全。
- Low 与 High 分开设定：先只让 Low 补足弱句，再只让 High 收窄响句；最后用 Output/下游增益匹配旁路。不要一开始同时拉到深值。
- 本轮 Low +26.2 已触及 0 dBFS。实际主唱需预留输出余量，并复查后续饱和器、削波器与限制器是否被额外驱动。
- 只需修补少数弱字时优先 Clip Gain；需要慢速宏动态时优先 Vocal Rider；需要明确 Ratio/Attack/Release/Range 时使用 Pro-C 2。

## 边界与未验证项

- L3 仅覆盖本机 VST3 Stereo 12.7.0.209、48 kHz、一个阶梯/脉冲夹具、Output 0、Low 0→+26.2 与 High 0→-12。
- Ableton 导出使用 PDC；64 samples 是宿主报告，不是从已补偿文件反推的裸延迟。
- 未验证隐藏阈值、Knee、Ratio、Attack/Release、表头弹道、Output 标度、Low/High 同时动作、真实语音/呼吸/噪声比例、Mono、Stereo Link、VST2、其它版本/采样率、自动化、CPU 或等响盲听。
- 两个单变量都大幅增响；本报告验证动态形状与风险，不把更响等同更好，也不把极端测试值写成推荐预设。

## 证据

- 旁路 SHA-256：`e1349b37241ae49caf6efc075ebaeb3de16801ee2de336a3f0eff4ee17378072`。
- 中性 SHA-256：`cd4517a9300a10e7fbd2f85ca5f5ae55826989ce6073e74372559f24814ee3be`。
- Low +26.2 SHA-256：`8c9e7024e433b444d3cc804d9fe4232655a78db8b6bce72e2dc688089bd27737`。
- High -12 SHA-256：`8f3f620ad86883ec204f32a32c0c4aef7104142d2c209182c9c364ab54e30f62`。
- 工程快照 SHA-256：`52d46c27dd9305c668e4ee3d2dbb7d9e04d94c531a6a0f499471d32e4f77de12`。
- 量化：`validation/results/98b9ef89ee33--dynamics-mv2-levels.json`。
- 测量脚本：`validation/scripts/analyze_mv2.py`。
