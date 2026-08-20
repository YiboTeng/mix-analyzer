---
type: plugin-card
status: active
created: 2026-08-19
updated: 2026-08-19
family_id: 8f1bf189fac1
vendor: "iZotope"
product: "RX 10 Mouth De-click"
evidence_level: L2
validation_status: S3-researched-S4-pending
batch: B01
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# RX 10 Mouth De-click

## 身份与版本

- 厂商：iZotope
- 产品族：RX 10 Mouth De-click
- Family ID：8f1bf189fac1
- 本机观测版本：10.4.2
- 格式：VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：restoration-mouth-click
- 次能力方向：lip-smack;click-repair;pre-mix-cleanup
- 当前证据等级：L2
- 验证状态：S3-researched-S4-pending

## 能做什么

- 检测并修复嘴部点击、口水音和 Lip Smack；既可长选区处理也可处理单个事件。
- Frequency Skew 把检测权重偏向低/高频，Click Widening 扩展修复区域以覆盖带衰减的嘴部声音。

## 不建议用来做什么

- 不要用高 Sensitivity 全轨一次性消灭所有短瞬态；硬辅音可能被损伤。
- 不要把爆破、齿音、数字削波和嘴部点击混成同一问题。

## 信号流位置

- Comping 后、压缩/激励前；先处理最明显嘴部点击，再考虑轻量第二遍。
- 用独听移除内容或局部选择检查，避免修复范围覆盖正常辅音。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Sensitivity | 检测多少嘴部点击。 | 从低向上，刚好抓到目标；出现 B/D/G/T 等词头时退回。 |
| Frequency Skew | 将检测偏向低或高频点击；0/正值更面向中频嘴部点击。 | 根据目标点击的频谱位置调整，不凭名称固定拉满。 |
| Click Widening | 扩展点击周围的修复区。 | Lip Smack 有尾巴时小幅增加；短点击不要过宽。 |

## Gain Staging

以未点击的辅音/元音为响度基准；单独记录点击窗口峰值和高频瞬态。修复后的整体更平滑不等于更好，必须确认可懂度未下降。

## 延迟、相位与过采样

插值修复可能改变局部波形；官方未给 RX 10 VST3 延迟。S4 需检查局部瞬态、报告延迟和两遍处理的累积涂抹。

## Mono/Stereo

优先处理单声道干声；分离 Stem 的水声/编码伪影可能被误判为点击，必须降低置信度。

## 适用场景

- 近讲、口腔干燥或高增益录音中的细小口水音。
- 压缩/空气激励后会被显著放大的嘴部点击。

## 路由

- 单轨 Insert 或 RX Connect 局部 Render；严重事件优先局部。
- 完成后再进入 De-esser、压缩和饱和。

## 参数起点

- Sensitivity 2–4 附近试点；Frequency Skew 从 0 向正值寻找嘴部点击中心；Click Widening 保持低到中。
- 若一遍遗漏被掩盖的轻点击，可两遍轻处理，不用一遍极重。

## 调整目标

- 点击退出注意力，但硬辅音边缘与咬字未软化。
- 第二遍只处理首遍后显露的轻点击，不扩大到正常纹理。

## 调整时听什么

- Output Clicks Only/差分中是否包含 B/D/G/T、齿音或元音瞬态。
- 修复处是否出现孔洞、相位化或音节边缘变钝。

## 何时停止

- 点击不再妨碍近距离聆听且差分主要是目标噪声时停止。
- 开始带走硬辅音或使人声失去颗粒细节时退回。

## 常见失败

- Sensitivity 过高破坏爆破音与硬辅音。
- Click Widening 过大涂抹正常音节。
- 把有损编码/分离水声当成嘴部点击反复处理。

## 替代方案

- 手工波形修复、Clip Gain 与短淡化。
- RX De-click 的特定算法用于数字点击，但不是 Mouth De-click 的同义替代。

## 专业案例与工作流线索

- iZotope 官方说明两次较轻处理有时优于一次重处理，因为首遍后会显露被遮蔽的小点击。

## 待执行测试

- 嘴部点击、硬辅音、齿音与数字点击四类事件的差分监听。
- 一遍重处理与两遍轻处理的瞬态、频谱和可懂度对比。
- 分离 Stem 上的误检率与干声对照。

## 已测结果

S4 待执行；当前知识未把旧版控制说明冒充 RX 10 本机回读。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | mouth-click-repair |
| mode | event-detection-interpolation |
| main_controls | sensitivity,frequency_skew,click_widening |
| risk_flags | consonant-damage,transient-smear,separation-artifact |
| validation | target-vs-consonant-difference |

## 来源

- [[sources/音乐制作/插件资料/iZotope/RX 10 Mouth De-click资料|RX 10 Mouth De-click 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]

## 开放问题

- RX 10.4.2 VST3 是否提供 Output Clicks Only，控件范围是否与 RX 6 相同？
- 两遍处理的推荐算法/质量设置在 VST3 中是否可选？
