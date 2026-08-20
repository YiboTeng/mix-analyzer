---
type: source-note
status: active
created: 2026-08-20
updated: 2026-08-20
vendor: "FabFilter"
product: "Pro-C 2"
tags:
  - music-production
  - plugin-source
---

# Pro-C 2 资料

- 对应知识卡：[[notes/音乐制作/插件/FabFilter/Pro-C 2|Pro-C 2]]
- 本机版本范围：2.1.7.0
- 访问日期：2026-08-20

## 来源记录

### FabFilter Pro-C 2 Manual

- 类型：official-manual
- URL：https://www.fabfilter.com/help/ffproc2-manual.pdf
- 版本适用：Pro-C 2；本机 2.1.7.0
- 可信度：high
- 支持的事实：v2 Style、完整控制、侧链、Lookahead、Hold、OS 与并行。

### FabFilter releases Pro-C 2

- 类型：official-release
- URL：https://www.fabfilter.com/press/1440572940/fabfilter-releases-fabfilter-pro-c-2-compressor-plug-in
- 版本适用：v2 功能边界
- 可信度：high
- 支持的事实：八 Style、20 ms Lookahead、500 ms Hold、4x OS 与 Sidechain EQ。

### 本机 Ableton Live 11.3.43 实测

- 类型：local-host-measurement
- 版本适用：FabFilter Pro-C 2 2.1.7.0，VST3 Stereo
- 证据：[[projects/p1-plugin-knowledge-base/validation/reports/a3005d9763bc--FabFilter-Pro-C-2|Pro-C 2 L3 验证]]
- 结果文件：`projects/p1-plugin-knowledge-base/validation/results/a3005d9763bc--dynamics-compressor-lookahead.json`
- 支持的事实：本机默认参数、默认 Auto Gain 回补、五档局部传递曲线、Attack 0.255→75.19 ms 的实际音频差异、0 samples 宿主观察，以及 Ableton Lookahead 暴露值未传播到插件 UI/DSP 的集成异常。

## 证据边界

- 官方资料用于确认功能和控制语义；本机 L3 只覆盖 Default Setting/Clean、默认 Auto Gain On、Attack 0.255→75.19 ms、UI Lookahead Off 与一次失败的 Ableton Lookahead 映射探针。
- `Lookahead 20 ms` 文件名记录实验意图，不代表内部参数已生效；插件 UI 仍为 Off，音频与默认在约 -141.48 dBFS 处空差，因此不得引用为 Lookahead DSP 或延迟结论。
- 当前安装版本早于 Pro-C 3；Character、Auto Threshold、32x OS 等 v3 功能不得倒灌。其它七种 Style、Auto Gain Off、真实 UI Lookahead、OS、外部侧链、Stereo Link/M/S 和 Studio One 尚未验证。

## 反向链接

- [[projects/P1 插件适配知识库]]
- [[notes/音乐制作/插件/FabFilter/Pro-C 2|Pro-C 2]]
