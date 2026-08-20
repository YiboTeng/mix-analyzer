---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: 877f2fb079d2
product: Abbey Road Chambers
evidence_level: L3
test_id: impulse-default-vs-shared-bypass
---

# Abbey Road Chambers 12.7：默认房间链脉冲验证

## 结论

本机 Abbey Road Chambers Stereo V12 默认预设在 Ableton Live 11.3.43 中产生明显晚于输入的短房间尾部：三次脉冲 onset 均为 121.0 ms，拟合 T60 为 1.0170/1.0094/1.0075 s。Correlation 0.372473、Side/Mid -3.3682 dB，比三款算法混响默认状态更集中，但仍生成显著 Stereo Side。

## 固定状态与量化

- A: Default Preset；KM53s / Classic；Chamber 2；Time X=1；B&W speaker / Wall；S.T.E.E.D Feedback Off、Drive 0、Mod 0；Filters to Chamber 保持 Flat/Gain 0；Reverb 与 Dry/Wet 保持默认界面顶部状态。
- 输入/对照：固定 `impulse_train_48k.wav` 与共享旁通；渲染 Master、6 s、48 kHz/24-bit WAV、Triangular dither。
- 工程快照：`validation/host/snapshots/877f2fb079d2--Abbey-Road-Chambers.als`。

| 指标 | Chambers 默认 | 共享旁通 |
|---|---:|---:|
| Peak | -33.8426 dBFS | -1.9383 dBFS |
| RMS | -62.3647 dBFS | -54.8054 dBFS |
| Correlation | 0.372473 | 1.000000 |
| Side/Mid | -3.3682 dB | -92.7012 dB |
| Onset | 121.0 ms | 0 ms |
| 拟合 T60 | 1.0170 s | 不适用 |

## 使用动作与副作用

- 约 121 ms 的默认起音足以与字头拉开，但对快节奏主唱可能听成独立房间反射；先用 Delay/Time X 与句速对齐。
- 约 1 s 尾部比默认 2.5–4 s 算法混响更紧，适合主唱黏合；同时 121 ms 起音可能让空间显得离散。
- Correlation 0.37、Side/Mid -3.37 dB 表明空间仍较宽，但中心成分更多；Mono Fold-down 仍需检查。
- 未做听感等响，Peak/RMS 不用于音质优劣判断；onset 也不能解释为插件 PDC。
- 只验证默认 KM53s/Classic/Chamber 2/B&W Wall 链，不外推其他话筒、房间、音箱或 S.T.E.E.D 反馈。

## 证据

- 渲染 SHA-256：`e711d8528c815b22975a1f275c5d24c182956f5a6ddf6e839433b55e6d4c4456`。
- 量化：`validation/results/877f2fb079d2--impulse--default.json`；共享旁通：`validation/results/a0c159c0ffd1--impulse--bypass.json`。
