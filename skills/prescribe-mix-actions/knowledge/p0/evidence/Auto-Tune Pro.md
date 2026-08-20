---
type: plugin-card
status: active
created: 2026-08-19
updated: 2026-08-20
family_id: 7b4d8c94b025
vendor: "Antares"
product: "Auto-Tune Pro"
evidence_level: L3
validation_status: passed-l3
batch: B01
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Auto-Tune Pro

## 身份与版本

- 厂商：Antares
- 产品族：Auto-Tune Pro
- Family ID：7b4d8c94b025
- 本机观测版本：10.0.0
- 格式：VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：pitch-realtime
- 次能力方向：pitch-graph;formant;creative-hard-tune
- 当前证据等级：L3
- 验证状态：passed-l3

## 能做什么

- Auto Mode 按 Key、Scale 与启用音级把检测到的音高连续拉向最近目标音，适合实时透明修音或明显 Hard Tune。
- Retune Speed 决定趋近目标音的速度；Flex-Tune 保留目标音附近的表现变化；Humanize 对长音段放慢校正。
- Graph Mode 可对特定音符/片段做手工曲线与对象编辑；MIDI To Notes、Learn Scale 可动态定义目标音。
- Formant 与 Throat 用于在较大移调时保留或有意改变声道角色。

## 不建议用来做什么

- 调性、音阶或转调自动化尚未确认时，不要先用极快 Retune Speed 掩盖错误目标音。
- 不要把 Tracking、Flex-Tune 或 Humanize 当作统一的音质增强旋钮；它们解决不同的检测与校正行为。
- 不要仅凭成品音高平台断言使用了 Auto-Tune 或某个 Retune Speed。

## 信号流位置

- 典型顺序：剪辑/Clip Gain 与必要的点击、爆破、噪声修复之后，主压缩、饱和与大幅调制之前。
- 若齿音或呼吸严重干扰检测，可在前级做轻量清理；最终去齿通常仍放在激励/饱和之后复查。
- Graph Mode 或 ARA 式精修应在音频剪辑结构稳定后完成，避免后续重剪导致映射失效。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Key / Scale / Scale Controls | 定义 Auto Mode 允许的目标音集合。 | 先核对歌曲调性、转调与借用音；错误音阶比速度设置更致命。 |
| Retune Speed | 输入音高趋近目标音的时间行为；越快效果越明显。 | 先把 Humanize 归零，从较慢向快调，直到短音稳定，再决定是否追求机器感。 |
| Flex-Tune | 允许目标音附近的表现性偏移通过。 | 滑音被吸平时增加；需要硬切换时降低。 |
| Humanize | 快速 Retune 下对持续音段放慢校正。 | 短音满意但长音僵硬时增加，不用它修正错误音阶。 |
| Input Type / Tracking | 约束检测音域并在噪声与不规则波形间取舍。 | 按声部选 Input Type；只在漏检或噪声误跟踪时调整 Tracking。 |
| Formant / Throat | 控制移调时的共振峰补偿与声道模型长度。 | 透明校音保持 Formant；角色化处理再小步改变 Throat 并等响度比较。 |

## Gain Staging

插件核心是音高处理，不应依靠输出更响制造好感。记录输入峰值与输出峰值，旁通比较时用后级 Trim 做等响度；若打开 Classic/Modern 或 Formant 模式造成电平差，也要补偿后再判断。

## 延迟、相位与过采样

本机 v10.0.0 VST3 在 Ableton Live 11.3.43 / 48 kHz 的 Auto/Modern 状态报告 `2670 samples / 55.6 ms`；导出由宿主 PDC 对齐。Graph、Classic、低延迟选项、其它采样率与 Studio One 尚未回读，因此这个数字只适用于当前实例和状态。录音监听前必须做实际往返延迟预算，不能把 Auto Mode 等同于零延迟。

## Mono/Stereo

主唱通常在单声道轨实例化；立体声叠唱或效果返回必须检查左右检测是否保持声像。不要为 Mono/Stereo 组件重复建卡。

## 适用场景

- 现代 Trap/Rap 主唱的可听 Hard Tune：正确 Key/Scale、快速 Retune、低 Flex-Tune。
- 旋律 Rap 的透明校正：中等 Retune、适量 Flex-Tune，长音再加 Humanize。
- 少数问题音的 Graph Mode 精修，避免整段加重自动校正。

## 路由

- 主唱 Insert；优先放在主要动态与非线性处理之前。
- Ad-lib/低八度角色声可复制轨道后单独设置 Formant/Throat，避免改变主唱本体。

## 参数起点

- 硬调音起点：正确 Key/Scale；Retune Speed 0–10 ms；Flex-Tune 0–10；Humanize 0，确认长音后再加。
- 自然起点：Retune Speed 15–50 ms；Flex-Tune 15–30；Humanize 先 0，再对僵硬长音尝试 10–30。
- 所有数值是工作起点；音节速度、滑音、颤音和风格比固定数值更重要。

## 调整目标

- 短音落在正确目标音且转音仍符合旋律意图。
- 长音中心稳定但颤音与滑音没有被统一拉直。
- Hard Tune 时音符切换有节奏性，而不是因错误音阶出现随机跳音。

## 调整时听什么

- 音符边界是否出现不合调的吸附、颤动或八度误检。
- 辅音、气息和滑音是否被不自然地拉扯。
- Formant 打开/关闭时角色是否改变而非单纯更亮。

## 何时停止

- 短音稳定、长音自然或已达到明确机器美学时停止。
- 继续加快只让转音更碎、长音更僵而没有提升旋律清晰度时退回。

## 常见失败

- Key/Scale 错误导致音符被拉向错误目标。
- 过快 Retune 与过低 Flex-Tune 把意图滑音、颤音和咬字切碎。
- Tracking 过宽在噪声/气声处误检，过窄又漏掉粗糙或低音声部。
- 大幅移调未管理 Formant，出现明显松鼠声或不一致角色。

## 替代方案

- Celemony Melodyne：逐音符、离线细修。
- Waves Tune Real-Time：同机现有的实时校音候补。
- Studio One 原生音高校正/ARA 工作流：在不追求 Auto-Tune 特定转换质感时使用。

## 专业案例与工作流线索

- Antares 官方指南把 Retune Speed、Flex-Tune、Humanize 分别用于速度、表现保留与长音自然度；这三者应按顺序诊断，而不是一起盲调。

## 待执行测试

- 用已知 Key/Scale、带音符标签的滑音/颤音/快速音节语料核对目标音、转换与误检。
- Flex-Tune、Humanize、Tracking、Classic、Graph 和低延迟选项的单变量矩阵。
- Formant/Throat、Mono、其它采样率、自动化、CPU 与等响盲听。

## 已测结果

本机 Auto-Tune Pro 10.0.0 VST3 已在 Ableton Live 11.3.43 / 48 kHz 真实加载。固定 Auto/Modern、Alto-Tenor、C Chromatic、Tracking 50、Flex-Tune/Humanize/Natural Vibrato 0、Formant 100、Mix 100，只把 Retune Speed 20 改为 0。

在 21–42 秒固定人声段的 491 个三态共同有声帧中，F0 距最近半音的绝对偏差中位数从旁路 `6.115 cents` 降至 Retune 20 的 `4.160`，Retune 0 的 `0.844`；落在 ±5 cents 内的帧比例为 `40.1% / 63.7% / 88.0%`。Retune 0 的帧间移动中位数为 `1.337 cents`，旁路为 `8.254 cents`，说明更低数值会更强平台化，但不代表旋律目标正确或听感更好。

固定人声段三态 RMS 约 `-25.94 dBFS`，当前差异不是整体增益偏置；宿主报告 `2670 samples / 55.6 ms`。完整证据见 [[projects/p1-plugin-knowledge-base/validation/reports/7b4d8c94b025--Antares-Auto-Tune-Pro|Auto-Tune Pro L3 验证]]。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | pitch-correction |
| mode | auto-or-graph |
| main_controls | key,scale,retune_speed,flex_tune,humanize,formant |
| risk_flags | wrong-scale,over-correction,formant-artifact |
| validation | pitch-transition-and-latency |

## 来源

- [[sources/音乐制作/插件资料/Antares/Auto-Tune Pro资料|Auto-Tune Pro 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]
- [[projects/p1-plugin-knowledge-base/validation/reports/7b4d8c94b025--Antares-Auto-Tune-Pro|Auto-Tune Pro L3 验证]]

## 开放问题

- 本机 v10.0.0 的 Low Latency、Classic 与 Graph 各自报告延迟是多少？
- Studio One 当前工程中 Graph Mode 的传输/同步行为是否稳定？
