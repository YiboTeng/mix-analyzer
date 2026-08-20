---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: 75f2f9574990
vendor: "Waves"
product: "X-Click"
evidence_level: L3
validation_status: passed-l3
batch: B01
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# X-Click

## 身份与能力

- 本机：Waves X-Click Stereo 12.7.0.209 VST3；Family ID `75f2f9574990`。
- 主方向：restoration-click；次方向：mouth-click-adjacent、digital-click、vinyl-scratch。
- 用途：压缩前移除孤立点击、唇拍和类似短脉冲缺陷；作为无法加载的 RX 10 Mouth De-click 的可验证近邻替代。
- 不适用：连续底噪、爆破低频、呼吸电平、宽带失真；不应整段高强度处理鼓或硬辅音素材。

## 控制语义

| 控制 | 含义 | 调整目标 |
|---|---|---|
| Threshold | 可被检测的点击强度/尺寸上限随数值增加。 | 从 0 提高到目标点击刚进入 Difference。 |
| Shape | 检测事件的形状/时间尺度。 | 较低偏短数字点击，较高偏宽刮擦；以 Difference 不含有效瞬态为准。 |
| Audio / Difference | 正常结果 / 被移除内容。 | 用 Difference 建立“只包含缺陷”的停止条件。 |

## 推荐工作流

置于重压缩、饱和、激励之前。循环最明显缺陷、最弱辅音、齿音和鼓串音；从 0/50 开始用 Difference 调 Threshold 与 Shape，再回 Audio 等响度复核。若 Difference 出现辅音或表演瞬态，先回退 Threshold；问题稀疏时优先片段自动化/事件编辑。

手册 MCR 50/70 只可作为诊断起点。本机压力测试在该值下把合成脉冲列削低 89.69 dB，说明必须按素材回退，不能当通用 Preset。

## 延迟、声道与风险

- 官方/本轮记录 2624 samples；不适合实时监听链，适合编辑或离线修复。
- 本轮只验证 Stereo VST3 / 48 kHz；Mono、VST2 与其它采样率未知。
- 主要失败模式：吞鼓击/硬辅音、擦音变薄、过度插值、两遍处理累积涂抹。
- 替代：稀疏事件用 Clip Gain/波形编辑；专用 Mouth De-click 可在安装修复后重新评估 RX；连续噪声用 NS1/WNS。

## P0 映射

- diagnosis：`mouth_click_or_short_impulse`
- route：`pre_compression_insert_or_offline_event`
- parameter_target：`difference_contains_only_defect`
- stop_conditions：Difference 出现有效辅音/鼓击；Audio 字头变钝；问题在编曲中已不可察。
- retest：缺陷事件峰值、Difference 审听、有效辅音残差、等响度 A/B。

## 证据与来源

- [[sources/音乐制作/插件资料/Waves/X-Click资料|X-Click 资料]]
- [[projects/p1-plugin-knowledge-base/validation/reports/75f2f9574990--Waves-X-Click|X-Click L3 验证]]
- 当前 L3 不包含带标签嘴部点击的准确率或真实工程 L4。

