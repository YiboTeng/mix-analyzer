---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: b6c750f3ccec
product: Vocal Rider
evidence_level: L3
test_id: composite-vocal-rider-fast-slow
---

# Waves Vocal Rider：Fast / Slow 自动骑乘验证

## 结论

本机 Waves `Vocal Rider Stereo` 12.7.0.209 VST3 已在 Ableton Live 11.3.43、48 kHz 中真实加载，宿主报告 `0 samples` 延迟。默认预设的 Target 居中、Vocal/Music Sensitivity 均为 0、Range 为 -6 至 +6 dB、Rider/Output 为 0、Automation Off，且未连接音乐侧链。

独立渲染确认默认开关状态就是 Slow：默认与显式 Slow 的相关为 `0.999999991007`、互差 RMS `-100.019 dBFS`；默认与显式 Fast 的互差 RMS 则为 `-43.135 dBFS`。因此 Fast/Slow 的差异不是界面标签推测，而由音频复现交叉确认。

默认 Slow 在 1037 个有效 50 ms 窗中有 993 个变化超过 0.05 dB；增益变化分布为最小 -5.782、P10 -1.054、中位 +0.226、P90 +2.036、最大 +6.000 dB，并有 39 个窗口命中 +6 dB 上限。它不是“只对真实人声透明工作”：稳定多音 +0.145 dB、空间夹具 -0.545 dB、动态阶梯整体 -3.325 dB，说明默认 Sensitivity 0 与宽 Range 会对非人声材料持续动作。

动态阶梯区的输入 P90-P10 为 24.000 dB，默认 Slow 输出降为 17.221 dB，收窄 6.779 dB；这证明 Rider 能重排宏观电平，但不等于压缩器的固定 Ratio。显式 Fast 在全程序的相邻 50 ms 增益变化 P90 为 0.242 dB，高于 Slow 的 0.155 dB；固定人声整体电平也由 Slow 的 +0.322 dB变为 Fast 的 -0.855 dB。Fast 会更快追逐节目，既可能抓到密集弱词，也更容易形成音节级动作。

## 固定状态与量化

- 插件：Waves `Vocal Rider Stereo` 12.7.0.209，VST3 Stereo。
- 宿主：Ableton Live 11.3.43；160 BPM；48 kHz；报告延迟 0 samples。
- 默认可见状态：Default Preset；Target 居中；Vocal/Music Sensitivity 0；Range -6/+6 dB；Rider/Output 0；Automation Off。
- 路由：Music Sidechain 未连接，Ableton Device Sidechain 显示 No Input。
- 单变量：只切换 Fast/Slow；其余可见控制保持不变。
- 导出：Master、2.1.1 起始、48.0.0 长度、72 s、48 kHz/24-bit WAV、Normalize Off、Triangular dither。
- 工程快照：`validation/host/snapshots/0072a637f389--FabFilter-Saturn-2 Project/b6c750f3ccec--Waves-Vocal-Rider.als`，最终保存为 Slow。

| 区域 | 默认 Slow vs 旁路 | Fast vs 旁路 | 显式 Slow vs 旁路 |
|---|---:|---:|---:|
| 0–6 s 稀疏事件 | +0.000 dB | +0.000 dB | +0.000 dB |
| 8–20 s 稳定多音 | +0.145 dB | +0.046 dB | +0.145 dB |
| 21–42 s 固定人声 | +0.323 dB | -0.855 dB | +0.322 dB |
| 45–57 s 空间夹具 | -0.545 dB | -1.816 dB | -0.545 dB |
| 60–72 s 动态阶梯 | -3.325 dB | -3.558 dB | -3.325 dB |

| 全程序 50 ms 有效窗 | 默认 Slow | Fast | 显式 Slow |
|---|---:|---:|---:|
| 有效窗数 | 1037 | 1037 | 1037 |
| 变化 ≥0.05 dB | 993 | 984 | 993 |
| 增益最小 / 中位 / 最大 | -5.782 / +0.226 / +6.000 dB | -5.795 / -0.900 / +6.000 dB | -5.782 / +0.223 / +6.000 dB |
| 命中 +5.9 dB 以上 | 39 | 28 | 39 |
| 相邻变化 P90 | 0.155 dB | 0.242 dB | 0.155 dB |

动态阶梯区 Fast 的输出电平跨度为 17.352 dB，相对输入收窄 6.649 dB；Slow 为 17.221 dB，收窄 6.780 dB。两种模式都到达可见 Range 边界，因此这里的差异受 Target、检测历史和限制范围共同影响，不能反推隐藏 Attack/Release 常数。

## 操作观察与工作流

- 先用 Clip Gain/Comping 修复明显错句，再加载 Rider；Target 的目标是让正常句的 Rider 围绕 0 小幅运动，不是把它当输出推子。
- 初次使用先把 Range 收窄到约 `-3/+2 dB`。本轮默认 ±6 dB 在 39 个有效窗命中正上限，足以把宽默认范围认定为风险端点，而非推荐预设。
- 用 Activity/Rider 表同时校准 Vocal Sensitivity；默认 0 仍对稳定多音和空间夹具动作，真实工程必须检查呼吸、底噪、伴奏泄漏和效果尾是否被误认。
- 自然长句先用 Slow；密集 Rap 或快速弱词再试 Fast。Fast 的相邻动作 P90 更高，选择它后需专听字头抽吸、词间回摆和下游压缩器是否追逐。
- Music Sensitivity 只有在 Instrumental Bus 已正确送入 Sidechain 后才有意义。本轮未接侧链，不能用这些结果解释 Mix-relative riding。
- 若需要可编辑自动化，先在副本中 Write，再切 Read 并检查 DAW 曲线；Automation Off 的本轮只验证实时 DSP，不验证 Ableton/Studio One 写回。
- 放在压缩器前可缩小送入压缩器的宏动态；放在后面则可能与已有 Volume Automation、总线压缩和限制器互相追逐。两种位置都要等响 A/B。

## 边界与未验证项

- L3 只覆盖本机普通 Stereo VST3 12.7.0.209、48 kHz、一个复合编排、默认 Target/Sensitivity/Range、无音乐侧链及 Fast/Slow。
- 50 ms 窗电平变化描述结果轨迹，不等于插件内部 Rider Fader 自动化数据，也不能给出隐藏检测阈值、Attack/Release 或固定 Ratio。
- 固定人声只有一个来源且无逐词标签；未验证不同歌手、语言、呼吸/噪声类别的检测准确率或主观自然度。
- 未验证音乐侧链、Target/Sensitivity/Range/Idle 单变量、Automation Write/Read、压缩器前后等响盲听、Mono/Live/VST2、其它版本/采样率、CPU 或 Studio One 专属行为。

## 证据

- 旁路 SHA-256：`38a74287a951ad7a62a6abeb219aa91afdd0e4f2abde062b972361851e0de16f`。
- 默认 SHA-256：`e5c58fe1d1d62c65520f9483f29a0109dda50bf31f813e37512575bc3f9149bd`。
- Fast SHA-256：`c6fade63a3e2079330b46412d0499cdce4b7cdd228f84336ebf29059fc6e58d8`。
- Slow SHA-256：`81abef80e87ad232b5d376aeeabd1e2edc42a8e2789b9d9e481b0e86a748759f`。
- 工程快照 SHA-256：`780b3b2e44fc99fe9004dc7fba714665346fcb98220757eb730d73d57f2c6e4f`。
- 量化：`validation/results/b6c750f3ccec--composite-vocal-rider-fast-slow.json`。
- 测量脚本：`validation/scripts/analyze_level_rider.py`。
