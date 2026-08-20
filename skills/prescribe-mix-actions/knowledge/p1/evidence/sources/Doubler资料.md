---
type: source-note
status: active
created: 2026-08-20
updated: 2026-08-20
vendor: "Waves"
product: "Doubler"
tags:
  - music-production
  - plugin-source
---

# Doubler 资料

- 对应知识卡：[[notes/音乐制作/插件/Waves/Doubler|Doubler]]
- 本机版本范围：12.7.0.209
- 访问日期：2026-08-20

## 来源记录

### Waves Doubler Guide

- 类型：official-manual
- URL：https://www.waves.com/1lib/pdf/plugins/doubler.pdf
- 版本适用：Doubler 核心；本机 v12
- 可信度：high
- 支持的事实：Voice、Range、Align Direct、固有延迟、反馈和调制。

### Waves Doubler

- 类型：official-product
- URL：https://www.waves.com/plugins/doubler
- 版本适用：v12 可用与官方延迟表
- 可信度：medium
- 支持的事实：四声部功能与宿主延迟 0。

## 证据边界

- 官方资料用于确认功能和控制语义；参数起点与信号链位置属于条件化工作流，必须在 S4 实测。
- 当前安装版本可能早于在线文档；任何新版专属功能在未回读本机界面前不得写成已验证。

## S4 本机验证

- 本机 Waves 12.7.0.209 `Doubler4 Stereo` VST3 默认状态已完成固定脉冲、宿主延迟、Side/Mid 与 Mono 折叠实测。
- 宿主 PDC 为 0 samples，但 Voice 的算法固有延迟与显示 Delay 仍会形成毫秒级效果响应；两者不得混写。
- 证据：[[projects/p1-plugin-knowledge-base/validation/reports/4bceae9f0a6f--Waves-Doubler|Doubler L3 验证]]。

## 反向链接

- [[projects/P1 插件适配知识库]]
