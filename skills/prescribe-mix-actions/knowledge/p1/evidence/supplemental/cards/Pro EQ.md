---
type: plugin-card
status: deferred
created: 2026-08-20
updated: 2026-08-20
family_id: e482c5d14f03
vendor: "PreSonus"
product: "Pro EQ"
evidence_level: L2
validation_status: S4-replaced-host-native-unavailable
batch: B02
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Pro EQ

> [!note] S4 替换
> Studio One 可执行文件当前缺失，宿主原生 Pro EQ 无法完成真实 L3；正式集合已由当前可达的 Waves F6 替换。本卡保留为历史研究，不计入最终 40 款。

## 身份与版本

- 厂商：PreSonus
- 产品族：Pro EQ
- Family ID：e482c5d14f03
- 本机观测版本：4.0.0
- 格式：Native
- Studio One 可用性：host-native-cache
- 主能力方向：eq-native-baseline
- 次能力方向：surgical-eq;dynamic-eq
- 当前证据等级：L2
- 验证状态：S3-researched-S4-pending

## 能做什么

- 作为 Studio One 原生均衡器提供无额外采购、工程可移植性较好的修正与音色塑形基线。
- PreSonus 5.5 官方手册确认 Pro EQ² 属于内置效果；参数化 EQ 的频率、Gain、Q 与 Cut/Shelf 是核心语义。
- 库存缓存标识产品族为 Pro EQ、版本 4.0.0；Studio One 6 实际 UI 与动态功能必须在 S4 回读后再定。

## 不建议用来做什么

- 不要根据后续 Studio One 7 或非官方页面，把 Pro EQ³ 功能无条件写回当前缓存项。
- 不要把原生等同于零延迟、线性相位或无染色；必须实测。
- 不要用窄带大幅扫频作为长期决策方式。

## 信号流位置

- 主唱链前段做高通、宽幅修正和必要窄削。
- 作为与 Pro-Q 3 对照的同曲线基线，隔离第三方工作流与算法的真实增益。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Frequency | 选择每个滤波段中心或转折频率。 | 结合音素和混音上下文定位，不凭固定表格。 |
| Gain | 提升或衰减目标频段。 | 宽幅从 ±0.5–2 dB 起，窄问题带先做最小必要减法。 |
| Q / Bandwidth | 控制受影响频率范围。 | 窄 Q 用于固定共振，宽 Q 用于整体音色；扫到问题后降低试听增益再确认。 |
| Cut / Shelf / Bell | 选择滤波拓扑。 | 高通只清除无用低频；Shelf 做整体倾斜；Bell 做局部塑形。 |

## Gain Staging

任何自动增益或输出控制的存在与行为需 S4 回读。当前阶段统一在后级加可测 Trim，匹配旁通 Active RMS/感知响度，再比较与 Pro-Q 3 的曲线和听感。

## 延迟、相位与过采样

官方 5.5 文档不足以证明 Studio One 6 缓存 v4.0.0 的延迟、相位模式或动态段行为。S4 使用宿主报告、脉冲与扫频建立基线；未验证前只按普通参数 EQ 使用。

## Mono/Stereo

Native 实例应随轨道通道布局加载，但每频段 M/S/L/R 能力未由当前版本官方资料确认；S4 回读。单声道主唱以通用频段为基线。

## 适用场景

- 常规高通、宽幅低中频修正、Presence 或 Air Shelf。
- 不需要第三方高级功能时的快速原生处理。
- 与 Pro-Q 3 匹配曲线做盲听和 CPU/延迟对比。

## 路由

- 主唱或叠唱总线 Insert。
- 实验工程中的原生 EQ 对照组。

## 参数起点

- 高通 60–90 Hz、温和斜率，仅在确有无用能量时。
- 宽幅音色 ±0.5–2 dB；窄共振 -1 至 -3 dB。
- 动态段、Band Solo、Auto Gain 等功能只有本机 UI 确认存在后才设起点。

## 调整目标

- 用最少频段解决可听问题。
- 与第三方匹配曲线时保持相同增益与相位条件。

## 调整时听什么

- 高通造成的重量损失。
- 窄带扫频导致的确认偏差。
- 不同 EQ 曲线匹配不精确造成的伪差异。

## 何时停止

- 原生 EQ 已达到目标且高级功能没有明确新增价值。
- 增加频段只让曲线更复杂而不改善上下文。

## 常见失败

- 把旧/新文档功能混写。
- 未匹配曲线、相位与增益就比较品牌音质。
- 原生便利性掩盖了过度处理。

## 替代方案

- FabFilter Pro-Q 3：动态频段、每频段 M/S 和更强可视化。
- Maag EQ4：宽幅色彩与 Air Band。

## 专业案例与工作流线索

- 把原生 EQ 作为对照能回答第三方插件是否真正改善结果，而不只是更快或更漂亮。

## 待执行测试

- 本机加载后截图/参数枚举，确认实际代际、频段数、动态功能与通道选项。
- 与 Pro-Q 3 匹配 3 组曲线做扫频、脉冲、Null、CPU、延迟和盲听。
- 自动化与离线导出一致性。

## 已测结果

S4 待执行；当前 L2 只确认缓存身份与官方历史手册中的原生 EQ 定位，不声称 Pro EQ³ 功能。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | native-parametric-eq |
| mode | host-native |
| main_controls | frequency,gain,q,filter_shape |
| risk_flags | version-ambiguity,curve-mismatch,sweep-bias |
| validation | ui-enumeration-native-eq-baseline |

## 来源

- [[sources/音乐制作/插件资料/PreSonus/Pro EQ资料|Pro EQ 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]

## 开放问题

- 缓存 v4.0.0 对应 Pro EQ²、Pro EQ³ 还是内部组件版本？
- 本机 UI 有几段、哪些动态和 M/S 控制、报告延迟多少？
