---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: ddb1354cf0c2
vendor: "Waves"
product: "Smack Attack"
evidence_level: L3
validation_status: S4-passed-L3-measured
batch: B03
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Smack Attack

## 身份与版本

- 厂商：Waves
- 产品族：Smack Attack
- Family ID：ddb1354cf0c2
- 本机观测版本：12.7.0.209
- 格式：VST2 | VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：transient-shaping
- 次能力方向：articulation;envelope
- 当前证据等级：L3
- 验证状态：S4-passed-L3-measured

## 能做什么

- 独立提升/衰减 Attack 与 Sustain，并以 Sensitivity、Duration、Shape 调整检测和包络。
- 可视化检测到的瞬态与处理包络；Mix/Output 支持并行和匹配。
- 瞬态检测依阈值/Sensitivity，不是传统压缩器的 Ratio/Threshold。

## 不建议用来做什么

- 产品主要面向打击乐；用于人声必须局限于字头/包络实验。
- 不要用它代替去齿或高频 EQ。
- 不要提升 Attack 后忽略爆破、齿音、嘴部点击。

## 信号流位置

- 基础修复和去齿后，小幅塑造主唱/Ad-lib 字头；常在压缩后使用。
- 若只需要个别词头，优先 Clip Gain/自动化而非整轨。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Sensitivity | 决定哪些瞬态被检测。 | 从低上推，只让目标词头触发，排除噪声与齿音。 |
| Attack Amount / Shape / Duration | 改变检测到的起始段电平、曲线和时长。 | 从 ±5–15% 小步；咬字不足提升，爆破/硬辅音过强衰减。 |
| Sustain | 改变瞬态后的持续包络。 | 需要更短更干时轻减；拉长会抬房间/呼吸。 |
| Mix / Output | 并行混合并补偿输出。 | 先全湿诊断，再回 Mix；始终等响度。 |

## Gain Staging

Attack/Sustain 改变短时峰值和平均响度。分别匹配整体 Active RMS并记录最大 Sample/True Peak；不要只用 Output 抹去峰值差异后声称无动态变化。

## 延迟、相位与过采样

本机 VST3 Stereo、48 kHz、A: Default Preset 在 Ableton 设备栏报告 0 samples。默认态与旁路整段相关 1.0、互差约 -141.478 dBFS；这是当前导出与 PDC 下的近似中性证据，不代表所有 Mix、Guard、格式或采样率都零延迟/位透明。

## Mono/Stereo

立体声检测链接不明；主唱 Mono 优先。立体声 Ad-lib/总线提升瞬态前检查声像。

## 适用场景

- 过压主唱的词头略显后缩。
- 爆破/硬辅音包络过强时做动态软化。
- 效果化 Ad-lib 的短促/延长。

## 路由

- 主唱链后段轻用。
- 只对复制的效果轨或自动化区段启用。

## 参数起点

- Sensitivity 刚好抓目标；Attack 从 ±5–10 小步开始；Duration 中短。本机 +100 极值已把固定瞬态推到 0 dBFS，不可作为人声起点。
- Sustain 0 起，仅在尾部包络确有目标时动。
- Mix 50–100% 由等响度盲听决定。

## 调整目标

- 字头更清楚或更柔和而不是更尖。
- 音节节奏更明确，元音主体不抽动。

## 调整时听什么

- 齿音、爆破、点击被提升。
- 检测漏抓弱字或误抓噪声。
- Sustain 抬房间和尾噪。

## 何时停止

- 目标词头达到存在感且硬辅音未超标。
- 进一步 Attack 主要增加峰值/刺耳时停止。

## 常见失败

- 把打击乐默认设置照搬人声。
- Sensitivity 过高全程动作。
- Attack 提升后用重度 De-ess 抵消。
- Output/峰值不校准。

## 替代方案

- Clip Gain/自动化：少数词头。
- CLA-76 慢 Attack：用压缩相对保留字头。
- Pro-C 2：显式 Attack/Release 控制。

## 专业案例与工作流线索

- Waves 官方对比文章强调 Sensitivity 是阈值相关，并用 Shape/Duration细化 Attack；人声用法必须先做检测再做幅度。

## 已执行与剩余测试

- 已执行：默认态对旁路、Attack +100 与 Sustain -100 的阶梯/隔离瞬态固定渲染和量化。
- 剩余：辅音/元音/爆破/齿音标注集的检测准确性。
- 剩余：Attack/Sustain Shape 与 Duration 的完整包络测量。
- 剩余：内部 Mix、Guard Limit/Clip、Stereo Link、真实人声等响盲听。

## 已测结果

- 本机 `Smack Attack Stereo` V12（文件系统 12.7.0.209）已真实加载；A: Default Preset 实见 Attack 0、Sustain 0、Output 0.0、Guard Off，宿主报告 0 samples。
- 默认态对旁路五档稳态与整段 RMS/峰值差均为 0 dB、相关 1.0，互差约 -141.478 dBFS，可作为当前状态的近似中性控制。
- Attack +100 使五档持续音增加约 +1.423 至 +1.470 dB；五个隔离瞬态前 20 ms RMS 增加约 +7.260 dB、20–120 ms 增加约 +9.884 dB，样本峰值由 -2.854 dBFS 推到 0 dBFS。Guard Off 下这是削顶风险，不是推荐设置。
- Sustain -100 保持隔离瞬态前 20 ms 的峰值不变，但把 20–120 ms 主体 RMS 降低约 7.156 dB、该窗峰值降低约 6.233 dB；验证其可缩短主体而不必同时削掉初始峰值。
- 整段 Attack +100 仅 +1.961 dB RMS、Sustain -100 仅 -0.239 dB RMS，说明整段电平会掩盖局部 6–10 dB 的包络改变；实际应用必须看局部短窗并等响。完整证据见 [[projects/p1-plugin-knowledge-base/validation/reports/ddb1354cf0c2--Waves-Smack-Attack|Smack Attack L3 验证]]。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | transient-shaper |
| mode | attack-sustain |
| main_controls | sensitivity,attack,shape,duration,sustain,mix |
| risk_flags | sibilance-plosive-boost,false-trigger,peak-rise |
| validation | phoneme-envelope-detection |

## 来源

- [[sources/音乐制作/插件资料/Waves/Smack Attack资料|Smack Attack 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]
- [[projects/p1-plugin-knowledge-base/validation/reports/ddb1354cf0c2--Waves-Smack-Attack|Smack Attack L3 验证]]

## 开放问题

- 本机各 Shape/Duration/Sensitivity 组合的检测窗与误检率？
- Stereo Link、Guard 与 Mix 的相位/峰值行为？
