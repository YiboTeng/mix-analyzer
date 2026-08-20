---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: fbfdbc32d12d
vendor: "Waves"
product: "RVox"
evidence_level: L3
validation_status: passed-l3
batch: B03
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# RVox

## 身份与版本

- 厂商：Waves
- 产品族：RVox
- Family ID：fbfdbc32d12d
- 本机观测版本：12.7.0.209
- 格式：VST2 | VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：compression-vocal-fast
- 次能力方向：gate;workflow-speed
- 当前证据等级：L3
- 验证状态：passed-l3

## 能做什么

- 用 Gate、Compression 与 Output Gain/Ceiling 三个主控制快速整理语音。
- 压缩比等内部参数随 Threshold 实时计算；Energy Meter 与 Total Compression 显示帮助找到动作区。
- Mono/Stereo 组件官方延迟表在 44.1/48 kHz 为 64 samples，随采样率成比例。

## 不建议用来做什么

- 不适合需要显式 Attack/Release/Ratio 或侧链滤波的任务。
- 不要把 Gate 当修复器重切句间噪声和词尾。
- 不要因控制少而默认适合所有声线。

## 信号流位置

- 清理和基础去齿后快速增加密度；Gate 只做轻度句间下压。
- 可作为快速草混或与复杂压缩器对照，判断额外参数是否真有价值。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Compression | 移动阈值并联动内部语音优化的比率/时间行为。 | 下降到响句达到目标 GR，再听轻句是否被过度拉平。 |
| Gate | 按能量检测降低阈值下信号。 | 从关闭开始，仅推到句间噪声退后且尾音完整。 |
| Output Gain / Ceiling | 补偿压缩并限定输出。 | 只做旁通等响度，不用它制造更贴脸错觉。 |
| Energy / Compression Display | 显示输入能量和总压缩。 | 用作动作线索，最终以音节与噪声听感确认。 |

## Gain Staging

Output Gain 必须匹配旁通 Active RMS；Gate 会降低句间平均能量，压缩回补会抬噪声。分别记录语音区与非语音区 RMS。

## 延迟、相位与过采样

Waves 当前技术表列 44.1/48 kHz 64 samples、88.2/96 kHz 128 samples；本机 VST3 Stereo 在 Ableton / 48 kHz 报告 64 samples（1.3 ms），与官方表一致。VST2 与其它采样率未测。官方未给出过采样开关。

## Mono/Stereo

支持 Mono/Stereo。Stereo 组件的检测链接未在简版手册明确；叠唱总线需测声像稳定。

## 适用场景

- 时间紧的 Rap 主唱草混。
- 已经有良好 Clip Gain，只需快速贴脸密度。
- Podcast/旁白或叠唱总线轻压。

## 路由

- 主唱 Insert。
- 作为 Pro-C 2/CL 1B 的效率对照组。

## 参数起点

- Gate 关闭；Compression 下拉到峰值约 3–6 dB 总压缩。
- Gate 只推到句间噪声轻退 3–6 dB，不追求静音。
- Output 还原旁通响度。

## 调整目标

- 主唱快速靠前且尾音、呼吸自然。
- 少参数结果不逊于复杂链时保留简单方案。

## 调整时听什么

- 轻句被抬后噪声/房间感。
- Gate 吞尾音和词头。
- 内部固定行为对某些节奏产生喘振。

## 何时停止

- 动态稳定且无明显门限动作。
- 继续下压只增加密度、噪声和含混时停止。

## 常见失败

- Gate 设太高。
- Output 更响造成偏差。
- 看表不听字尾。
- 把内部算法臆测为固定比率/时间。

## 替代方案

- Pro-C 2：需要显式时间/侧链。
- CL 1B：平滑电平。
- CLA-76：更强峰值与色彩。

## 专业案例与工作流线索

- Waves 把 RVox 定位为三控语音优化器，参数在内部实时计算；卡片只记录可观测控制，不虚构隐藏时间常数。

## 待执行测试

- 不同输入电平下 Compression 旋钮的静态曲线与包络。
- Gate 对词尾、呼吸、噪声的数据集。
- VST2/VST3 与官方 64-sample 延迟核验。

## 已测结果

- 本机 RVox 12.7.0.209 VST3 Stereo / Ableton Live 11.3.43 / 48 kHz 报告 64 samples（1.3 ms），与官方 44.1/48 kHz 表一致。
- Gate -Inf、Gain 0.0 时，Compression 0.0 相对旁路为线性 -0.0873 dB 偏移、相关 1.0；可作本轮近似中性控制，但不是数学上的 0 dB 直通。
- Compression -20 相对中性把五档稳态分别抬高 17.834、16.102、13.426、9.738、5.178 dB；输出对输入斜率 0.471931，对应当前五档局部约 2.119:1 的动态收敛。
- 最高输入档处理峰值达 -0.911 dBFS，全文件 RMS 比中性高 7.735 dB；Compression 同时包含明显回补/靠近 Ceiling 的行为，必须预留 Headroom 并在插件外等响。
- 四个持续音进入稳态 ±1 dB 约 28–80 ms；五个隔离脉冲比中性高约 1.21 dB。该夹具含前序历史，不能反推隐藏 Attack/Release 常数。
- Gate 未做音频实测；词尾、呼吸、噪声和 Stereo Link 仍是明确开放边界。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | vocal-compressor-gate |
| mode | energy-dependent |
| main_controls | gate,compression,output |
| risk_flags | hidden-ballistics,gate-chop,noise-lift,loudness-bias |
| validation | static-curve-tail-latency |

## 来源

- [[sources/音乐制作/插件资料/Waves/RVox资料|RVox 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]
- [[projects/p1-plugin-knowledge-base/validation/reports/fbfdbc32d12d--Waves-RVox|RVox L3 验证]]

## 开放问题

- v12 的 Mono/Stereo 通道联动？
- Compression 控制随输入的实际静态曲线和释放？
