---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: a8c2063eb007
vendor: "FabFilter"
product: "Pro-MB"
evidence_level: L3
validation_status: passed-l3
batch: B02
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Pro-MB

## 身份与版本

- 厂商：FabFilter
- 产品族：Pro-MB
- Family ID：a8c2063eb007
- 本机观测版本：1.2.8.0
- 格式：VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：multiband-dynamics
- 次能力方向：dynamic-tone;deessing;upward-dynamics
- 当前证据等级：L3
- 验证状态：passed-l3

## 能做什么

- 只需为目标区域创建一个或多个自由频带，无需把全频强制切成连续多段。
- 每段提供 Threshold、Range、Compress/Expand、Ratio、Knee、节目相关 Attack/Release、Lookahead、Output、Pan 与专家侧链。
- Range 正负与 Compress/Expand 组合可实现向下/向上压缩或扩展。
- Dynamic Phase、Linear Phase、Minimum Phase 三种分频/滤波方式与 2x/4x Oversampling。

## 不建议用来做什么

- 不要用多个相邻频段重建全带压缩器，除非确实需要。
- 不要把 Linear Phase 默认当作最透明；它有延迟与前振铃。
- 不要忽略 Range 的正负和 Dynamics Mode 组合，否则可能得到相反行为。

## 信号流位置

- 在主压缩前控制 150–500 Hz 偶发堆积，可让全带压缩更稳定。
- 在主压缩后控制 Presence/齿音或提升低电平细节，避免前级触发关系被改写。
- 由主唱侧链在伴奏总线建立频率选择性让位。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Band Range | 限制最大增益变化并以正负决定上下方向。 | 向下压缩先 -1 至 -3 dB，明确确认箭头与 GR 方向。 |
| Threshold / Ratio / Knee | 定义触发点、压缩比例与过渡。 | 先 Range 限深，再让最坏音素触发；用软 Knee 避免边界明显。 |
| Attack / Release | 节目与频率相关的 0–100% 速度。 | 吞字头则放慢 Attack；音色抽动则放慢 Release。 |
| Lookahead | 每段预读值与顶部全局启用开关共同决定反应；本机全局 On 预留完整 20 ms 宿主延迟。 | 捕捉快速齿音/爆发时 A/B On/Off；低延迟监听先检查全局开关与宿主 PDC。 |
| Processing Mode | Dynamic、Linear 或 Minimum Phase。 | 混音默认 Dynamic Phase；只有相位叠加证据才比较其他模式。 |
| Stereo Link / Mid-Side | 决定双声道检测联动和处理中/侧比重。 | 主唱/总线先高 Link；降低前后检查声像。 |

## Gain Staging

Output Level 可改变每段静态增益，应与动态 Range 分开记录。所有对比匹配整体 Active RMS；向上压缩尤其会提升噪声、呼吸和混响，需同时测非语音区。

## 延迟、相位与过采样

关闭全局 Lookahead、关闭 Oversampling 且使用 Dynamic 或 Minimum Phase 时官方称零延迟。本机实测：Default Setting 即使无频段也因全局 Lookahead On 报告 960 samples / 20 ms；单频段的 band Lookahead 显示 1.000 ms 时仍是 960 samples，关闭全局开关后才为 0 samples，且 band Lookahead 控件灰显。Linear Phase 与 Oversampling 另加延迟。Dynamic Phase 静止时近线性/平坦相位、动作时才引入小相位变化；Linear 有前振铃风险。

## Mono/Stereo

单声道主唱禁用无关 Stereo Pan。立体声总线高 Link 防声像摆动；M/S 处理低频或高频宽度时做 Mono Fold-down。

## 适用场景

- 控制个别音节 150–400 Hz 的胸腔/箱体堆积。
- 2–5 kHz 只在喊唱时过冲。
- 6–12 kHz 宽带齿音辅助控制。
- 向上压缩补低电平清晰度，但需控制噪声。

## 路由

- 主唱 Insert 前/后动态按诊断选择。
- 伴奏总线外部侧链让位。
- Backing Vocal 总线宽频动态统一。

## 参数起点

- 单段 Dynamic Phase；Range -1 至 -3 dB、Ratio 1.5:1–3:1、Soft Knee。
- Attack/Release 从中值起；字头过软提高 Attack 百分比，泵动则提高 Release。
- 每段 Lookahead 从低值起，但同时核对顶部全局开关；本机全局 On 固定预留 20 ms，录音监听不要只看每段的 1 ms 数字。

## 调整目标

- 目标频段仅在问题音素动作，频带外主体不变。
- 比静态削减保留更多正常音节重量/明亮度。

## 调整时听什么

- 分频边界相位和音色变化。
- Attack 太快吞掉辅音或气势。
- 向上压缩抬噪声、呼吸和混响。
- Stereo Link 太低造成声像游移。

## 何时停止

- 最坏音素被限制到邻近音素范围。
- 再加 Range 只让动态趋近平坦或出现泵动时停止。

## 常见失败

- Range 符号和 Mode 组合错误。
- 多段重叠导致不可预测总 GR。
- Linear Phase 前振铃。
- 输出静态增益与动态增益混淆。

## 替代方案

- Pro-Q 3 动态 EQ：更少参数、更窄和自动时间行为。
- soothe2：大量移动共振。
- Pro-DS：齿音专用检测。

## 专业案例与工作流线索

- FabFilter 官方说明 Dynamic Phase 是默认且最适合常规混音；本卡把它作为起点，不把 Linear Phase 当升级。

## 扩展测试

- 同一音素用 Pro-MB、Pro-Q 3 动态频段与 soothe2 对比。
- Dynamic/Minimum/Linear 脉冲、Null、延迟与前振铃。
- Lookahead 0/5/20 ms、Attack/Release 极值的瞬态测试。

## 已测结果

- 本机 `1.2.8.0` VST3 Stereo 在 Ableton Live 11.3.43 / 48 kHz 真实加载。无频段默认态为 Dynamic Phase、OS Off、全局 Lookahead On、Mix 100%、Output 0 dB；对共享旁路三个主区域约 0 dB，残差约 -141.5 dBFS。
- 单一 Compress 频段中心 1720.8 Hz，Threshold -32.10 dB、Range -6.00 dB、Ratio 4:1、Knee 24 dB、Attack/Release 20%、band Lookahead 1.000 ms。全局 On 时三个稀疏短事件约 -0.228/-0.148/-0.031 dB；Off 时约 0 dB。
- 全局 On 宿主延迟 960 samples / 20 ms；全局 Off 为 0 samples。稳定多音整体只约 -0.0017/-0.0009 dB，说明当前动态动作依赖内容与时间，Range 不是必达 GR。
- 证据：[[projects/p1-plugin-knowledge-base/validation/reports/a8c2063eb007--FabFilter-Pro-MB|Pro-MB L3 验证]]。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | multiband-dynamics |
| mode | dynamic-phase |
| main_controls | band,threshold,range,ratio,knee,attack,release,lookahead |
| risk_flags | wrong-direction,overlap,pumping,pre-ringing |
| validation | composite-multiband-single-band-lookahead |

## 来源

- [[sources/音乐制作/插件资料/FabFilter/Pro-MB资料|Pro-MB 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]

## 开放问题

- 本机 1.2.8.0 各 Linear Resolution/OS 组合的报告延迟？
- Studio One 外部侧链映射和多输出自动化参数名？
- 专用单音/扫频下的精确频段边界、三种相位模式与所有 Oversampling 组合？
