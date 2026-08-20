---
type: source-note
status: active
created: 2026-08-20
updated: 2026-08-20
vendor: "Waves"
product: "Vocal Bender"
tags:
  - music-production
  - plugin-source
---

# Vocal Bender 资料

- 对应知识卡：[[notes/音乐制作/插件/Waves/Vocal Bender|Vocal Bender]]
- 本机版本范围：12.7.0.209
- 访问日期：2026-08-20

## 来源记录

### Vocal Bender 产品页

- 类型：official-product
- URL：https://www.waves.com/plugins/vocal-bender
- 版本适用：V12–V17；本机 V12
- 可信度：high
- 支持的事实：实时 Pitch/Formant、zero latency 和适用风格。

### Vocal Bender User Guide

- 类型：official-manual
- URL：https://assets.wavescdn.com/pdf/plugins/vocal-bender.pdf
- 版本适用：Vocal Bender 用户指南
- 可信度：high
- 支持的事实：Flatten、调制器与控制语义。

## 证据边界

- 官方资料用于确认功能和控制语义；本机 S4 已确认 `Vocal Bender Stereo` V12、0 samples PDC、默认界面与 -12 st 命令精度。
- 本地固定人声实测为 -1198.808 cents（目标 -1200，误差 1.192 cents）；默认脉冲的局部峰值偏移为 0/0/1 samples，但整段最佳相关偏移为 105 samples。后者是算法时间纹理，不是固定 PDC。
- 当前安装版本可能早于在线文档；任何新版专属功能在未回读本机界面前不得写成已验证。
- S4 报告：[[projects/p1-plugin-knowledge-base/validation/reports/06fad1aad9d8--Waves-Vocal-Bender|Vocal Bender L3 验证]]。

## 反向链接

- [[projects/P1 插件适配知识库]]
