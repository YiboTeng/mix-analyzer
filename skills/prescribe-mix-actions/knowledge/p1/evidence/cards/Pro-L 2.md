---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: 98d9ac6060f6
vendor: "FabFilter"
product: "Pro-L 2"
evidence_level: L3
validation_status: S4-passed-L3-measured
batch: B03
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Pro-L 2

## 身份与版本

- 厂商：FabFilter
- 产品族：Pro-L 2
- Family ID：98d9ac6060f6
- 本机观测版本：2.21 (64-bit; June 29, 2023)
- 格式：VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：limiting
- 次能力方向：true-peak;vocal-bus;metering
- 当前证据等级：L3
- 验证状态：S4-passed-L3-measured

## 能做什么

- 八种节目相关 Limiting Style、Gain/Output、Lookahead、Attack/Release 与瞬态/释放 Channel Link。
- True Peak Limiting/Metering、最高 32x Oversampling、响度表、Unity Gain 与 Audition Limiting。
- 可做透明峰值保护或有意 Bus 风格泵动，但不应无条件追求响度。

## 不建议用来做什么

- 不要用人声轨限制器代替前级 Clip Gain 与压缩。
- 不要把 0 dBFS Sample Ceiling 当安全 True Peak。
- 不要在主唱总线持续深限造成齿音和失真。

## 信号流位置

- 人声总线或并行返回末端做 1–3 dB 峰值保护。
- 最终母带限制不是本卡的人声主用途；Dither 只在最终位深转换一次。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Gain / Output Level | Gain 驱入限制，Output 设置最大样本或真峰值。 | 先设 Ceiling/TP，再推 Gain 到目标 GR；用 Unity Gain 判断。 |
| Style | 八种算法从透明到 Aggressive/Bus。 | 人声总线先 Transparent/Modern/Safe 比较；Bus 只作风格。 |
| Lookahead | 短值保瞬态/更响但失真风险高，长值更安全但可能变软。 | 从默认或 0.1–1 ms 起，极短时开 OS/TP 监测。 |
| Attack / Release | 控制较慢释放包络介入和恢复。 | 默认起；泵动加快 Release或减 GR，失真则更安全时间。 |
| Transient / Release Link | 分别链接短峰和慢包络左右声道。 | Release 从 100% Link；Transient 可稍低但要检查声像。 |

## Gain Staging

使用 Unity Gain 或后级 Trim 比较限制前后相同感知响度；同时记录 GR、LUFS、Sample Peak 与 dBTP。人声总线的目标是峰值安全，不把响度增加当收益。

## 延迟、相位与过采样

Style、True Peak、Lookahead 与 2–32x OS 都影响延迟/CPU；极短 Lookahead 接近硬削并增加混叠/ISP。本机 Default Setting、TP On、OS Off 在 Ableton/48 kHz 报告 3115 samples / 64.9 ms；渲染由 PDC 对齐。该数字只对应当前组合，不默认最高 OS。

## Mono/Stereo

Mono 禁用 Link。Stereo Release 先 100% Link防声像摆动，短峰 Link 可降低以减少无关侧压，但需相关性测试。

## 适用场景

- Vocal Bus 偶发峰值保护。
- 并行压缩返回防止尖峰。
- 效果化 Bus 限制/泵动。

## 路由

- Vocal Bus 最后一个动态处理，Meter 可后置。
- 不在每条人声都默认插入。

## 参数起点

- Transparent/Modern；TP Meter 开；Output -1 dBTP 仅作通用安全实验，不代表发布标准。
- Gain 到最大 GR 1–3 dB。
- 4x OS、Lookahead 0.1–1 ms 作为高质量试点，并与零/低延迟比较。

## 调整目标

- 偶发峰值受控，主体响度和瞬态不泵。
- 编码/真峰值不过目标且等响度收益成立。

## 调整时听什么

- 齿音失真、爆破挤压。
- 短 Lookahead 的毛刺/混叠。
- Release 过慢的整体下沉。
- 低 Link 的声像摆动。

## 何时停止

- 最坏峰值满足目标且通常 GR 接近 0。
- 限制持续动作或可听失真时回到前级解决。

## 常见失败

- 追 LUFS 而非峰值保护。
- 最高 OS 默认开启。
- True Peak/Output 误读。
- 用 Dither 多次处理。

## 替代方案

- Clip Gain/自动化：少数峰值。
- Pro-C 2/CLA-76：需要有时间行为的压缩。
- Studio One 原生 Limiter：宿主基线。

## 专业案例与工作流线索

- FabFilter 官方说明 Style 无绝对优劣，并建议 Release Link 从 100% 起；本卡据此把算法选择与声像稳定分开测试。

## 已执行与剩余测试

- 八 Style 在 1/3/6 dB GR 下的失真、ISP 和盲听。
- Lookahead/OS/TP 组合延迟和编码后峰值。
- Stereo Link 的单边峰值和声像测试。

## 已测结果

- 本机 Pro-L 2 2.21 VST3 Stereo 已真实加载；Default Setting 为 Gain 0.00 dB、Output 0.0 dBTP、True Peak Limiting On、Oversampling Off、Dither Off，宿主报告 3115 samples / 64.9 ms。
- 默认 Gain 0 对旁路五档稳态差均为 -0.000001 dB、峰值差 0 dB、直接相关 1.0，只剩约 -141.483 dBFS 的独立宿主抖动残差，支持未触发时的默认中性。
- 驱动态主读数 +6.0 dB，高精度悬停读回 +5.96 dB。五档持续音均线性增加约 +5.963 dB，最高持续音样本峰值 -0.037 dBFS，Crest 变化小于 0.00002 dB；不能因插件已插入就假设持续段都在限幅。
- 五个隔离瞬态只增加约 +1.699 dB，相对线性 +5.96 dB 参考削减约 4.261 dB，驱动态整段 RMS +5.900 dB、样本峰值 -0.037 dBFS、相关 0.998713。实际应用必须等响 A/B，并分开看持续音与尖峰。
- WAV 样本峰值不是独立 dBTP/ISP 证明；`0.0 dBTP` 仅是本轮固定状态，不是推荐发布 Ceiling。完整证据见 [[projects/p1-plugin-knowledge-base/validation/reports/98d9ac6060f6--FabFilter-Pro-L-2|Pro-L 2 L3 验证]]。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | true-peak-limiter |
| mode | multi-style |
| main_controls | gain,output,style,lookahead,attack,release,channel_link,tp,oversampling |
| risk_flags | loudness-chasing,distortion,isp,stereo-shift |
| validation | true-peak-style-latency-codec |

## 来源

- [[sources/音乐制作/插件资料/FabFilter/Pro-L 2资料|Pro-L 2 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]
- [[projects/p1-plugin-knowledge-base/validation/reports/98d9ac6060f6--FabFilter-Pro-L-2|Pro-L 2 L3 验证]]

## 开放问题

- 本机 2.21 各 Style/TP/OS 报告延迟与 CPU？
- Studio One 离线导出与 Unity Gain 自动化一致性？
