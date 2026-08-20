---
type: source-note
status: active
created: 2026-08-19
updated: 2026-08-20
vendor: "FabFilter"
product: "Pro-G"
tags:
  - music-production
  - plugin-source
---

# Pro-G 资料

- 对应知识卡：[[notes/音乐制作/插件/FabFilter/Pro-G|Pro-G]]
- 本机版本范围：1.3.1.0
- 访问日期：2026-08-20

## 来源记录

### FabFilter Pro-G Manual

- 类型：official-manual
- URL：https://www.fabfilter.com/help/ffprog-manual.pdf
- 版本适用：Pro-G 当前手册；本机 1.3.1.0 需界面回读
- 可信度：high
- 支持的事实：核心动态、Style、Lookahead、过采样、侧链、M/S、格式与延迟关系。

### Pro-G Dynamic Controls

- 类型：official-help
- URL：https://www.fabfilter.com/help/pro-g/using/dynamiccontrols
- 版本适用：Pro-G
- 可信度：high
- 支持的事实：Threshold、Ratio、Range 的精确定义。

### Pro-G Time Controls

- 类型：official-help
- URL：https://www.fabfilter.com/help/pro-g/using/timecontrols
- 版本适用：Pro-G
- 可信度：high
- 支持的事实：Attack、Release、Hold、Lookahead 与延迟/过采样说明。

## 证据边界

- 官方资料用于确认功能和控制语义；参数起点与信号链位置属于条件化工作流，必须在 S4 实测。
- 当前安装版本可能早于在线文档；任何新版专属功能在未回读本机界面前不得写成已验证。

## S4 本机验证

- Ableton Live 11.3.43 / 48 kHz 中真实加载 Pro-G 1.3.1.0 VST3 Stereo；验证 Classic、内部侧链、Left/Right、OS Off 与固定 Threshold/Ratio/Range/Attack/Hold/Release。
- Lookahead Off 回读 0 samples；On 的界面值为 9.951 ms、宿主回读 480 samples / 10.0 ms。
- 零 Lookahead 对单样本脉冲列约 -11.748791 dB，接近 11.94 dB Range 地板；开启 Lookahead 后约 0 dB。稳定阶梯在两条件下均约 0 dB。
- 报告：[[projects/p1-plugin-knowledge-base/validation/reports/290814706035--FabFilter-Pro-G|Pro-G L3 验证]]；量化：`projects/p1-plugin-knowledge-base/validation/results/290814706035--composite-pro-g-vocal-expander-lookahead.json`。
- 所有其它链上设备在最终两份渲染中停用；一次隔离审计发现 Melodyne 被重新启用后，污染渲染已被覆盖并重新分析，不作为证据保留。
- 本轮未验证其它 Style、外部侧链、侧链滤波、M/S、Stereo Link、MIDI Trigger、Oversampling、Mono、其它采样率或盲听。

## 反向链接

- [[projects/P1 插件适配知识库]]
