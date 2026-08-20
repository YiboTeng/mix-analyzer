---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: a094b33b301c
vendor: "Waves"
product: "Scheps Omni Channel"
evidence_level: L3
validation_status: passed-l3
batch: B03
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Scheps Omni Channel

## 身份与版本

- 厂商：Waves
- 产品族：Scheps Omni Channel
- Family ID：a094b33b301c
- 本机观测版本：12.7.0.209
- 格式：VST2 | VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：channel-strip
- 次能力方向：preamp;eq;dynamics;deessing;gate
- 当前证据等级：L3
- 验证状态：passed-l3
- 本机真实加载：Waves `Scheps Omni Channel Stereo` V12（文件系统 12.7.0.209），Ableton Live 11.3.43 / VST3 Stereo / 48 kHz。

## 能做什么

- 原版由 Pre、EQ、DS² 双动态频段、Compressor、Gate 与可重排 Insert 构成，可自定义模块顺序。
- Pre 提供滤波、Thump 与 ODD/EVEN/HEAVY 饱和；Compressor 有 VCA/FET/OPT 三模式。
- DS² 两段可在任意频率做动态控制，不局限齿音；Gate 可作扩展。
- 本机 v12 对应原版边界，不把 Omni Channel 2 的 CRUSH、SOFT、24 dB Filter 或任意第三方 VST3 Host 写回。

## 不建议用来做什么

- 不要一次启用所有模块而无法归因。
- 不要把当前产品页的 Omni 2 新功能倒灌本机 v12。
- 不要因一体化方便而跳过模块级等响度和顺序判断。

## 信号流位置

- 先按问题决定模块顺序；主唱可从 Compressor→Pre/EQ→DS²，Gate/Expander 置前。
- 官方 Andrew Scheps 教程建议比较 Compressor 前/后 EQ、DS² 前/后 Compressor，而不是固定教条。
- Insert 插件能力按本机原版仅信任 Waves 内部兼容性，待 S4 回读。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Pre Saturation / Thump / Filters | 增加谐波、低频共振和边界滤波。 | 先滤除无用频率，再选一个饱和模式小推；Thump 仅缺重量时。 |
| VCA / FET / OPT Compressor | VCA 快且透明，FET 更有色/泵，OPT 最慢平滑。 | Vocal 从 VCA 4:1、慢 Attack/快 Release 起，再 A/B 类型。 |
| DS² 1/2 | 两段频率选择性动态抑制。 | 一段 6–10 kHz 齿音，一段 2.5–3.5 kHz 喊唱鼻刺，仅在对应事件动作。 |
| Gate / Expander | 降低阈值下泄漏。 | 放链前，从温和扩展开始，保护尾音。 |
| Module Drag Order / Insert | 改变处理先后和可插入点。 | 每次只移动一个模块，重新匹配响度和压缩阈值。 |

## Gain Staging

每模块都有可能改变电平。用逐模块 Bypass/总 Bypass 两级校准；饱和、EQ、压缩后的输出分别记录，避免模块顺序变化只是输入驱动差异。本机实测 `Full Reset` 对旁路为 0 dB 电平差，但仅切到 `HEAVY` 且 Drive 仍为 0.0 就约增响 0.505 dB；因此比较饱和模式必须先用 Output 等响，不能把“Drive=0”视为中性。

## 延迟、相位与过采样

本机原版 v12 VST3 Stereo 在 Full Reset 与 HEAVY Drive 0/3.2 时，Ableton 均报告 0 samples；Full Reset 对旁路最佳偏移 0 samples、互差 RMS -141.483962 dBFS。该结果不能外推到 Omni Channel 2、Insert、其它模块/模式、VST2 或其它采样率。

## Mono/Stereo

原版提供 Stereo/M/S/Duo 路由的具体范围需本机回读。单声道主唱简化通道模式；Stereo 总线重排模块后检查声像。

## 适用场景

- 快速搭建完整现代 Rap 主唱通道。
- 一窗口比较三种压缩色彩。
- 双动态频段同时控制齿音和喊唱鼻刺。

## 路由

- 主唱 Insert 的一体化通道。
- Backing Vocal Bus 统一处理；Gate/DS² 更保守。

## 参数起点

- Compressor 4:1、相对慢 Attack/快 Release、3–5 dB GR。
- DS² Band 1 先找齿音，Band 2 只在 2.5–3.5 kHz 喊唱问题存在时启用。
- Pre 只选一种轻饱和；所有模块逐个开启。比较 ODD/EVEN/HEAVY 前先匹配 Output；HEAVY Drive 0 已比 Full Reset 约响 0.5 dB。

## 调整目标

- 用最少启用模块完成完整主唱链。
- 顺序改变带来可描述收益，而非电平和阈值漂移。

## 调整时听什么

- 多模块叠加过度饱和/去齿/压缩。
- EQ 前后移动使 Compressor 触发变化。
- Gate 吞尾、DS² 造成暗哑。

## 何时停止

- 每个启用模块都有独立可听目标和旁通收益。
- 关闭任何模块无差异时删除而不是保留。

## 常见失败

- Omni 2 功能误写。
- 预设全开无法归因。
- 模块重排未重调阈值/增益。
- 一体化替代精确源修复。

## 替代方案

- 分立 Pro-Q 3 + Pro-C 2 + Pro-DS：更精确可测。
- RVox + 原生 EQ：更简单快速。
- Studio One Fat Channel：原生通道基线。

## 专业案例与工作流线索

- Andrew Scheps 官方教程的人声起点是 4:1、慢 Attack/快 Release，并主动比较 Compressor/DS² 顺序；本卡保留为实验矩阵。

## 已执行与剩余测试

- ODD/EVEN/HEAVY 的等响 Drive 扫描、稳态频谱和高电平输入余量。
- Gate/DS²/EQ/VCA-FET-OPT Compressor/Limiter/模块顺序逐一消融，另测 Insert 与 Stereo/M/S/Duo。
- 官方 Vocal 顺序三组等响度盲听与分立链对照；补测 VST2/Mono、其它采样率、CPU 和自动化。

## 已测结果

- `A: Full Reset` 实见 Pre Drive 0、Saturation Off、Gate -144 dB、DS² 两段 -48 dB、四段 EQ 0 dB、VCA Compressor -50 dB/1:1、Input/Output 0 dB、Limiter Off；对旁路延时 0 samples、相关 1.0、电平差 0 dB、互差 RMS -141.483962 dBFS。
- Full Reset→HEAVY 且 Drive 保持 0.0 后，RMS +0.504912 dB、Peak +0.501807 dB，非输入音调能量比 -81.352696→-77.675508 dB；HEAVY 零驱动不是中性。
- HEAVY Drive 0.0→3.2 单变量后，RMS 再 +0.105300 dB、Peak 再 +0.099415 dB，十个测试音均约 +0.105 dB，非输入音调能量比再升 7.220305 dB。
- 八度相关多音不能分离谐波阶数/THD/别名；L3 只覆盖原版 V12 VST3 Stereo 的这三个状态，不倒灌 Omni Channel 2。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | modular-channel-strip |
| mode | reorderable-modules |
| main_controls | pre,eq,ds2,compressor,gate,order,insert |
| risk_flags | version-leak,stacking,order-gain-confound |
| validation | ui-module-ablation-order-matrix |

## 来源

- [[sources/音乐制作/插件资料/Waves/Scheps Omni Channel资料|Scheps Omni Channel 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]
- [[projects/p1-plugin-knowledge-base/validation/reports/a094b33b301c--Waves-Scheps-Omni-Channel|Scheps Omni Channel L3 验证]]

## 开放问题

- ODD/EVEN、各模块、重排与 Insert 的增益/延迟是否保持一致？
- Stereo/M/S/Duo、VST2/Mono 与其它采样率是否改变通道一致性或延迟？
