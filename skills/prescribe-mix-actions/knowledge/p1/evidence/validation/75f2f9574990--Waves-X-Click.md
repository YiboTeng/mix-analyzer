---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: 75f2f9574990
product: X-Click
evidence_level: L3
test_id: composite-xclick-audio-difference-stress
---

# Waves X-Click：Audio、Difference 与 50/70 压力验证

## 结论

本机 Waves X-Click Stereo 12.7.0.209 VST3 已在 Ableton Live 11.3.43 / 48 kHz 真实加载。默认 Threshold 0、Shape 50 的 Audio 输出相对旁路全段差约 0.0000000003 dB、相关 0.9999999999995，Difference 为 -144.49 dBFS；这组 Composite 没有被默认检测器认定为点击。

按手册 MCR 工作流起点设置 Threshold 50、Shape 70 后，插件几乎完全移除 0–6 秒脉冲列（-89.69 dB），而对固定人声整体电平仅 -0.00018 dB、但产生 -59.29 dBFS 残差。这证明检测对尖锐事件具有强选择性，同时也构成“可能把鼓、硬辅音或真实瞬态当点击”的风险边界。当前夹具没有人工标注的嘴部点击，因此本轮不声称实际 Mouth De-click 准确率。

## 固定状态与量化

- 插件：Waves `X-Click Stereo` 12.7.0.209 VST3。
- 宿主：Ableton Live 11.3.43；48 kHz。
- 宿主延迟：2624 samples（当前 Waves 延迟表/手册；不适合实时监听链）。
- 默认：Threshold 0、Shape 50、Audio；另导出 Difference。
- 压力：Threshold 50、Shape 70、Audio；这是手册 MCR 建议起点的受控边界，不是通用 Preset。
- 隔离：只启用 X-Click；此前链上设备全部停用。

| Composite 区域 | 默认 Audio vs Bypass | 50/70 Audio vs Bypass |
|---|---:|---:|
| 0–6 s 脉冲列 | +0.0000007 dB | -89.692 dB |
| 8–20 s 稳定多音 | +0.0000000 dB | -0.000407 dB |
| 21–42 s 固定人声 | -0.0000000 dB | -0.000182 dB |
| 45–57 s 空间夹具 | -0.0000000 dB | 约 0 dB |
| 60–72 s 动态夹具 | +0.0000000 dB | 约 0 dB |

## 操作工作流

1. 把插件放在重压缩、激励和饱和之前；这些后级会把点击和修复伪影一起放大。
2. 从 Threshold 0、Shape 50 开始，切到 Difference，只提高 Threshold 到能听见目标点击。
3. 调 Shape：较低值倾向短促数字点击，较高值倾向较宽/唱片刮擦型事件；只让目标缺陷进入 Difference。
4. 若 Difference 出现齿音、辅音、鼓击或表演瞬态，先回退 Threshold，再降低/重调 Shape；必要时只自动化问题片段。
5. 切回 Audio，以等响度检查字头、齿音、唇齿细节和空间尾部；修复量达到“编曲内不再显眼”即停止。

手册的 Master Click Removal 建议先用 50/70 并录制 Difference 作为点击日志；本轮把该值用作压力测试，结果显示它对合成脉冲过强，不能直接复制到人声。

## 边界与未验证项

- Composite 没有手工标注的嘴部点击、唇拍或数字 Click，无法报告 Precision、Recall 或事件衰减准确率。
- 未验证 Mono、VST2、其它采样率、两遍处理、自动化边界、离线与实时一致性或主观盲听。
- `default-difference.wav` 是一次监控模式坐标误操作得到的 Audio 重复件；正式证据只使用 `default-difference-verified.wav`。
- X-Click 是 RX Mouth De-click 无法加载后的可验证替代，但算法并非同一产品，不能写成一比一等价。

## 证据

- Bypass SHA-256：`c9802fbfa40487d6d60676d831f1ecb3a35d18ffca5ecb2d26361af56e429f04`。
- Default Audio SHA-256：`e606d7fdd9edd0fde618b2364bdcf27e0fe126fb817705f3b76cee6d04af99a7`。
- Default Difference SHA-256：`9e5f3627c0377a28c3e2223b1009ebc1c1fc0aee670e643ad60e21fa753721bd`。
- Threshold 50 / Shape 70 SHA-256：`e3c474c215502fdd0855801284d7b0ff45bc8cdbb37375dd40584011eae78f9f`。
- 工程快照 SHA-256：`0c4c5fe76427b0e5cf299a12b44b6cbcb42b6a034423bfc3f804190a4a5b1c62`。
- 量化：`validation/results/75f2f9574990--composite-xclick.json`（SHA-256 `986ca0c9ccba341485eb246ba1895c8d31e4f631123094de2b59e2e5d1b7e519`）。
- 测量脚本：`validation/scripts/analyze_xclick.py`。

