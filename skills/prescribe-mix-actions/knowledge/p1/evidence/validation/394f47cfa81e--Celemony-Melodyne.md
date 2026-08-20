---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: 394f47cfa81e
product: Melodyne
evidence_level: L3
test_id: melodyne-transfer-pitch-center100
---

# Celemony Melodyne：Transfer 与 Pitch Center 100% 验证

## 结论

本机 Celemony Melodyne 5.4.1 VST3 已在 Ableton Live 11.3.43 / 48 kHz 中真实加载，界面右上角明确显示 `melodyne studio`，解决了 Edition 开放问题。由于 Ableton 11 不提供本轮所需 ARA 路径，本测试走 VST3 实时 Transfer；宿主报告 `0 samples` 延迟。

空 Transfer 状态对共享旁路在 21–37、37.15–41.70、45–57、60–72 秒四个区域均为 0.000 dB 电平差、相关约 1.0，互差 RMS 约 -141.48 至 -141.50 dBFS。这确认“插件已插入但未转入/未编辑”在当前实例中是中性控制，不能由此推断已经完成 Detection 或编辑。

实际从宿主约 27.1.1 起实时 Transfer 约 7 秒后，Melodyne 生成 13 个可见音符 Blob 并自动识别 `D Minor`。选中全部转入音符，只应用 Correct Pitch Macro 的 `Pitch Center 100%`，保持 `Pitch Drift 0%`，且 `Snap to chord scale` 关闭。处理差异被 50 ms 窗定位在导出 37.15–41.65 秒，共 72 个窗；此前与 45 秒之后仍是约 -141.48 dBFS 的空差，证明编辑只回放于 Transfer 区域。

当前片段本来已经接近各自音符中心，宏编辑的实际音高位移很小：85 个共同有声帧的位移中位约 +0.732 cents，P10/P90 为 -3.615/+3.767 cents；帧间移动中位由 8.450 降到 8.105 cents。外部最近半音偏差中位反而由 5.929 变为 6.141 cents，±10 cents 比例由 91.8% 降到 77.6%。这不是“Pitch Center 100% 失效”，而是一个重要边界：Melodyne 以检测到的音符对象和感知中心为编辑单位，外部短窗 F0 与其内部中心不等价；片段已近中心时，100% 宏也不保证第三方逐帧最近半音统计更漂亮，更不保证音乐上更正确。

## 固定状态与量化

- 插件：Celemony Melodyne Studio 5.4.1，VST3。
- 宿主：Ableton Live 11.3.43；160 BPM；48 kHz；报告延迟 0 samples。
- Transfer：宿主约 27.1.1 至 31.3.4；可见 13 个音符 Blob；自动检测 D Minor。
- 选择：Edit → Select All，作用于全部已转入音符。
- 宏：Edit → Macros → Correct Pitch；Pitch Center 100%；Pitch Drift 0%；Snap to chord scale Off。
- 导出：Master、2.1.1 起始、48.0.0 长度、72 s、48 kHz/24-bit WAV、Normalize Off、Triangular dither。
- 工程快照：`validation/host/snapshots/0072a637f389--FabFilter-Saturn-2 Project/394f47cfa81e--Celemony-Melodyne.als`。

| 中性控制区域 | 空 Transfer vs 旁路电平差 | 相关 | 互差 RMS |
|---|---:|---:|---:|
| 21–37 s | 0.000 dB | 0.999999999999 | -141.480 dBFS |
| 37.15–41.70 s | 0.000 dB | 0.999999999998 | -141.503 dBFS |
| 45–57 s | 0.000 dB | 1.000000000000 | -141.484 dBFS |
| 60–72 s | 0.000 dB | 1.000000000000 | -141.491 dBFS |

| 37.2–41.65 s F0 指标 | 空 Transfer | Pitch Center 100% |
|---|---:|---:|
| 共同有声帧 | 85 | 85 |
| 最近半音绝对偏差中位 | 5.929 cents | 6.141 cents |
| ±5 cents 比例 | 40.0% | 38.8% |
| ±10 cents 比例 | 91.8% | 77.6% |
| 帧间移动中位 | 8.450 cents | 8.105 cents |

编辑区整体 RMS 相对空 Transfer 为 -0.147 dB，但相关降至 -0.125，说明小音高位移足以产生大相位/波形差，不能把负相关误写成响度或品质下降。最大 50 ms 残差为 -19.440 dBFS；区域之外则回到 dither 级空差。

## 操作观察与工作流

- 当前本机 Edition 是 Studio，界面提供 Transfer、Correct Pitch、Quantize Time、Note Leveling、音高/时间/分隔等工具；但项目仍应按真正用到的工具记证，不因 Edition 高就默认所有算法已验证。
- 非 ARA 宿主必须先点击 Transfer，再从所需片段起实时播放；只插入插件不会自动生成 Blob。Transfer 前应先完成 Comping 和源修复，以免后续片段替换让缓存内容失配。
- Detection 后先检查 Algorithm、Note Assignment、分隔与调性。自动显示 D Minor 只是检测建议；本轮未勾选 Snap to chord scale，因此宏没有强制到 D 小调音级。
- Correct Pitch Macro 把 Pitch Center 与 Pitch Drift 分开。自然主唱先从 Center 30–60%、Drift 10–40% 试起，再按音符回退；本轮 100% 只为端点验证。
- 100% 宏不等于“所有 F0 帧贴网格”。内部音符中心、颤音/滑音、分隔和外部短窗 F0 是不同层级；应听音符重心、语气和过渡，而不是只追求逐帧 cents 更小。
- 要处理长音下坠，先单独增加 Drift；不要用 Pitch Center 代替 Drift，也不要把 Pitch Modulation/颤音一并归零。
- 保存含 Transfer 数据的 DAW 工程或 Melodyne 文档，并保留未编辑版本；算法重检或片段结构改变前先做版本快照。

## 边界与未验证项

- L3 只覆盖本机 Studio 5.4.1 VST3、Ableton 实时 Transfer、一个约 4.5 秒固定人声尾段和 Pitch Center 100% / Drift 0% / 不按音阶吸附。
- 自动 D Minor 没有作为编辑目标；结果不验证歌曲调性、旋律正确性或主观自然度。
- 外部 F0 使用 120 ms 自相关窗与 40 ms hop；它不能复现 Melodyne 的音符分隔、感知中心或内部 Detection。
- 未验证 ARA、Studio One、Melodic/Universal/Polyphonic 算法切换、Note Assignment、手工分隔、Pitch Drift/Modulation、Formant、Amplitude、Sibilant、Timing、Quantize Time、Note Leveling、Bounce 一致性、其它格式/采样率或盲听。

## 证据

- 旁路 SHA-256：`38a74287a951ad7a62a6abeb219aa91afdd0e4f2abde062b972361851e0de16f`。
- 空 Transfer SHA-256：`e0d395a9127c8504b1378f46ad68715b312d3002ce359f58e84cafe0e96b5a06`。
- Pitch Center 100% SHA-256：`e21aca8a3cf0d5dc32b8d4e61c0c0ec1539ff340276db49d756772916d87dc59`。
- 工程快照 SHA-256：`5ce9e3091be2630f53ca65cd79a313b121bc2061341ca5269592e2f2ea7c8f53`。
- 量化：`validation/results/394f47cfa81e--melodyne-transfer-pitch-center100.json`。
- 测量脚本：`validation/scripts/analyze_melodyne_transfer.py`。

