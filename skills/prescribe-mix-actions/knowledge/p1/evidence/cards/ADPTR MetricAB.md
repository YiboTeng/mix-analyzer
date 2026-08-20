---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: fb4b55cbf4ec
vendor: "Plugin Alliance"
product: "ADPTR MetricAB"
evidence_level: L3
validation_status: S4-passed
batch: B05
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# ADPTR MetricAB

## 身份与版本

- 厂商：Plugin Alliance
- 产品族：ADPTR MetricAB
- Family ID：fb4b55cbf4ec
- 本机观测版本：1.0.0 | 1.0.0.0
- 格式：VST2 | VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：reference-ab
- 次能力方向：loudness-match;spectrum;dynamics;stereo
- 当前证据等级：L3
- 验证状态：S4-passed

## 能做什么

- 载入多首Reference，A/B切换DAW输入与参考流，支持Latch/Cue/Sync、Cue/Loop和Delay Compensation。
- Volume/Loudness Match减少更响偏差；Filter、Stereo/Mono/L/R/Sides监测。
- Spectrum、Correlation、Stereo Image、Dynamics、Loudness分析可比较目标区间。

## 不建议用来做什么

- 不要把整首母带参考的绝对频谱目标直接套到独唱。
- 不要同时经过母带处理器与MetricAB错误路由形成双处理。
- 不要只信自动Loudness Match而不复核短段。

## 信号流位置

- 放在Monitor/最后总线末端，确保Reference绕过项目母带处理而A流路径清楚。
- 独唱插件知识库主要用它做参考人声/Stem的响度匹配和频段监听。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| A/B / Track Select | 切换当前工程输入与参考轨。 | 映射快捷键，随机切换短段。 |
| Loudness Match / Track Gain | 估算并补偿参考响度。 | 先Match，再用短期LUFS/ActiveRMS人工微调。 |
| Cue/Sync/Delay Comp | 对齐音乐位置与宿主延迟。 | 同功能段落Cue；Sync异常时校PDC/手动延迟。 |
| Filter / Stereo Mode | 只听低/中/高频或Mono/Sides等。 | 分频比较可懂度/齿音/低中频，检查Mono。 |
| Analysis Tabs | 频谱、动态、声像、响度可视化。 | 只用作证据，不替代盲听。 |

## Gain Staging

核心就是匹配。记录算法Match值与人工微调值；对人声短段同时匹配Active RMS/Short-term LUFS，避免静音占比。

## 延迟、相位与过采样

PDC开关/毫秒值用于同步参考播放。本机默认 Metric 源实测最佳整数延迟为 0 samples；这不等于内部参考、Cue/Sync 或 PDC 已被验证。

## Mono/Stereo

可监测Stereo/Mono/L/R/Sides；Reference声道布局不同必须标注。Mono检查只用于兼容，不把宽度本身视为好坏。

## 适用场景

- 插件前后等响度A/B。
- 与多首参考人声Stem比较正常区间。
- 频段、动态、相关性诊断。

## 路由

- Monitor/Main Out最后，避免写入导出。
- Reference内部播放，不经过待测链。

## 参数起点

- 先Load 3–5首参考、设Cue、Loudness Match All。
- Filter分别低<200Hz、中200Hz–5kHz、高>5kHz粗检。
- 每次A/B 2–10秒随机切换。

## 调整目标

- 参考差异来自音色/动态而非响度和段落。
- 路由确保A/B只差目标变量。

## 调整时听什么

- 参考被二次处理。
- Match在短段漂移。
- 不同编曲/人声类型造成伪目标。

## 何时停止

- A/B路由可Null验证且响度误差在预设容差内。
- 再调只是追单一参考个性时停止。

## 常见失败

- 双母带路由。
- 静音影响Loudness Match。
- 整曲与独唱直接比。
- 图形追平。

## 替代方案

- Insight2：连续计量。
- Studio One Listen Bus/手动参考路由。
- 离线分析脚本。

## 专业案例与工作流线索

- 官方手册把PDC、Loudness Match与分析分成独立层；卡片要求先修路由/响度，再读图。

## 待执行测试

- 已完成：默认蓝色 Metric 源对共享旁通的中性对照。
- 待扩展：Match 对粉噪/语音/音乐误差。
- 待扩展：内部参考播放、PDC/Cue/Sync、Filter 与 Stereo 监测校验。

## 已测结果

- Ableton Live 11.3.43，Default、蓝色 Metric 源、Gain 0.0 dB、Loudness Match 关闭。
- 固定 6 s、48 kHz/24-bit、Triangular dither 渲染对共享旁通：最佳整数延迟 0 samples，直接相关 0.999999998926，RMS 电平差 -0.000000 dB。
- 独立渲染残差 RMS -141.486632 dBFS、Peak -132.453198 dBFS；差异受两次随机 dither 主导，支持 Metric 源中性。
- 参考槽菜单、A/B 源状态、Playback、Filter 与六个分析页完成真实界面观察；内部参考播放、Loudness Match、Cue/Sync/PDC 未量化。
- 详细证据：[[projects/p1-plugin-knowledge-base/validation/reports/fb4b55cbf4ec--ADPTR-MetricAB|ADPTR MetricAB L3 验证]]。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | reference-comparator |
| mode | ab-loudness-match |
| main_controls | ab,track,cue,sync,pdc,loudness_match,filter,stereo_mode |
| risk_flags | routing,double-processing,loudness-error,reference-mismatch |
| validation | route-null-match-error |

## 来源

- [[sources/音乐制作/插件资料/Plugin Alliance/ADPTR MetricAB资料|ADPTR MetricAB 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]

## 开放问题

- 本机1.0的最大轨数、Match模式与当前1.4文档差异？
