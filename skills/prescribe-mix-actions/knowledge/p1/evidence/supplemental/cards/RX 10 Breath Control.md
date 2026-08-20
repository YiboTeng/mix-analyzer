---
type: plugin-card
status: active
created: 2026-08-19
updated: 2026-08-19
family_id: e4502ba6e6cb
vendor: "iZotope"
product: "RX 10 Breath Control"
evidence_level: L2
validation_status: S3-researched-S4-pending
batch: B01
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# RX 10 Breath Control

## 身份与版本

- 厂商：iZotope
- 产品族：RX 10 Breath Control
- Family ID：e4502ba6e6cb
- 本机观测版本：10.4.2
- 格式：VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：restoration-breath
- 次能力方向：pre-mix-cleanup;gain-conditioning
- 当前证据等级：L2
- 验证状态：S3-researched-S4-pending

## 能做什么

- 检测呼吸的谐波结构并用 Gain Mode 统一衰减，或用 Target Mode 只把过响呼吸压到目标电平。
- Output Breaths Only 可独听检测结果，辅助避免把弱辅音、气声元音或房间噪声误判为呼吸。

## 不建议用来做什么

- 不要把所有呼吸完全抹掉；Rap 的呼吸常包含节奏、力度与真实感。
- 不要在重压缩和激励之后才做大幅呼吸控制，因为后级已放大并改变检测对象。

## 信号流位置

- Comping/剪辑后、主压缩和饱和前；必要时在 Mouth De-click 与 De-plosive 之后。
- 先用 Output Breaths Only 校准检测，再在全信号中决定保留多少呼吸。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Gain Mode / Gain | 每个检测到的呼吸衰减固定量。 | 呼吸整体都偏响时使用；从小幅衰减开始。 |
| Target Mode / Target Level | 只把高于目标的呼吸拉向指定电平。 | 需要保留自然弱呼吸时优先。 |
| Sensitivity | 呼吸检测灵敏度。 | 独听 Breaths Only，刚好完整捕获呼吸但不带词头/气声元音。 |
| Output Breaths Only | 只输出被检测的呼吸。 | 作为校准监听，完成后关闭。 |

## Gain Staging

这是电平修复器。记录处理前后呼吸事件和整段 Integrated/Active RMS，但主观 A/B 要对非呼吸主体做等响度；否则整体电平下降会被误认为更干净。

## 延迟、相位与过采样

官方旧版模块说明控制语义，但未提供本机 RX 10 VST3 延迟/相位数据。S4 需在实时插件实例中测量报告延迟和离线导出一致性。

## Mono/Stereo

优先在单声道独唱轨处理；立体声 Stem 可能把混响/伴奏泄漏误识别为呼吸，必须更保守。

## 适用场景

- 近讲 Rap 中个别吸气过响，压缩后会跳出。
- 双轨或 Ad-lib 的呼吸密度过高，需要保留节奏但降低干扰。

## 路由

- 单轨 Insert；批量前先在代表性强/弱呼吸段预听。
- 严重个别事件仍优先 Clip Gain 或手工编辑。

## 参数起点

- 自然起点：Target Mode，目标设在不抢词尾的位置；Sensitivity 从低向上，独听检测。
- 统一衰减起点：Gain Mode -4 至 -8 dB；重呼吸可试 -10 至 -12 dB，但保留可听空气。

## 调整目标

- 大呼吸不再触发后级压缩/激励显著跳出。
- 弱呼吸、气声唱法和词头仍保留自然连续性。

## 调整时听什么

- Breaths Only 中是否出现 F/H/S、气声元音或房间尾音。
- 呼吸被压后句间是否出现突然真空或噪声门感。

## 何时停止

- 呼吸退到节奏背景且后级不再过度触发时停止。
- 开始削弱气声质感、词头或造成句间真空时降低 Sensitivity/Reduction。

## 常见失败

- Sensitivity 过高误抓辅音和气声元音。
- 固定 Gain 过深让弱呼吸消失、重呼吸仍显突兀。
- 处理顺序太后，检测受饱和谐波与混响影响。

## 替代方案

- Clip Gain/事件增益手工降低关键呼吸。
- Waves DeBreath（若当前可用）或动态 EQ 仅作替补，不能等同专用检测。

## 专业案例与工作流线索

- iZotope 官方说明 Target Mode 对强呼吸处理更深、对自然弱呼吸处理更少，适合保留真实感。

## 待执行测试

- 强/弱呼吸、气声元音和 S/H 辅音标注集的检测精确度测试。
- Gain 与 Target 两模式在同一事件上的电平与听感对比。
- 处理前后压缩器增益衰减触发差异。

## 已测结果

S4 待执行；当前参数起点来自官方控制语义与条件化工作流。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | breath-control |
| mode | gain-or-target |
| main_controls | sensitivity,gain,target,breaths_only |
| risk_flags | consonant-misdetect,unnatural-silence |
| validation | event-detection-and-level |

## 来源

- [[sources/音乐制作/插件资料/iZotope/RX 10 Breath Control资料|RX 10 Breath Control 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]

## 开放问题

- RX 10.4.2 VST3 是否保留旧版全部 Target/Gain 控件与范围？
- 本机实时实例延迟和自动化平滑度是多少？
