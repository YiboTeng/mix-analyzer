---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: 585b0952e62c
vendor: "iZotope"
product: "Insight 2"
evidence_level: L3
validation_status: S4-passed
batch: B05
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Insight 2

## 身份与版本

- 厂商：iZotope
- 产品族：Insight 2
- Family ID：585b0952e62c
- 本机观测版本：2.0.6.0 | 2.6.0
- 格式：VST2 | VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：metering
- 次能力方向：loudness;spectrum;stereo;intelligibility
- 当前证据等级：L3
- 验证状态：S4-passed

## 能做什么

- Loudness显示Momentary、Short-term、Integrated、LRA和True Peak，支持BS.1770目标。
- Levels、Sound Field、Spectrum/Spectrogram、History提供电平、声像、频谱时间信息。
- Relay可发送多轨数据到Spectrogram/Intelligibility，比较对话与背景。

## 不建议用来做什么

- 不要把广播/流媒体预设当所有音乐必须目标。
- 不要用Integrated LUFS评价单一短音节。
- 不要让Meter替代听感和因果测试。

## 信号流位置

- 放在Vocal Bus/Main/Monitor末端只测不处理；Relay放在需要对照的干声、处理声、伴奏或参考轨。
- 固定窗口和Reset时点，避免不同段落历史混在一起。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Momentary/Short-term/Integrated/LRA | 约400ms、3s、累计响度及范围。 | 短人声用Momentary/Short-term；整段/整曲才Integrated/LRA。 |
| True Peak/Levels | 估算重建峰值与样本电平。 | 限制/饱和后监控dBTP，不只Sample Peak。 |
| Sound Field | 声像、相关性和Mono兼容。 | 宽化/混响/Delay后检查相关与中心。 |
| Spectrum/Spectrogram | 频率与时间/多Relay可视化。 | 定位音素/尾部，不追静态曲线。 |
| Relay/Intelligibility | 跨轨发送与语音相对背景评估。 | 标注Relay身份；音乐人声适用性先做实验。 |

## Gain Staging

Meter不改增益；建立统一Reset、Window、Gate、Target和采样率。L3记录设置快照，确保不同插件比较同一窗口。

## 延迟、相位与过采样

默认 VST3 的 Ableton 设备栏报告 2399 samples（约 50 ms）延迟；宿主 PDC 后导出最佳整数延迟 0 samples、RMS 电平差 -0.000000 dB。Relay 通信与其它模块仍需扩展测试。

## Mono/Stereo

支持至7.1.2；P1聚焦Mono/Stereo。Sound Field判断相关性但不能单独判空间好坏。

## 适用场景

- 插件前后响度/真峰值匹配。
- 宽化/空间Mono兼容。
- 频谱尾部、动态历史和参考区间。

## 路由

- VocalBus/Main末端。
- Relay在干声、处理声、伴奏、参考。

## 参数起点

- Reset后播放固定30–60秒代表段。
- 记录M/S/I/LRA/TP及窗口/标准。
- 宽化实验同时截图SoundField和Mono RMS。

## 调整目标

- 所有L3测量可复现。
- 指标与主观结论有明确因果关系。

## 调整时听什么

- Gate/历史未Reset。
- Meter窗口不同。
- 标准预设版本变化。
- Relay选错源。

## 何时停止

- 测量重复三次在容差内。
- 增加更多图表不再改变诊断时停止。

## 常见失败

- 短段看Integrated。
- 把相关性>0当唯一目标。
- 未保存设置。
- Meter参与导出链未验证。

## 替代方案

- MetricAB：参考播放与A/B。
- FabFilter内置表。
- 离线Python/ffmpeg测量。

## 专业案例与工作流线索

- iZotope官方定义Momentary约400ms、Short-term约3s；本项目按信号时间尺度选择指标。

## 待执行测试

- 已完成：默认 Loudness + Levels 实时读数、音频中性、0-sample 延迟。
- 待扩展：校准正弦/粉噪/官方响度测试文件，与离线 BS.1770/True Peak 工具交叉验证。
- 待扩展：Relay 身份、Sound Field、Spectrum/Spectrogram、History、Intelligibility。

## 已测结果

- Ableton Live 11.3.43 默认 Loudness + Levels，固定稀疏脉冲从 1.1.1 开始计量：Integrated -41.2 LUFS、LRA 11.1 LU、True Peak -1.9 dB、Max Momentary -37.4 LUFS，左右 Peak 均 -1.9 dB。
- Ableton 设备栏报告插件延迟 2399 samples（约 50 ms）；宿主 PDC 后对共享旁通的导出最佳整数延迟 0 samples，直接相关 0.999999998922，RMS 电平差 -0.000000 dB；独立 dither 残差 RMS -141.469510 dBFS。
- 静音后 Short-term/Momentary 回 `-Inf` 而累计值保留；离线导出后 Integrated/Momentary/LRA 被重置而 Peak 历史保留，正式测量必须在导出前截图并记录 Reset 时点。
- 详细证据：[[projects/p1-plugin-knowledge-base/validation/reports/585b0952e62c--Insight-2|Insight 2 L3 验证]]。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | metering-suite |
| mode | loudness-spectrum-soundfield |
| main_controls | loudness,levels,soundfield,spectrum,spectrogram,relay |
| risk_flags | window-mismatch,stale-history,metric-overreach,relay-routing |
| validation | calibration-cross-meter |

## 来源

- [[sources/音乐制作/插件资料/iZotope/Insight 2资料|Insight 2 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]

## 开放问题

- 本机2.0.6与2.6的实际功能差异和共存原因？
