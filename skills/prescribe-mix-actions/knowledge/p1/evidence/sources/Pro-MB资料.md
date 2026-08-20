---
type: source-note
status: active
created: 2026-08-20
updated: 2026-08-20
vendor: "FabFilter"
product: "Pro-MB"
tags:
  - music-production
  - plugin-source
---

# Pro-MB 资料

- 对应知识卡：[[notes/音乐制作/插件/FabFilter/Pro-MB|Pro-MB]]
- 本机版本范围：1.2.8.0
- 访问日期：2026-08-20

## 来源记录

### FabFilter Pro-MB Basic Band Controls

- 类型：official-help
- URL：https://www.fabfilter.com/help/pro-mb/using/basicbandcontrols
- 版本适用：Pro-MB 1.x 核心行为
- 可信度：high
- 支持的事实：Threshold、Range、Dynamics Mode、时间、Lookahead 与零延迟条件。

### FabFilter Pro-MB Processing Mode

- 类型：official-help
- URL：https://www.fabfilter.com/help/pro-mb/using/processingmode
- 版本适用：Pro-MB 1.x
- 可信度：high
- 支持的事实：Dynamic/Linear/Minimum Phase 的相位、延迟和前振铃边界。

### FabFilter Pro-MB Oversampling

- 类型：official-help
- URL：https://www.fabfilter.com/help/pro-mb/using/oversampling
- 版本适用：Pro-MB 1.x
- 可信度：high
- 支持的事实：2x/4x 对混叠、相位响应、CPU 与延迟的影响。

## 证据边界

- 官方资料用于确认功能和控制语义；参数起点与信号链位置属于条件化工作流，必须在 S4 实测。
- 当前安装版本可能早于在线文档；任何新版专属功能在未回读本机界面前不得写成已验证。

## 本机 S4 证据

- 宿主：Ableton Live 11.3.43；格式：VST3 Stereo；采样率：48 kHz；文件系统版本：1.2.8.0。
- 默认回读：无频段、Dynamic Phase、Oversampling Off、全局 Lookahead On、Analyzer Pre+Post、Mix 100%、Output 0 dB；宿主延迟 960 samples / 20 ms，音频对共享旁路近似空差。
- 固定单频段：中心 1720.8 Hz、Compress、Threshold -32.10 dB、Range -6.00 dB、Ratio 4:1、Knee 24 dB、Attack/Release 20%、band Lookahead 1.000 ms。
- 全局 Lookahead On 对三个稀疏短事件产生约 -0.228/-0.148/-0.031 dB 变化；Off 时约 0 dB，宿主延迟同时由 960 samples 降为 0。
- 量化与边界：[[projects/p1-plugin-knowledge-base/validation/reports/a8c2063eb007--FabFilter-Pro-MB|Pro-MB L3 验证]]。

## 反向链接

- [[projects/P1 插件适配知识库]]
