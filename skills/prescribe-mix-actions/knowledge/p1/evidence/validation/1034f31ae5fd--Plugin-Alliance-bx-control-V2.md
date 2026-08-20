---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: 1034f31ae5fd
product: bx_control V2
evidence_level: L3
test_id: bx-control-ms-utility-v1
---

# Plugin Alliance bx_control V2：M/S 工具与 Mono Maker 验证

## 结论

本机 `bx_control V2` VST3 已在 Ableton Live 11.3.43 中真实加载。默认状态为 Input Gain 0.0 dB、Balance/Pan M/Pan S 居中、Mono Maker Off、Stereo Width 100%，输入/输出均为 L/R，L/R Flip、Phase Reverse、Solo 与 Solo in Place 均关闭；宿主状态栏报告 `Latency: 0 samples`。

默认状态与同选区旁路渲染的直接相关和最佳延迟相关均为 1.0，最佳整数延迟 0 samples，RMS 电平差 0.0 dB；独立 24-bit 三角抖动下残差 RMS -141.487198 dBFS，支持默认路径为透明、零固定延迟。Width=0% 时 Mid 完全保持，Side 降至 -147.503431 dBFS，L/R 相关 0.999999999999，证明该控制确实把 Side 收至 Mono，而不是生成新声像。

`spatial_correlation_48k.wav` 只有约 440 Hz 主能量。Mono Maker=117 Hz 对它几乎不动：Side 仅 -0.021483 dB、Mid +0.002611 dB，相当于“高于截止频率”的控制组。为验证功能端点，再将 Mono Maker 调到 5.82 kHz，使整段夹具位于阈值以下：整体 Side 相对旁路降低 45.257409 dB，L/R 相关升至 0.999955940103；这证明阈值以下 Side 会被强烈收束。5.82 kHz 是实验极限，不是混音建议。

## 固定状态与量化

- 组件：`bx_control V2` VST3；本机文件系统同时记录 2.0.0.0、2.10.0.0、2.3.0.0，GUI 未显示本次实例精确小版本。
- 输入：`spatial_correlation_48k.wav`；导出 Master、48 kHz/24-bit WAV、Normalize 关闭、Triangular dither。
- Ableton 自动把 10 s 夹具 Warp 为 12 s；所有条件使用完全相同的 7.2.2–15.2.2 选区，因此配对差分有效。
- 快照：`validation/host/snapshots/0072a637f389--FabFilter-Saturn-2 Project/1034f31ae5fd--Plugin-Alliance-bx_control-V2.als`，保存状态为 Width 100%、Mono Maker 117 Hz，其余默认。

| 条件 | L/R 相关 | Mid RMS dBFS | Side RMS dBFS | Side/Mid dB | Mono Fold Delta dB |
|---|---:|---:|---:|---:|---:|
| Bypass | 0.1232910412 | -22.002936 | -23.073945 | -1.071009 | -2.507727 |
| Default 100% | 0.1232910412 | -22.002936 | -23.073945 | -1.071009 | -2.507727 |
| Width 0% | 0.999999999999 | -22.002936 | -147.503431 | -125.500495 | -0.000000 |
| Mono Maker 117 Hz | 约 0.13 | -22.000325 | -23.095428 | -1.095103 | 约 -2.50 |
| Mono Maker 5.82 kHz | 0.999955940103 | -21.793568 | -68.331354 | -46.537786 | -0.000096 |

## 操作观察与工作流

- `Stereo Width` 是 Side 增益控制：100% 为基线，0% 为 Mono，官方范围可到 400%。它不能给原本 Mono 的主唱创造 Side。
- `Mono Maker` 应用于已有 Stereo 内容：先从 60–120 Hz 试，再在 Solo S、相关表、Mono 与扬声器/耳机之间核对。阈值太高会把可听宽度主体一并收窄。
- `Solo M/S/L/R` 是诊断状态，不应遗留在导出；`Solo in Place` 改变监听定位语义，也应在交付前复位。
- L/R↔M/S 编解码必须成对使用；常规轨保持 L/R in/out。只有明确要让中间插件分别处理 M 与 S 时，才用两个 bx_control 包住链路。
- 作为主唱工作流，适合放在 Doubler/MicroShift/PS22 返回或 Backing Vocal Bus 末端做收束和诊断；主唱干声中心通常只监测，不靠它制造宽度。

## 边界与未验证项

- 本轮只验证一个 VST3 实例、48 kHz、默认、Width 0%、Mono Maker 117 Hz 与 5.82 kHz；未测 130/200/400% Width、自动化、VST2、其它采样率、CPU 或所有 Solo/Matrix 组合。
- 夹具主能量约 440 Hz，因此 117 Hz 结果只证明“高于阈值基本不动”，不等于低频扫频或 60–200 Hz 补偿曲线验证。
- 极限 Mono Maker 仍有约 -68.33 dBFS Side，且微移调段局部相关会被极低电平残差主导；整体相关接近 1 才是本轮端点判断依据。
- 未完成人声/总线等响盲听；L3 覆盖主要默认传输、Width 端点、Mono Maker 阈值内外行为与零 PDC，不代表穷尽全部功能。

## 证据

- 默认中性结果：`validation/results/1034f31ae5fd--spatial-default-neutral.json`。
- M/S 功能结果：`validation/results/1034f31ae5fd--spatial-ms-utility.json`。
- 分析脚本：`validation/scripts/analyze_neutral.py`、`validation/scripts/analyze_ms_utility.py`。
- 快照 SHA-256：`2e029ffb99e7d11efb14b8465823cd8ecbbe769476aef5a9af68fbf8c1820838`。
- 官方产品页：https://www.plugin-alliance.com/products/bx_control-v2
- 官方手册：https://files.plugin-alliance.com/products/bx_control_v2/bx_control_v2_manual.pdf
