---
type: plugin-card
status: active
created: 2026-08-19
updated: 2026-08-19
family_id: 5a5ddef31a66
vendor: "iZotope"
product: "RX 10 De-plosive"
evidence_level: L2
validation_status: S3-researched-S4-pending
batch: B01
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# RX 10 De-plosive

## 身份与版本

- 厂商：iZotope
- 产品族：RX 10 De-plosive
- Family ID：5a5ddef31a66
- 本机观测版本：10.4.2
- 格式：VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：restoration-plosive
- 次能力方向：low-frequency-event-repair;pre-mix-cleanup
- 当前证据等级：L2
- 验证状态：S3-researched-S4-pending

## 能做什么

- 识别 P/T/K/B 等气流冲击造成的低频爆破并衰减，同时尽量保留语音基频与谐波。
- Sensitivity 控制检测，Strength 控制衰减深度，Frequency Limit 限制最高处理频率。

## 不建议用来做什么

- 不要用它替代话筒角度、防喷罩和录音阶段控制。
- 不要先高通掉 20–80 Hz 检测线索再期望 De-plosive 正常识别。
- 不要对所有低音元音持续高 Strength 批量处理。

## 信号流位置

- 尽量放在高通、低频动态 EQ、重压缩和饱和之前；官方说明检测依赖 20–80 Hz。
- 先在爆破事件上定位 Frequency Limit，再扩展到整轨并复核正常低音音节。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Sensitivity | 爆破检测灵敏度，官方指出对总体效果影响大于 Strength。 | 漏检时先提高；正常低音也被抓时降低。 |
| Strength | 对已检测爆破的衰减深度。 | 检测正确后再加深，避免伤害正常语音。 |
| Frequency Limit | 被衰减的最高频率。 | 从只覆盖爆破的低频上限开始，必要时再向 300–400 Hz 扩展。 |

## Gain Staging

比较时匹配非爆破区的主体响度，并单独记录爆破窗口 20–300 Hz 峰值/RMS。整体变薄不能被当作修复成功。

## 延迟、相位与过采样

专用修复可能包含分析/插值，官方旧版页未给本机实时延迟。S4 需测瞬态对齐、报告延迟与离线/实时一致性。

## Mono/Stereo

在原始单声道人声上最可控；立体声 Stem 中 Side 的低频残留可能误导检测。

## 适用场景

- 近讲主唱 P/B 产生 20–300 Hz 砰声。
- 单个爆破使压缩器、饱和器或限制器错误触发。

## 路由

- 主唱 Insert 链前端；高通和动态处理之前。
- 少量严重事件可只对事件区域 Render，避免整轨不必要处理。

## 参数起点

- Sensitivity 中低起步，先捕获最明显事件；Strength 2–5/10 级别试点。
- Frequency Limit 先约 120–200 Hz；仍有上部砰声再推至 250–350 Hz。

## 调整目标

- 爆破低频峰下降但元音胸声与基频仍连续。
- 后级压缩器不再因爆破瞬间产生额外泵动。

## 调整时听什么

- P/B 后主体是否变薄或出现孔洞。
- 正常低音音节、近讲厚度是否被误削。
- 爆破上部 200–400 Hz 是否仍残留。

## 何时停止

- 砰声不再抢注意力且胸声未改变时停止。
- 继续提高 Strength 只让音节变薄时退回，改用局部 Clip Gain/动态 EQ。

## 常见失败

- 前置高通导致检测失效。
- Sensitivity 过高把正常低频元音当爆破。
- Frequency Limit 过高削弱可懂度与声体，过低则留下爆破上缘。

## 替代方案

- 手工 Clip Gain + 短交叉淡化。
- FabFilter Pro-Q 3 动态低频 Bell/低架，仅在爆破触发。

## 专业案例与工作流线索

- iZotope 官方明确建议在尚未高通的音频上使用，因为 20–80 Hz 是检测线索。

## 待执行测试

- 标注爆破与正常低音元音，比较 Sensitivity/Strength 的误检率。
- Frequency Limit 120/200/350 Hz 三档的频谱、波形和主体听感。
- 处理前后后级压缩器增益衰减峰值。

## 已测结果

S4 待执行；尚未验证本机 RX 10.4.2 控件范围。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | plosive-repair |
| mode | event-selective-low-frequency-reduction |
| main_controls | sensitivity,strength,frequency_limit |
| risk_flags | body-loss,pre-filter-detection-failure |
| validation | plosive-vs-vowel-events |

## 来源

- [[sources/音乐制作/插件资料/iZotope/RX 10 De-plosive资料|RX 10 De-plosive 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]

## 开放问题

- RX 10 VST3 实例是否允许 Output Plosives Only 或其他新版监听？
- 实时与模块 Render 的算法是否一致？
