---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: 8987809250b1
vendor: "FabFilter"
product: "Pro-R"
evidence_level: L3
validation_status: S4-validated-Ableton-temporary-host
batch: B05
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Pro-R

## 身份与版本

- 厂商：FabFilter
- 产品族：Pro-R
- Family ID：8987809250b1
- 本机观测版本：1.1.5.0
- 格式：VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：reverb-natural
- 次能力方向：decay-rate-eq;distance
- 当前证据等级：L3
- 验证状态：S4-validated-Ableton-temporary-host

## 能做什么

- v1 以连续 Space、Decay Rate、Brightness、Character、Distance、Stereo Width、Predelay 与 Mix 构建自然算法空间。
- 六段 Decay Rate EQ 调整不同频率尾长，六段 Post EQ 调最终湿声频响。
- 可把房间模型/尾长与最终 EQ 分离，适合可测自然空间。

## 不建议用来做什么

- 不要把 Pro-R 2 的 Style、Thickness、Ducking、Auto Gate、Freeze、IR Import 写回 v1。
- 不要把 Post EQ 与 Decay Rate EQ 混淆。
- 不要仅以更宽/更亮判断自然。

## 信号流位置

- 100% Wet Aux，锁 Mix；先 Space/Decay/Distance，再 Decay Rate EQ，最后 Post EQ。
- 外部 Duck 用后级压缩/自动化，因为 v1 无内置 Duck。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Space / Decay Rate | 连续房间模型/基准尾长与整体倍率。 | 先选空间形态，再把尾长贴合节奏。 |
| Distance | 改变靠近/远离声源的早反射与建立。 | 主唱保持较近，背景层再拉远。 |
| Brightness / Character | 高低频/高频衰减与从透明到调制/反射性格。 | 从中性开始，小步加入角色。 |
| Decay Rate EQ | 按频率缩短/延长尾长。 | 缩短低中频和齿音尾，而非只用 Post EQ。 |
| Post EQ / Width / Predelay | 最终湿声频响、宽度和起始间隔。 | Aux 低切/低通，Width/Predelay 用 Mono/咬字检查。 |

## Gain Staging

Wet RMS 匹配不同 Space/Decay；Post EQ 改响度后补偿。避免引用 Pro-R 2 的输出计量。

## 延迟、相位与过采样

v1 手册未给具体延迟/OS；S4 测 PDC、脉冲、频段 RT60。

## Mono/Stereo

Width 从 Mono 到 Stereo/超宽的确切 v1范围待回读；干声中心独立，湿声折叠验证。

## 适用场景

- 自然短 Room/Ambience。
- 主唱透明 Hall。
- 按频率缩短低中频/齿音尾。

## 路由

- Stereo Aux 100% Wet。
- 后级外部 Duck/自动化。

## 参数起点

- Space 对应 0.6–1.5 s、Predelay 20–60 ms、Distance 近中。
- Decay Rate EQ：低频 50–80%、高频 50–80% 起。
- Post EQ 高通 120–250 Hz、低通 6–12 kHz。

## 调整目标

- 空间自然且频段尾长不遮词。
- Distance 增加深度而不让主唱退后。

## 调整时听什么

- Decay Rate 与 Post EQ误用。
- Character 过高造成 Echo/Chorus。
- 低中频尾堆积。

## 何时停止

- 空间在上下文成立且每个频段尾长有理由。
- 继续增加 Character/Width 只显效果时停止。

## 常见失败

- v2 功能倒灌。
- 只用 Post EQ 削尾。
- Distance/Predelay混淆。
- Aux Mix错误。

## 替代方案

- ValhallaVintageVerb：更多复古算法。
- ValhallaPlate：专向 Plate。
- Abbey Road Chambers：音箱/话筒房间链。

## 专业案例与工作流线索

- FabFilter v1 手册确认 Decay Rate EQ 与 Post EQ 是不同层：前者改变尾长，后者只改最终频响。

## 待执行测试

- v1 UI 枚举和 v2功能排除。
- Space/Distance/Character 脉冲与早晚能量。
- Decay Rate EQ 分频 RT60 与 Post EQ 对照。

## 已测结果

- [[projects/p1-plugin-knowledge-base/validation/reports/8987809250b1--Pro-R|S4 默认全湿脉冲验证]]：本机 1.1.5、Default Setting、Mix 100%、Space 2.50 s、Predelay 0.6 ms。
- 首脉冲 onset 7.292 ms、拟合 T60 2.1497 s；三次拟合 2.1497/2.1129/2.1394 s。
- Correlation -0.018777、Side/Mid +0.1632 dB；默认尾部很宽，Aux 返回必须检查 Mono Fold-down。
- 未做听感等响；Peak/RMS 只记录渲染条件，不用于音质优劣判断。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | natural-algorithmic-reverb |
| mode | pro-r-v1 |
| main_controls | space,decay_rate,distance,brightness,character,predelay,width,decay_eq,post_eq |
| risk_flags | version-leak,masking,over-width |
| validation | early-late-band-rt60 |

## 来源

- [[sources/音乐制作/插件资料/FabFilter/Pro-R资料|Pro-R 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]

## 开放问题

- v1.1.5 的 Width/Predelay 范围和报告延迟？
