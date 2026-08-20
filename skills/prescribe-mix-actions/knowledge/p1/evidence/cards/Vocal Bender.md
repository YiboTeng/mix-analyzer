---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: 06fad1aad9d8
vendor: "Waves"
product: "Vocal Bender"
evidence_level: L3
validation_status: S4-host-validated-passed
batch: R01
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Vocal Bender

## 身份与版本

- 厂商：Waves
- 产品族：Vocal Bender
- Family ID：06fad1aad9d8
- 本机观测版本：12.7.0.209
- 格式：VST2 | VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：pitch-formant-creative
- 次能力方向：octave;formant;modulation
- 当前证据等级：L3
- 验证状态：S4-host-validated-passed

## 能做什么

- 实时独立改变 Pitch 与 Formant，适合低八度层、角色声线与短促自动化效果。
- 支持音高、包络、LFO 和音序调制，把静态移调扩展为节奏化人声设计。

## 不建议用来做什么

- 不要把极端移调当作透明校音。
- 不要在主唱核心上忽略辅音和低频伪影。

## 信号流位置

- 复制轨或并行 Aux 做创意层，主唱干声保持中心。
- 自动化前先清理爆破与口水音，避免检测被噪声驱动。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Pitch | 以半音改变音高。 | 低八度从 -12 st 起，按调性与伪影调整。 |
| Formant | 改变声道共振而不等同音高。 | 小步调整角色感，避免元音身份丢失。 |
| Flatten | 把输入音高收拢到固定中心。 | 只用于机器人/硬效果，不用于透明人声。 |
| Modulators | Pitch、Amplitude、LFO、Sequencer 驱动参数。 | 一次只启用一个调制源并控制深度。 |

## Gain Staging

移调层按 Active RMS 与主唱匹配后再设 Blend；低八度同时检查低频峰值和总线余量。

## 延迟、相位与过采样

官方产品页声明 zero latency；本机 Ableton 确认 0 samples PDC，但默认脉冲仍有明显时间扩散与电平变化。“零延迟”不等于时间域透明。

## Mono/Stereo

主唱核心保持 Mono/Mid；处理层可 Stereo，但低八度优先居中并检查相关性。

## 适用场景

- -12 st 低八度 Ad-lib。
- Formant 自动化的角色转换与句尾效果。

## 路由

- 复制主唱轨做 100% 效果层。
- 短句 Throw Aux 配合自动化。

## 参数起点

- Pitch -12 st、Formant 0 作为低八度起点。
- 角色声线从 Formant ±1–3 小步试。

## 调整目标

- 效果身份明确但咬字仍可辨。
- 低八度不吞掉贝斯与主唱基频。

## 调整时听什么

- 辅音颤动、元音塑料感、低频颗粒。
- 调制过深造成节奏失焦。

## 何时停止

- 效果层在 Solo 明显、混音中只提供角色或重量。
- 再提高 Blend 开始覆盖原唱。

## 常见失败

- 把 Formant 与 Pitch 当成同一控制。
- 低八度全频不高通且电平过高。

## 替代方案

- Little AlterBoy：经典 SoundToys 工作流但本轮 VST2 不可达。
- Auto-Tune Pro：实时校音而非角色移调。

## 专业案例与工作流线索

- 官方明确定位实时 Pitch/Formant 操作，并给出 hip-hop、pop、R&B 的创意人声用途。

## 已执行与剩余测试

- 已完成固定人声 -12 st、Formant 0 的音高命令验证，以及默认脉冲的 PDC、起音、相关和电平传输验证。
- 待补 +12 st、Formant ±3 单变量、Flatten、Fine、调制器、其它采样率、Mono/VST2 与连续人声盲听。

## 已测结果

- 实际加载 `Vocal Bender Stereo` V12（12.7.0.209）；默认 Pitch/Formant=0、Link 开、Flatten/Fine 关、Mix 100；Ableton 报告 0 samples 延迟。
- 关闭 Link、Pitch=-12 st、Formant=0 后，固定人声加权中位 F0 从 173.771698 Hz 到 86.945707 Hz；实测 -1198.808 cents，距目标仅 1.192 cents。
- 默认脉冲三次攻击峰值偏移 0/0/1 samples，但整段最佳相关偏移 105 samples / 2.1875 ms、最佳相关 0.693373；三档峰值增益 -5.256/-5.089/-4.805 dB。它没有固定 PDC 延迟，却不是中性旁通。
- 实用路径：复制轨/Aux 100% 效果，关闭 Link 后先定 Pitch，再小步调 Formant；低八度层高通、去齿、按 Active RMS 匹配，并持续检查辅音、低频遮蔽与 Mono。
- 完整报告：[[projects/p1-plugin-knowledge-base/validation/reports/06fad1aad9d8--Waves-Vocal-Bender|Vocal Bender L3 验证]]。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | pitch-formant |
| mode | realtime-creative |
| main_controls | pitch,formant,flatten,modulators |
| risk_flags | artifacts,low-end-mask,intelligibility,modulation-overuse |
| validation | pitch-cents,formant-spectrum,onset,artifacts |

## 来源

- [[sources/音乐制作/插件资料/Waves/Vocal Bender资料|Vocal Bender 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]

## 开放问题

- +12 st、Formant ±3、Flatten 与调制器在连续人声上的频谱、咬字、伪影和 Mono 折叠边界如何？
