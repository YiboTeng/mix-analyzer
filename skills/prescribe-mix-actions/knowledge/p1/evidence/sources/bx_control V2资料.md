---
type: source-note
status: active
created: 2026-08-20
updated: 2026-08-20
vendor: "Plugin Alliance"
product: "bx_control V2"
tags:
  - music-production
  - plugin-source
---

# bx_control V2 资料

- 对应知识卡：[[notes/音乐制作/插件/Plugin Alliance/bx_control V2|bx_control V2]]
- 本机文件系统版本范围：2.0.0.0 | 2.10.0.0 | 2.3.0.0
- 本轮宿主组件：VST3；GUI 未显示精确小版本
- 访问日期：2026-08-20

## 来源记录

### Plugin Alliance bx_control V2 产品页

- 类型：official-product
- URL：https://www.plugin-alliance.com/products/bx_control-v2
- 版本适用：当前产品族；页面当前安装器为 2.16.1，本机是旧版集合
- 可信度：high
- 支持的事实：M/S Matrix、Mono Maker、0–400% Stereo Width、L/R/M/S Solo、Peak/RMS Meter、全自动化、参数直接输入与 latency-free M/S 定位。

### bx_control V2 Manual

- 类型：official-manual
- URL：https://files.plugin-alliance.com/products/bx_control_v2/bx_control_v2_manual.pdf
- 版本适用：V2 控制体系；本机 GUI 控件名与布局一致
- 可信度：high
- 支持的事实：L/R↔M/S 输入输出矩阵、L/R Flip、独立 Phase Reverse、Solo/Solo in Place、Balance/Pan M/Pan S、Mono Maker 20 Hz–22 kHz、Width 0–400%、Meter 与成对 Encoder/Decoder 工作流。

## 本机证据

- Ableton Live 11.3.43 成功载入 `bx_control V2` VST3，默认 Input Gain 0 dB、Balance/Pan M/Pan S 居中、Mono Maker Off、Width 100%，其余监测/路由开关关闭。
- 宿主报告 0 samples；默认与旁路 0 samples、0.0 dB、相关 1.0，残差 RMS -141.487198 dBFS。
- Width 0%：Mid 不变，Side -147.503431 dBFS，L/R 相关 0.999999999999。
- Mono Maker 117 Hz 对 440 Hz 夹具 Side 只变化 -0.021483 dB；5.82 kHz 使整体 Side 相对旁路降低 45.257409 dB。
- 结果：`validation/results/1034f31ae5fd--spatial-default-neutral.json`、`validation/results/1034f31ae5fd--spatial-ms-utility.json`。

## 证据边界

- 官方产品页当前 2.16.1 不能证明本机实例精确小版本；本轮只把功能语义与本机 GUI/渲染交叉确认。
- 117 Hz 条件的夹具主能量约 440 Hz，所以它是阈值外控制组，不是低频扫频。
- 5.82 kHz 是为把 440 Hz 整段纳入阈值以下而设的功能端点，不是工作流推荐。
- Width 110–130% 与 Mono Maker 60–120 Hz 是条件化起点，仍需按来源、Correlation、Solo S 与 Mono Fold 回听。

## 反向链接

- [[projects/P1 插件适配知识库]]
- [[projects/p1-plugin-knowledge-base/validation/reports/1034f31ae5fd--Plugin-Alliance-bx-control-V2|bx_control V2 L3 验证]]
