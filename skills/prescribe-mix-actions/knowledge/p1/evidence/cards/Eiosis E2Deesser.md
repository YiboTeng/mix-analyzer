---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: 0188bc583c26
vendor: "Eiosis"
product: "Eiosis E2Deesser"
evidence_level: L3
validation_status: passed-l3
batch: B02
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Eiosis E2Deesser

## 身份与版本

- 厂商：Eiosis
- 产品族：Eiosis E2Deesser
- Family ID：0188bc583c26
- 本机观测版本：1.0.9.3
- 格式：VST2 | VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：deessing-spectral
- 次能力方向：sibilance;voice-specific;fine-smoothing
- 当前证据等级：L3
- 验证状态：passed-l3

## 能做什么

- 以 Solo Vocal、Background Vocals、Voice Over、Guitar Squeaks、Overheads、Stereo/M-S Mastering 等检测模式适配不同素材。
- Auto 动态调整齿音频响并削平不悦峰值；Smooth 以轻柔饱和降低齿音峰度；Dry/Wet、Gain 提供并行与补偿。
- 独立处理被检测齿音的音色与电平，目标是把齿音重新塑形而非只做宽带压低。

## 不建议用来做什么

- 不要把 Background Vocals 模式用于带立体声混响的单人主唱，官方指出左右独立检测可能被混响不同触发。
- 不要把 Voice Over 的更灵敏检测直接用于所有人声；它更易抓到噪声和呼吸。
- 不要同时把 Sensitivity、Auto、Smooth 和 Reduction 推到极端。

## 信号流位置

- 通常在主要高频激励前；若后级增加新谐波，可在链尾轻度补控。
- 先选与素材相符的检测 Mode，再用齿音独听/可视化校准，最后用 Auto/Smooth 塑形。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Mode | 切换按独唱、叠唱、旁白、乐器或母带优化的检测与通道行为。 | 干单主唱先 Solo Vocal；硬分轨叠唱才 Background Vocals；其余按官方用途试。 |
| Sensitivity / Idle Threshold | 控制检测灵敏度与静默/噪声处误触发。 | 提高至完整捕获齿音，再用 Manual Idle Threshold 排除呼吸与底噪。 |
| Auto | 动态平滑齿音内部的频率峰值。 | 口哨/尖峰式齿音逐步增加；完整辅音被掏空时回退。 |
| Smooth | 以温和饱和降低齿音峰度和尖锐幅度。 | 需要保留空气但减硬时小幅使用，并等响度比较。 |
| Dry/Wet / Gain | 混合原信号与处理结果并补偿 ±18 dB 输出。 | 先 100% Wet 校准，再用 Dry/Wet 回添自然齿音；Gain 只做电平匹配。 |

## Gain Staging

Gain 范围大，Smooth 也会改变峰度与感知响度。固定 Output Gain 状态、用后级 Trim 等响度，分别记录齿音事件峰值和主体 Active RMS；Dry/Wet 不能用于偷偷增加旁路音量。

## 延迟、相位与过采样

本机 1.0.9.3 VST3 在 Ableton Live 11.3.43 / 48 kHz 报告固定 `720 samples / 15 ms`，Solo Vocal、Voice Over 与所测 Auto/Smooth 状态一致；导出由宿主 PDC 对齐。当前 UI 未见可关闭的 Lookahead 或过采样控件，不把它当零延迟处理器，也不把 VST3 结果外推到 VST2、其它采样率或其它 build。

## Mono/Stereo

Solo Vocal 对左右统一检测；Background Vocals 左右独立，适合硬声像叠唱但不适合带立体声混响的独唱；M/S Mastering 只用于明确的立体声总线。

## 适用场景

- 尖峰式或口哨式齿音，需要同时平滑频谱。
- 硬声像 Background Vocal 的左右独立检测。
- 旁白/说唱中需要更快检测但可管理呼吸误触发。

## 路由

- 主唱或叠唱 Insert。
- Stereo/M-S 模式仅用于对应总线实验，不作为默认。

## 参数起点

- Solo Vocal；Sensitivity 从低上推，先保证只抓目标；Auto 与 Smooth 从 0 小步增加。
- Dry/Wet 100% 校准，再视自然度回到 70–100%；Gain 等响度。
- Voice Over 模式若使用，必须同时设置 Manual Idle Threshold。

## 调整目标

- 齿音峰度和刺耳下降，但 S 仍有空气与可辨识形态。
- 独听检测不包含大量呼吸、F/H 和元音。

## 调整时听什么

- Auto 过高造成齿音空洞或带滤波感。
- Smooth 过高造成沙哑、饱和或更亮错觉。
- 左右独立检测造成声像跳动。

## 何时停止

- 最坏齿音被重新整形而不是消失。
- 开始出现咬舌、声像不稳或呼吸被持续处理时回退。

## 常见失败

- Mode 与素材不匹配。
- Voice Over 未管理 Idle Threshold。
- Background Vocal 模式处理带混响独唱。
- Auto/Smooth/Dry-Wet 未做电平匹配。

## 替代方案

- FabFilter Pro-DS：Wide/Split 和更直接的阈值/范围工作流。
- soothe2：问题不只齿音而是多处移动共振。
- Pro-Q 3 动态 EQ：单一稳定频率。

## 专业案例与工作流线索

- 官方指南给出不同检测 Mode 的明确禁忌，尤其 Background Vocals 与带混响独唱的冲突；选择模式应先于调旋钮。

## 待执行测试

- 与 Pro-DS 在带音素标注的 S/T/CH 数据集上做检测精确度、亮度保留和 lisp 盲听。
- Back Vocals 左右独立检测、Stereo/M-S/Mid Mastering、Idle Threshold 与误触发。
- Sensitivity、Amount、自定义 EQ、Dry/Wet、Auto/Smooth 多档曲线和其它采样率/格式。

## 已测结果

本机 1.0.9.3 VST3 已在 Ableton Live 11.3.43 / 48 kHz 真实加载。默认 Solo Vocal（Sensitivity/Amount/Auto/Smooth/Dry-Wet 均 50%、Gain 0 dB）相对共享旁路，把三个稀疏源事件各降低约 `2.449 dB`，但稳定多音和晚段动态区约为 0 dB 差。

只切 Voice Over 后，源事件相对 Solo 再低 `0.676 dB`，7–14 kHz 与 14 kHz 以上分别再低约 `0.63/1.06 dB`。只把 Auto 50→100%、Smooth 固定 50% 时，源事件约 `+0.063 dB`；只把 Smooth 50→100%、Auto 固定 50% 时，源事件约 `-0.316 dB`，7–14 kHz约 `-0.41 dB`。因此 Auto 不是“更多去齿”的线性量，Smooth 的当前端点会进一步降低事件，但实际工作仍应从默认附近微调并等响复核。

Auto100/Smooth0 与 Auto0/Smooth100 的组合端点相差 `1.061 dB`，只用于显示两者组合边界，不冒充单控件传递函数。宿主固定报告 `720 samples / 15 ms`；默认 Dry/Wet 50%，所测衰减不是全湿上限。完整证据见 [[projects/p1-plugin-knowledge-base/validation/reports/0188bc583c26--Eiosis-E2Deesser|E2Deesser L3 验证]]。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | spectral-de-esser |
| mode | source-specific-detection |
| main_controls | mode,sensitivity,idle_threshold,auto,smooth,dry_wet,gain |
| risk_flags | wrong-mode,breath-trigger,stereo-wander,lisp |
| validation | mode-detection-spectral-difference |

## 来源

- [[sources/音乐制作/插件资料/Eiosis/Eiosis E2Deesser资料|Eiosis E2Deesser 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]
- [[projects/p1-plugin-knowledge-base/validation/reports/0188bc583c26--Eiosis-E2Deesser|E2Deesser L3 验证]]

## 开放问题

- 1.0.9.3 与在线手册其它 build 的 Idle Threshold、模式与通道行为是否完全一致？
- Back Vocals、M/S 与自定义 EQ 在真实语音、立体声混响和自动化下的可重复边界？
