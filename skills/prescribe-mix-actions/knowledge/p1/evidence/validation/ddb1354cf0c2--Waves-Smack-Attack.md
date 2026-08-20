---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: ddb1354cf0c2
product: Smack Attack
evidence_level: L3
test_id: dynamics-steps-smack-attack-envelope
---

# Waves Smack Attack：默认中性、Attack +100 与 Sustain -100 验证

## 结论

本机 Waves `Smack Attack Stereo` V12（文件系统版本 12.7.0.209）VST3 已在 Ableton Live 11.3.43、48 kHz 中真实加载。`A: Default Preset` 实见 Attack `0`、Sustain `0`、Output `0.0`、Guard `Off`，其余 Sensitivity、Shape、Duration 与 Mix 保持默认可见位置；设备栏报告 `Latency: 0 samples`。

默认态对旁路的五档稳态 RMS 与峰值差均为 `0 dB`，整段 RMS/峰值差也为 `0 dB`、直接相关 `1.0`，互差 RMS 约 `-141.478 dBFS`。因此本机默认 Attack 0/Sustain 0 可作为当前夹具、当前宿主导出的近似中性控制；这不证明所有隐藏状态、其它采样率或其它格式都严格位透明。

单独把 Attack 设为 `+100` 后，五档持续音仍增加 `+1.423` 至 `+1.470 dB`，说明在默认检测/形状/时长下，它并非只改变一个不可见的“第一采样点”。五个隔离瞬态的前 20 ms RMS 一致增加约 `+7.260 dB`，20–120 ms 主体增加约 `+9.884 dB`；样本峰值由约 `-2.854 dBFS` 推到 `0.0 dBFS`。由于 Guard 为 Off，本极值已经撞到数字满刻度，峰值只显示 `+2.854 dB` 并不代表真实请求增益只有这么多；这是削顶/失真风险证据，不是推荐起点。

单独把 Sustain 设为 `-100`、Attack 回到 `0` 后，五档持续音只降低约 `-0.130` 至 `-0.141 dB`，但五个隔离瞬态的 20–120 ms 主体 RMS 稳定降低约 `-7.156 dB`、该窗峰值降低约 `-6.233 dB`；前 20 ms 样本峰值保持不变，RMS 仅约 `-0.307 dB`。这清楚验证了当前状态下 Sustain 主要削短瞬态后的主体，而不是把字头峰值一起压掉。

整段 Attack +100 比默认高 `+1.961 dB RMS`、峰值到 `0.0 dBFS`、相关 `0.977742`；Sustain -100 比默认低 `-0.239 dB RMS`、峰值不变、相关 `0.997027`。实际人声工作流必须先用 Sensitivity 只抓目标辅音，再以小幅 Amount 调整，并用 Output 或后级 Trim 做等响 A/B；整段 RMS 很小的变化可能掩盖局部 6–10 dB 的包络改变。

## 固定状态与量化

- 插件：Waves `Smack Attack Stereo` V12，文件系统版本 12.7.0.209，VST3。
- 宿主：Ableton Live 11.3.43；160 BPM；48 kHz；设备栏报告 0 samples。
- 预设：`A: Default Preset`。
- 固定：Output `0.0`、Guard `Off`；Sensitivity、Attack/Sustain Shape、Duration 与 Mix 保持默认可见位置。
- 三态：旁路；Attack `0` / Sustain `0`；Attack `+100` / Sustain `0`；Attack `0` / Sustain `-100`。
- 导出：Master、42.1.1–50.1.1、12 s、48 kHz/24-bit WAV、Normalize Off、Triangular host dither。
- 夹具：`dynamics_steps_48k.wav`；Ableton 自动 Warp 为 160 BPM 下 8 bars/12 s。
- 工程快照：`validation/host/snapshots/0072a637f389--FabFilter-Saturn-2 Project/ddb1354cf0c2--Waves-Smack-Attack.als`。

| 输入峰值 | Attack +100 稳态 RMS 变化 | Attack +100 稳态峰值变化 | Sustain -100 稳态 RMS 变化 | Sustain -100 稳态峰值变化 |
|---:|---:|---:|---:|---:|
| -30 dBFS | +1.423 dB | +1.484 dB | -0.130 dB | 0.000 dB |
| -24 dBFS | +1.447 dB | +1.581 dB | -0.130 dB | 0.000 dB |
| -18 dBFS | +1.460 dB | +1.534 dB | -0.131 dB | 0.000 dB |
| -12 dBFS | +1.460 dB | +1.527 dB | -0.141 dB | 0.000 dB |
| -6 dBFS | +1.470 dB | +1.529 dB | -0.131 dB | 0.000 dB |

五个隔离瞬态的重复性很高：

| 单变量 | 前 20 ms RMS | 前 20 ms峰值 | 20–120 ms RMS | 20–120 ms峰值 | 0–300 ms事件 RMS |
|---|---:|---:|---:|---:|---:|
| Attack +100 | +7.260 dB | +2.854 dB（到 0 dBFS） | +9.884 dB | +9.901 dB | +7.262 dB |
| Sustain -100 | -0.307 dB | 0.000 dB | -7.156 dB | -6.233 dB | -0.309 dB |

## 操作观察与工作流

- 第一顺序是 Sensitivity，而不是 Amount：从低处上推到只让目标鼓点、词头或拨弦触发；如果噪声、齿音和呼吸也持续触发，先修检测范围。
- Attack 用于字头存在感或软化。官方 Amount 全范围很大，本轮 +100 已让隔离瞬态撞到 0 dBFS；人声从约 ±5–15 的小步开始比直接推极值安全得多。
- Sustain 用于主体/尾部长度。本轮 -100 保留了前 20 ms 峰值，却把 20–120 ms 主体削去约 7.16 dB；需要更短、更干时可小减，但过量会让元音、房间与尾字突然抽空。
- Shape 决定变化曲线，Duration 决定作用时间。比较时一次只改一个，并保留同一 Sensitivity；否则“量变”和“时间窗变了”无法区分。
- 先 100% Wet 诊断检测和包络，再回 Mix 做并行；最后以 Output 或后级 Trim 等响。不能把更大峰值或更响的短窗自动当成更清楚。
- Guard Off 时必须独立看峰值。本轮 Attack +100 到 0 dBFS；实际链路应预留 Headroom，必要时减 Amount/Output，而不是依赖下游限制器掩盖失真。
- 对只有少数问题字头的人声，Clip Gain/自动化通常比整轨瞬态塑形更可控；Smack Attack 更适合连续、可检测且方向一致的包络目标。

## 边界与未验证项

- L3 仅覆盖本机 V12 VST3 Stereo 12.7.0.209、48 kHz、A: Default Preset、Guard Off、Output 0，以及 Attack 0→+100 与 Sustain 0→-100 两个独立极值。
- Ableton 导出使用 PDC；0 samples 是宿主设备栏报告，不是从 WAV 反推所有内部检测时序。
- 持续 220 Hz 阶梯不是语音；它只说明默认检测状态在该夹具上仍造成约 +1.45 dB 稳态变化，不能直接解释为对元音的固定增益。
- Attack +100 已撞到 0 dBFS，量化峰值受数字上限约束；未做 Guard Limit/Clip 对比，也未把极值当音乐推荐。
- 未验证 Sensitivity 阈值/误检率、三种 Attack/Sustain Shape、Duration 全范围、Mix 并行相位、Guard Limit/Clip、Stereo Link、Mono、VST2、其它采样率/版本、自动化、CPU 或真实人声等响盲听。
- 本轮没有建立辅音、爆破、齿音和元音的标注集；“人声更清楚/更自然”仍需后续素材盲听，不能由合成夹具替代。

## 证据

- 旁路 SHA-256：`842e7218300943a883da6cfb223e99c32384de0fe0e68a2244e88fc59909a0d0`。
- 默认 SHA-256：`30eeae3e3c26898e96932de31c1165f30460074e14bb7944b0ecb7d6e85a59c1`。
- Attack +100 SHA-256：`ea9dec803aa4804af6b14468b8d7f0f2add33268a1ac7d0f54a0fa5c470321e8`。
- Sustain -100 SHA-256：`9ea15b039dd93795504a52d0f72ba51bd8e3c1a375bbe49c08e860bdccdba477`。
- 工程快照 SHA-256：`4bf0c02a03cd6e342a8f9e4db5af9bfbe845b438a1a3f27b0063e04743d5f167`。
- 量化：`validation/results/ddb1354cf0c2--dynamics-smack-attack.json`。
- 测量脚本：`validation/scripts/analyze_transient_shaper.py`。
