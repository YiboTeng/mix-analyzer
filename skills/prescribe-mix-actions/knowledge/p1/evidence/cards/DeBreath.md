---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: ad123c8856d3
vendor: "Waves"
product: "DeBreath"
evidence_level: L3
validation_status: passed-l3
batch: B01
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# DeBreath

## 身份与版本

- 厂商：Waves
- 产品族：DeBreath
- Family ID：ad123c8856d3
- 本机观测版本：12.7.0.209
- 格式：VST2 / VST3；本轮实际加载 `DeBreath Mono` VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：restoration-breath
- 次能力方向：breath-detection;voice-breath-split;room-tone
- 当前证据等级：L3（本机可加载、控制/延迟/Mono 边界已验证；当前夹具未验证检测效果）
- 验证状态：passed-l3

## 能做什么

- 以模板匹配的 Breath 评分和输入 Energy 双条件识别呼吸事件，再独立衰减检测到的呼吸。
- 在 Voice 与 Breath 两条互补路径之间切换监听；官方定义两路径之和应等于原始输入。
- 用 Room Tone 在被衰减区间加入极低电平噪声，减少完全抽空造成的洞感。

## 不建议用来做什么

- 不要在没有逐段监听 Breath 路径的情况下批量删除所有呼吸；呼吸承担节奏、情绪和句间连贯。
- 不要把 `Reduction -Inf` 当万能起点；它是完全移除端点，易造成不自然空洞。
- 当前仅有 Mono 组件实测。不要把它直接插在需要保留空间/双轨信息的立体声 Stem 上。

## 信号流位置

- 单声道主唱编辑/修复前段，在 Vocal Rider、MV2、重压缩、激励和饱和之前。
- 先做明显剪辑与嘴音修复，再做呼吸控制；之后压缩器才不会把残余呼吸重新抬高。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Breath Threshold | incoming event 与呼吸模板的相似度门槛，0–100%，默认 50%。 | 在 Breath Monitor 下，把线放在目标呼吸评分峰值下方；若听到有音高的字头/尾音，向更严格方向回退。 |
| Energy Threshold | 仅允许低于该平均能量的事件被判为呼吸，0 至 -64 dBFS，默认 -30 dBFS。 | 先看呼吸与正文的能量分布；强呼吸可向 -25/-20 dBFS 调，正文误检时不要盲目放宽。 |
| Reduction | 对已检出呼吸的衰减，0 至 -Inf，默认 -Inf。 | 实际混音通常先从温和衰减开始，保留节奏和自然吸气；只有确需删除的事件才走深。 |
| Fade Out / Fade In | Voice 与 Breath 路径之间交叉转移的过渡，0.1–200 ms，默认 5 ms。 | 吞字头/切尾时加长或回退阈值；呼吸边缘拖尾时缩短，但要避免点击与突变。 |
| Monitor Voice/Breath | 监听保留路径或被移除路径。 | 调参必须来回切换；Breath 路径理想上只有呼吸，不应包含有音高元音或辅音主体。 |
| Room Tone | 在衰减区按衰减量加入最高约 -80 dB 的白噪。 | 完全移除造成“真空洞”时尝试；已有连续真实底噪时谨慎，避免噪声纹理跳变。 |

## Gain Staging

Energy 是平均能量判定，输入 Clip Gain 会改变分类。先把整轨人声响度稳定到合理范围，再调阈值；后续如果大幅改变前级增益，必须重新检查检测。对比时匹配 Voice 路径主体响度，并单独监听 Breath 路径，不要只看整段 RMS。

## 延迟、相位与过采样

- 本机 48 kHz 回读 35248 samples / 734.3 ms，与 Waves 当前延迟表一致；不适合实时跟唱或低延迟监听。
- Ableton 离线导出会补偿延迟，但播放定位、自动化手感和实时录音仍受影响。
- 官方旧 PDF 的 48 kHz 数字与当前表不一致；本卡以当前表和本机回读为准。

## Mono/Stereo

本轮只找到并加载 `DeBreath Mono`。在立体声 Composite 上，Voice 输出等于输入 Mid 并复制到左右：全文件 Side 从 -30.85 dBFS 降到约 -147.5 dBFS。它不是“旁路透明”的立体声用法；单声道主唱可接受，立体声和声/效果 Stem 应改用真正 Stereo 组件或先确认折叠是有意决定。

## 适用场景

- 近讲人声、旁白、播客中吸气频繁且后续压缩会放大的单声道轨。
- 需要比手工 Clip Gain 更快地先做检测，再逐段复核的长素材。

## 路由

- 常规：单声道人声 Insert 前段，Monitor Voice 输出。
- 高级：若宿主允许独立获取 Voice/Breath 路径，可给 Breath 路径单独做暗化/轻压缩，再按自然度混回；必须保证相加关系和延迟对齐。

## 参数起点

- 从官方默认 Breath 50%、Energy -30 dBFS、Fade 5/5 ms 开始，先切 Breath Monitor，不先决定 Reduction。
- 先调 Breath 阈值剔除有音高内容，再用 Energy 阈值排除较响正文；最后把 Reduction 从温和衰减逐步加深。
- 强、响的吸气可能需要把 Energy 提到 -25 至 -20 dBFS；这是条件化范围，不是所有录音的固定值。

## 调整目标

- 后级压缩后呼吸不抢拍、不遮词，但句间仍保留演唱连续性。
- Breath Monitor 只剩目标呼吸；Voice Monitor 不吞字头、元音尾部和擦音。

## 调整时听什么

- Breath 路径里是否出现有明确音高的元音、清辅音或房间尾音。
- Voice 路径是否出现硬切、真空洞、吞字头或节奏被抽走。

## 何时停止

- 在完整编曲中呼吸不再抢注意力、但演唱仍“会呼吸”时停止。
- 若为了去掉极少数重呼吸而开始误检正文，撤回自动深度，对个别事件用 Clip Gain/剪辑。

## 常见失败

- 只听 Voice，不听 Breath，导致误删正文。
- 前级增益改变后不重调 Energy。
- 立体声素材误用 Mono 组件，导致 Side 完全坍缩。
- Reduction 一上来设 -Inf，叠加过短 Fade 造成洞感和边缘突变。

## 替代方案

- iZotope RX Breath Control：若本机依赖完整且需要 RX 工作流；当前本机加载失败，不作为可验证首选。
- 手工 Clip Gain/剪辑：数量少、需要保留精确呼吸节奏时更可靠。
- 自动化或窄区段 Region Gain：不想引入 734 ms 高延迟时。

## 专业案例与工作流线索

- Waves 官方要求先在 Voice/Breath 两路径间反复监听，确认检测，再决定 Reduction；这是本插件最关键的“用到精”纪律。
- 阈值不是单一音量门：Breath 模板评分必须超过阈值，同时事件能量必须低于 Energy 阈值。

## 已执行测试

- Ableton Live 11.3.43 / 48 kHz；DeBreath Mono 12.7.0.209 VST3；其余链上设备全部停用。
- Default：Breath 50、Energy -30 dBFS；Stress：Breath 89.5、Energy -57 dBFS；Reduction -Inf、Fade 5/5 ms、Room Tone Off。
- 分别导出 Voice/Breath Monitor，量化五个 Composite 区域、50 ms 活跃窗、频带能量、左右相关和 Mid/Side；保存宿主快照。

## 已测结果

- Default Voice 相对旁路整段 -0.528 dB、相关 0.941；该差异主要来自 Mono 折叠，不是呼吸衰减。固定人声区域仅 -0.00278 dB。
- Default 与 Stress 的 Breath Monitor 都约 -144.5 dBFS，Stress 提高到 Breath 89.5、Energy -57 后仍无可测检测分量；当前 Composite 不可用于证明呼吸识别性能。
- 稳定多音区域 Voice -2.508 dB，是左右相位/能量折叠造成；空间、动态和脉冲的原本近单声道部分几乎不变。
- 宿主延迟 35248 samples / 734.3 ms。详细证据：[[projects/p1-plugin-knowledge-base/validation/reports/ad123c8856d3--Waves-DeBreath|DeBreath L3 验证]]。

## 后续测试

- 带人工标注呼吸/正文事件的真实单声道人声，统计检出率、误检率、衰减、边缘过渡与盲听。
- 逐个扫 Breath/Energy 阈值，并确认 Voice + Breath 路径重构原始源。
- Stereo 组件、其它采样率、Room Tone、自动化与压缩前后顺序。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | breath-detector-attenuator |
| mode | template-and-energy-threshold |
| main_controls | breath_threshold,energy_threshold,reduction,fade_in,fade_out,monitor,room_tone |
| risk_flags | speech-misclassification,unnatural-holes,mono-collapse,high-latency |
| validation | labeled-breath-detection-and-speech-preservation |

## 来源

- [[sources/音乐制作/插件资料/Waves/DeBreath资料|DeBreath 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]
- [[projects/p1-plugin-knowledge-base/validation/reports/ad123c8856d3--Waves-DeBreath|DeBreath L3 验证]]

## 开放问题

- 当前夹具为什么未触发 Breath 检测；真实标注呼吸上的检出/误检边界是什么？
- 本机是否存在可加载的 Stereo 组件，或只有 Mono 枚举？
