---
type: plugin-card
status: active
created: 2026-08-19
updated: 2026-08-20
family_id: 290814706035
vendor: "FabFilter"
product: "Pro-G"
evidence_level: L3
validation_status: passed-l3
batch: B01
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Pro-G

## 身份与版本

- 厂商：FabFilter
- 产品族：Pro-G
- Family ID：290814706035
- 本机观测版本：1.3.1.0
- 格式：VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：gate-expander
- 次能力方向：noise-control;sidechain;ducking;mid-side
- 当前证据等级：L3
- 验证状态：passed-l3

## 能做什么

- Threshold、Ratio、Range 构成门限/扩展核心，并提供多种程序相关 Style、Attack、Release、Hold、Knee 和 Lookahead。
- Expert Mode 提供内/外部侧链、48 dB/oct 高低通、Audition、Stereo Link/Mid-Side 与 Wet/Dry。
- 最高 4x 线性相位过采样；Lookahead 最多 10 ms。

## 不建议用来做什么

- 不要用无限 Range 和高 Ratio 把所有句间变成数字静音。
- 不要用极快 Release 追随人声波形，避免颤动、失真和语尾抽吸。
- 不要在单声道主唱上为了功能炫技启用不必要的 M/S。

## 信号流位置

- 连续噪声先由 NS1/RX 处理，Pro-G 再控制句间与低电平泄漏。
- 通常放在主压缩前；若后级压缩抬起噪声，可在压缩后增加更轻的第二级扩展，但需避免双重门控。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Threshold | 超过阈值时打开/恢复。 | 观察最弱有效字尾，设在噪声与有效语音之间。 |
| Ratio | 低于阈值后的扩展斜率；高于约 5:1 更像 Gate。 | 人声优先 2:1–4:1 温和扩展，再考虑更高。 |
| Range | 最大衰减地板。 | 只压低噪声 6–15 dB，保留房间连续性。 |
| Attack / Lookahead | 打开速度与预开时间。 | 词头被切时开启/增加 Lookahead，比一味极速 Attack 更稳。 |
| Hold / Release | 保持打开与关闭时间。 | Hold 跨过音节间隙，Release 跟随自然词尾和呼吸。 |
| Side-chain Filter / Audition | 限制检测频段并独听触发信号。 | 滤掉低频震动和极高噪声，让中频语音驱动开门。 |

## Gain Staging

Range/Expansion 改变低电平段而非强声主体。比较时分别记录活跃段、句尾和静音 RMS；全段 LUFS 会受静音比例影响。输出 Trim 只用于匹配活跃人声，不掩盖噪声下降。

## 延迟、相位与过采样

本机 1.3.1.0 在 Lookahead 模块关闭且 Oversampling Off 时由 Ableton 回读 0 samples；开启后界面为 9.951 ms、宿主为 480 samples / 10.0 ms。离线导出由 PDC 对齐，但录音监听仍承担这段实时延迟。Oversampling 延迟尚未实测，不能从新版资料外推。

## Mono/Stereo

VST3 自动适配轨道布局；单声道主唱用常规模式。立体声叠唱/效果返回若独立检测导致声像漂移，应提高 Link；M/S 只在明确控制 Side 尾部时使用。

## 适用场景

- 降低句间耳机漏音、房间噪声与前级底噪。
- 温和扩展弱噪声而不完全切断自然房间。
- Ducking/外部侧链用于效果返回闪避。

## 路由

- 主唱 Insert 前段，通常在压缩前。
- 混响/延迟 Return 上可用外部侧链做 Ducking，干声触发。

## 参数起点

- 人声自然扩展：Ratio 2:1–3:1，Range 6–12 dB，Attack 0–5 ms，Hold 40–100 ms，Release 100–250 ms。
- 词头被切：Lookahead 开；低频误触发：侧链高通约 80–150 Hz；齿音误触发可低通检测。
- 设置 Threshold 时循环最弱有效词尾和最响噪声，而不是只看强句。

## 调整目标

- 句间噪声退后，最弱字尾、呼吸和连读仍完整。
- 开关动作不跟随每个音高周期或短停顿颤动。

## 调整时听什么

- F/H/S、字尾和呼吸是否被截断。
- Release 是否造成噪声床上下抽吸。
- 立体声返回是否因未链接检测而左右漂移。

## 何时停止

- 完整编曲中噪声不再妨碍、单独听仍自然连续时停止。
- 继续加 Range/Ratio 只让空隙更假或吞掉词尾时退回。

## 常见失败

- Threshold 只按强句设置，弱句不开门。
- Range 过深和 Release 过快造成数字静音与颤动。
- 侧链包含爆破/低频震动导致错误开门。
- 过采样/Lookahead 延迟未记录，自动化或并联产生错位。

## 替代方案

- PreSonus Gate/Expander：宿主原生基线。
- Waves RVox Gate：更快但控制更少。
- 手工事件增益：对少量问题最可控。

## 专业案例与工作流线索

- FabFilter 官方把 Range 明确定义为最大扩展量，并建议用 Side-chain Audition/Filter 精确触发；这支持温和扩展而不是全静音。

## 已执行测试

- 固定 Composite：Classic、Threshold -30.00 dB、Ratio 3.01:1、Range 11.94 dB、Attack 4.894 ms、Hold 60.10 ms、Release 148.5 ms、Knee 0 dB、内部侧链、Left/Right、OS Off。
- 单变量切换 Lookahead 模块 Off 与 On（界面 9.951 ms），记录宿主延迟、单样本脉冲、35 ms 瞬态、稳定动态阶梯与固定人声区域。
- Pro-G 以外的链上设备全部停用；保存零 Lookahead 工程快照和两份独立渲染。

## 已测结果

- 零 Lookahead 把 0–6 秒单样本脉冲列降低 11.748791 dB，接近 11.94 dB Range 地板；9.951 ms Lookahead 仅 -0.000001 dB。
- 五个 35 ms 瞬态在零 Lookahead 下前 5 ms 低约 2.14–2.20 dB，前 20–50 ms仍低约 1.78–1.83 dB；开启 Lookahead 后约 0 dB。Lookahead 的作用是预开门，不是增加亮度。
- 五档稳定阶梯充分稳定后均约 0 dB；固定人声区两条件也约 0 dB，表示当前输入保持开门，不代表所有弱字尾或呼吸安全。
- 宿主延迟为 Off 0 samples、On 480 samples / 10.0 ms。详细证据：[[projects/p1-plugin-knowledge-base/validation/reports/290814706035--FabFilter-Pro-G|Pro-G L3 验证]]。

## 后续测试

- 带标签的弱字尾、呼吸、句间噪声与爆破，测漏检、误截和主观自然度。
- 其它 Style、侧链 HP/LP/Audition、外部侧链、M/S、MIDI Trigger 与 Oversampling。
- Stereo Link 0/100% 对立体声双轨或效果返回声像稳定性的影响。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | gate-expander |
| mode | downward-expansion |
| main_controls | threshold,ratio,range,attack,hold,release,lookahead,sidechain |
| risk_flags | tail-chop,chatter,latency,stereo-wander |
| validation | event-envelope-and-latency |

## 来源

- [[sources/音乐制作/插件资料/FabFilter/Pro-G资料|Pro-G 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]
- [[projects/p1-plugin-knowledge-base/validation/reports/290814706035--FabFilter-Pro-G|Pro-G L3 验证]]

## 开放问题

- 本机其它 Style、侧链滤波、外部 Sidechain、M/S、Stereo Link、MIDI Trigger 与 Oversampling 的具体行为如何？
- Studio One VST3 Sidechain 与 MIDI Trigger 在该版本是否稳定？
