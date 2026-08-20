---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: 7a146380912e
vendor: "oeksound"
product: "soothe2"
evidence_level: L3
validation_status: passed-l3
batch: B02
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# soothe2

## 身份与版本

- 厂商：oeksound
- 产品族：soothe2
- Family ID：7a146380912e
- 本机观测版本：1.1.2
- 格式：VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：resonance-suppression
- 次能力方向：harshness;dynamic-resonance;deessing
- 当前证据等级：L3
- 验证状态：passed-l3

## 能做什么

- 持续分析输入共振并以大量自适应凹口动态衰减；频率图不是静态 EQ，而是处理灵敏度轮廓。
- Soft 模式更透明并保留瞬态；Hard 更依赖电平、力度更大且更容易过用。
- Depth、Sharpness、Selectivity、Attack、Release 共同决定处理量、凹口形态和时间行为。
- 可分 L/R 或 M/S、调 Link/Balance、使用外部侧链，并为实时与离线分别设置 Oversample/Resolution。

## 不建议用来做什么

- 不要把 Depth 当作固定 dB 衰减；数值不等于实际 Reduction。
- 不要用极高 Sharpness 和 Depth 代替先修录音、静态 EQ 或专用去齿音。
- 不要只听 Delta 后追求删除最多；Delta 应主要包含问题共振而不是完整音素与音色。

## 信号流位置

- 通常放在清理 EQ 后、主压缩前控制音素相关共振；若饱和或压缩后产生新刺耳，可在后段再用更轻实例。
- 用作去齿时与专用 De-esser 二选一或分担不同区域，避免 2–12 kHz 多重压制。
- 外部侧链让位放在被让位的伴奏/效果返回，不放在主唱本体。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Soft / Hard | 选择透明、较不依赖电平或更强、更可调的行为。 | 先 Soft；突出共振仍穿出时才试 Hard，并重新校准 Depth。 |
| Depth | 全局灵敏度/处理量，越高通常减得越多。 | 从默认上推到明显过量，再回退到刚好不显处理。 |
| Sharpness | 凹口的深窄程度。 | 宽泛堆积用低值；口哨式窄共振提高，但出现噪声状失真即回退。 |
| Selectivity | 选择只削最突出共振还是更广泛均衡。 | 窄口哨提高；宽带齿音/不均衡降低，并联动 Depth。 |
| Attack / Release | 频率相关的反应与恢复速度。 | 瞬态被吞放慢 Attack；滤波移动/相位伪影明显时加长 Release。 |
| Delta / Mix | Delta 独听被移除内容；Mix 平行混合。 | 用 Delta 校准目标，回全信号后以 100% Wet 优先，必要时再小幅并行。 |

## Gain Staging

Reduction 会降低局部能量和整体感知响度。先保持 Output 自动补偿关闭或记录其状态，再用输出增益匹配旁通；Delta 仅用于诊断，不能以被移除内容越多越好。

## 延迟、相位与过采样

Attack/Release 是频率相关常数；快移动深凹口可能产生可听相位失真。高 Oversample 提升频率分辨率并让高 Sharpness 更平滑，高 Resolution 提升时域更新平滑度，二者增加 CPU；实时与离线可分设，S4 必须验证导出是否切换。

## Mono/Stereo

Mono 实例禁用 Stereo 区。Stereo 中 100% Link 会合并分析并对两边施加相同处理；0% 为 Dual Mono。复杂立体声从 M/S + 100% Link 起，硬分轨素材可试 L/R 低 Link。

## 适用场景

- 2–5 kHz 随某些元音突然出现的刺耳。
- 150–600 Hz 只在个别音节隆起的箱体感。
- 宽带齿音或口哨式齿音的频谱型辅助控制。
- 由主唱侧链让伴奏共振区域短暂退让。

## 路由

- 主唱 Insert，修正 EQ 后、主要压缩前。
- 伴奏/混响总线外部侧链动态让位。

## 参数起点

- Soft 默认；Depth 从默认上推至过量后回退，目标常是峰值衰减约 1–4 dB 而非固定旋钮值。
- 宽泛粗糙：较低 Sharpness、中低 Selectivity；窄口哨：中高 Sharpness/Selectivity。
- 实时 Quality 先 Normal/Eco 可工作设置，离线 High；实际档名和 CPU 在 S4 回读。

## 调整目标

- 问题元音不再跳出，但普通音节的亮度、胸腔与咬字仍完整。
- Delta 以短暂共振为主，而非持续输出可辨识的完整人声。

## 调整时听什么

- 齿音是否变成咬舌、lisp 或暗哑。
- 低中频是否被持续抽走，使人声忽远忽近。
- 快速深凹口造成的噪声状失真、相位飘动或瞬态变软。

## 何时停止

- 最坏音素稳定且普通音素几乎听不出处理。
- Delta 开始包含完整元音或旁通后人声明显更有生命力时退回。

## 常见失败

- Depth、Sharpness、Selectivity 同时推高。
- 频率轮廓覆盖全频导致整体去个性。
- 双声道 Link 太低引起声像游移。
- 离线质量与实时差异未记录导致导出改变。

## 替代方案

- Pro-Q 3 动态 EQ：问题集中在少数已知频段。
- Pro-DS / E2Deesser：主要问题是齿音检测而非广泛共振。
- 手工 Clip EQ/自动化：只有少数事件。

## 专业案例与工作流线索

- oeksound 官方 Quick Start 明确建议把 Depth 推到过量再回退，并用 Delta 和频率轮廓聚焦；本卡沿用这一可复核顺序。

## 待执行测试

- 后续仍需包含移动元音共振、宽带齿音和口哨式窄共振的标注语音集。
- 后续扫描 Depth、Sharpness、Selectivity、Attack/Release、Delta 与频率轮廓，并做等响盲听。
- 后续验证实时/离线 Quality 切换、外部侧链、M/S/Link、CPU 与导出一致性。

## 已测结果

本机 soothe2 1.1.2 VST3 Stereo 已在 Ableton Live 11.3.43 / 48 kHz 真实加载。默认工厂态为 Soft、Depth 3.0、Sharpness 4.6、Selectivity 3.6、Attack 1.0、Release 快、Mix 100%、Trim 0 dB、Delta Off、L/R、Link 100%、Balance 居中、Normal 1x；宿主报告延迟 `2048 samples / 42.7 ms`，Soft 与 Hard 相同。

72 秒复合夹具中，Soft 默认对 8–20 秒稳定十音多频整体降低 `2.198920 dB`；Hard 保持其余旋钮不变时降低 `2.645424 dB`，即比 Soft 再低 `0.446504 dB`。除 55/110 Hz 外，Soft 在 220 Hz–16 kHz 各固定音约降低 `1.85–5.00 dB`，Hard 约降低 `2.18–6.17 dB`；55/110 Hz 的正增益只说明当前自适应滤波与多音相互作用，不应解读为固定低架增益。

66–72 秒动态区域中，Soft 整体仅 `-0.043151 dB`，50 ms 窗最深 `-0.047474 dB`；Hard 整体 `-0.076788 dB`，68 个活跃窗中 53 个达到至少 `0.05 dB` 衰减，最深 `-0.087516 dB`。这与插件内联帮助“Hard 更随电平反应、可推得更重”的方向一致，但数值很小，只证明当前合成夹具与默认 Depth 3 的模式差异，不代表真实人声上的自然度或最佳设置。

0–6 秒三个稀疏短事件在两模式下都与旁路约 `0.00001 dB` 内一致，说明默认状态并非只要有瞬态就动作；也揭示该夹具缺少足够的移动人声共振，不能据此评价检测准确率。工程快照、三份 WAV、SHA-256、50 ms 窗与十频点传输见 [[projects/p1-plugin-knowledge-base/validation/reports/7a146380912e--oeksound-soothe2|soothe2 L3 验证]]。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | adaptive-resonance-suppressor |
| mode | soft-or-hard |
| main_controls | depth,sharpness,selectivity,attack,release,stereo_link |
| risk_flags | over-suppression,lisp,phase-motion,stereo-wander |
| validation | delta-selectivity-quality-render |

## 来源

- [[sources/音乐制作/插件资料/oeksound/soothe2资料|soothe2 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]

## 开放问题

- 本机已确认默认 Normal 1x 与 `2048 samples / 42.7 ms`；其它 Quality/Resolution、离线切换与 CPU 尚未验证。
- 外部侧链及 Studio One 暴露行为尚未验证。
