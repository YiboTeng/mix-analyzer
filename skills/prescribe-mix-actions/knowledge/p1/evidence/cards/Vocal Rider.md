---
type: plugin-card
status: active
created: 2026-08-19
updated: 2026-08-20
family_id: b6c750f3ccec
vendor: "Waves"
product: "Vocal Rider"
evidence_level: L3
validation_status: passed-l3
batch: B01
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Vocal Rider

## 身份与版本

- 厂商：Waves
- 产品族：Vocal Rider
- Family ID：b6c750f3ccec
- 本机观测版本：12.7.0.209
- 格式：VST2 / VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：level-riding
- 次能力方向：automation;pre-compression-conditioning;music-sidechain
- 当前证据等级：L3
- 验证状态：passed-l3

## 能做什么

- 实时自动抬高/压低人声，使其保持在相对 Target 范围；不是传统压缩器，不以时间常数和增益衰减着色。
- 可接收 Instrumental Mix Sidechain，让 Music Sensitivity 决定对伴奏电平变化的适应程度。
- 可把 Rider Fader 动作写入 DAW Automation，再手工编辑。

## 不建议用来做什么

- 不要用 ±6 dB 或更大范围替代 Comping、Clip Gain 和问题词手工修正。
- 不要把 Rider 当峰值限制器；快速爆破和单采样峰仍需压缩/限制。
- 不要在未路由音乐侧链时假设 Music Sensitivity 正在工作。

## 信号流位置

- 常用顺序：Clip Gain/源修复 → Vocal Rider 宏观整理 → FET/Opto 压缩与音色链。
- 也可放在后段做轻微 Mix-relative 修正，但必须避免与已有自动化和总线压缩互相追逐。
- 官方工程师案例支持放在压缩前，让压缩器获得更一致输入与颜色。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Target | 人声定位参考；改变 Rider Fader 的 0 校准。 | 让大多数正常句的 Rider 围绕 0 小幅动作，不把 Target 当输出音量。 |
| Vocal Sensitivity | 区分人声与噪声/泄漏并识别词头词尾。 | Activity 漏掉弱词时提高，句间噪声也 Ride 时降低。 |
| Attack Fast/Slow | 同时影响检测时机和 Rider 速度。 | 密集 Rap 先试 Fast；自然长句先试 Slow，并听是否追逐音节。 |
| Music Sensitivity | 根据侧链伴奏电平改变 Ride。 | 先正确路由 Instrumental Bus，再从 0 小步调。 |
| Range Min/Max | 自动衰减/增益的最大边界。 | 把范围限制在必要的少量 dB，避免补偿录音根本问题。 |
| Idle Arrow | 无检测活动时 Rider 返回值。 | 保持接近 0，避免词间大跳。 |

## Gain Staging

先用 Target 让 Rider 平均围绕 0，再以 Output Trim 匹配旁通响度。记录 Rider 动作分布、P90–P10 和活跃 RMS，而不是只看全段 LUFS。若写入 Automation，保留未写入版本。

## 延迟、相位与过采样

Waves 官方称实时、零延迟且无需预扫描；本机 `Vocal Rider Stereo` VST3 在 Ableton Live 11.3.43 / 48 kHz 中报告 `0 samples`。该结果不外推到 Live/VST2/其它版本或 Studio One。

## Mono/Stereo

产品族包含 Mono/Stereo/Live 变体；主唱用匹配轨道布局的普通组件。立体声 Stem 与叠唱可能让检测受 Side 效果影响，优先处理独立主唱。

## 适用场景

- 压缩前整理乐句与音节宏观电平，使后级压缩颜色更一致。
- 伴奏编排密度变化时，通过音乐侧链维持主唱相对位置。
- 写出 Automation 后手工修正少数错误动作。

## 路由

- 主唱 Insert；Instrumental Bus Send 到插件 Sidechain。
- 若使用 Write/Read，先保存版本并确认 DAW Automation 模式，避免覆盖已有自动化。

## 参数起点

- Target 调到 Rider 大部分时间围绕 0；Range 先限制约 -3 至 +2 dB。
- Vocal Sensitivity 从 0 开始，按 Activity Display 校准；密集 Rap 试 Fast，自然演唱试 Slow。
- Music Sensitivity 从 0 开始，只在侧链已正确路由后小步增加。

## 调整目标

- 弱词更稳定、强词不过分突出，后级压缩增益衰减更一致。
- Rider 不追逐每个字头，也不在词间突然跳到 Range 边界。

## 调整时听什么

- Fast 是否造成音节级泵动，Slow 是否漏掉快速弱词。
- 句间噪声、呼吸和效果尾是否被错误抬高。
- 音乐侧链变化是否让主唱不自然地随编曲起伏。

## 何时停止

- Rider 多数动作在小范围内且解决宏观不稳时停止。
- 需要持续超过 3–4 dB 的快速补偿时，回到 Clip Gain/Comping/压缩，而不是扩大 Range。

## 常见失败

- Target 设置错误让 Rider 长期贴 Range 上下限。
- Sensitivity 太高抬噪声/呼吸，太低漏掉弱词。
- Music Sidechain 未接却调 Music Sensitivity。
- Automation Write/Latch 覆盖已有数据，或插件窗口/模式不满足写入要求。

## 替代方案

- 手工 Clip Gain 与 Volume Automation：最可控。
- Waves MV2：上下行压缩，行为和音色不同。
- 压缩器 Sidechain/Auto Gain：不能等同 Rider。

## 专业案例与工作流线索

- Waves 官方产品页收录 Bob Power 的用法：放在压缩器前，使压缩器在不同演唱动态下获得更一致颜色。
- Waves 官方教程建议先设 Target，再限制 Range；过大动作会听起来不自然。

## 待执行测试

- 正确音乐侧链下测试 Music Sensitivity 与编曲密度变化。
- Target、Vocal Sensitivity、Range、Idle 的单变量和带标签呼吸/噪声语料。
- Vocal Rider 前置/后置于压缩器的增益衰减分布与等响度听感。
- Automation Write/Read 在 Ableton 与 Studio One 的可回读性。

## 已测结果

- 本机 Waves `Vocal Rider Stereo` 12.7.0.209 VST3 在 Ableton Live 11.3.43 / 48 kHz 中真实加载，宿主报告 0 samples。
- 默认预设为 Target 居中、Vocal/Music Sensitivity 0、Range -6/+6 dB、Rider/Output 0、Automation Off、无音乐侧链；默认音频与显式 Slow 相关 `0.999999991007`，确认默认就是 Slow。
- 默认 Slow 的 1037 个有效 50 ms 窗中，增益变化最小 -5.782、中位 +0.226、最大 +6.000 dB；39 窗命中 +6 dB 上限。动态阶梯电平跨度由 24.000 收窄到 17.221 dB。
- Fast 的全程序相邻增益变化 P90 为 0.242 dB，高于 Slow 的 0.155 dB；固定人声整体电平相对旁路为 -0.855 dB，而 Slow 为 +0.322 dB。Fast 更易追逐局部节目，必须专听音节级泵动。
- 默认 Sensitivity 0 仍使稳定多音 +0.145 dB、空间夹具 -0.545 dB；不要假设它只对人声动作。
- 详见 [[projects/p1-plugin-knowledge-base/validation/reports/b6c750f3ccec--Waves-Vocal-Rider|Vocal Rider L3 验证]]。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | automatic-level-rider |
| mode | vocal-detection-with-optional-music-sidechain |
| main_controls | target,vocal_sensitivity,attack,music_sensitivity,range,idle |
| risk_flags | noise-lift,pumping,automation-overwrite,sidechain-misroute |
| validation | rider-automation-and-compressor-conditioning |

## 来源

- [[sources/音乐制作/插件资料/Waves/Vocal Rider资料|Vocal Rider 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]

## 开放问题

- 本机 v12.7 在 Studio One 中 Automation Write/Read 的参数名和模式要求是什么？
- 普通与 Live 组件的检测/延迟差异是否影响本机选择？
- 正确音乐侧链下，Music Sensitivity 如何改变同一人声在稀疏/密集伴奏中的 Rider 分布？
