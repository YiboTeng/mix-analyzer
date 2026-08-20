---
type: plugin-card
status: deferred
created: 2026-08-20
updated: 2026-08-20
family_id: f9e0e7aeb790
vendor: "SoundToys"
product: "MicroShift"
evidence_level: L2
validation_status: S4-replaced-vst2-unavailable
batch: B04
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# MicroShift

> [!note] S4 替换
> 本机仅有 VST2，现有 Ableton 配置未暴露 VST2 且本任务不改扫描偏好；正式集合已由当前可达的 Waves PS22 Spread 替换。本卡保留为历史研究，不计入最终 40 款。

## 身份与版本

- 厂商：SoundToys
- 产品族：MicroShift
- Family ID：f9e0e7aeb790
- 本机观测版本：5.0.1.0
- 格式：VST2
- Studio One 可用性：current-filesystem-match
- 主能力方向：width-micro-pitch
- 次能力方向：doubler;send-effect
- 当前证据等级：L2
- 验证状态：S3-researched-S4-pending

## 能做什么

- 三种硬件启发 Style 结合时变微移调与短延迟制造宽度。
- Detune 与 Delay 以百分比缩放各 Style 的时变参数；Focus 只让分频以上受影响。
- Mix 100% 产生最清晰最宽湿声，混入干声更厚但更易 Chorus/梳状。

## 不建议用来做什么

- 不要直接用在必须保持 Mono 核心的主唱全湿 Insert。
- 不要把 Focus 当高通干声；它限制的是受影响频带。
- 不要只看 Stereo 更宽而忽略 Mono 相消。

## 信号流位置

- 优先 100% Wet Aux，主唱干声居中，返回高通/去齿。
- Backing Vocal Bus 可 Insert 轻 Mix，但仍做折叠。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Style I/II/III | 不同硬件/算法的延迟、移调与色彩。 | 固定 Detune/Delay，等响度比较空间位置和 Mono。 |
| Detune | 缩放时变微移调。 | 从 50–100% 起；Chorus 明显则降低。 |
| Delay | 缩放时变延迟。 | 从 50–100% 起；与干声梳状/分离则调整。 |
| Focus | 分频以下保持未受影响。 | 从 120–300 Hz 或更高试，防低中频模糊。 |
| Mix | 干湿比例。 | Aux 100% Wet；Insert 10–30% 起。 |

## Gain Staging

宽度常因能量增加显得更好。将 Stereo Active RMS 匹配旁通，并同时测 Mid/Side RMS、相关性和 Mono Fold-down。

## 延迟、相位与过采样

时变延迟/移调必然产生相位变化；官方未给宿主延迟。S4 测报告延迟、时变差分和 Mix。

## Mono/Stereo

必须用 Stereo 实例才有核心用途。干声保持 Mid；Aux 返回的 Side 增益以 Mono 折叠损失为上限。

## 适用场景

- 主唱极轻宽度 Send。
- Backing Vocal/Ad-lib 拉宽并后置。
- 效果化 Chorus 层。

## 路由

- 100% Wet Stereo Aux。
- Backing Vocal Bus 小比例 Insert。

## 参数起点

- Style I，Detune/Delay 50–100%，Focus 150–300 Hz，Aux 100% Wet。
- Send 从 -20 dB 起推。
- 主唱中心变空或 Mono 下降即减。

## 调整目标

- 干声中心不动，宽度层退后两侧。
- Mono 折叠仍有稳定主唱。

## 调整时听什么

- Chorus、相位游移、梳状。
- 低中频变宽变糊。
- 齿音在 Side 过强。

## 何时停止

- Stereo 可感而 Mono 几乎不损主唱。
- 继续加只让中心变虚时停止。

## 常见失败

- 主唱 Insert 全湿。
- Focus 太低。
- 只听 Stereo。
- 干湿响度未匹配。

## 替代方案

- Waves Doubler：多声部精细延迟/声像。
- 真实双轨：自然随机差异。
- bx_control V2：仅调整已有 Side，不生成新宽度。

## 专业案例与工作流线索

- Soundtoys 官方明确 100% Wet 最清晰最宽、混干更 Chorus；因此 Aux 与 Insert 是两种不同实验。

## 待执行测试

- 三 Style 的 Mid/Side、相关性、Mono 损失。
- Detune/Delay/Focus 单变量。
- Aux 与 Insert Mix 的相位/盲听。

## 已测结果

S4 待执行。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | micro-pitch-widener |
| mode | three-style |
| main_controls | style,detune,delay,focus,mix |
| risk_flags | mono-cancellation,chorus,mud,side-sibilance |
| validation | correlation-mono-fold |

## 来源

- [[sources/音乐制作/插件资料/SoundToys/MicroShift资料|MicroShift 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]

## 开放问题

- 本机 v5.0.1 报告延迟和 Style 的实际时变范围？
