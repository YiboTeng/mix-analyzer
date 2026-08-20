---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: 83165b3547f7
vendor: "FabFilter"
product: "Timeless 3"
evidence_level: L3
validation_status: S4-validated
batch: B05
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Timeless 3

## 身份与版本

- 厂商：FabFilter
- 产品族：Timeless 3
- Family ID：83165b3547f7
- 本机观测版本：3.0.5.0
- 格式：VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：delay-creative
- 次能力方向：multitap;modulation;ducking;feedback-fx
- 当前证据等级：L3
- 验证状态：S4-validated

## 能做什么

- 双延迟线、最多16 Tap、0–200% Feedback/Cross Feedback、Ping Pong、Tape/Stretch Read Mode。
- 最多6 Filter置于Delay之后、Feedback之前，重复逐次被滤；Drive/LoFi/Diffuse/Dynamics/Pitch五效果。
- Envelope/LFO/EG/MIDI/XY可调制Wet Level实现Ducking；Freeze和Auto Mute Self-Osc管理创意反馈。

## 不建议用来做什么

- 不要一开始使用16 Tap与多调制。
- 不要 Feedback>100 或非线性Filter自激而关闭Auto Mute。
- 不要把Dynamics旋钮直接称专用Duck；常用是Envelope Follower调Wet Level。

## 信号流位置

- 100% Wet Aux并Lock Mix；先基础Delay/Feedback/Filter，再加Tap/Mod/FX。
- Ducking用主输入Envelope Follower负向调Wet Level。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Delay/Sync/Read Mode | 基础时间、节拍与Tape变调或Stretch保音高。 | 常规Sync；自动化时间时按想要Pitch Glide与否选。 |
| Feedback/Cross/PingPong | 同通道/跨通道反馈和反弹。 | 20–40%起，>100只短自动化。 |
| Taps | 最多15附加Tap+主Tap的时间/电平/声像。 | 先2–4 Tap按节奏空隙排，不铺满。 |
| Filters | 重复每轮进一步滤波。 | HP/LP置反馈路径，逐次变暗/变薄。 |
| EF→Wet Level / FX | 输入包络Duck湿声及Drive/LoFi/Diffuse/Pitch。 | 先搭Duck，再一次加一个FX。 |

## Gain Staging

Aux 100% Wet；比较Tap/FX时匹配Wet RMS。Feedback>100和Drive会改变峰值，设置Output上限并记录重复衰减。

## 延迟、相位与过采样

Pitch开启会把最短Delay从5提高到45ms；官方未列PDC/OS。S4测各FX、ReadMode和PDC。

## Mono/Stereo

Stereo Width、Delay Time Pan、Cross Feedback和M/S模式会改变声场；主唱干声保持中心，Mono强制。

## 适用场景

- 复杂句尾Throw。
- Ducked节奏Delay。
- 扩散成Reverb-like尾。
- Pitch反馈上升/下降。

## 路由

- Stereo Aux 100% Wet并Lock Mix。
- 自动化Send、Freeze、Feedback或Tap电平。

## 参数起点

- 1/8D或1/4、Feedback20–35%、2–4 Tap、HP180–300Hz、LP5–9kHz。
- EF负向调Wet Level，主唱发声时退3–8dB。
- Auto Mute Self-Osc On。

## 调整目标

- 重复占据节奏空隙并在发声时退后。
- 复杂度可逐层消融解释。

## 调整时听什么

- 自激、Pitch递增失控、Filter共振。
- Tap过密像混响并遮词。
- M/S/跨反馈Mono相消。

## 何时停止

- 每个Tap/FX有明确作用。
- 关闭任何层无差异就删除。

## 常见失败

- 多功能全开。
- Dynamics/Ducking语义混淆。
- Pitch最短时间变化未记录。
- Freeze遗留。

## 替代方案

- H-Delay：快速实用。
- Abbey Road Chambers STEED。
- VintageVerb：直接混响。

## 专业案例与工作流线索

- FabFilter 官方明示Send应100% Wet、Pitch使最短Delay变45ms、Filter在反馈前；三点直接约束路由与测试。

## 待执行测试

- Tap时间/电平矩阵与节拍。
- EF Duck响应和FX消融。
- Feedback>100、Freeze、AutoMute安全测试。
- Pitch/ReadMode/PDC/Mono。

## 已测结果

- Ableton Live 11.3.43、48 kHz、Host 160 BPM、Default Setting：左右 Delay 350.0/353.5 ms。
- 原生 `MIX` 100% 时，首脉冲左右首个湿声 350.229/353.729 ms，固定左右差 3.500 ms；后四次重复间隔 352.792/351.958/352.604/353.021 ms。
- 首五个反馈峰值 -18.4448/-30.9966/-42.6345/-51.3951/-60.6956 dBFS；Correlation 0.809128，Side/Mid -9.7673 dB。
- Default Setting 的原生 Mix 为 0%；Send/Aux 必须显式把主旋钮右侧 `MIX` 环设到 100%，不能依赖宿主设备壳的 Mix 显示。
- 本轮未验证 Taps、FX、Duck、Freeze、Pitch、Read Mode、Feedback>100 或 Auto Mute 安全行为。
- 详见 [[projects/p1-plugin-knowledge-base/validation/reports/83165b3547f7--Timeless-3|Timeless 3 L3 验证]]。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | programmable-delay |
| mode | multitap-feedback |
| main_controls | delay,feedback,cross,taps,filters,fx,mod,width,mix |
| risk_flags | self-oscillation,masking,complexity,mono-loss |
| validation | tap-timing-duck-feedback-safety |

## 来源

- [[sources/音乐制作/插件资料/FabFilter/Timeless 3资料|Timeless 3 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]

## 开放问题

- 本机3.0.5.0各FX报告延迟和Envelope映射范围？
