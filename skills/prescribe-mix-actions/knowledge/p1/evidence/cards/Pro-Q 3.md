---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: 497c2536aeff
vendor: "FabFilter"
product: "Pro-Q 3"
evidence_level: L3
validation_status: S4-validated
batch: B02
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Pro-Q 3

## 身份与版本

- 厂商：FabFilter
- 产品族：Pro-Q 3
- Family ID：497c2536aeff
- 本机观测版本：界面 3.23 (64-bit; June 29, 2023)；文件系统产品族记录 3.2.3.0
- 格式：VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：eq-surgical-dynamic
- 次能力方向：resonance;mid-side;external-sidechain
- 当前证据等级：L3
- 验证状态：S4-validated

## 能做什么

- 提供最多 24 个静态或动态频段、从常规斜率到 Brickwall 的滤波形状，以及 Zero Latency、Natural Phase、Linear Phase 三种处理模式。
- Bell 与 Shelf 频段可设置正负 Dynamic Range；v3 的攻击、释放与 Knee 是随节目、频段和 Range 自动变化的，不应套用 Pro-Q 4 的手动时间参数。
- 每个频段可独立选择 Stereo、Left、Right、Mid 或 Side；外部侧链可触发动态频段。
- Band Solo、Spectrum Grab、碰撞显示和频谱分析用于定位问题，但最终增益决策必须回到混音上下文。

## 不建议用来做什么

- 不要因频谱有峰就自动窄削；峰值可能是音符、共振峰或必要咬字。
- 不要把 Linear Phase 当作默认更高品质；它带来延迟并可能产生前振铃。
- 不要把 Pro-Q 4 的 Spectral Dynamics、可调 Attack/Release 或 Character 写成本机 Pro-Q 3 功能。

## 信号流位置

- 修正型高通、宽幅减法与动态共振通常放在主压缩前，减少后级被无用能量或偶发共振触发。
- 压缩或饱和后可加第二实例做小幅音色修整，因为非线性与压缩会重塑频谱。
- 与伴奏做外部侧链动态让位时，把 Pro-Q 3 放在被让位的总线，并由主唱发送侧链。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Frequency / Gain / Q / Shape | 定义每个滤波器的中心、幅度、带宽和拓扑。 | 先用 Solo 临时定位，再在全混音中用最小必要增益和合适带宽。 |
| Dynamic Range | 限制该频段最大动态增益变化；负值压制、正值扩展。 | 偶发问题从 -1 至 -3 dB 起，先调 Range，再决定是否需要手动 Threshold。 |
| Auto / Manual Threshold | 自动阈值随输入适应；手动阈值固定触发点。 | 自然音量变化优先 Auto；需要与确定事件或侧链对齐时再手动。 |
| Stereo Placement | 限定频段作用于 Stereo、L/R 或 M/S 成分。 | 主唱单轨通常 Stereo；效果返回只在明确证据下处理 Side，始终检查单声道。 |
| Processing Mode | 选择零延迟、自然相位或线性相位。 | 常规混音从 Zero Latency；只有相位叠加问题有证据时才试 Linear Phase。 |

## Gain Staging

Auto Gain 是频谱曲线的估算补偿，不是严格响度匹配。每次大幅 EQ 后以输出 Trim 或后级增益匹配旁通响度；动态频段要比较相同音节的 Active RMS、峰值和主观前后位置。

## 延迟、相位与过采样

本机 48 kHz 实测宿主报告 Zero Latency `0 samples`、Natural Phase `320 samples (6.7 ms)`、Linear Phase Medium `5120 samples (106.7 ms)`；Ableton PDC 后三态最佳整数偏移均为 0。Zero/Natural 的静态 Bell 都有频率相关相位，Linear Medium 在十个稳态输入频点约为 0°；Linear 的代价仍包括大延迟和潜在前振铃。Pro-Q 3 没有应被当作常规开关的新版 Spectral 模式。

## Mono/Stereo

插件会适配单声道和立体声。单声道主唱不要用 Side 频段；立体声叠唱/效果返回可用 M/S，但任何宽化收益都要用 Mono Fold-down 和相关性复核。

## 适用场景

- 清除不需要的次声、低频隆隆和固定窄共振。
- 对 150–500 Hz 偶发箱体感、2–5 kHz 偶发刺耳或 6–12 kHz 齿音做小范围动态削减。
- 由主唱侧链触发伴奏 Presence 区域的窄幅让位。

## 路由

- 主唱 Insert 的前段修正 EQ。
- 伴奏或音乐总线上的外部侧链动态频段。
- 空间返回上的 M/S 清理；低频 Side 高通前先确认不是自然房间信息。

## 参数起点

- 高通仅在确有噪声时启用；从 60–90 Hz、12 或 24 dB/oct 起，边听低音主体边上移。
- 宽幅减法从 -0.5 至 -2 dB、Q 0.7–1.5 起；窄共振从 -1 至 -3 dB、Q 3–8 起。
- 动态问题从 Range -1 至 -3 dB、Auto Threshold 起；不要先堆多个深达 -6 dB 的动态结点。

## 调整目标

- 问题音素出现时才明显动作，普通元音的主体与距离感保持。
- 人声在伴奏中更清楚但不因高频增加而变薄。
- 等响度旁通时收益仍成立。

## 调整时听什么

- Solo 中定位的频率在全混音中是否真是问题。
- 高通是否削弱男声胸腔、低音气势或爆破修复后的自然低端。
- 动态频段是否随音节抽动、使音色忽明忽暗。

## 何时停止

- 问题不再抢注意力且旁通后不会觉得声音被挖空。
- 再多 0.5–1 dB 只让人声更薄、更远或更有相位感时回退。

## 常见失败

- 频谱追峰导致过度窄削和音符随演唱变化。
- 多个深动态结点叠加成隐性多段压缩。
- Linear Phase 在字头产生前振铃或延迟。
- M/S 调整在单声道折叠后改变主体音色。

## 替代方案

- PreSonus Pro EQ：宿主内低成本基线。
- oeksound soothe2：移动共振很多时的自动抑制。
- FabFilter Pro-MB：需要明确 Attack、Release 与跨更宽频带的动态控制。

## 专业案例与工作流线索

- FabFilter v3 官方手册说明动态行为由节目、频段、Range 自动决定；因此本卡把 Range/Threshold 视为主要动态控制，而不虚构时间参数。

## 待执行测试

- 动态 Bell 与 Pro-MB 单频带在同一问题音素上的等响度盲听。
- Zero/Natural/不同 Linear 分辨率的脉冲、前振铃和短字头可闻性比较。
- Stereo 与 M/S/L/R placement 的相关性、单声道折叠和外部侧链触发检查。

## 已测结果

- 本机 Pro-Q 3 VST3 已真实加载；About 回读为 3.23 (64-bit; June 29, 2023)，`Default Setting` 无频段、Output 0.0 dB、Analyzer Pre+Post+SC、Zero Latency。
- 默认平直态对旁路直接相关 1.0、最佳偏移 0 samples、RMS/峰值差约 0 dB；十个频点均 0.000 dB/0°，互差约 -141.481 dBFS。
- 单一 Stereo Bell 界面回读 1763.0 Hz、+6.00 dB、Q 1.000；在夹具 1760 Hz 处三模式实测 +5.999963/+6.000002/+5.999889 dB。
- Zero 在 880/1760/3520 Hz 相位约 +19.467/+0.284/-18.994°；Natural 约 +19.373/+0.098/-19.379°。Natural 相对 Zero 幅度非常接近，但 16 kHz 相位再差约 -2.451°。
- Linear Phase Medium 十个稳态频点相位均约 0°，但宿主延迟为 5120 samples；全段峰值变化也不同于 Zero，不能把线性相位简写成“同曲线无副作用”。
- 完整证据：[[projects/p1-plugin-knowledge-base/validation/reports/497c2536aeff--FabFilter-Pro-Q-3|Pro-Q 3 L3 验证]]。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | dynamic-eq |
| mode | zero-natural-linear |
| main_controls | frequency,gain,q,shape,dynamic_range,threshold,placement |
| risk_flags | spectrum-chasing,over-cut,pre-ringing,mono-shift |
| validation | impulse-latency-dynamic-band |

## 来源

- [[sources/音乐制作/插件资料/FabFilter/Pro-Q 3资料|Pro-Q 3 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]
- [[projects/p1-plugin-knowledge-base/validation/reports/497c2536aeff--FabFilter-Pro-Q-3|Pro-Q 3 L3 验证]]

## 开放问题

- 其它 Linear Phase 分辨率在 48/96 kHz 的报告延迟、脉冲前振铃与 CPU 如何变化？
- Studio One 外部侧链端口、per-band placement 与自动化参数名如何暴露？
