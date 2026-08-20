---
type: source-note
status: active
created: 2026-08-20
updated: 2026-08-20
vendor: "Waves"
product: "Abbey Road Saturator"
tags:
  - music-production
  - plugin-source
---

# Abbey Road Saturator 资料

- 对应知识卡：[[notes/音乐制作/插件/Waves/Abbey Road Saturator|Abbey Road Saturator]]
- 本机版本范围：12.7.0.209
- 访问日期：2026-08-20

## 来源记录

### Abbey Road Saturator 产品页

- 类型：official-product
- URL：https://www.waves.com/plugins/abbey-road-saturator
- 版本适用：Waves 产品家族；本机 V12 需实测
- 可信度：high
- 支持的事实：REDD/TG、TG12321 compansion、饱和与失真定位。

### Waves Plugin Latency

- 类型：official-support
- URL：https://www.waves.com/support/tech-specs/plugin-latency
- 版本适用：当前官方延迟表；本机版本需复核
- 可信度：high
- 支持的事实：44.1/48 kHz 49 samples 延迟声明。

## 证据边界

- 官方资料用于确认功能和控制语义；参数起点与信号链位置属于条件化工作流，必须在 S4 实测。
- 当前安装版本可能早于在线文档；任何新版专属功能在未回读本机界面前不得写成已验证。

## S4 本机验证补充

- 本机 12.7.0.209 `Abbey Road Saturator Stereo` VST3 默认实例在 Ableton Live 11.3.43 / 48 kHz 报告 `49 samples (1.02 ms)`，与官方延迟表一致。
- 默认 `A: Default Preset` 实际观察到 TG、Saturator Mix 100%、Pre/Post EQ 开启；对三档脉冲的峰值增益为 -9.305/-4.866/+0.237 dB，呈 9.542 dB 电平依赖范围。
- 量化和工程证据：[[projects/p1-plugin-knowledge-base/validation/reports/edb2c31ffd45--Waves-Abbey-Road-Saturator|默认 TG L3 验证]]。
- 边界：脉冲结果只支持默认瞬态传输、延迟与短响应判断；不支持 REDD/TG 稳态谐波优劣、THD、别名、频响或音乐偏好结论。

## 反向链接

- [[projects/P1 插件适配知识库]]
