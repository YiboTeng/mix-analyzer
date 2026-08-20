---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: 4bceae9f0a6f
vendor: "Waves"
product: "Doubler"
evidence_level: L3
validation_status: S4-host-validated-passed
batch: B04
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Doubler

## 身份与版本

- 厂商：Waves
- 产品族：Doubler
- Family ID：4bceae9f0a6f
- 本机观测版本：12.7.0.209
- 格式：VST2 | VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：width-multivoice
- 次能力方向：pitch-delay;adlib
- 当前证据等级：L3
- 验证状态：S4-host-validated-passed

## 能做什么

- 最多四声部，每声部独立 Gain、Pan、Delay 最多 100 ms、Detune ±100 cents、调制、Feedback。
- Range 80/20 Hz 决定最低无伪影移调频率和固有延迟；80 Hz 约 7 ms，20 Hz 约 24 ms。
- Align Direct 可延迟干声到声部固有延迟；Output Shelf 和 Feedback HP 管理频谱。

## 不建议用来做什么

- 不要把宿主报告 0 samples 等同声部无固有延迟。
- 不要所有声部同延迟/同调制造成固定梳状。
- Lead Vocal 有低频但不需处理到 20 Hz 时不要白付 24 ms。

## 信号流位置

- 优先 100% Effects Aux/组件无 Direct，干声单独中心。
- 四声部分散左右、错开 Delay/Detune，返回滤除低频和齿音。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Voice Delay / Detune / Pan | 定义每个副本的时间、音高和位置。 | 左右不同：如 ±6–12 cents、10–30 ms，避免完全对称。 |
| Mod Depth/Rate / Reset | 时变音高并可重置相位。 | 低深度慢速；需要可重复 Cue 才自动化 Reset。 |
| Range 80/20 Hz | 最低移调频率与 7/24 ms 声部延迟。 | Lead Vocal 选 80 Hz；Bass/全频才 20 Hz。 |
| Align Direct | 把直接声延迟到 Voice。 | Aux 通常不要 Direct；Insert 比较 Align On/Off 与梳状。 |
| Feedback / Output EQ | 重复再生和整体高低 Shelf。 | 常规 Doubler Feedback 0；返回高通/削高。 |

## Gain Staging

多声部叠加提高总能量。匹配 Stereo RMS，记录 Mid/Side RMS、Peak、相关性；Voice Gain 和 Dry 不得共同造成响度偏差。

## 延迟、相位与过采样

Waves 表列插件宿主延迟 0，但手册明确 Voice 固有 7/24 ms；这是效果设计延迟而非 PDC。本机 `Doubler4 Stereo` VST3 默认 Range 80 Hz、Align No 实测宿主报告 0 samples，且 Direct 三档峰值增益约 0.000 dB；效果声部仍有毫秒级响应，两个概念必须分开。

## Mono/Stereo

Stereo 是核心。Direct 保持中心，Voices 分布两侧；Mono Fold-down 检查移调副本梳状和音色。

## 适用场景

- Lead Vocal 轻宽度层。
- Ad-lib/Backing Vocal 四声部扩散。
- 效果化八度下/反馈副本。

## 路由

- Stereo Aux，100% Voice。
- 复制轨作角色层。

## 参数起点

- Range 80 Hz；两声部 Pan L/R；Delay 12/22 ms；Detune -8/+8 cents；Feedback 0。
- 返回高通 150–300 Hz、低通 6–10 kHz 作为试点。
- 四声部从低 Gain 加第二层。

## 调整目标

- 副本形成两侧点状/区域层而不遮主唱。
- Mono 时主体音色保持。

## 调整时听什么

- 梳状、Chorus、Slap。
- 左右完全对称导致静态假宽。
- Voice 齿音和低频堆积。

## 何时停止

- Stereo 宽度支持情绪，Mono 不空心。
- 再加 Voice 只增混浊时停止。

## 常见失败

- 20 Hz Range 滥用。
- Align Direct 误设。
- 同 Delay/Detune。
- Feedback 失控。

## 替代方案

- MicroShift：快速三 Style。
- 真实双轨：更自然。
- Little AlterBoy：大幅 Pitch/Formant 角色。

## 专业案例与工作流线索

- Waves 手册区分 PDC 0 与 Voice 固有延迟，并建议人声可用 80 Hz Range；卡片保持这两个概念分离。

## 待执行测试

- 80/20 Hz Range 的 Voice 延迟、低频伪影与 CPU。
- Align Direct On/Off 脉冲和 Mono。
- 2/4 Voice 参数矩阵的相关性与盲听。

## 已测结果

Ableton Live 11.3.43 / Waves Doubler 12.7.0.209 `Doubler4 Stereo` VST3 默认状态：Direct 0 dB、Align No、Range 80 Hz，四 Voice 为 -6/-12/-6/-12 dB、Pan -45/+45/+45/-45、Delay 9.4/16.0/23.7/21.0 ms、Detune +6/+10/-6/-10 cents、Depth 0、Feedback 0。宿主报告 0 samples；三档源脉冲左右 Direct 峰值增益均约 0.000 dB。0–65 ms 响应窗平均 L/R 相关 0.712932、Side/Mid -7.747 dB、Mono 折叠差 -0.676 dB；主导左能量团 5.417–13.750 ms、右能量团 21.729–28.917 ms。默认微移调响应把 Voice 合并为时变能量团，不能把显示 Delay 与官方约 7 ms 固有延迟机械相加后当成样本精确到达。证据见 [[projects/p1-plugin-knowledge-base/validation/reports/4bceae9f0a6f--Waves-Doubler|Doubler L3 验证]]。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | multi-voice-doubler |
| mode | two-or-four-voice |
| main_controls | voice_gain,pan,delay,detune,mod,range,align_direct |
| risk_flags | comb-filter,mono-loss,latency-confusion,mud |
| validation | voice-delay-correlation |

## 来源

- [[sources/音乐制作/插件资料/Waves/Doubler资料|Doubler 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]
- [[projects/p1-plugin-knowledge-base/validation/reports/4bceae9f0a6f--Waves-Doubler|Doubler L3 验证]]

## 开放问题

- Doubler2、Mono/Stereo、Mono 组件及 Range 20 Hz、Align Yes 的实际响应？
