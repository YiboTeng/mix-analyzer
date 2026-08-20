---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: 5d8d036ccd33
vendor: "FabFilter"
product: "Pro-DS"
evidence_level: L3
validation_status: passed-l3
batch: B02
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Pro-DS

## 身份与版本

- 厂商：FabFilter
- 产品族：Pro-DS
- Family ID：5d8d036ccd33
- 本机文件版本：1.2.1.0；界面回读：1.21 (64-bit), June 29, 2023
- 格式：VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：deessing-wide-split
- 次能力方向：single-vocal;allround
- 当前证据等级：L3
- 验证状态：passed-l3

## 能做什么

- Single Vocal 模式区分齿音与非齿音；Allround 按 2–20 kHz 侧链范围与阈值触发。
- Wide Band 检出齿音时压低全频，Split Band 只衰减自动分频以上高频。
- Threshold、Range、侧链 HP/LP、Trigger/Sidechain Audition、Lookahead、Stereo Link 与外部侧链构成完整检测和处理链。

## 不建议用来做什么

- 不要只把频率范围对准 8–10 kHz；不同声线、麦克风和辅音位置不同。
- 不要为了看到持续 GR 把 Threshold 压得过低，除非明确需要近恒定齿音衰减。
- 不要把 Split Band 默认视为更透明；单人主唱 Wide Band 有时更自然。

## 信号流位置

- 基础修正后、激励和明亮 EQ 前先控制原始齿音；若后级重新生成刺耳，再在链尾加轻度第二阶段。
- 严重失真的人声可用原始干声作外部侧链改善检测。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Threshold | 滤波侧链超过阈值时触发。 | 用 Audition Triggering 降到捕获 S/T/CH 而尽量不抓普通元音。 |
| Range | 限制最大衰减量。 | 先 2–4 dB；最坏齿音仍跳出再加，不靠 Threshold 同时决定深度。 |
| HP/LP Sidechain | 限定 2–20 kHz 检测范围。 | Sidechain Audition 中从宽到窄，保留目标齿音而排除元音/军鼓泄漏。 |
| Single Vocal / Allround | 人声专用分类或通用频带触发。 | 独唱先 Single Vocal；总线、混音或特殊高频限制才 Allround。 |
| Wide / Split Band | 全频衰减或仅高频衰减。 | 独唱先 Wide 比较自然度；低频主体不应随齿音下沉时试 Split。 |
| Lookahead | 提前最多 15 ms 处理齿音起始。 | 官方建议人声约 10 ms 是常用起点；若 S 失去自然起始则减少。 |

## Gain Staging

De-essing 降低局部响度，不应以整体更柔和即更好。用相同句子对齐 Active RMS/峰值，输出补偿只做等响度；Audition 模式关闭后再判断词义和明亮度。

## 延迟、相位与过采样

本机 48 kHz 实测：Wide + Lookahead 12 ms + OS Off 为 720 samples / 15.0 ms；Split 同状态为 1232 samples / 25.7 ms。Lookahead 旋钮即使为 0.000 ms，只要模块仍启用，宿主仍报 720 samples；真正关闭模块且 Wide/OS Off 才为 0 samples。Lookahead Off 下 2x/4x OS 为 34/40 samples。

## Mono/Stereo

Stereo Link 与 Mid/Side 可控制检测/处理联动；单主唱优先链接，Backing Vocal 或 Side 处理要防声像抖动。Mono 实例不需要立体声策略。

## 适用场景

- 近讲主唱的 S/T/CH 偶发过亮。
- 激励前预控齿音和链尾二次轻控。
- Backing Vocal 总线或全混高频瞬态限制。

## 路由

- 主唱 Insert；通常在 Air EQ/Exciter 前。
- 失真人声可由干净分轨外部侧链触发。

## 参数起点

- Single Vocal + Wide Band；Range 2–4 dB；Lookahead 约 5–10 ms。
- 侧链先覆盖约 4–12 kHz，再用 Audition 缩窄；不是固定频率答案。
- 链尾第二阶段只做 1–2 dB 峰值控制。

## 调整目标

- 最尖锐齿音退回元音之后，但辅音仍可辨。
- 普通明亮元音和气声不持续被压。

## 调整时听什么

- lisp、咬舌、S 开头消失。
- Wide Band 造成整个人声随 S 下沉；Split 造成高频光泽抽动。
- Trigger Audition 是否包含普通词头。

## 何时停止

- 齿音不再刺穿伴奏且语义清晰。
- 再加 1 dB Range 只让说话含混或暗淡时回退。

## 常见失败

- 阈值过低导致持续动作。
- Sidechain 过宽误抓元音。
- 多级去齿加动态 EQ/soothe 叠加。
- Lookahead 过长/处理过深抹掉自然辅音。

## 替代方案

- Eiosis E2Deesser：更多语音检测模式与频谱塑形。
- Pro-Q 3 动态 Bell：单一窄齿音频率。
- soothe2：齿音伴随多处移动共振。

## 专业案例与工作流线索

- FabFilter 官方建议独唱先 Single Vocal，并指出 Wide Band 在独唱上常更自然；约 10 ms Lookahead 是起点而非硬规则。

## 后续可扩展测试

- 不同性别/音高的 S/T/CH、气声与明亮元音标注集。
- Wide/Split、Lookahead 0/5/10/15 ms 的等响度盲听与延迟测量。
- 外部干声侧链对失真人声的检测精度。

## 已测结果

- Ableton Live 11.3.43 / 48 kHz 中真实加载 Pro-DS 1.21 VST3 Stereo；默认 Threshold -36 dB、Range 6 dB、Single Vocal、Wide、约 7–14 kHz、Lookahead 12 ms、OS Off。
- 复合夹具三个短促源事件：Wide + LA 12 ms 相对旁路为 -1.158/-0.992/-0.747 dB；Split 为 -1.022/-0.877/-0.662 dB。
- 8–20 秒稳定多音在 Wide/Split 下均约 0.000 dB 变化，说明当前 Single Vocal 默认态没有持续误触发该非语音夹具。
- 关闭 Lookahead 模块后三个短事件与旁路在约 ±0.000002 dB 内一致；当前夹具需要 Lookahead 才抓到事件起始。
- 1037 个高于 -70 dBFS 的 50 ms 活跃窗中，Wide/Split 各仅 3 个达到 ≥0.05 dB 衰减，Lookahead Off 为 0 个。
- 证据：[[projects/p1-plugin-knowledge-base/validation/reports/5d8d036ccd33--FabFilter-Pro-DS|Pro-DS L3 验证]]；量化 `validation/results/5d8d036ccd33--composite-deesser-wide-split-lookahead.json`。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | de-esser |
| mode | single-vocal-wide-or-split |
| main_controls | threshold,range,sidechain_hp_lp,lookahead,stereo_link |
| risk_flags | lisp,over-trigger,brightness-pumping |
| validation | composite-source-event-lookahead-latency |

## 来源

- [[sources/音乐制作/插件资料/FabFilter/Pro-DS资料|Pro-DS 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]

## 开放问题

- 真实标注人声上，不同歌手/音素的检测 Precision/Recall、lisp 与可懂度边界？
- Studio One 中外部侧链与 Mid/Side 端口如何显示？
