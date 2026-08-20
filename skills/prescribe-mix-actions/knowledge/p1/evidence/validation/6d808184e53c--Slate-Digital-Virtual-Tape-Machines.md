---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: 6d808184e53c
product: Virtual Tape Machines
evidence_level: L3
test_id: multitone-tape-machine-speed
---

# Slate Digital Virtual Tape Machines：默认 30 ips 与 15 ips 单变量验证

## 结论

本机 Slate Digital Virtual Tape Machines VST3 已在 Ableton Live 11.3.43 中真实加载。实例默认主面板为 2-inch 16-track、FG456、30 ips、Normal Bias、Input/Output 0.00 dB、Ungrouped；Advanced 页面实见 Global Calibration -15.0 dB、Noise Reduction -24.0 dB、Wow & Flutter 25%、Bass Alignment 0.00 dB。宿主设备栏报告 `Latency: 1882 samples (39.2 ms)`。

同一 12 秒双单声道十音夹具分别导出旁路、默认 30 ips 与仅把 Speed 改为 15 ips 的变体。30 ips 相对旁路 RMS +1.552950 dB、峰值 +3.019170 dB；55 Hz +3.150 dB，220–1760 Hz约 +1.35 至 +1.44 dB，7.04 kHz -0.33 dB，12/16 kHz约 -0.69/-0.68 dB。它不是透明默认态：低频明显抬升、中频略增益、高频轻收。

15 ips 相对旁路 RMS +0.728860 dB、峰值 +2.404451 dB；55 Hz +1.39 dB，220–1760 Hz约 +0.78 至 +0.96 dB，7.04 kHz -0.39 dB，12/16 kHz -2.22/-4.84 dB。相对 30 ips，15 ips 的 55 Hz 低 1.76 dB、220–1760 Hz低约 0.45–0.62 dB、12 kHz低 1.58 dB、16 kHz低 4.23 dB。就这台 2-inch/FG456/Normal/0 dB 输入组合而言，15 ips 不是简单“低频更多”，而是整体电平稍低且最高频更明显滚降；速度选择必须在等响度后按频谱角色判断。

两个处理态都保持左右完全一致；L-R 残差约 -141.49 dBFS。30/15 ips 的 20 Hz–20 kHz 非输入音调能量比分别为 -14.75/-12.35 dB，包含建模噪声、Wow/Flutter 频谱裙、非线性产物和独立 Triangular dither，不能解释为纯 THD。全段相关最佳偏移分别为 436/1308 samples，但周期多音与频率相关相位会产生多个相关峰；这些数值只描述波形整体相似度，不是插件 PDC。实时补偿依据仍是宿主报告的 1882 samples。

## 固定状态与量化

- 插件：Slate Digital Virtual Tape Machines，VST3；文件系统记录产品族版本 1.1.11.1 / 1.2.1.1，界面未暴露本次实际加载文件的精确版本。
- 默认主面板：Process On、Ungrouped、Input 0.00 dB、Output 0.00 dB、Bias Normal、Machine 2-inch 16-track、Tape FG456、Speed 30 ips。
- Advanced：Global Calibration -15.0 dB、Groups 1–8 相对 +0.0 dB、Noise Reduction -24.0 dB、Wow & Flutter 25%、Bass Alignment 0.00 dB、Hiss Automute 开、Default Group Ungrouped。
- 单变量：只把 Speed 从 30 ips 改为 15 ips；Machine、Tape、Bias、Input/Output 与 Advanced 均不变。
- 导出：Master、32.1.1–40.1.1、12 s、48 kHz/24-bit WAV、Normalize 关闭、Triangular dither。
- 工程快照：`validation/host/snapshots/0072a637f389--FabFilter-Saturn-2 Project/6d808184e53c--Slate-Digital-Virtual-Tape-Machines.als`。

| 全局指标 | 默认 30 ips vs 旁路 | 15 ips vs 旁路 | 15 vs 30 ips |
|---|---:|---:|---:|
| RMS 电平差 | +1.552950 dB | +0.728860 dB | -0.824133 dB |
| 峰值差 | +3.019170 dB | +2.404451 dB | -0.614719 dB |
| 直接相关 | 0.666529948239 | 0.661080269017 | 0.837354224890 |
| 最佳相关偏移 | 436 samples | 1308 samples | -3492 samples |
| 最佳相关 | 0.797338019958 | 0.743072791103 | 0.868916577084 |
| 残差 RMS | -23.605505 dBFS | -23.251972 dBFS | -25.294177 dBFS |
| 非输入音调能量比 | -14.747090 dB | -12.349507 dB | -12.329583 dB |

| 频率 | 30 ips vs 旁路 | 15 ips vs 旁路 | 15 vs 30 ips |
|---:|---:|---:|---:|
| 55 Hz | +3.15 dB | +1.39 dB | -1.76 dB |
| 110 Hz | +1.81 dB | +0.83 dB | -0.98 dB |
| 220 Hz | +1.44 dB | +0.82 dB | -0.62 dB |
| 440 Hz | +1.41 dB | +0.91 dB | -0.51 dB |
| 880 Hz | +1.41 dB | +0.96 dB | -0.45 dB |
| 1.76 kHz | +1.35 dB | +0.78 dB | -0.57 dB |
| 3.52 kHz | +0.84 dB | +0.76 dB | -0.09 dB |
| 7.04 kHz | -0.33 dB | -0.39 dB | -0.09 dB |
| 12 kHz | -0.69 dB | -2.22 dB | -1.58 dB |
| 16 kHz | -0.68 dB | -4.84 dB | -4.23 dB |

## 操作观察与工作流

- 主唱链先把 VTM 当会改变频响、平均电平、峰值和相位的处理器，而不是“自动模拟胶水”。默认 30 ips 已比旁路高约 1.55 dB RMS，比较前必须用 Output 回配 Active RMS。
- 官方建议可从把 Input 推到失真刚明显再回约 0.5 dB开始；实际混音仍应固定 Calibration、Machine/Tape/Speed/Bias，只移动 Input，再以 Output 等响。VU 由 Calibration 与输入共同决定，不是峰值表。
- 2-inch/FG456/30 ips/Normal 是本机默认，不代表“干净基线”。较干净试验可改 FG9 或降低 Input，但必须重新测，因为 FG9 约多 3 dB headroom。
- 15 ips 在本轮主要表现为更强高频滚降，而非更大的 55 Hz；若目标是厚度，先等响检查 80–300 Hz、1–4 kHz清晰度和 8–16 kHz，再决定是否保留。
- Group 只给同用途实例；Global Calibration 与 Advanced 全局状态需在会话开始记录。Input/Output Link 只是界面联动，自动化仍应分别确认。
- 现代清晰主唱不宜默认关闭 Noise Reduction 或提高 Wow & Flutter。默认 25% 已是官方“调校机器”量级；Hiss Automute 只在无输入时静音建模磁带嘶声。
- 官方人声链示例是 De-esser → VTM → EQ → VCC，并建议 2-inch、FG456、30 ips、High Bias；这是一条可测试起点，不是对所有主唱的固定模板。

## 边界与未验证项

- 本轮只覆盖本机可达 VST3、2-inch/FG456/Normal/Input 0 dB、30/15 ips；未量化 1/2-inch、FG9、High/Low Bias、Input 驱动曲线、Noise/Wow/Bass/Calibration/Group 单变量、VST2、其它采样率、CPU、自动化或连续人声等响盲听。
- 十个输入音调多为倍频关系，不能从非输入音调能量分离具体谐波阶次；该指标也混有 dither、建模噪声和调制裙带。
- 周期多音的全段相关偏移不等于固定延迟；要验证 PDC 后瞬态起音与群延迟，应另做脉冲/扫频。
- 官方 1.2.6.0 发行说明修复了异常低频噪声/失真，并列出 Ableton 复制 Clip 时 Bias 自动化的已知问题；本机记录版本更旧，因此新版修复不得外推到当前实例。

## 证据

- 旁路 SHA-256：`022b3014616a4f0c41c900922e68b2c6ed565a8885bc2cb45e661b1a75cb91f0`。
- 默认 30 ips SHA-256：`109f153c2c704431b9f4b8156768ef75b88f6a34f3a3531776cf69de6ed510c1`。
- 15 ips SHA-256：`8640a0f37c11c03fa8d1ed77a94304dad95202a5fe2c4baca92d44df5ec9cd8f`。
- 工程快照 SHA-256：`56746eb05901ea41fe08daf205a898ac01827df32970675cf1ab122ef1677236`。
- 量化：`validation/results/6d808184e53c--multitone-tape-machine.json`。
- 测量脚本：`validation/scripts/analyze_tape_machine.py`。
