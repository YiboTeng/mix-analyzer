---
type: plugin-card
status: deferred
created: 2026-08-20
updated: 2026-08-20
family_id: 3e3b26a92fe1
vendor: "SoundToys"
product: "LittleAlterBoy"
evidence_level: L2
validation_status: S4-replaced-vst2-unavailable
batch: B04
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# LittleAlterBoy

> [!note] S4 替换
> 本机仅有 VST2，现有 Ableton 配置未暴露 VST2 且本任务不改扫描偏好；正式集合已由当前可达的 Waves Vocal Bender 替换。本卡保留为历史研究，不计入最终 40 款。

## 身份与版本

- 厂商：SoundToys
- 产品族：LittleAlterBoy
- Family ID：3e3b26a92fe1
- 本机观测版本：5.0.1.0
- 格式：VST2
- Studio One 可用性：current-filesystem-match
- 主能力方向：pitch-formant-creative
- 次能力方向：octave;hard-tune;robot;drive
- 当前证据等级：L2
- 验证状态：S3-researched-S4-pending

## 能做什么

- 单音人声 Pitch 与 Formant 独立移动；Transpose、Quantize、Robot 三模式。
- Quantize 快速吸附最近半音，Robot 锁定单一音高；可用 MIDI 控制 Pitch。
- Drive 加入模拟管式饱和，Mix 做干湿。

## 不建议用来做什么

- 不适合复调叠唱/完整伴奏。
- Quantize 只按半音，不等同按歌曲 Key/Scale 智能校音。
- 不要把极端 Formant 当透明移调。

## 信号流位置

- 通常复制主唱/Ad-lib 到独立轨后处理，避免破坏主唱。
- 移调后再 EQ、去齿、压缩和空间，因为算法会改变频谱/辅音。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Pitch | 以半音移动音高或在 Robot 定义固定音。 | 低八度 -12；和声先按调性确认间隔。 |
| Formant | 改变声道共振峰与角色。 | 下移 1–3 作为增厚起点；大移调时同向小调以增自然。 |
| Transpose / Quantize / Robot | 连续移调、半音硬吸附、固定音。 | 角色层用 Transpose；硬调音谨慎 Quantize；Drone 用 Robot。 |
| Drive / Mix | 管式饱和与干湿。 | 先 Drive 0 判断算法，再小加；角色层多用 100% Wet。 |

## Gain Staging

Pitch/Formant 改变频谱和感知响度，Drive 再增加谐波。用后级 Trim 匹配；角色层以 Send/轨道电平定位，不用 Mix 制造梳状。

## 延迟、相位与过采样

官方手册未给 v5.0.1 VST2 延迟；Pitch 算法和 Mix 必须 S4 测。

## Mono/Stereo

面向单音源；Mono 主唱复制轨最安全。Stereo Stem 可能含复调/空间信息，不应直接处理。

## 适用场景

- -12 semitone 低八度 Ad-lib。
- Formant 下移增厚/反派角色。
- Quantize/Robot 特效和 MIDI 音高演奏。

## 路由

- 复制轨或 Aux 100% Wet。
- 主唱自动化只用于明确片段并保留回退。

## 参数起点

- 低八度：Pitch -12、Formant -1 至 -3、Drive 0、Mix 100%。
- 仅增厚：Pitch 0、Formant -1 至 -3、Mix 10–30% 或复制轨低音量。
- Quantize+Drive 只用于可听效果。

## 调整目标

- 角色层可辨但不抢主唱中心。
- 辅音和齿音不产生明显算法碎裂。

## 调整时听什么

- 复调/混响导致颤抖。
- 低八度浑浊、Formant 过度怪异。
- Dry/Wet 相干梳状。

## 何时停止

- 角色清晰且在 Mono/小音箱仍支持主体。
- 继续移调只增加伪影时停止。

## 常见失败

- Quantize 当调内校音。
- 处理立体声复调 Stem。
- 主轨全湿。
- Drive 掩盖算法伪影。

## 替代方案

- Auto-Tune Pro：调内实时校音。
- Melodyne：逐音符编辑。
- Waves Doubler/MicroShift：只需宽化。

## 专业案例与工作流线索

- Soundtoys 官方建议 Formant 下移 -1 至 -3 增厚，并明确 Quantize 是最近半音；两者用途不能混写。

## 待执行测试

- Pitch ±12、Formant 0/±3 的频谱与伪影。
- Transpose/Quantize/Robot 单音/复调测试。
- Mix/延迟与 MIDI 自动化。

## 已测结果

S4 待执行。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | monophonic-pitch-formant |
| mode | transpose-quantize-robot |
| main_controls | pitch,formant,mode,drive,mix |
| risk_flags | polyphonic-artifact,chromatic-mistune,comb-filter |
| validation | pitch-formant-artifact-latency |

## 来源

- [[sources/音乐制作/插件资料/SoundToys/LittleAlterBoy资料|LittleAlterBoy 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]

## 开放问题

- 本机 v5.0.1 实际报告延迟和 MIDI 暴露？
