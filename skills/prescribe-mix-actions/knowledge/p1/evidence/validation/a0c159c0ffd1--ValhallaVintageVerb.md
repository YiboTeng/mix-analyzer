---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: a0c159c0ffd1
product: ValhallaVintageVerb
evidence_level: L3
test_id: impulse-default-wet-vs-bypass
---

# ValhallaVintageVerb 2.2.0：默认全湿脉冲验证

## 结论

在本机 VST3 2.2.0、Ableton Live 11.3.43 临时宿主中，默认全湿 Concert Hall 设置把三个单声道脉冲变成宽立体声衰减尾音。第一个脉冲相对输入检测到 25.562 ms 起音，拟合 T60 为 4.5925 s；这与界面中的 Predelay 20 ms、Decay 4.00 s 方向一致。全湿输出相关系数为 0.010724，旁通对照为 1.0，说明该设置会显著增加侧向能量；Mono Fold-down 前应单独检查尾部损失与音色变化。

## 测试身份

| 字段 | 值 |
|---|---|
| Family ID | `a0c159c0ffd1` |
| Test ID | `impulse-default-wet-vs-bypass` |
| 宿主 | Ableton Live 11.3.43（Studio One 6 可执行文件当前缺失，故不作 Studio One 专属结论） |
| 插件 | ValhallaVintageVerb 2.2.0 VST3 |
| 工程 | `validation/host/P1-S4-Validation Project/P1-S4-Validation.als` |
| 输入 | `validation/fixtures/impulse_train_48k.wav`，48 kHz、16-bit、Stereo |
| 渲染 | Master，起点 2.1.1，长度 4.0.0（160 BPM 下 6 s），48 kHz、24-bit WAV、Triangular dither |

## 固定插件状态

- Mix 100%，Predelay 20 ms，Decay 4.00 s，Mode Concert Hall，Color 1970s。
- HighFreq 6000 Hz，HighShelf -24 dB，BassFreq 700 Hz，BassMult 1.50x。
- Size 100%，Attack 50%，Early/Late Diffusion 100%。
- Mod Rate 2.53 Hz，Mod Depth 38%，HighCut 8000 Hz，LowCut 10 Hz。

## 量化结果

| 指标 | 全湿 | 旁通 | 解释边界 |
|---|---:|---:|---|
| Peak | -23.4295 dBFS | -1.9383 dBFS | 全湿与干声不应按峰值直接比较主观响度。 |
| RMS | -60.3040 dBFS | -54.8054 dBFS | 本次未做听感等响；只用于记录输出条件。 |
| Stereo correlation | 0.010724 | 1.000000 | 对整体增益缩放不敏感，可支持“宽化”判断。 |
| Side/Mid | -0.0931 dB | -92.7012 dB | 干输入近似纯 Mid；全湿产生显著 Side。 |
| 首脉冲 onset | 25.562 ms | 0 ms | 阈值为各段峰值下 60 dB；含算法建立时间。 |
| 首脉冲拟合 T60 | 4.5925 s | 不适用 | 50 ms 窗；只拟合峰值下 5–35 dB 段。 |

后两个湿声段的 onset 为 0 ms，是前一脉冲尾音跨入下一分析段所致，不能解释为预延迟消失。三次拟合 T60 分别为 4.5925、4.6430、4.4416 s，受尾音重叠和最后 4 s 尾部截断影响。

## 主行为、代价与使用动作

- 主行为：在 100% Wet 辅助轨上生成约 4.6 s 的密集立体声尾音，并以约 25.6 ms 的可测延迟把首个脉冲与尾部拉开。
- 代价：侧向能量显著增加；默认长尾会跨过下一次 2 s 间隔脉冲，连续主唱上容易遮盖下一句。
- 动作：把 Mix 锁为 100% 放在 Stereo Aux；先按句间空间缩短 Decay，再用 Predelay 保留首字；回到 Mono 检查尾部是否塌陷。
- 停止条件：下一关键重音前尾部已明显下降，且 Mono 下空间没有不成比例消失。

## 响度匹配声明

本次脉冲试验没有做听感等响，原因是核心指标为 onset、衰减斜率与相关性；它们不依赖整体输出增益。Peak/RMS 差异只作为渲染条件记录，不用于声称“更好听”或“更响”。后续若比较 Mode、Color 或调制强度，必须在湿声 RMS 匹配后盲听。

## 可复现证据

- 全湿渲染 SHA-256：`a578acc91ef1b72ffad2e608c4e19b8b9b2c7d9b52ee1e64c3c14e7fb4095121`
- 旁通渲染 SHA-256：`0123293a90801b37bbabd43e59492875ca3c319b9420363a653a2629903f92fc`
- 量化结果：`validation/results/a0c159c0ffd1--impulse--default-wet.json`、`validation/results/a0c159c0ffd1--impulse--bypass.json`
- 分析器：`validation/scripts/analyze_render.py`

## 限制

- 这是 Ableton 临时宿主结果，不证明 Studio One 扫描、PDC、自动化或预设兼容性。
- 导出使用 Triangular dither；对 -60 dBFS 附近的噪声底有影响。
- 6 s 渲染会截断最后一个长尾，不能把第三段拟合当作完整 RT60。
- 只验证一个默认 Concert Hall 状态，不外推到其他 Mode、Color 或版本。
