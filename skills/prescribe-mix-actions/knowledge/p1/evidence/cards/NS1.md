---
type: plugin-card
status: active
created: 2026-08-19
updated: 2026-08-20
family_id: 29b6d9504a55
vendor: "Waves"
product: "NS1"
evidence_level: L3
validation_status: passed-l3
batch: B01
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# NS1

## 身份与版本

- 厂商：Waves
- 产品族：NS1
- Family ID：29b6d9504a55
- 本机观测版本：12.7.0.209
- 格式：VST2 / VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：noise-reduction-simple
- 次能力方向：adaptive-suppression;workflow-speed
- 当前证据等级：L3
- 验证状态：passed-l3

## 能做什么

- 实时自适应区分前景语音/音乐与背景噪声。
- 单一 Fader 决定抑制量，Attenuation Meter 显示从输入移除的总能量。

## 不建议用来做什么

- 不要把 NS1 当作可精确选择噪声模型、频段或伪影类型的修复套件。
- 不要在低信噪比人声上把 Fader 推到语尾水声、呼吸门控和高频孔洞明显。

## 信号流位置

- 主唱链前段，在重压缩、上行压缩、激励与饱和之前。
- 先处理稳定底噪，再用 Gate/Expander 控制句间；两者职责不要重叠到过度。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Suppression Fader | 决定自动噪声抑制量。 | 从 0 慢慢上推，刚好让噪声退到编曲下方，不追求独听绝对静音。 |
| Attenuation Meter | 显示被移除的总体能量。 | 观察强弱音节是否持续触发过深衰减，并结合听感回退。 |

## Gain Staging

NS1 会减少噪声能量，从而改变整体 RMS。对比时以活跃人声主体匹配响度，另测静音/句间噪声 RMS；不要把整体电平下降误写成音质提升。

## 延迟、相位与过采样

本机 NS1 Stereo 12.7.0.209 VST3 在 Ableton / 48 kHz 回读 0 samples。当前只验证该格式和采样率；不外推 Mono、VST2 或其它采样率。

## Mono/Stereo

手册列出 Mono/Stereo 组件；产品族合并建卡。单声道主唱优先 Mono/自动适配组件，立体声 Stem 要检查左右噪声差异是否造成声像摆动。

## 适用场景

- 家录稳定空调、电脑风扇或前级底噪。
- 需要比 RX 精修更快的实时草混/录音监听清理。

## 路由

- 单轨 Insert 前段；在 Vocal Rider/MV2 等会抬高低电平的工具之前。
- 严重、变化快或音乐性噪声改用 RX/Spectral 工具。

## 参数起点

- Fader 从 0 上推，不给固定万能数值；以噪声刚退到伴奏下、语尾仍自然为起点。
- 若独唱检查出现水声/门控，退回一档并让编曲遮蔽剩余噪声。

## 调整目标

- 句间稳定底噪下降，活跃人声的音色、气息和尾音基本不变。
- 后级压缩/骑乘不再显著抬起噪声底。

## 调整时听什么

- 词尾、气息和低电平辅音是否出现水声或开合。
- 高频是否变空、立体声噪声是否造成声像漂移。

## 何时停止

- 在完整编曲中噪声不再分散注意力时停止。
- 继续上推只改善独唱静音、却伤害语尾和气息时回退。

## 常见失败

- 把动态房间反射、伴奏泄漏或分离伪影当稳定噪声处理。
- 与 Gate/Expander 叠加过深，形成句间真空和音节截断。
- 在 MV2/Vocal Rider 之后处理，噪声已被抬高且检测更困难。

## 替代方案

- iZotope RX Spectral De-noise：需要噪声学习与更精细控制时。
- FabFilter Pro-G：句间扩展，不替代连续噪声抑制。
- 手工 Clip Gain 与房间音铺底。

## 专业案例与工作流线索

- Waves 官方把 NS1 定义为实时、自适应、单推子噪声抑制，适合语音、广播与音乐。

## 已执行测试

- A: Default Preset，仅切 Suppression 0、50、100；48 kHz/24-bit Composite，所有其它链上设备停用。
- 分别量化脉冲、稳定多音、固定人声、空间与动态区域的整体电平、50 ms 活跃窗、相关/残差和固定人声频带能量。
- 回读宿主延迟并保存 Suppression 100 风险端点工程快照。

## 已测结果

- Suppression 50 对固定人声整体 -0.271 dB，390 个活跃窗中位 -0.272 dB、仅 2 窗达到 1 dB；对脉冲/稳定多音分别 -2.808/-1.978 dB，证明是内容自适应而非固定输出衰减。
- Suppression 100 对固定人声整体 -13.141 dB，390/390 活跃窗全部超过 6 dB 衰减；这是有效语音损伤端点，不是推荐值。
- 50 条件下固定人声 7–14/14–24 kHz 区域能量约 -2.06/-4.07 dB；应听高频孔洞、擦音和气息，长窗频带结果不等于静态 EQ。
- 宿主延迟 0 samples。详细证据：[[projects/p1-plugin-knowledge-base/validation/reports/29b6d9504a55--Waves-NS1|NS1 L3 验证]]。

## 后续测试

- 已知 SNR 的白/粉噪、风扇噪与变化房间噪，测噪声下降、语音保留和伪影阈值。
- 强/弱音节、气息、句尾上的标注事件和盲听。
- NS1 前置与后置于压缩/上行压缩，以及 Mono/VST2/其它采样率。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | adaptive-noise-suppressor |
| mode | single-control-real-time |
| main_controls | suppression,attenuation_meter |
| risk_flags | musical-noise,tail-gating,stereo-wander |
| validation | noise-floor-and-speech-preservation |

## 来源

- [[sources/音乐制作/插件资料/Waves/NS1资料|NS1 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]
- [[projects/p1-plugin-knowledge-base/validation/reports/29b6d9504a55--Waves-NS1|NS1 L3 验证]]

## 开放问题

- 本机 Stereo 内部左右联动、Mono/VST2 与自动化行为是什么？
- 已知噪声类型/SNR 与 44.1/96 kHz 下的伪影阈值如何变化？
