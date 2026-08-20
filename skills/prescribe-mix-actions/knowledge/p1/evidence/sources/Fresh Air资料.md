---
type: source-note
status: active
created: 2026-08-20
updated: 2026-08-20
vendor: "Slate Digital"
product: "Fresh Air"
tags:
  - music-production
  - plugin-source
---

# Fresh Air 资料

- 对应知识卡：[[notes/音乐制作/插件/Slate Digital/Fresh Air|Fresh Air]]
- 本机版本范围：1.1.1
- 访问日期：2026-08-20

## 来源记录

### Slate Digital Fresh Air

- 类型：official-doc
- URL：https://docs.slatedigital.com/FreshAir/Fresh%20Air.html
- 版本适用：Fresh Air 核心控制；本机 1.1.1
- 可信度：high
- 支持的事实：Mid/High Air、Link、Trim、Bypass、Peak/RMS 表和动态并行处理定位。

## 证据边界

- 官方资料用于确认功能和控制语义；参数起点与信号链位置属于条件化工作流，必须在 S4 实测。
- 当前安装版本可能早于在线文档；任何新版专属功能在未回读本机界面前不得写成已验证。

## 本机验证补充

- 2026-08-20 在 Ableton Live 11.3.43 / 48 kHz 中加载本机 1.1.1 VST3；界面回读与官方核心控制一致，宿主报告 0 samples。
- 单变量复合夹具结果：Mid 21% 的稳定多音整体约 +0.651 dB；High 21% 约 +0.911 dB，12/16 kHz 约 +1.57/+2.34 dB，并把峰值推至约 0 dBFS。
- 这些数值只适用于当前安装态、设置与夹具；不能把旋钮百分比写成固定 dB，也不能由谐波相关多音断言 THD、混叠或所有动态行为。
- 验证报告：[[projects/p1-plugin-knowledge-base/validation/reports/0c0769036773--Slate-Digital-Fresh-Air|Fresh Air L3 验证]]。

## 反向链接

- [[projects/P1 插件适配知识库]]
