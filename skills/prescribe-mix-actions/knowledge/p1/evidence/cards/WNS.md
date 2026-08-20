---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: 6756edefac77
vendor: "Waves"
product: "WNS"
evidence_level: L3
validation_status: passed-l3
batch: B01
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# WNS

## 身份与能力

- 本机：Waves WNS Stereo 12.7.0.209 VST3；Family ID `6756edefac77`。
- 主方向：noise-reduction-multiband-dialogue；次方向：six-band-suppression、zero-latency-restoration。
- 用途：无需 Noise Print 的对白/人声宽带噪声抑制，对不同频带分别限定最大衰减。
- 不适用：专用爆破音、嘴部点击、呼吸电平或频谱修复；尤其不能冒充 De-plosive。

## 控制语义

| 控制 | 范围/默认 | 调整目标 |
|---|---|---|
| Threshold | -80–0 dB / -20 dB | 放在对白主体下方，区分噪声与有效语音。 |
| 6 Band Gains | -32–+6 dB / 0 dB | 限定各频带最大抑制；只降低含噪频段。 |
| Smoothing | 1–100 / 50 | 平滑频带间/时间变化，防止孔洞与颗粒。 |
| Low/High boundary | LF 20–4000；HF 400–20000 | 把处理限制在问题频谱。 |
| Suggest | 自动起点 | 只作起点，必须人工复核弱字尾和擦音。 |

## 推荐工作流

置于压缩、Vocal Rider、激励和饱和之前。从所有 Gain 0 dB 开始，循环纯噪、弱字尾、正常语句与齿音；设置 Threshold 后逐段降低，噪声刚退入编曲即停止。过量迹象是语尾断裂、齿音水声、高频孔洞、空间尾不连续或有效音节上持续大衰减。

本机压力状态把固定人声整体压低约 13.91 dB，仅用来展示风险。默认电平中性但独立宿主状态不能可靠 Null；不声称逐比特透明。

## 延迟、声道与替代

- 本机 Stereo VST3 / 48 kHz 宿主报告 0 samples；适合实时对白链。
- Mono、VST2、其它采样率及 Suggest 行为未验证。
- 简单单推子快速降噪：NS1；可学习噪声轮廓/频谱修复：专用 RX Editor 类工具；爆破音：Clip Gain + 动态低频 EQ/自动化。

## P0 映射

- diagnosis：`broadband_dialogue_noise`
- route：`early_insert_before_dynamics`
- parameter_target：`noise_below_context_while_weak_speech_survives`
- stop_conditions：弱字尾丢失、擦音水声、频谱孔洞、有效语句持续深衰减。
- retest：句间噪声 RMS、弱字尾保留、活动语句残差、等响度 A/B。
- conflict：若诊断是 `plosive_low_frequency_event`，不得选 WNS，回退 Clip Gain/动态 EQ。

## 证据与来源

- [[sources/音乐制作/插件资料/Waves/WNS资料|WNS 资料]]
- [[projects/p1-plugin-knowledge-base/validation/reports/6756edefac77--Waves-WNS|WNS L3 验证]]
- 当前 L3 不包含校准噪声 SNR 或真实工程 L4。

