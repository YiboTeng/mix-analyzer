---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: efa4ad9005f3
product: ValhallaPlate
evidence_level: L3
test_id: impulse-default-wet-vs-shared-bypass
---

# ValhallaPlate 1.6.3：默认 Chrome 全湿脉冲验证

## 结论

本机 VST3 1.6.3 在 Ableton Live 11.3.43 临时宿主中，以默认 Chrome、Mix 100%、Predelay 0 ms、Decay 3.0 s、Size/Width 100% 把近似纯 Mid 脉冲变成宽立体声板式尾部。首脉冲检测起音 21.229 ms、拟合 T60 2.4174 s、相关系数 0.027008。Predelay 为 0 不等于算法输出瞬时出现；默认尾部也会跨过 2 s 的下一个脉冲。

## 固定条件

- 输入：`validation/fixtures/impulse_train_48k.wav`；对照复用同一工程和区间的 `a0c159c0ffd1--impulse--bypass.wav`。
- 宿主/工程：Ableton Live 11.3.43；`validation/host/snapshots/efa4ad9005f3--ValhallaPlate.als`。
- 插件：ValhallaPlate 1.6.3 VST3；Chrome；Mix 100%；Predelay 0 ms；Decay 3.0 s；Size 100%；Width 100%；LowFreq 700 Hz/LowGain 0 dB；HighFreq 10 kHz/HighGain 0 dB；Mod 0.50 Hz/Depth 0%。
- 渲染：Master，起点 2.1.1，长度 4.0.0（160 BPM 下 6 s），48 kHz、24-bit WAV、Triangular dither。

## 量化

| 指标 | 默认全湿 | 共享旁通 | 解释 |
|---|---:|---:|---|
| Peak | -26.8535 dBFS | -1.9383 dBFS | 未做听感等响，不比较主观响度。 |
| RMS | -59.0523 dBFS | -54.8054 dBFS | 只记录输出条件。 |
| Correlation | 0.027008 | 1.000000 | 默认板式生成大量 Side。 |
| Side/Mid | -0.2356 dB | -92.7012 dB | Mono Fold-down 必须复核。 |
| 首脉冲 onset | 21.229 ms | 0 ms | 算法建立时间可测。 |
| 首脉冲拟合 T60 | 2.4174 s | 不适用 | 50 ms 窗、峰值下 5–35 dB 拟合。 |

后两段 onset 约 0.917 ms，是上一尾音跨入下一分析段，不代表独立脉冲的真实起音。三次 T60 为 2.4174/2.4077/2.4078 s；最后尾部受 6 s 渲染窗截断。

## 使用动作与副作用

- 用作 Stereo Aux 时保持 Mix 100%，以 Send 控制量；默认 3 s 尾部对连续 Rap 主唱通常过长，应先按句间缩 Decay。
- 100% Width 的相关系数接近 0，能获得宽而密的板式空间，但 Mono 下可能明显改变尾部；主唱干声核心保持 Mid。
- Predelay=0 仍有约 21 ms 算法建立，不应只按旋钮数值判断首字分离。
- 本次未做听感等响；onset、衰减斜率和相关性不依赖整体增益，Peak/RMS 不用于音质优劣结论。

## 证据与限制

- 渲染 SHA-256：`bd14c8e3c9cf1c5f39f8e0956da3065f1fcfbea03f225bac1fff8865653c5cba`。
- 结果：`validation/results/efa4ad9005f3--impulse--default-wet.json`；共享旁通：`validation/results/a0c159c0ffd1--impulse--bypass.json`。
- 只验证默认 Chrome；不外推其他 Mode、调制、宿主 PDC 或 Studio One 兼容性。
