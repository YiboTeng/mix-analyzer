---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: 7a146380912e
product: soothe2
evidence_level: L3
test_id: composite-resonance-soft-hard
---

# oeksound soothe2：默认 Soft 与 Hard 单变量验证

## 结论

本机 oeksound soothe2 `1.1.2` VST3 Stereo 已在 Ableton Live 11.3.43、48 kHz 中真实加载。默认工厂态回读为 Soft、Depth `3.0`、Sharpness `4.6`、Selectivity `3.6`、Attack `1.0`、Release 快、Mix `100%`、Trim `0 dB`、Delta Off、L/R、Link `100%`、Balance 居中、Normal `1x`。插件内联帮助将 Soft 描述为更透明、更易调且更适合动态素材；Hard 描述为更可调、可推得更重且更随素材电平反应。

本轮保持所有其它旋钮不变，只切换 Soft/Hard。72 秒复合夹具中，默认 Soft 对 8–20 秒稳定十音多频整体降低 `2.198920 dB`；Hard 降低 `2.645424 dB`，即比 Soft 再低 `0.446504 dB`。这证明默认 Depth 3.0 并非中性，且 Hard 在稳定多音上更强。

十频点传输并非静态 EQ 曲线：Soft 在 220 Hz 降低 `4.995652 dB`，440 Hz–16 kHz 约降低 `1.847–2.148 dB`，而 55/110 Hz 分别为 `+1.608/+2.114 dB`；Hard 在 220 Hz 为 `-6.173849 dB`，440 Hz–16 kHz 约 `-2.183` 至 `-2.582 dB`，55/110 Hz 为 `+2.158/+2.631 dB`。这些结果反映当前自适应滤波、十音同时输入与默认敏感度轮廓的交互，不能把正值写成固定低频 Boost，也不能从合成稳态直接外推真实人声音色。

66–72 秒动态区域中，Soft 整体 `-0.043151 dB`，50 ms 窗中位数 `-0.036680 dB`、最深 `-0.047474 dB`；Hard 整体 `-0.076788 dB`，中位数 `-0.057575 dB`、最深 `-0.087516 dB`，68 个活跃窗有 53 个达到至少 `0.05 dB` 衰减。方向与 Hard 更随电平反应的界面说明一致，但绝对量很小，只能作为本夹具的模式差异证据。

0–6 秒三个高于 -70 dBFS 的稀疏短事件中，Soft/Hard 均与旁路约 `0.00001 dB` 内一致。它是一项有用的负结果：默认状态没有对任意短峰无差别动作；同时也说明当前固定事件不是充分的移动共振/齿音语料，不能据此评判 soothe2 的真实语音检测准确率。

宿主对 Soft 与 Hard 均报告 `2048 samples / 42.7 ms`，独立导出由 Ableton PDC 对齐。这个延迟足以影响实时录音监听，工作流上应在低延迟监听链中旁路，编辑/混音时依赖 PDC，并在切换 Quality/Resolution 后重新查看宿主延迟。

## 可执行工作流

- 先加载 Soft，保持频率轮廓只覆盖可疑区域；Depth 从明显过量回退到最坏音素刚稳定，不能把旋钮数值当实际 dB。
- 用 Delta 只检查被移除内容是否主要为短暂共振；若能听清完整元音、胸腔或字头，优先降低 Depth/Sharpness/Selectivity 或缩窄轮廓。
- Hard 不是“更高品质”模式。本轮相同 Depth 下稳定多音多削约 `0.447 dB`，动态区域也更随电平变化；切换 Hard 后必须重新校准 Depth，并做等响旁路。
- 稳定十音出现 55/110 Hz 正传输，说明自适应处理的频点变化不能孤立理解。处理低中频时应同时看整个轮廓与上下文，避免只追一个分析器读数。
- 默认 2048 samples 延迟不适合无 PDC 的实时录音路径；离线 Quality/Resolution 改动必须另记设置与延迟，不能假定只改变 CPU。

## 边界与未验证项

- L3 只覆盖本机 VST3 Stereo 1.1.2、48 kHz、默认频率轮廓与 Depth/Sharpness/Selectivity/Attack/Release、Soft/Hard 单变量和默认 Normal 1x。
- 固定多音和动态阶梯是确定性合成夹具，不是标注语音；未测移动元音共振、口哨式齿音、语言/歌手差异、自然度、lisp 风险或等响盲听。
- 未测 Depth/Sharpness/Selectivity/Attack/Release 扫描、Delta/Mix/Trim、轮廓绘制、外部侧链、M/S、Link/Balance、Mono、其它 Quality/Resolution、离线切换、CPU、其它采样率/格式/版本。
- 十频点幅度是同时输入多音下的稳态结果，不等同单独正弦扫频或线性时不变频响；55/110 Hz 正值不得表述为固定增益功能。

## 证据

- 旁路 SHA-256：`38a74287a951ad7a62a6abeb219aa91afdd0e4f2abde062b972361851e0de16f`。
- Soft 默认 SHA-256：`5fd9888948b06317819910da2f61dcfcaa3192f79d4f56fce62155c7dcd70166`。
- Hard 默认 SHA-256：`4b235f748327b9e88e2280edfb7423c5a911c7043ac1efc4d49958b0d31aa00a`。
- 工程快照 SHA-256：`8f003799ff174adeda41440896d542e091a3018961ee4c6e0be3ee435d6879ff`。
- 量化：`validation/results/7a146380912e--composite-resonance-soft-hard.json`。
- 测量脚本：`validation/scripts/analyze_resonance_suppressor.py`。
