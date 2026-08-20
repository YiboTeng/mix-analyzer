---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: e98173f7f4df
vendor: "Plugin Alliance"
product: "Maag EQ4"
evidence_level: L3
validation_status: passed-l3
batch: B02
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Maag EQ4

## 身份与版本

- 厂商：Plugin Alliance
- 产品族：Maag EQ4
- Family ID：e98173f7f4df
- 本机观测版本：1.3.0.0 | 1.9.0.0
- 格式：VST2 | VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：eq-air-color
- 次能力方向：broad-tone;air-band
- 当前证据等级：L3
- 验证状态：passed-l3

## 能做什么

- 以 SUB、40 Hz、160 Hz、650 Hz、2.5 kHz 五个固定宽频段和可选 2.5/5/10/20/40 kHz 的 Air Band Shelf 做音乐性塑形。
- Air Band 即使选择高于可听上限的 20/40 kHz 也会因宽缓曲线影响可听高频。
- Level Trim 用于补偿多个频段与 Air Band 叠加造成的总体增益。

## 不建议用来做什么

- 不适合寻找并切除精确窄共振。
- 不要因为选择 40 kHz 就认为不会增加 8–15 kHz 齿音区能量。
- 不要在未做 Trim 等响度时把更响误判为更通透。

## 信号流位置

- 可放在修正型 EQ 与去齿之后做宽幅色彩；若 Air 明显激发齿音，则在其后再轻度 De-ess。
- 在压缩前提升 Presence 会改变压缩器触发；在压缩后更像最终色彩，二者需按目标选择。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| SUB / 40 / 160 / 650 / 2.5K | 固定中心/转折的宽幅增益频段。 | 按整体重量、浑浊、鼻音和咬字小步调整；不能当作窄 Q 工具。 |
| Air Band Frequency | 选择宽缓高频 Shelf 的转折/音色。 | 从 20 或 40 kHz 起求空气；需要更多 Presence 再试 10/5 kHz。 |
| Air Gain | 提升宽范围高频并增加总体电平。 | 从 0.5–1 dB 起，逐步到满足目标；每步用 Trim 对齐。 |
| Level Trim | 全局输出补偿。 | 按旁通 Active RMS/感知响度回调，不用它继续推色彩。 |

## Gain Staging

官方手册明确 Air 与其他频段会提高总体增益。每次改变后用 Level Trim 匹配旁通；同时记录峰值，防止后级饱和/压缩因输入增加而产生额外好感。

## 延迟、相位与过采样

本机旧版 VST3 在当前状态下由 Ableton 报告 `0 samples` 延迟。界面未见过采样控制；不把当前在线新版的附加功能写回旧版本，也不把 0 samples 外推到 VST2、其它 build 或采样率。

## Mono/Stereo

本机同时有 VST2/VST3 产品族；具体 Mono/Stereo 组件不重复建卡。单声道主唱关注左右一致，立体声叠唱处理后检查声像和单声道。

## 适用场景

- 修正后主唱缺少空气和昂贵感。
- 用宽幅 2.5 kHz 或 650 Hz 轻调存在感/鼻腔，再以 Air 完成顶部。
- 叠唱总线的统一光泽。

## 路由

- 主唱后段色彩 EQ。
- Backing Vocal Bus 或 Vocal Bus 上的轻量宽幅塑形。

## 参数起点

- Air 20 或 40 kHz、+0.5 至 +2 dB；Level Trim 等响度。
- 160/650/2.5K 每次先试 ±0.5 至 1 dB，不同时大幅推动多个相邻宽频段。

## 调整目标

- 空气与清晰度增加，S/T/CH 不跳出。
- 旁通等响度后仍感到更开放，而非只更响更薄。

## 调整时听什么

- 齿音、嘴部点击和底噪是否被同步抬高。
- 多个宽频段相加后是否造成整体电平偏差。

## 何时停止

- Air 在混音中可感但 Solo 不显沙亮。
- 再加 0.5 dB 使齿音先于元音出现时回退或移动到去齿前。

## 常见失败

- Air 过多造成刺耳并抬高噪声。
- 低频固定带误增肥导致后级压缩泵动。
- 不做 Level Trim 的响度偏差。

## 替代方案

- Fresh Air：动态/激励式的极简空气感。
- Pro-Q 3：更透明、频率连续可调的 Shelf。
- Slate Fresh Air 后再 Pro-DS：若需要激励质感并管理齿音。

## 专业案例与工作流线索

- 官方手册要求 Air 增益后用 Level Trim 补偿；这也是判断该插件真实音色价值的核心实验。

## 待执行测试

- Air 10/20/40 kHz 同增益与等响度三组频响/盲听。
- Air 放在 De-esser 前后对真实齿音触发、噪声与亮度的对比。
- 固定五段的单音/扫频、Level Trim 标定以及 VST2/VST3 同设置输出、延迟与自动化兼容性。

## 已测结果

- Ableton Live 11.3.43 / 48 kHz 真实加载旧版 VST3；界面回读为固定五段、Air OFF/2.5/5/10/20/40 kHz、Air Gain 与 Level Trim；宿主报告 0 samples。
- 在所有固定频段为 0 的基线上，Air 20 kHz/+3 dB 使稳定十音整体约 +0.163 dB，55 Hz 至 16 kHz 各点约 +0.208/+0.231/+0.119/+0.163/+0.153/+0.160/+0.170/+0.206/+0.265/+0.325 dB；峰值由 -1.678 升至 -0.898 dBFS。
- Air 20 kHz/+5 dB 将当前夹具推到约 0 dBFS，结果只作为余量风险，不作干净曲线。选择 20 kHz 仍影响可听高频，实务起点应保持在 +1 至 +3 dB并做 Trim/峰值复查。
- 零增益实例与较早独立共享旁路有小幅差异；因独立 dither、非即时 A/B 与可能的旧 build 固定路径，不能声称逐比特透明。主结论来自零增益实例与 Air 变体的相对比较。
- 证据：[[projects/p1-plugin-knowledge-base/validation/reports/e98173f7f4df--Plugin-Alliance-Maag-EQ4|Maag EQ4 L3 验证]]。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | fixed-band-color-eq |
| mode | air-shelf |
| main_controls | fixed_bands,air_frequency,air_gain,level_trim |
| risk_flags | sibilance,noise-lift,loudness-bias |
| validation | frequency-response-level-match |

## 来源

- [[sources/音乐制作/插件资料/Plugin Alliance/Maag EQ4资料|Maag EQ4 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]
- [[projects/p1-plugin-knowledge-base/validation/reports/e98173f7f4df--Plugin-Alliance-Maag-EQ4|Maag EQ4 L3 验证]]

## 开放问题

- 本机两个版本是否来自 VST2/VST3 还是并行旧安装？
- 本机两个文件系统版本与宿主中具体加载 build 的对应关系仍未由插件界面直接显示。
