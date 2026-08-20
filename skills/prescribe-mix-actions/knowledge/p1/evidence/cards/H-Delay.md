---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: bbf795a9fd06
vendor: "Waves"
product: "H-Delay"
evidence_level: L3
validation_status: S4-validated-Ableton-temporary-host
batch: B05
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# H-Delay

## 身份与版本

- 厂商：Waves
- 产品族：H-Delay
- Family ID：bbf795a9fd06
- 本机观测版本：12.7.0.209
- 格式：VST2 | VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：delay-vocal
- 次能力方向：tempo-sync;filter;analog;throw
- 当前证据等级：L3
- 验证状态：S4-validated-Ableton-temporary-host

## 能做什么

- 1–3500 ms 或 Tempo Sync、Ping Pong、Feedback 0–200%、四种 Analog、LoFi、HP/LP Link、Modulation 与 Dry/Wet。
- 100%以上 Feedback 会累积并可自激；相位反转可独立左右，Mono 输入 Ping Pong 下可能相消。
- 官方表列 Native 宿主延迟 0 samples；实际 Delay Time 是效果延迟。

## 不建议用来做什么

- 不要把 Feedback >100% 留在无人控制状态。
- 不要 Ping Pong 单边反相后不检查 Mono。
- 不要用全频延迟复制齿音和低频。

## 信号流位置

- 100% Wet Aux；HP/LP 让重复避开主唱主体，Send 自动化做 Throw。
- 需要 Duck 时后接侧链压缩或自动化返回。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Delay / Sync / Tap | 毫秒或节拍定义重复。 | Slap 70–140 ms；节奏从 1/8、1/4、Dotted/Triplet试。 |
| Feedback | 0–100衰减，100–200累积。 | 常规 10–40%；Throw 更高但自动化回落。 |
| HP/LP / Link | 滤除重复频段并可联动成 Bandpass。 | HP 150–300 Hz、LP 4–10 kHz起。 |
| Analog 1–4 / LoFi | 模拟色彩和低采样质感。 | 先 Off 基线，逐模式等响度；LoFi只作角色。 |
| Mod / Ping Pong / Phase | 时变音高与立体声反弹/极性。 | 低调制；Ping Pong 后做 Mono，避免单边反相。 |

## Gain Staging

固定 Dry 0/ Mix100% 在 Aux，用 Wet返回电平匹配；Analog可能作用 Dry，必须分离。记录重复1/2/3的RMS与衰减。

## 延迟、相位与过采样

官方 Native PDC 0；效果 Delay 独立。S4 验证 v12/格式和自动化。

## Mono/Stereo

Ping Pong/Phase 是关键风险。中心主唱干声独立；返回在 Mono 下不应明显消失。

## 适用场景

- Slap 增厚。
- 1/8或1/4主唱节奏延迟。
- 句尾 Throw、自激上升效果。

## 路由

- Stereo Aux 100% Wet。
- Send/Feedback 自动化，返回后级 Duck。

## 参数起点

- Slap 90–120 ms、Feedback 0–15%、HP 180 Hz、LP 6–9 kHz。
- 节奏 1/8D或1/4、Feedback 20–35%。
- Throw 自动化 Send/Feedback，段尾归零。

## 调整目标

- 重复填空隙不撞下一词。
- 重复逐次变暗/变窄并退后。

## 调整时听什么

- 齿音/爆破复制。
- 反馈失控。
- 相位反转 Mono 相消。
- Delay与节奏打架。

## 何时停止

- 重复服务节奏且干声仍中心。
- 下一句可懂度下降时减 Feedback/频段/Send。

## 常见失败

- 全频高 Feedback。
- Analog更响偏差。
- Ping Pong只听Stereo。
- 自动化不回收。

## 替代方案

- Timeless 3：多 Tap/调制/Duck可编程。
- Doubler：微短多声部。
- Abbey Road Chambers STEED：Delay-Reverb混合。

## 专业案例与工作流线索

- Waves 手册明确 Feedback 100以上为 build-up 且会迅速变响；任何 Throw 必须有回收自动化。

## 待执行测试

- Feedback静态衰减与>100稳定性。
- Analog/LoFi频响、谐波、噪声。
- Ping Pong/Phase Mono 和 PDC。

## 已测结果

- Ableton Live 11.3.43、Host 160 BPM、Default Preset、`1/8 D`、Dry/Wet 100：理论附点八分 281.250 ms，三次首 Tap 280.938/280.854/281.438 ms，最大绝对误差 0.396 ms。
- Peak -7.5445 dBFS，RMS -58.4475 dBFS，Correlation 0.996975，Side/Mid -28.1963 dB；默认全湿 Tap 接近中心。
- 默认 Feedback 未检测到阈值以上后续重复；不外推 Feedback、Ping Pong、Analog、LoFi、Filter、Mod 或 Phase。
- 详见 [[projects/p1-plugin-knowledge-base/validation/reports/bbf795a9fd06--H-Delay|H-Delay L3 验证]]。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | vocal-delay |
| mode | sync-or-ms |
| main_controls | delay,sync,feedback,filters,analog,lofi,mod,pingpong,mix |
| risk_flags | runaway-feedback,masking,mono-cancel |
| validation | repeat-decay-mono-latency |

## 来源

- [[sources/音乐制作/插件资料/Waves/H-Delay资料|H-Delay 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]

## 开放问题

- v12 自动化精度和 Dual Mode是否不存在于旧版？
