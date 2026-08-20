---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: edb2c31ffd45
vendor: "Waves"
product: "Abbey Road Saturator"
evidence_level: L3
validation_status: passed-l3-default-tg
batch: R01
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Abbey Road Saturator

## 身份与版本

- 厂商：Waves
- 产品族：Abbey Road Saturator
- Family ID：edb2c31ffd45
- 本机观测版本：12.7.0.209
- 格式：VST2 | VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：saturation-character
- 次能力方向：compander;parallel-distortion
- 当前证据等级：L3
- 验证状态：passed-l3-default-tg

## 能做什么

- TG12321 compander 激励链与 REDD/TG 两种前级路径提供从细微谐波到明显失真。
- Mix、Input、Output、Bass/ Treble 与 Compander 可并行塑造人声密度和存在感。

## 不建议用来做什么

- 不要用输入推高造成的响度提升替代等响判断。
- 不要在齿音未受控时全频重驱动。

## 信号流位置

- 通常在清理 EQ/去齿之后、主压缩之前或作为并行返回。
- 重失真并行轨先高通/低通再混回。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| REDD/TG | 两种模拟路径与失真性格。 | 固定响度和 Drive 逐一比较。 |
| Input/Output | 驱动非线性并补偿电平。 | 每次增加 Input 都回调 Output 做旁通等响。 |
| Compander | 引入 TG12321 压扩器的激励和动态质感。 | 从低量开始，听辅音颗粒和噪声底。 |
| Mix/Bass/Treble | 并行比例与前后色调。 | 先定失真，再用 Mix 和色调融入主唱。 |

## Gain Staging

用 Output 抵消 Input/Compander 的平均响度提升；记录 THD 变化和 RMS/LUFS-S 差。

## 延迟、相位与过采样

官方延迟表在 44.1/48 kHz 列出 49 samples；本机 V12 Stereo 默认实例在 Ableton 48 kHz 实际报告 `49 samples (1.02 ms)`，与官方声明一致。离线导出经过宿主补偿，波形局部峰值偏移不得当作 PDC。

## Mono/Stereo

Mono 主唱优先 Mono 或 linked Stereo；并行 Stereo 返回检查通道一致性和 Mono Fold-down。

## 适用场景

- 主唱轻推获得中频密度。
- 副歌或 Ad-lib 并行重驱动。

## 路由

- Insert 轻度驱动。
- Parallel Aux 重度驱动并带通。

## 参数起点

- Mix 10–30% 或完全并行起步。
- Input 逐步推到谐波可闻，再回调 Output 等响。

## 调整目标

- 近距离感增加但齿音、爆破不被夸张。
- 等响旁通仍保留密度和颗粒收益。

## 调整时听什么

- 高频砂砾、低中频膨胀、噪声被抬。
- 辅音扁平或字头发硬。

## 何时停止

- 再增加 Drive 只增加响度或毛刺。
- 并行返回在混音中可感但不抢词。

## 常见失败

- 不补偿 Output。
- 全频并行重失真造成低频与齿音堆积。

## 替代方案

- Saturn 2：多段和调制更精细。
- HG-2：电子管并行谐波结构。

## 专业案例与工作流线索

- 官方强调 REDD/TG 管与晶体管路径以及 TG12321 compansion 激励链。

## 待执行测试

- 多音信号扫 Input/Mix，补测稳态谐波阶次、THD、别名和频响。
- 对 REDD/TG、Compander Off/On 与 Input/Output 做单变量等响对照。
- 固定人声等响盲听轻驱动与并行重驱动副作用。

## 已测结果

- 真实状态：`Abbey Road Saturator Stereo` VST3，`A: Default Preset`，TG、Saturator Mix 100%，Pre/Post EQ 开启且旋钮保持中心；Host 160 BPM，48 kHz。
- 宿主报告延迟：49 samples / 1.02 ms。
- 三档脉冲输入 -1.938/-6.021/-12.041 dBFS 对应峰值增益 -9.305/-4.866/+0.237 dB，范围 9.542 dB；默认 TG 明确为电平依赖非线性处理。
- 全局直接相关 0.121423、RMS 电平差 -2.020908 dB、左右输出相关 0.999999998260；强/中/弱脉冲核心外短时能量占 38.800%/24.859%/10.359%。
- 边界：上述数字只覆盖默认 TG 的固定三电平脉冲，不代表 REDD、稳态 THD、别名、频响或音乐素材盲听。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | saturation |
| mode | redd-tg-compander |
| main_controls | mode,input,output,compander,mix,bass,treble |
| risk_flags | loudness-bias,sibilance,noise,low-mid-buildup |
| validation | harmonics,level-match,latency,artifacts |

## 来源

- [[sources/音乐制作/插件资料/Waves/Abbey Road Saturator资料|Abbey Road Saturator 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]
- [[projects/p1-plugin-knowledge-base/validation/reports/edb2c31ffd45--Waves-Abbey-Road-Saturator|默认 TG L3 验证]]

## 开放问题

- REDD 与 TG 在等响、相同峰值输入下的谐波阶次、压缩曲线和短响应差异是多少？
- Compander、crossover 与 Pre/Post EQ 各自对 49-sample 延迟和频响的贡献是否变化？
