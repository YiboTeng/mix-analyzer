---
type: source-note
status: active
created: 2026-08-20
updated: 2026-08-20
vendor: "Slate Digital"
product: "Virtual Tape Machines"
tags:
  - music-production
  - plugin-source
---

# Virtual Tape Machines 资料

- 对应知识卡：[[notes/音乐制作/插件/Slate Digital/Virtual Tape Machines|Virtual Tape Machines]]
- 本机文件系统版本：1.1.11.1 | 1.2.1.1
- 访问日期：2026-08-20

## 来源记录

### Virtual Tape Machines Manual

- 类型：official-manual
- URL：https://docs.slatedigital.com/VTM/Virtual_Tape_Machines.html
- 版本适用：VTM 控制、机器/磁带/速度/Bias、Advanced、Groups 与全局状态
- 可信度：high
- 支持事实：2-inch=A827、1/2-inch=A80 RC；FG456/FG9；15/30 ips；Bias；Input/Output；VU/Calibration；Noise Reduction、Wow & Flutter、Hiss Automute、Bass Alignment、Groups；Global 与 Session 状态边界。

### Virtual Tape Machines FAQ

- 类型：official-support
- URL：https://support.slatedigital.com/hc/en-us/articles/115011299328-Virtual-Tape-Machines
- 版本适用：VTM 核心与支持边界
- 可信度：high
- 支持事实：FG456 +6、FG9/GP9 +9 与约 3 dB headroom 差；预期插件延迟；默认无 factory presets；输入驱动工作流。

### Slate Digital Virtual Tape Machines

- 类型：official-product
- URL：https://slatedigital.com/virtual-tape-machines/
- 版本适用：当前产品定位与两机器/两速度工作流
- 可信度：medium
- 支持事实：两机器、两磁带速度、录音/混音用途与主唱链案例。

### VTM 1.2.6.0 Release Notes

- 类型：official-release-notes
- URL：https://support.slatedigital.com/hc/en-us/articles/33303375763347-VTM-1-2-6-0-Release-Notes
- 版本适用：1.2.6.0，不等同本机旧版本
- 可信度：high
- 支持事实：修复异常低频噪声/失真；Ableton 复制 Clip 时 Bias 自动化的已知问题。

## 本机观察

- Ableton Live 11.3.43 成功加载 VST3；默认主面板为 2-inch 16-track、FG456、30 ips、Normal Bias、Input/Output 0.00 dB、Ungrouped。
- Advanced 实见 Global Calibration -15.0 dB、Noise Reduction -24.0 dB、Wow & Flutter 25%、Bass Alignment 0.00 dB、Hiss Automute On、Groups 1–8 +0.0 dB、Default Group Ungrouped。
- 宿主设备栏报告 1882 samples / 39.2 ms。
- 受控测量见 `validation/reports/6d808184e53c--Slate-Digital-Virtual-Tape-Machines.md` 与 `validation/results/6d808184e53c--multitone-tape-machine.json`。

## 证据边界

- 在线文档支持功能语义；具体默认数值与 30/15 ips 结果由本机 VST3 观察和固定渲染支持。
- 本机文件系统有两个旧版本记录，插件界面未显示实际加载 minor version；不得把 1.2.6.0 修复写成本机已具备。
- 参数起点是条件化工作流，不是官方保证或普适最佳值；必须在等响、固定链序和单变量条件下复测。
