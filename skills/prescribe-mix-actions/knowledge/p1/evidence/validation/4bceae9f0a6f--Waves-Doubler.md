---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: 4bceae9f0a6f
product: Doubler
evidence_level: L3
test_id: impulse-default-doubler4-stereo
---

# Waves Doubler：默认 Doubler4 Stereo 脉冲与折叠验证

## 结论

本机 Waves Doubler 12.7.0.209 `Doubler4 Stereo` VST3 在 Ableton Live 11.3.43 的真实默认实例中保留 Unity Direct，并增加四个分散声部。宿主设备栏报告 `Latency: 0 samples`；三档源脉冲的左右 Direct 峰值增益均为 0.000 dB（最大舍入误差 0.000002 dB），证明宿主 PDC 与直接声路径没有可测样本偏移或电平改变。但这不代表效果声部“无延迟”：默认 `Range 80 Hz` 的官方固有 Voice 延迟约 7 ms，界面另设四个 Voice Delay 9.4/16.0/23.7/21.0 ms，并以 -6/-12/-6/-12 dB、Pan -45/+45/+45/-45、Detune +6/+10/-6/-10 cents 分布。

固定脉冲响应的 0–65 ms 活动窗内，三次左右相关为 0.733493/0.713113/0.692190，平均 0.712932；Side/Mid 为 -8.122/-7.745/-7.374 dB，平均 -7.747 dB；折成 Mono 后，相对逐通道 Stereo RMS 损失 -0.622/-0.675/-0.730 dB，平均 -0.676 dB。默认状态因此不是“只变宽不改 Mono”的中性工具：它保留中心 Direct，但四个微移调/离散延时副本同时引入可量化 Side 与轻度折叠损失。

0.35 ms 移动 RMS 包络显示，三次事件的主导左侧能量团落在 5.417–13.750 ms、右侧落在 21.729–28.917 ms。它们没有稳定表现为四个孤立 Delta 峰，因为微移调算法把脉冲展开成时变响应，且同侧多个 Voice 会合并；因此这些主导能量团不能逐一反推为某个 Voice 的显示 Delay，也不能把“显示 Delay + 7 ms”机械当作样本精确到达时刻。

## 固定状态与量化

- 插件：Waves Doubler，本机文件清单版本 12.7.0.209，`Doubler4 Stereo` VST3。
- Direct：Gain 0 dB、Pan 0、Align Direct=`No`。
- 全局：Range 80 Hz；Feedback 16 显示位置但四声部 FDBK 均 0；Modulation Reset 保持默认。
- Voice 1：Gain -6 dB、Pan -45、Delay 9.4 ms、Detune +6 cents、Depth 0、Rate 1.0。
- Voice 2：Gain -12 dB、Pan +45、Delay 16.0 ms、Detune +10 cents、Depth 0、Rate 1.0。
- Voice 3：Gain -6 dB、Pan +45、Delay 23.7 ms、Detune -6 cents、Depth 0、Rate 1.0。
- Voice 4：Gain -12 dB、Pan -45、Delay 21.0 ms、Detune -10 cents、Depth 0、Rate 1.0。
- Output EQ：Left Gain 0/Freq 101；Right Gain +4.1/Freq 1306；Output Gain 0；输入路由 1/3=L、2/4=R。
- 输入：实际 `impulse_train_48k.wav`；夹具位于 2.1.1，Host 160 BPM，Warp 关闭。
- 导出：Master、2.1.1 起、4.0.0 长（6 s）、48 kHz/24-bit WAV、Triangular dither、Normalize 关闭。
- 工程快照：`validation/host/snapshots/4bceae9f0a6f--Waves-Doubler.als`。

| 指标 | 脉冲 1 | 脉冲 2 | 脉冲 3 | 平均/范围 |
|---|---:|---:|---:|---:|
| 输入峰值 dBFS | -1.938333 | -6.020600 | -12.041200 | 三档固定输入 |
| Direct 左增益 dB | 0.000000 | 0.000000 | 0.000000 | 0.000000 |
| Direct 右增益 dB | -0.000001 | -0.000002 | 0.000000 | 约 0.000000 |
| 左主导能量团 ms | 12.333 | 5.417 | 13.750 | 5.417–13.750 |
| 右主导能量团 ms | 28.917 | 24.792 | 21.729 | 21.729–28.917 |
| L/R 相关 | 0.733493 | 0.713113 | 0.692190 | 0.712932 |
| Side/Mid dB | -8.122 | -7.745 | -7.374 | -7.747 |
| Mono 折叠差 dB | -0.622 | -0.675 | -0.730 | -0.676 |

## 操作观察与工作流

- 默认实例的 Direct 已是 0 dB 中心声，不是纯湿 Aux 预设。作为 Insert 使用时，先保持 Align Direct=`No` 记录中心路径；作为 Send/Aux 时，应改用无 Direct 的组件/状态或关闭 Direct，避免把主唱重复叠加并误把响度增加当宽度改善。
- `Range 80 Hz` 适合作为人声起点：它以约 7 ms 声部固有延迟换取 80 Hz 以上移调。切到 20 Hz 会把官方固有延迟提高至约 24 ms；只有低频内容确实需要完整移调才值得测试。
- 默认四 Voice 已刻意采用不同 Gain、Pan、Delay 与 Detune；不要把它们“整理”为完全镜像。完全对称会让固定梳状和静态假宽更容易出现。
- 这次折叠平均只损失约 0.68 dB，但它是稀疏脉冲、Depth 0 的结果。真实长元音、齿音、Depth/Rate 调制、反馈与 Output EQ 都可能改变相关性；因此实际工作流必须在等响 Stereo、Mono 和 Side Solo 三种监听间切换。
- 默认 Direct 峰值严格保持，不需要为主行为做响度匹配；本轮也不据此比较“好听”。若比较 2/4 Voice、Range 或 Align，则须以后级 Trim 匹配活动 RMS，再比较宽度与音色。

## 何时用、如何用精

- 主唱轻宽化：优先独立 Stereo Aux，Direct 关闭；Range 80 Hz、Feedback 0、Depth 0 起步，先只开两个低增益 Voice，再按需要补另两个。返回从主唱下方约 -20 dB 起推，并在返回端高通 150–300 Hz、必要时低通 6–10 kHz 或去齿。
- Ad-lib/Backing Vocal：可保留四 Voice 和更宽 Pan，但仍先固定不同 Delay/Detune；先用 Voice Gain 定层次，最后才动 Output EQ，便于归因。
- Insert：只有需要 Direct 与副本共同构成角色时使用；记录 Align Direct 状态。Align=`Yes` 会改变中心的时间基准，不应与 Aux 工作流混写。
- 调到精的顺序：Direct/路由 → Range → Voice Gain/Pan → Delay → Detune → Depth/Rate → Feedback → Output EQ；每次只改变一组变量，并记录相关、Side/Mid 与 Mono 折叠。
- 停止条件：Stereo 中宽度层可感而中心仍稳，Mono 主体音色不空，Side Solo 没有过多齿音和低中频；继续增加 Voice 或 Detune 主要带来 Chorus、Slap 或糊时回退。

## 边界与未验证项

- 本轮用固定脉冲而不是矩阵最初分配的 `spatial_correlation_48k.wav`，因为它能把宿主 PDC、Direct、算法响应与显示 Voice Delay 分开。主行为与 Mono 副作用已量化，但不等于完成连续人声的听感验证。
- 未切换 Doubler2、Mono/Stereo、Mono 组件；未测试 Range 20 Hz、Align Direct=`Yes`、Depth/Rate、Reset 自动化、Feedback、Output Shelf 单变量或 MIDI/自动化暴露。
- 到达团是包络特征，不是四个 Voice 的逐一系统辨识。默认微移调具有时变响应，三档脉冲的主导团位置不同不代表 Delay 参数随电平改变。
- `Latency: 0 samples` 仅表示本机 VST3 默认状态的宿主报告，不涵盖效果声部的设计延迟，也不得外推到 Studio One 或其它组件。
- 源文件为 8 秒 PCM16，候选为 6 秒 PCM24；分析使用共同前 6 秒。Triangular dither 只贡献极低噪声底，不解释毫秒级能量团、Side 或 Mono 差异。

## 证据

- Doubler 渲染 SHA-256：`d4a45e3d46ea40eb943e85cbdc08e137b16907f19fe434218b5e8b3cb6633356`。
- 固定脉冲 SHA-256：`aafbd0a42ee57fde77b79aae591d54f87383b391e76803af9405757f92e3cf2e`。
- 量化：`validation/results/4bceae9f0a6f--impulse-default-doubler4-stereo.json`。
- 测量脚本：`validation/scripts/analyze_doubler.py`。

