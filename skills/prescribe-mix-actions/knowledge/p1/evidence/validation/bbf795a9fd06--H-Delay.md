---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: bbf795a9fd06
product: H-Delay
evidence_level: L3
test_id: impulse-host-dotted-eighth-wet
---

# H-Delay 12.7：默认 Host 同步延迟验证

## 结论

本机 H-Delay Stereo V12 在 Ableton Live 11.3.43、Host 160 BPM、默认 `1/8 D`、Dry/Wet 100 的固定脉冲测试中，三次首个湿声 Tap 分别出现在 280.938、280.854、281.438 ms。理论附点八分音符为 281.25 ms，三次误差分别为 -0.312、-0.396、+0.188 ms，证实默认 Host Sync 的时间语义。默认 Feedback 未产生检测阈值以上的后续重复，因此本测试不外推反馈衰减或自激行为。

## 固定状态与量化

- A: Default Preset；Host 160 BPM；Delay=`1/8 D`；Dry/Wet=100；Output=0；其余默认界面状态不变。
- 输入：固定 `impulse_train_48k.wav`；渲染 Master、6 s、48 kHz/24-bit WAV、Triangular dither。
- 工程快照：`validation/host/snapshots/bbf795a9fd06--H-Delay.als`。

| 指标 | 实测 |
|---|---:|
| 理论附点八分 Tap | 281.250 ms |
| Tap 1 / 2 / 3 | 280.938 / 280.854 / 281.438 ms |
| 最大绝对时间误差 | 0.396 ms |
| Peak | -7.5445 dBFS |
| RMS | -58.4475 dBFS |
| Correlation | 0.996975 |
| Side/Mid | -28.1963 dB |

## 使用动作与副作用

- 默认 `1/8 D` 在 160 BPM 约为 281 ms，适合切分感 Throw；它不是普通八分音符的 187.5 ms。看到 `D` 标记时必须按 0.75 个四分音符计算。
- 当前默认 Feedback 在本阈值下只出现一个 Tap，适合先建立单次节奏位置；需要连续重复时再逐步增加 Feedback，并为自动化回收设置明确终点。
- Correlation 0.997、Side/Mid -28.20 dB 表明该默认全湿 Tap 接近中心，而不是宽 Ping-Pong 结果；需要横向运动时应显式启用 Ping Pong 后重做 Mono 测试。
- 本次不测试 Analog、LoFi、Filters、Modulation、Phase、Ping Pong 或 Feedback>100%；这些参数的谐波、滤波、相消与自激风险不能由本渲染推断。
- 效果 Tap 的约 281 ms 不是插件 PDC。Waves 手册所列 Native 0-sample latency 与本次创作延迟应分开记录。

## 证据

- 渲染 SHA-256：`b36a029d57b3519bddda2f8130961ef8aa1e904bc223122858c64c2c41f78ee4`。
- 量化：`validation/results/bbf795a9fd06--impulse--host-eighth-wet.json`。
- 测量脚本：`validation/scripts/analyze_delay.py`。
