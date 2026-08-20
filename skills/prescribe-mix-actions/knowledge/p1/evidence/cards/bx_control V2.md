---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: 1034f31ae5fd
vendor: "Plugin Alliance"
product: "bx_control V2"
evidence_level: L3
validation_status: S4-host-validated-passed
batch: B04
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# bx_control V2

## 身份与版本

- 厂商：Brainworx / Plugin Alliance
- 产品族：bx_control V2
- Family ID：1034f31ae5fd
- 本机文件系统版本：2.0.0.0 | 2.10.0.0 | 2.3.0.0
- 本轮组件：VST3；GUI 未显示精确小版本
- 当前证据等级：L3
- 验证状态：S4-host-validated-passed

## 能做什么

- M/S Matrix、0–400% Stereo Width、20 Hz–22 kHz Mono Maker、L/R/M/S Solo、L/R Flip、Balance/Pan 与 Peak/RMS Meter。
- Width 调整 Side 相对 Mid；100% 为透明基线，0% 收至 Mono。它不会给真正的 Mono 信号创造 Side。
- Mono Maker 把阈值以下的 Side 强烈收束，并补偿潜在低频能量损失；适合低频相位管理。
- 可用一对实例完成 L/R↔M/S 编解码，让中间 Stereo 插件分别处理 M 与 S；官方与本机均支持零延迟定位。

## 不建议用来做什么

- 不要在 Mono 主唱轨用 Width 创造不存在的宽度。
- 不要把 Mono Maker 当高通、Bass Enhancer 或总线修复万能键。
- 不要把 200–400% Width 当默认修正；相关性下降和中心变薄应先于“更宽”被处理。

## 信号流位置

- 放在 Doubler、MicroShift、PS22、Chorus 或 Reverb/Delay 返回末端做诊断与低频收束。
- Backing Vocal/FX Bus 可轻调 Width/Mono Maker；主唱干声中心通常只监测。
- 需要 M/S 插件链时，以 Encoder → 中间处理 → Decoder 成对使用。

## 路由

- Stereo Vocal FX/Backing Bus 末端：轻调 Width 或 Mono Maker，并在 Mono 下复核。
- 成对 M/S 链：第一实例编码、最后实例解码；中间处理不得改变通道含义。
- Mix Bus 默认只监测；若实际处理，必须保存旁路对照并确认所有 Solo/Flip/Phase 状态复位。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Stereo Width 0–400% | 调整 Side/Mid 比；100%不变，0% Mono。 | 从 100% 小幅到 110–130%，同时查 Correlation 与 Mono。 |
| Mono Maker 20 Hz–22 kHz | 阈值以下收束 Side并补偿低频。 | 总线从 60–120 Hz 试；过高会削掉可听宽度主体。 |
| Solo M/S/L/R | 把所选成分相位校正后送到两只扬声器。 | Solo S 检查低频、齿音与主唱核心泄漏，完成后复位。 |
| Solo in Place | 按原位置监听所选元素。 | 只用于定位问题，不留在导出。 |
| Input/Output L/R-M/S | 编码、解码或格式声明。 | 常规保持 L/R；M/S 链必须成对恢复。 |
| Balance / Pan M / Pan S | 调中心与 M/S 位置。 | 先判断来源是否真的偏，再修正；不凭表针盲调。 |

## Gain Staging

Width 与 Mono Maker 会改变 Side/Mid 能量。至少记录 Mid RMS、Side RMS、总 Stereo RMS、Correlation 和 Mono Fold；宽度判断前先确认中心主体未因 Side 变化而被响度错觉掩盖。

## 调整目标

- 让 Side 支持空间感而中心主体、低频重量与 Mono Fold 基本稳定。
- 只收束确实需要居中的低频 Side，不把宽化主体或空间尾巴整体折进中心。
- 任何 Matrix、Solo、Flip、Phase 状态都应可解释且可复现。

## 延迟、相位与过采样

- 本机 Ableton 状态栏：0 samples。
- 默认与旁路最佳整数延迟：0 samples；RMS 电平差 0.0 dB，残差 RMS -141.487198 dBFS。
- 没有过采样控制；Mono Maker 本身是频率相关处理，端点 Mono 不等同普通声像旋钮。

## Mono/Stereo

只对 Stereo 输入有生成性意义。Width=0% 实测 Side -147.503431 dBFS、L/R 相关 0.999999999999，Mid 完全保持；Mono Maker 5.82 kHz 对 440 Hz 夹具把 Side 相对旁路降低 45.257409 dB。

## 适用场景

- 诊断 Doubler/MicroShift/PS22 返回。
- Backing Vocal 或 FX Bus 轻宽化/收束。
- 低频 Side 管理与 M/S 编解码。
- 快速监听 Left、Right、Mid、Side 的内容归属。

## 参数起点

- 监测基线：Width 100%、Mono Maker Off、L/R in/out、所有 Solo/Flip/Phase 关闭。
- Vocal FX/Backing Bus：Width 110–130%，Mono Maker 60–120 Hz 起步。
- Master/总线：优先只用 Mono Maker 60–100 Hz，小步上调；任何明显宽度损失都应回退。

## 调整时听什么

- 相关性、中心稳定、低频重量与 Mono Fold-down。
- Solo S 中是否有主唱主体、齿音或应留在中心的低频。
- Matrix/solo 状态是否误留，Pan M/Pan S 是否造成声像偏移。

## 何时停止

- Stereo 获得所需宽度或低频稳定，而 Mono 主体与中心定位基本不变。
- 再提高 Width/Mono Maker 开始让中心变薄、空间主体消失或相关性恶化时停止。

## 常见失败

- 在 Mono 主唱轨上旋 Width，期待凭空变宽。
- Mono Maker 设到过高，把和声、Reverb 或宽化主体一起折进中心。
- L/R↔M/S 只编码不解码。
- Solo、Phase Reverse、L/R Flip 或 Solo in Place 遗留导出。

## 替代方案

- Studio One 原生方向/相关表：基本宽度和相位检查。
- MetricAB/Insight 2：更全面测量，不替代这里的路由控制。
- MicroShift/Doubler/PS22：生成 Side；bx_control 只管理已有 Side。

## 专业案例与工作流线索

- 官方手册要求高 Width 时同时关注 Correlation；本卡进一步把 Mono Fold-down 与中心稳定列为强制检查。
- Mono Maker 的阈值不是“更高越安全”：应从低频问题的实际频带出发，逐步上调到改善刚出现，再回退到最小有效值。
- 诊断顺序优先 Solo S → Mono Fold → 等响 Stereo A/B，避免只看宽度表或相关表作结论。

## 已执行与剩余测试

- 已完成：默认 vs 旁路 Null/延迟；Width 0% 端点；Mono Maker 117 Hz 高于截止控制组与 5.82 kHz 阈值内极限；48 kHz VST3 宿主 PDC。
- 剩余：Width 130/200/400% M/S 增益映射；60–200 Hz 多频 Side 扫频与能量补偿；VST2/其它版本、自动化、其它采样率、CPU、所有 Solo/Matrix 组合与连续人声盲听。

## 已测结果

默认与旁路直接相关 1.0、0 samples、0.0 dB，残差 RMS -141.487198 dBFS。Width 0% 保持 Mid、Side 降至 -147.503431 dBFS。Mono Maker 117 Hz 对 440 Hz 夹具 Side 仅 -0.021483 dB；5.82 kHz 则把整体 Side 降低 45.257409 dB，L/R 相关升至 0.999955940103。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | stereo-ms-utility |
| mode | lr-ms-matrix |
| main_controls | width,mono_maker,solo,pan,balance,matrix |
| risk_flags | mono-loss,phase,monitor-state,matrix-error |
| validation | null,latency,ms-gain,correlation,mono-maker |

## 来源

- [[sources/音乐制作/插件资料/Plugin Alliance/bx_control V2资料|bx_control V2 资料]]
- [[projects/p1-plugin-knowledge-base/validation/reports/1034f31ae5fd--Plugin-Alliance-bx-control-V2|bx_control V2 L3 验证]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]

## 开放问题

- 本机多个旧版 VST3/VST2 路径中，Studio One 实际实例化的是哪个精确小版本？
- 60–200 Hz 多频 Side 输入下，Mono Maker 的转折斜率与低频能量补偿曲线如何？
