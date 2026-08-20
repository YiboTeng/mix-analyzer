---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: a3005d9763bc
vendor: "FabFilter"
product: "Pro-C 2"
evidence_level: L3
validation_status: passed-l3
batch: B03
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Pro-C 2

## 身份与版本

- 厂商：FabFilter
- 产品族：Pro-C 2
- Family ID：a3005d9763bc
- 本机观测版本：2.1.7.0
- 格式：VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：compression-flexible
- 次能力方向：clean;sidechain;parallel
- 当前证据等级：L3
- 验证状态：passed-l3
- 本机已验证实例：FabFilter Pro-C 2 2.1.7.0，VST3 Stereo；Ableton Live 11.3.43/48 kHz

## 能做什么

- 八种压缩 Style，包括 Vocal、Clean、Classic、Opto、Mastering、Bus、Punch、Pumping。
- 提供 Threshold、Ratio、Knee、Range、Attack、Release/Auto、Lookahead 最多 20 ms、Hold、Wet/Dry 与 Auto Gain。
- Sidechain HP/LP/可调 Bell、Audition、外部侧链、Stereo Link 与 M/S 处理；最高 4x Oversampling。

## 不建议用来做什么

- 不要把当前 Pro-C 3 的 Character、32x OS、Auto Threshold 等功能写回 Pro-C 2。
- 不要依赖 Auto Gain 做严格响度匹配。
- 不要同时用极快时间、高 Ratio、大 Range 和高 OS 后忽略延迟/失真。

## 信号流位置

- 作为透明或可控主压缩器；前有清理/修正 EQ，后接色彩或第二级。
- 外部侧链可用于伴奏/效果 duck；内部 Sidechain EQ 只改变检测，不直接 EQ 主信号。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Style | 选择不同静态/动态曲线和节目行为。 | Vocal 快速起点；Clean 做基准；Opto/Classic 比较色彩。 |
| Threshold / Ratio / Range / Knee | 定义触发、比例、最大 GR 与过渡。 | 先 Range 限 3–6 dB，再设 Ratio/Threshold；软 Knee 提高渐进性。 |
| Attack / Release / Auto | 控制 GR 建立和恢复；Auto 增加节目依赖。 | 从 10–30 ms Attack、50–200 ms Release 起，按字头和节奏调。 |
| Lookahead / Hold | 提前捕捉峰值并延长 GR 峰。 | 透明控峰加 0–5 ms；需要零延迟关闭；Hold 只在抖动时小加。 |
| Sidechain EQ / Stereo Link | 筛选检测频率并联动声道。 | HP 防爆破误触发；Stereo 总线从高 Link 起。 |

## Gain Staging

关闭 Auto Gain 做实验，以 Output/Wet Gain 匹配旁通 Active RMS；Dry/Wet 并行先保证全湿设置本身无削波。记录 GR 分布而非只看最大值。本机 `Default Setting` 的 Auto Gain 为黄色启用态：低档回补约 +4.8 dB，五个隔离瞬态都被推到约 0 dBFS，是不能直接用默认态做透明比较的实测理由。

## 延迟、相位与过采样

本机 UI Lookahead Off、OS Off 时 Ableton 报告 0 samples。一次宿主映射探针把 Ableton 暴露的 Lookahead 推到 20.00 ms，但 Pro-C 2 UI 仍为 Off，导出与默认态只在约 -141.48 dBFS 的抖动底噪处不同；因此本机必须以插件 UI 回读和音频差分确认 Lookahead，不能只信宿主暴露旋钮。2x/4x OS、真实 UI Lookahead 与并行相位仍未验证。

## Mono/Stereo

Mono 禁用 Stereo 控制。Stereo Link 降低可保留单边短峰，但会改变声像；主唱总线先 100% Link。

## 适用场景

- 透明主唱电平压缩。
- Vocal Style 快速贴脸。
- Sidechain EQ 防爆破触发。
- 外部侧链 duck 混响/伴奏。

## 路由

- 主唱 Insert 主压缩。
- 伴奏或效果返回外部侧链。
- 内部 Dry/Wet 或 Aux 并行。

## 参数起点

- Vocal/Clean；Ratio 2:1–4:1；Range 3–6 dB；Attack 10–30 ms；Release 60–180 ms；先关闭 Auto Gain。
- Sidechain HP 80–150 Hz 仅在低频误触发时。
- Lookahead 0–2 ms 混音起点；追求峰值透明再上推。

## 调整目标

- GR 随短句动作，字头和节奏保留。
- 不同 Style 的差异在等响度后仍有用。

## 调整时听什么

- Attack 太快吞字头，太慢漏峰。
- Release 与音节不同步产生喘动。
- SC HP 过高让低音响句穿出。
- Auto Gain 偏差。

## 何时停止

- 主唱稳定且仍有微动态。
- 增加参数复杂度不再改善诊断目标。

## 常见失败

- 把 v3 功能倒灌。
- Auto Gain 未关闭。
- Range 不限导致意外深压。
- Dry/Wet 和 Lookahead 造成并行相位问题。

## 替代方案

- RVox：极简效率。
- CLA-76：FET 色彩。
- CL 1B：光学平滑。

## 专业案例与工作流线索

- FabFilter v2 官方发布把 Vocal Style、Range、Lookahead、Hold、Sidechain EQ 和 4x OS 定义为 v2 边界，本卡据此排除 v3 功能。

## 待执行测试

- 八 Style 的同 GR 静态/动态曲线与盲听。
- Auto Gain Off 下的 Attack/Release/真实 UI Lookahead 阶跃与瞬态测试。
- Auto Gain 误差、OS 混叠和延迟。

## 已测结果

- 默认宿主回读：Clean、Threshold -18.00 dB、Ratio 4:1、Attack 0.255 ms、Release 209.2 ms、Knee +18 dB、Range +60 dB、Hold 0 ms、Auto Release Off、Output/Wet Gain 0 dB、Mix 100%、OS Off、UI Lookahead Off；Auto Gain 为启用态。
- 五档输入峰值 -30/-24/-18/-12/-6 dBFS 的默认稳态净增益为 +4.836/+4.735/+3.440/+0.687/-3.282 dB；输出对输入局部斜率 0.66185。这个局部斜率不等于面板标称 4:1。
- 只在插件 UI 把 Attack 0.255 改到 75.19 ms 后，稳态净增益变为 +0.539/+0.480/-0.456/-2.684/-6.097 dB，五个隔离瞬态比默认低 2.325–2.345 dB。默认 Auto Gain 造成明显整体回补差异，所以不能把结果简化为慢 Attack 的纯包络方向；正确比较要先关 Auto Gain 并等响。
- Ableton 暴露 Lookahead 20.00 ms 但插件 UI 仍 Off；渲染对默认空差 RMS -141.48 dBFS、估计延时 0 samples。只记为宿主映射失败，不记为 Lookahead DSP 结论。
- 当前处理态 L-R 残差约 -141.5 dBFS；仅支持双单声道输入下左右一致，未证明 Stereo Link/M/S。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | digital-compressor |
| mode | multi-style |
| main_controls | style,threshold,ratio,knee,range,attack,release,lookahead,hold |
| risk_flags | version-leak,autogain-bias,over-compression,latency |
| validation | style-envelope-os-latency |

## 来源

- [[sources/音乐制作/插件资料/FabFilter/Pro-C 2资料|Pro-C 2 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]
- [[projects/p1-plugin-knowledge-base/validation/reports/a3005d9763bc--FabFilter-Pro-C-2|Pro-C 2 L3 验证]]

## 开放问题

- Auto Gain Off、等响条件下八 Style 的静态/动态差异？
- Studio One 与真实插件 UI Lookahead/OS 的延迟、自动化和外部侧链映射？
