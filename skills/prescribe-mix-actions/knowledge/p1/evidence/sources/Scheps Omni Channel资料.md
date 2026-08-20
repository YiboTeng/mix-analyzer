---
type: source-note
status: active
created: 2026-08-20
updated: 2026-08-20
vendor: "Waves"
product: "Scheps Omni Channel"
tags:
  - music-production
  - plugin-source
---

# Scheps Omni Channel 资料

- 对应知识卡：[[notes/音乐制作/插件/Waves/Scheps Omni Channel|Scheps Omni Channel]]
- 本机版本范围：12.7.0.209
- 访问日期：2026-08-20

## 来源记录

### Waves Scheps Omni Channel User Guide

- 类型：official-manual
- URL：https://www.waves.com/1lib/pdf/plugins/scheps-omni-channel.pdf
- 版本适用：原版 Omni Channel；与本机 v12 对应
- 可信度：high
- 支持的事实：五模块、原版三压缩模式、控制范围、重排和路由。

### Scheps Omni Channel In-Depth Tutorial

- 类型：official-tutorial
- URL：https://www.waves.com/scheps-omni-channel-in-depth-tutorial
- 版本适用：原版官方工作流
- 可信度：medium
- 支持的事实：主唱 4:1 慢 Attack/快 Release、Pre/EQ/DS² 与模块顺序实验。

## 证据边界

- 官方资料用于确认功能和控制语义；参数起点与信号链位置属于条件化工作流，必须在 S4 实测。
- 当前安装版本可能早于在线文档；任何新版专属功能在未回读本机界面前不得写成已验证。

## 本机宿主观察与量化证据

- 本机真实加载：Waves `Scheps Omni Channel Stereo` V12（文件系统 12.7.0.209），Ableton Live 11.3.43 / VST3 Stereo / 48 kHz；确认是原版而非 Omni Channel 2。
- UI 回读：`A: Full Reset` 的 Pre Drive 0、Saturation Off、Gate -144 dB、DS² -48/-48 dB、EQ 四段 0 dB、VCA Compressor -50 dB/1:1、Input/Output 0 dB、Limiter Off；可见 PRE/GATE/DS²/EQ/COMP、Insert、模块重排与 Stereo/M/S/Duo 控制。
- 量化结果：`Full Reset` 对旁路 0 samples、相关 1.0、互差 RMS -141.483962 dBFS；HEAVY Drive 0 相对 Full Reset +0.504912 dB；HEAVY Drive 0→3.2 再 +0.105300 dB，非输入音调能量比增加 7.220305 dB。
- 证据：[[projects/p1-plugin-knowledge-base/validation/reports/a094b33b301c--Waves-Scheps-Omni-Channel|L3 验证报告]]、`validation/results/a094b33b301c--channel-strip-pre-saturation.json`、`validation/scripts/analyze_channel_strip.py`、任务工程快照。
- 边界：只覆盖原版 V12 VST3 Stereo、一个低电平多音夹具、Full Reset 与 HEAVY Drive 0/3.2；不证明 Omni Channel 2、其它模块、谐波阶数、THD/aliasing、其它格式/采样率或听感优劣。

## 反向链接

- [[projects/P1 插件适配知识库]]
