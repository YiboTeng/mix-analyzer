---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: a0c159c0ffd1
vendor: "Valhalla DSP, LLC"
product: "ValhallaVintageVerb"
evidence_level: L3
validation_status: S4-validated-Ableton-temporary-host
batch: B05
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# ValhallaVintageVerb

## 身份与版本

- 厂商：Valhalla DSP, LLC
- 产品族：ValhallaVintageVerb
- Family ID：a0c159c0ffd1
- 本机观测版本：2.2.0
- 格式：VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：reverb-vintage-algorithmic
- 次能力方向：plate;hall;chorus
- 当前证据等级：L3
- 验证状态：S4-validated-Ableton-temporary-host

## 能做什么

- 多种 Hall/Plate/Room/Chamber/Random/Nonlin 算法覆盖透明、复古、调制和反向/门式空间。
- Color 改变带宽、量化/年代质感；Decay、Size、Attack、Predelay、Diffusion、Mod Rate/Depth 与频率衰减控制尾部。
- Mix 可锁定，适合 100% Wet Send 浏览预设。

## 不建议用来做什么

- 不要按模式名称直接假定现实房间尺寸。
- 不要用长亮尾掩盖咬字或填满句间。
- 不要把当前 4.x 新模式写回本机 2.2.0。

## 信号流位置

- 100% Wet Stereo Aux；Send 决定量，返回做高通/低通/去齿和 Duck。
- Predelay 与 Attack 分开：Predelay 隔开干声，Attack 改尾部建立形态。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Mode | 选择算法拓扑、密度、攻击与调制性格。 | 主唱从 Chamber/Smooth Plate/Smooth Random 起，逐模式等响度。 |
| Decay / Size / Attack | 尾长、模态尺度和建立形态。 | 先按节奏定 Decay，再用 Size/Attack 避免金属或淹字。 |
| Predelay | 干声到混响起始的间隔。 | Rap 从 20–80 ms 或节拍分数试，让首字保持前。 |
| Color / High-Low Decay | 年代带宽和不同频段尾长。 | 先 NOW/中性，低切尾、缩短高频尾以腾位置。 |
| Mod Rate/Depth / Mix Lock | 调制尾部并锁定干湿。 | 自然空间低调制；Aux 锁 Mix 100%。 |

## Gain Staging

Aux 发送返回以 Wet RMS/主唱 Active RMS 比例记录；比较 Mode 时固定 Predelay/Decay、匹配湿声响度。

## 延迟、相位与过采样

官方未列本机 2.2.0 延迟/OS；算法内部时变不可做静态相位结论。S4 测 PDC、脉冲衰减与导出。

## Mono/Stereo

Stereo Aux 为常规；Width/算法差异需相关性和 Mono Fold-down。干声核心保持 Mono/Mid。

## 适用场景

- 短 Chamber 给主唱黏合。
- Smooth Plate 提供明亮密度。
- 长 Hall/Nonlin 用于 Throw 与段落效果。

## 路由

- Stereo Reverb Aux 100% Wet。
- 需要自动 Duck 时由主唱侧链后级压缩或自动化 Send。

## 参数起点

- Decay 0.6–1.5 s、Predelay 30–70 ms、High Cut 6–10 kHz、Low Cut 120–250 Hz。
- 长效果 2–4 s 只自动化句尾。
- Mix Lock 100%。

## 调整目标

- Solo 可闻空间，混音中不抢词。
- 尾部在下一关键重音前下降。

## 调整时听什么

- 齿音尾、低中频堆积、调制跑音。
- Predelay 变成离散 slap。

## 何时停止

- 空间感可感但关掉才明显。
- 尾部遮下一句时先缩 Decay/频段而非只降 Send。

## 常见失败

- 长亮尾常开。
- Mode 新旧版本混写。
- Aux Mix 非 100%。
- 只 Solo 调混响。

## 替代方案

- ValhallaPlate：专向板式。
- Pro-R：Decay Rate EQ 可视化自然空间。
- Abbey Road Chambers：具体音箱/房间链。

## 专业案例与工作流线索

- Valhalla 官方模式说明把 Smooth Plate 定位为透明自然、Chamber 为密集低染色；它们是候选起点而非优劣排名。

## 待执行测试

- 本机 2.2.0 实际模式枚举。
- 短脉冲测 RT60、早期建立、频段尾长和相关性。
- Send/Duck/Mono 盲听。

## 已测结果

- [[projects/p1-plugin-knowledge-base/validation/reports/a0c159c0ffd1--ValhallaVintageVerb|S4 默认全湿脉冲验证]]：本机 2.2.0、Concert Hall、Mix 100%、Predelay 20 ms、Decay 4.00 s。
- 首脉冲 onset 25.562 ms，拟合 T60 4.5925 s；三次拟合 4.5925/4.6430/4.4416 s，后两段受前尾重叠、末段受 6 s 截断。
- 全湿相关系数 0.010724、Side/Mid -0.0931 dB；旁通为 1.0、-92.7012 dB。默认全湿会把近似纯 Mid 脉冲扩展为宽 Side 尾部，需做 Mono Fold-down 检查。
- 本次未做听感等响，只用 onset、衰减和相关性支持行为判断；不得据 Peak/RMS 差异声称音质优劣。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | algorithmic-reverb |
| mode | multi-vintage-mode |
| main_controls | mode,decay,size,attack,predelay,color,damping,mod,mix |
| risk_flags | masking,sibilant-tail,version-gap,mono-loss |
| validation | rt60-build-correlation |

## 来源

- [[sources/音乐制作/插件资料/Valhalla DSP, LLC/ValhallaVintageVerb资料|ValhallaVintageVerb 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]

## 开放问题

- 2.2.0 各 Mode 的 PDC、等响音色差异与 Mono Fold-down 仍需后续扩展测试；不影响当前默认状态 L3 结论。
