---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: 47e12f69eb3c
vendor: "Waves"
product: "CLA-76"
evidence_level: L3
validation_status: passed-l3
batch: B03
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# CLA-76

## 身份与版本

- 厂商：Waves
- 产品族：CLA-76
- Family ID：47e12f69eb3c
- 本机观测版本：12.7.0.209
- 格式：VST2 | VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：compression-fet
- 次能力方向：peak-control;parallel;character
- 当前证据等级：L3
- 验证状态：passed-l3

## 能做什么

- 模拟两台不同修订的快速 FET 压限器，以 Input 驱动固定阈值结构并用 Output 回补。
- Attack/Release 旋钮 1–7 且数值越大越快；Ratio 有 4/8/12/20 与 All 模式。
- Bluey/Blacky 提供不同硬件修订音色；本机 v12 面板有 Analog 50/60 Hz/Off，但没有新版在线资料所示 Mix、Trim，不能把新版控件外推到当前实例。

## 不建议用来做什么

- 不适合首选透明大幅电平整理。
- 不要误把 Attack 1 当最快、7 当最慢。
- 不要在 Input 推高后只用 Output 让结果更响而不匹配。

## 信号流位置

- 常作为串联压缩的快速峰值控制，放在较慢电平压缩之前。
- 也可在 Aux 做重压并行；发送返回必须处理噪声、齿音和相位。
- 去齿可在前面降低检测干扰，饱和/激励后仍需复查。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Input / Output | Input 同时提高进电路电平与压缩量，Output 回补。 | 先用 Input 达到目标 GR，再用 Output 做等响度；本机 v12 无 Trim。 |
| Attack 1–7 | 从慢到快；高数字更快。 | 保留字头从 3–4 起；尖峰仍穿出向 6–7。 |
| Release 1–7 | 从慢到快。 | 从 5–7 的较快释放找贴脸感；出现喘振或失真则减慢。 |
| Ratio / All | 决定压缩强度与反馈网络音色；All 为夸张模式。 | 主唱从 4:1 起；8:1 控峰；All 多用于并行。 |
| Revision / Analog | 硬件修订与 50/60 Hz 模拟底噪选项。 | 先用 Analog Off 判断核心压缩，再等响度比较 Bluey/Blacky；并行需外部 Aux。 |

## Gain Staging

本机 v12 只有 Input 与 Output 负责核心增益结构，没有 Mix/Trim。Input 不是独立阈值：推高会同时增加送入固定阈值电路的电平和压缩量。应先锁定 Ratio/Attack/Release，用 Input 达到目标 GR，再用 Output 做等响度；Analog Off 作为无噪声基线。若需并行，使用 DAW Aux 或并行总线并复查相位与总电平。

## 延迟、相位与过采样

本机 Ableton Live 11.3.43 在 48 kHz 下对 `CLA-76 Stereo` VST3 报告 `Latency: 0 samples`。这只证明当前组件与采样率的宿主 PDC；Analog 噪声、非线性相位、其它格式与采样率仍需另测。本机没有内部 Mix，因此不存在本版本内部并行补偿的验证对象。

## Mono/Stereo

有 Mono/Stereo 组件但产品族只建一张卡。立体声总线应确认左右联动；主唱通常 Mono 实例。

## 适用场景

- 激进 Rap 主唱快速抓峰并增加前冲感。
- 与 CL 1B/Pro-C 2 串联：CLA-76 先削 2–5 dB 峰值。
- 并行 All-buttons 风格增加咬字和密度。

## 路由

- 主唱 Insert 的第一或第二级压缩。
- 100% Wet Aux 重压，Send 控制回添。

## 参数起点

- 4:1；Attack 3–4；Release 5–7；Input 调到响句约 2–5 dB GR。
- 更硬控峰：8:1、Attack 5–7、Release 5–7。
- 并行：All、较快 Attack/Release，返回从干声下 -15 至 -25 dB 起。

## 调整目标

- 响字峰值更稳定，辅音仍清楚。
- 释放跟随节奏恢复，不在每个音节间喘动。

## 调整时听什么

- Attack 过快让字头发钝。
- Release 过快在低音/元音处失真或噪声呼吸。
- Input 过高造成持续夹紧和中高频粗糙。

## 何时停止

- 峰值不再驱动后级失控且主唱仍有微动态。
- 再加 GR 只增加侵略性和噪声而不提高可懂度时回退。

## 常见失败

- 时间旋钮方向反读。
- All 模式直接全湿重压主唱。
- Analog 噪声在多实例叠加。
- 未等响度比较 Bluey/Blacky。

## 替代方案

- Pro-C 2：透明、可量化的控峰。
- Tube-Tech CL 1B mk II：更平滑电平整理。
- RVox：极简快速密度。

## 专业案例与工作流线索

- Waves 官方 Rap 指南把 Attack 6–7 用于激进主唱快速控峰；这只作为风格起点，仍需与字头保留对照。

## 待执行测试

- Release 1 与 7 的独立包络恢复测试；本轮固定 Release 4。
- Bluey/Blacky、Analog 50/60/Off、4/8/12/20/All 的谐波、底噪与等响度单变量。
- Mono/Stereo 链接行为、连续主唱等响盲听，以及串联 CL 1B 与单级重压比较。

## 已测结果

- 本机真实加载：Waves `CLA-76 Stereo` V12（文件系统 12.7.0.209）VST3；Ableton Live 11.3.43、48 kHz 报告 0 samples。
- 面板预置 `A: Start Me Up`：Bluey、Input 30、Output 18、Attack 3、Release 4、Ratio 4:1、Meter GR、Analog Off；实见无 Mix/Trim。
- 同一 12 s 阶梯/瞬态夹具中，默认 Attack 3 相对旁路的稳态增益随输入峰值 -30/-24/-18/-12/-6 dBFS 分别为 +6.269/+6.275/+5.579/+0.882/-4.184 dB；从最低到最高档下降 10.454 dB，输出对输入回归斜率 0.5616，证明固定阈值 Input 驱动下压缩随电平显著增强。
- 仅把 Attack 3 改到 6.99（名义 7）后，五个隔离瞬态相对 Attack 3 的峰值进一步降低 0.882/1.707/1.637/1.644/1.653 dB；全文件峰值从 -1.424 降至 -2.306 dBFS。高数字确实更快、更强地抑制瞬态，而不是“更慢”。
- Attack 7 相对 Attack 3 的高电平稳态只再低约 0.13–0.15 dB，主要差异集中在瞬态，而非简单整体降音量；因此调 Attack 时应同时看字头与稳态 GR。
- 两个处理态 L-R 残差约 -141.49 dBFS；本夹具是双单声道，结果只证明该输入下左右一致，不等于完整 Stereo Link 测试。
- 详细报告：[[projects/p1-plugin-knowledge-base/validation/reports/47e12f69eb3c--Waves-CLA-76|CLA-76 L3 验证]]；量化：`validation/results/47e12f69eb3c--dynamics-compressor.json`。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | fet-compressor |
| mode | bluey-or-blacky |
| main_controls | input,output,attack,release,ratio,revision,analog |
| risk_flags | attack-direction,over-compression,noise,loudness-bias |
| validation | envelope-harmonic-latency |

## 来源

- [[sources/音乐制作/插件资料/Waves/CLA-76资料|CLA-76 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]

## 开放问题

- Blacky、All-buttons 与 Analog 50/60 在本机 v12 的可量化差异？
- Stereo 组件的通道链接行为，以及其它采样率/格式的宿主延迟？
