---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: aeaf742fd9a2
vendor: "Softube"
product: "Tube-Tech CL 1B mk II"
evidence_level: L3
validation_status: passed-l3
batch: B03
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Tube-Tech CL 1B mk II

## 身份与版本

- 厂商：Softube
- 产品族：Tube-Tech CL 1B mk II
- Family ID：aeaf742fd9a2
- 本机观测版本：2.5.0.9 | 2.5.9
- 格式：VST2 | VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：compression-opto
- 次能力方向：leveling;tube-color;parallel
- 当前证据等级：L3
- 验证状态：passed-l3

## 能做什么

- 提供 0.5–300 ms Attack、0.05–10 s Release、Threshold、Ratio、Gain 的光学/电子管式电平控制。
- Fixed 为 1 ms/50 ms；Manual 使用旋钮时间；Fixed/Manual 用固定快 Attack，并依节目在快释放与手动释放间过渡。
- Mk II 增加侧链 Low Cut 与 Parallel Compression；VST3 支持外部侧链。

## 不建议用来做什么

- 不要把 Fixed/Manual 误当普通手动 Attack；此时 Attack 旋钮控制延迟转入手动 Release 的时间。
- 不要用慢光学风格承担所有毫秒级尖峰。
- 不要按旋钮钟点复制设置而忽略输入电平和实际 GR。

## 信号流位置

- 可单独做 2–5 dB 平滑电平，也可在 CLA-76 后做第二级较慢稳定。
- 侧链 Low Cut 防爆破/胸腔低频过度触发，但主信号不被滤。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Threshold / Ratio | 决定开始压缩的电平和强度。 | 以 GR 表调 Threshold；Ratio 从低到中等，先让响句 3–5 dB。 |
| Manual Attack / Release | 0.5–300 ms 与 0.05–10 s。 | 人声从中慢 Attack、与节奏匹配的 Release 起。 |
| Fixed | 1 ms Attack、50 ms Release。 | 只在需要快速控制时试，并检查字头。 |
| Fixed/Manual | 快 Attack，短峰快释、长事件转向手动 Release。 | 总线/复杂节目可试；Attack 此时调延迟释放转换而非攻击。 |
| Sidechain Low Cut / Parallel | 降低低频检测权重并混合干湿。 | 爆破触发过多时逐步升 Low Cut；先全湿设压缩再回 Mix。 |

## Gain Staging

Gain 是补偿输出；Parallel 也改变感知响度。以旁通 Active RMS 匹配，记录峰值与响句/轻句 GR；不要因电子管色彩或补偿更响误判平滑。

## 延迟、相位与过采样

本机 VST3 在 Ableton Live 11.3.43 / 48 kHz 报告 4 samples（0.083 ms）；这只是当前宿主、格式和状态的 PDC 读数，不外推到 VST2、其它采样率、外部侧链或其它并行路径。官方手册未给出通用插件延迟或过采样规格。

## Mono/Stereo

Stereo 模式官方说明左右 GR 始终链接，避免声像漂移；Mono 主唱正常使用，Stereo 总线仍需复核相关性。

## 适用场景

- 主唱 3–5 dB 平滑电平。
- CLA-76 后第二级把残余宏动态拉稳。
- 并行增加厚度但保留干声瞬态。

## 路由

- 主唱 Insert，单级或串联第二级。
- 内部 Parallel 或 Aux；不要双重并行。

## 参数起点

- Manual；Ratio 约 2:1–4:1；Attack 10–40 ms；Release 0.1–0.5 s；响句 3–5 dB GR。
- Fixed/Manual 用于更稳的节目相关恢复，先保持低 Ratio。
- Sidechain Low Cut 从关闭开始，仅爆破/胸腔误触发时升。

## 调整目标

- 轻句靠前、响句不跳，仍保留词头。
- GR 在下一重音前基本恢复而不抽动。

## 调整时听什么

- 慢 Release 累积导致句尾持续压低。
- 快 Attack 吞辅音。
- 侧链 Low Cut 过高让低音响句穿出。

## 何时停止

- 宏动态稳定且呼吸/噪声没有被补偿增益明显抬起。
- 继续压缩只让主唱变平和远时停止。

## 常见失败

- 误读 Fixed/Manual。
- Gain 回补过多。
- 串联两级都做深 GR。
- Parallel 相位/补偿未验证。

## 替代方案

- CLA-76：更快更激进控峰。
- Pro-C 2：完整侧链与可视化。
- RVox：更少参数快速密度。

## 专业案例与工作流线索

- Softube 官方应用把 Vocals 的标准压缩目标写为 4–5 dB GR，并强调具体 Threshold/Gain 依输入而定。

## 已执行与剩余测试

- 已覆盖 Fixed 与 Fixed/Manual 的稳态阶梯、隔离瞬态和宿主延迟；Manual 仍待单独验证。
- 串联 CLA-76 前后顺序的等响度盲听。
- 侧链 Low Cut 对爆破与低音元音 GR 的选择性。

## 已测结果

- 固定状态：Threshold -20 dB、Gain 0 dB、Parallel 100%、Sidechain Low Cut Off，其余控制保持默认；旁路、Fixed 与 Fixed/Manual 使用同一 48 kHz 动态阶梯夹具。
- Fixed/Manual 在输入峰值 -30/-24/-18/-12/-6 dBFS 的稳态净增益为 -0.326/-4.746/-9.409/-14.078/-18.710 dB，局部输出斜率 0.231520（等效比约 4.32:1）；五个隔离瞬态相对旁路为 +0.589/+1.863/+1.863/+1.863/+1.863 dB。
- Fixed 的五档稳态净增益为 -0.015/-3.288/-7.528/-11.932/-16.431 dB，局部输出斜率 0.308584（等效比约 3.24:1）；五个隔离瞬态约 -2.641 dB。
- 在本轮固定历史中，Fixed 对短峰比 Fixed/Manual 再低约 3.23–4.50 dB；Fixed/Manual 对持续阶梯反而更深约 0.31–2.28 dB。前者支持 Fixed 更强地约束短峰，后者体现节目相关释放与历史记忆，不能简化成“某模式总是压得更多”。
- -24 至 -6 dBFS 阶梯进入稳态 ±1 dB 的时间约为 Fixed 30–84 ms、Fixed/Manual 110–172 ms；这是整个检测/释放历史下的输出稳定时间，不是把官方 1 ms Attack 重新测成几十毫秒。
- Fixed/Manual 的隔离脉冲峰值高于旁路是实测传输结果；本轮未分离检测器、释放记忆、模拟建模和输出路径，不把它归因为某一个机制。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | opto-tube-compressor |
| mode | manual-fixed-fixedman |
| main_controls | threshold,ratio,attack,release,gain,sc_lowcut,parallel |
| risk_flags | mode-misread,release-buildup,loudness-bias |
| validation | mode-envelope-stereo-link |

## 来源

- [[sources/音乐制作/插件资料/Softube/Tube-Tech CL 1B mk II资料|Tube-Tech CL 1B mk II 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]
- [[projects/p1-plugin-knowledge-base/validation/reports/aeaf742fd9a2--Softube-Tube-Tech-CL-1B-mk-II|Tube-Tech CL 1B mk II L3 验证]]
- [[projects/p1-plugin-knowledge-base/validation/results/aeaf742fd9a2--dynamics-cl1b-mode.json|量化结果 JSON]]

## 开放问题

- 本机两个版本对应格式还是重复组件？
- VST3 Sidechain 与 Parallel 的延迟/相位？
