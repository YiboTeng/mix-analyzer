---
type: plugin-card
status: deferred
created: 2026-08-20
updated: 2026-08-20
family_id: bc411ff14519
vendor: "SoundToys"
product: "Decapitator"
evidence_level: L2
validation_status: S4-replaced-vst2-unavailable
batch: B04
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Decapitator

> [!note] S4 替换
> 本机仅有 VST2，现有 Ableton 配置未暴露 VST2 且本任务不改扫描偏好；正式集合已由当前可达的 Waves Abbey Road Saturator 替换。本卡保留为历史研究，不计入最终 40 款。

## 身份与版本

- 厂商：SoundToys
- 产品族：Decapitator
- Family ID：bc411ff14519
- 本机观测版本：5.0.1.0
- 格式：VST2
- Studio One 可用性：current-filesystem-match
- 主能力方向：saturation-character
- 次能力方向：parallel-distortion;five-styles
- 当前证据等级：L2
- 验证状态：S3-researched-S4-pending

## 能做什么

- 五种硬件建模 Style 提供不同奇偶谐波、压缩与频率响应。
- Drive 控制进入饱和电路的电平，Punish 额外大幅推驱；Mix 支持内部并行。
- Low Cut/Thump、Tone、High Cut/Steep 在饱和前后塑形，Auto/Output 帮助补偿。

## 不建议用来做什么

- 不要把 Punish 当常规增稠开关。
- 不要未匹配 Output/Mix 就比较 Style。
- 不要忽略 Tone 位于饱和前，会改变哪些频率产生谐波。

## 信号流位置

- 主唱后段轻饱和通常在基础压缩/去齿之后；若高频新谐波激发齿音，链尾复查。
- 重度角色常放 Aux，100% Wet 后以 Send 控量并滤波。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Style A/E/N/T/P | 选择不同模拟电路与谐波/频响。 | 固定 Drive 与等响度逐个 A/B，不凭字母预设结论。 |
| Drive / Punish | 推入非线性；Punish 进入极端驱动。 | Insert 从 1–3 小步；Punish 主要并行并严格限峰。 |
| Low Cut / Thump | 饱和前减少低频；Thump 在切点附近提升。 | 防低频松散用 Low Cut；主唱通常慎用 Thump。 |
| Tone / High Cut / Steep | 倾斜进入饱和的频谱并限制高频输出。 | 齿音硬则偏 Dark/降 High Cut，避免靠更亮制造存在感。 |
| Mix / Output / Auto | 干湿与输出补偿。 | 先全湿设音色，再回 Mix；最终人工等响度。 |

## Gain Staging

Attitude Meter 显示进入 Drive 的相对电平，不是输出表。关闭 Auto 或记录其状态，用 Output 匹配旁通 Active RMS；同时记录 True Peak、THD 与噪声。

## 延迟、相位与过采样

v5 手册未给本机 5.0.1 的延迟/OS；内部 Mix 与 VST2 宿主补偿需 S4 以脉冲/Null 验证。

## Mono/Stereo

本机只观测 VST2 产品族；Stereo 处理时 Style 非线性可能改变相关性，主唱 Mono 优先，Aux 返回做折叠测试。

## 适用场景

- 主唱轻增稠与中频前冲。
- Ad-lib/低八度角色失真。
- 并行重饱和增加可懂度和质感。

## 路由

- 主唱 Insert 轻用。
- 100% Wet Aux 重度处理，返回高通/低通。

## 参数起点

- Drive 1–3、Punish Off、Mix 100%，找 Style 后再回 5–30% Mix。
- 并行 Punish 可开，但 Send 从 -20 dB 以下起。
- Low Cut 80–150 Hz 仅在低频失真松散时。

## 调整目标

- 谐波让弱播放更可懂，而非只更响更亮。
- 字头、齿音和低中频仍受控。

## 调整时听什么

- 齿音沙亮、爆破毛刺、低频松散。
- Auto/Output 带来的响度偏差。
- 并行梳状或噪声。

## 何时停止

- 等响度下质感增加但可懂度和动态未受损。
- 再加 Drive 主要增加粗糙与失真时回退。

## 常见失败

- Punish 全湿。
- Tone/Low Cut 位置误读。
- Style 比较未匹配响度。
- 饱和后重度去齿互相抵消。

## 替代方案

- Saturn 2：多段、OS 与调制可控。
- HG-2：更平滑管式串并联。
- VTM：磁带动态与频响。

## 专业案例与工作流线索

- Soundtoys 官方手册强调 Tone 在饱和前、Attitude Meter 非输出表；这两点决定测试的输入与输出必须分开。

## 待执行测试

- 五 Style 同 THD/同响度对比。
- Drive/Punish 静态曲线、谐波、别名与瞬态。
- 内部 Mix 与 Aux 并行 Null/延迟。

## 已测结果

S4 待执行。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | analog-model-saturator |
| mode | five-style |
| main_controls | style,drive,punish,filters,tone,mix,output |
| risk_flags | aliasing,sibilance,loudness-bias,parallel-phase |
| validation | thd-style-latency |

## 来源

- [[sources/音乐制作/插件资料/SoundToys/Decapitator资料|Decapitator 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]

## 开放问题

- 本机 5.0.1 的 Style 命名、Auto 行为与报告延迟？
