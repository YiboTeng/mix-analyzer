---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: 98b9ef89ee33
vendor: "Waves"
product: "MV2"
evidence_level: L3
validation_status: passed-l3
batch: B03
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# MV2

## 身份与版本

- 厂商：Waves
- 产品族：MV2
- Family ID：98b9ef89ee33
- 本机观测版本：12.7.0.209
- 格式：VST2 | VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：compression-upward-downward
- 次能力方向：density;low-level-detail
- 当前证据等级：L3
- 验证状态：passed-l3

## 能做什么

- Low Level 从下向上提升低于阈值的内容，High Level 从上向下衰减高于阈值的内容。
- Cut/Boost 表与最大值数字分别显示上下行增益变化；Output Gain 做最终补偿。
- 少量控制可快速增加低电平细节和限制峰值。

## 不建议用来做什么

- 不要在噪声、呼吸、房间尾音未清理时大推 Low Level。
- 不要把 Low Level 当普通 Makeup Gain。
- 不要同时大幅向上和向下把所有微动态夹成窄带。

## 信号流位置

- 清理、呼吸控制、降噪后再用，避免低电平垃圾被抬起。
- 常放在基础峰值压缩后做轻度密度，而不是取代所有动态。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Low Level | 对阈值以下内容做 bottom-up 提升，范围至 +48 dB。 | 从 0 小推，观察 Boost 表并听弱字/噪声共同变化。 |
| High Level | 对阈值以上内容做 top-down 压缩，范围至 -48 dB。 | 先限 1–3 dB 峰值，不与前级重复重压。 |
| Output Gain | 最终输出衰减。 | 将整体 Active RMS 匹配旁通并防削波。 |
| Cut / Boost Meters | 显示上下行处理及最大值。 | 重置后在代表片段记录分布，不只看峰值数字。 |

## Gain Staging

向上压缩必然改变平均响度。用 Output Gain 匹配主语音 Active RMS，并单独测句间/呼吸 RMS；否则更近、更清楚可能只是低电平整体变响。

## 延迟、相位与过采样

本机 Waves MV2 12.7.0.209 VST3 Stereo 在 Ableton Live 11.3.43 / 48 kHz 报告 64 samples / 1.3 ms；离线导出由宿主 PDC 对齐。官方手册未给过采样，本轮也未验证 VST2、其它采样率或裸延迟。

## Mono/Stereo

Mono/Stereo 组件归一为产品族。立体声向上压缩可能放大左右不一致底噪，需测链接和声像。

## 适用场景

- Rap 轻句/尾字不够贴脸。
- Backing Vocal Bus 增加持续密度。
- 并行小比例提升细节。

## 路由

- 主唱链后段，先完成噪声/呼吸清理。
- Aux 并行，返回做高通/去齿。

## 参数起点

- Low Level 2–6 dB 的轻度 Boost 目标；High Level 从浅值开始，以实际 Cut 表与峰值约束判断，不能把旋钮负数直接当作最终衰减。
- Output 还原旁通响度。
- 若噪声同步升高，先减 Low Level 而非用 Gate 抵消。

## 调整目标

- 弱字更可懂，响字仍有重音。
- 句间噪声与呼吸不成为新前景。

## 调整时听什么

- 底噪、房间、耳机串音和呼吸抬升。
- 所有音节等高导致疲劳。
- High Level 与前级压缩重复。

## 何时停止

- 弱字进入稳定区而噪声仍在背景。
- 进一步 Low Level 主要提升非语音时停止。

## 常见失败

- 把向上压缩当透明清晰度。
- 未清理输入。
- Output 不匹配。
- Low/High 同时极端。

## 替代方案

- Vocal Rider：更慢的电平骑乘。
- Clip Gain：少数弱字手工补。
- Pro-MB 向上压缩：只提升指定频段。

## 专业案例与工作流线索

- Waves 官方手册把 Low/High 明确定义为 bottom-up 与 top-down，实验必须分别测 Boost 与 Cut。

## 待执行测试

- 已完成 Low/High 分离的静态曲线、持续音阶梯与隔离瞬态测试。
- 待补语音、呼吸、噪声三类 RMS 抬升比例。
- 待补 Output 单变量、Low/High 联动、Stereo Link 与 Clip Gain/Vocal Rider 等响盲听。

## 已测结果

- 本机 `MV2 Stereo` 12.7.0.209 VST3、Ableton Live 11.3.43 / 48 kHz 真实加载；宿主报告 64 samples / 1.3 ms。
- Low/High/Output 均为 0 时对旁路五档稳态增益 0 dB、直接相关 1.0，是本轮中性控制。
- Low `+26.2` 相对中性五档稳态增益从 +20.726 递减到 +6.541 dB，局部斜率 0.402948；最高持续音峰值触及 0 dBFS，全文件 RMS +8.797 dB。
- High `-12.0` 相对中性五档稳态增益从 +11.289 递减到 +4.087 dB，局部斜率 0.703470；它在本机并非简单输出衰减，而是伴随回补的较轻动态收敛，全文件 RMS +5.404 dB。
- 两种深度的持续音进入稳态 ±1 dB 约为 27–82 ms；这是含历史的输出稳定窗口，不是隐藏 Attack/Release 标定。
- 证据：[[projects/p1-plugin-knowledge-base/validation/reports/98b9ef89ee33--Waves-MV2|Waves MV2 L3 验证]]；量化：`validation/results/98b9ef89ee33--dynamics-mv2-levels.json`。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | upward-downward-compressor |
| mode | dual-level |
| main_controls | low_level,high_level,output |
| risk_flags | noise-lift,flattening,loudness-bias |
| validation | static-curve-speech-noise-ratio |

## 来源

- [[sources/音乐制作/插件资料/Waves/MV2资料|MV2 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]
- [[projects/p1-plugin-knowledge-base/validation/reports/98b9ef89ee33--Waves-MV2|MV2 L3 验证报告]]

## 开放问题

- Low/High 的隐藏阈值、Knee、时间常数与同时动作如何？
- Output 标度、Mono/Stereo Link、VST2 与其它采样率如何？
