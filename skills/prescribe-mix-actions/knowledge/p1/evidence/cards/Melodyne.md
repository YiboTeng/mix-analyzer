---
type: plugin-card
status: active
created: 2026-08-19
updated: 2026-08-20
family_id: 394f47cfa81e
vendor: "Celemony"
product: "Melodyne"
evidence_level: L3
validation_status: passed-l3
batch: B01
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Melodyne

## 身份与版本

- 厂商：Celemony
- 产品族：Melodyne
- Family ID：394f47cfa81e
- 本机观测版本：5.4.1
- 格式：VST3 / ARA
- Studio One 可用性：current-filesystem-match
- 主能力方向：pitch-editor
- 次能力方向：timing;formant;amplitude;sibilant-editing
- 当前证据等级：L3
- 验证状态：passed-l3

## 能做什么

- 通过 Detection 把音频解析为 Blob，并按 Melodic、Percussive、Universal 或 Polyphonic 算法提供不同编辑粒度。
- 对音符 Pitch Center、Pitch Modulation、Pitch Drift、Formant、Amplitude、Timing、Attack Speed 与 Sibilant Balance 做独立编辑。
- Correct Pitch Macro 分开控制音高中心与慢速漂移；Note Separation 可把长音尾、滑入或误识别片段拆开处理。
- Studio One 的 ARA 集成无需实时 Transfer，能随 DAW 片段变化并直接打开编辑。

## 不建议用来做什么

- 不要在确认 Detection、算法和 Note Assignment 前批量 100% 校正。
- 不要把所有颤音当成 Pitch Drift；Melodyne 区分慢漂移与快速调制。
- 不要先做精修再切换算法，因为重新 Detection 可能丢失已有编辑。

## 信号流位置

- 完成剪辑、Comping 与基本源修复后，通过 Studio One ARA 打开；先确认 Melodic 算法与音符分配，再编辑。
- Pitch/Timing 精修通常先于压缩、饱和和空间效果；渲染或冻结后保留可回退版本。
- 对持续音尾或滑音仅分离问题区，保持相邻软分隔以维持自然过渡。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Algorithm / Detection | 决定音频如何被解析和可编辑。 | 人声优先检查 Melodic；先修 Note Assignment，再做声音编辑。 |
| Pitch Center | 音符音高重心。 | 只把真正偏离目标的音符拉回；保留风格性蓝调音、滑入和语气。 |
| Pitch Drift | 音符内慢速音高漂移。 | 长音后半段下坠时小幅减少，不动正常颤音。 |
| Pitch Modulation | 快速变化，如颤音。 | 颤音过宽时轻减；完全归零容易失去生命力。 |
| Note Separation | 把 Blob 切分或连接，影响音高中心和过渡。 | 把错误音尾、滑入、辅音或误识别段单独分离，再局部编辑。 |
| Timing / Time Handles | 移动音符边界、整体位置或内部时间演化。 | 先对齐节奏重音，避免把全部音节硬贴网格。 |

## Gain Staging

Amplitude Tool 会直接改变音符电平；音高/时间编辑也可能改变瞬态与感知响度。旁通比较应关闭后级响度补偿干扰，并对整体输出做等响度 Trim。保留原始未编辑版本用于回退。

## 延迟、相位与过采样

ARA 编辑通常不是常规实时 Insert 延迟问题，但检测、时间拉伸与导出算法可能改变相位/瞬态。本机 Melodyne Studio 5.4.1 VST3 在 Ableton Live 11.3.43 / 48 kHz 中报告 0 samples；这不代表 ARA、时间编辑或其它宿主没有渲染差异。

## Mono/Stereo

单人主唱使用 Melodic；带双轨/叠唱的立体声 Stem 会形成实际复调和空间混杂，不宜按单一主唱逐音符精修。优先在独立单声道轨处理。

## 适用场景

- 修正少数偏音、长音漂移和音符边界。
- 对 Rap 进入点、拖尾和双音节时值做细微节奏编辑。
- 局部 Formant/Amplitude 角色设计与和声复制。

## 路由

- Studio One ARA 事件级编辑；完成 Comping 后再进入。
- 保留原始事件副本，必要时 Bounce 到新轨后进行后续混音。

## 参数起点

- 先检查 Melodic 算法与 Note Assignment；错误 Detection 先修正。
- Correct Pitch Macro：Pitch Center 30–60%、Pitch Drift 10–40% 作为自然修音试点，再逐音符回退。
- 极端风格只对明确目标段提高至 80–100%，不要默认作用整轨。

## 调整目标

- 音符中心进入音乐可接受区，但滑音、颤音和语气保留。
- 长音尾不再明显下坠，词头和节奏重音仍自然。
- 修改后的音符分隔不产生断裂或重算音高中心的跳变。

## 调整时听什么

- 辅音和气息是否被时间/音高编辑拉长或切短。
- Blob 分离后是否出现新的音高重心跳变。
- 过度量化导致的平直颤音、机械时值和音色相位感。

## 何时停止

- 关闭 Compare 时错误不再分散注意力，同时演唱个性仍在。
- 继续校正只让图形更整齐但听感更假时停止并回退。

## 常见失败

- 算法错误、Note Assignment 错误或混响过多导致 Detection 失真。
- 先编辑后切算法导致已有编辑丢失。
- 把 Pitch Modulation 与 Pitch Drift 混淆，误杀颤音。
- 对所有音符整齐量化，破坏说唱的抢拍/拖拍律动。

## 替代方案

- Antares Auto-Tune Pro Graph Mode：同类手工修音。
- Studio One 原生 ARA/音高工具：较轻量的宿主工作流。

## 专业案例与工作流线索

- Celemony 官方训练强调先校正 Note Assignment；错误检测会让相同编辑产生更差音质。
- 官方建议人声使用 Melodic，并在开始编辑前决定算法。

## 待执行测试

- 同一人声用 Macro 轻修、逐音符轻修与中心/漂移组合三组导出，等响度盲听。
- 含滑音、颤音、长音尾和快速 Rap 音节的 Detection/分隔检查。
- Studio One ARA 回放、Bounce 和离线导出一致性测试。

## 已测结果

- 本机界面明确显示 `melodyne studio`，版本 5.4.1；Ableton Live 11.3.43 / 48 kHz VST3 报告 0 samples。
- 插入但未 Transfer 时，四个区域对共享旁路均为 0.000 dB、相关约 1.0、互差 RMS 约 -141.48 至 -141.50 dBFS。
- 实时 Transfer 约 7 秒后生成 13 个可见 Blob 并自动检测 D Minor。选中全部音符，应用 Pitch Center 100%、Pitch Drift 0%、Snap to chord scale Off。
- 处理差异只出现在 37.15–41.65 秒的 72 个 50 ms 窗；区域之外回到 dither 级空差。
- 85 个共同有声帧的实际位移中位约 +0.732 cents，帧间移动由 8.450 降到 8.105 cents；最近半音偏差中位没有改善（5.929→6.141 cents）。当前片段已近中心，说明 100% 宏不等于第三方逐帧 F0 必然更贴半音，也不能替代逐音符判断。
- 详见 [[projects/p1-plugin-knowledge-base/validation/reports/394f47cfa81e--Celemony-Melodyne|Melodyne L3 验证]]。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | note-based-pitch-time-editor |
| mode | ARA-melodic |
| main_controls | detection,pitch_center,drift,modulation,separation,timing |
| risk_flags | wrong-detection,over-quantization,edit-loss-on-algorithm-change |
| validation | ARA-render-consistency |

## 来源

- [[sources/音乐制作/插件资料/Celemony/Melodyne资料|Melodyne 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]

## 开放问题

- D 盘 Studio One 恢复后，ARA 菜单与渲染路径如何表现？
- 本机 ARA 与 VST3 Transfer 对同一片段的 Detection、回放与 Bounce 是否一致？
