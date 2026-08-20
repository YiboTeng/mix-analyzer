---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: efa4ad9005f3
vendor: "Valhalla DSP, LLC"
product: "ValhallaPlate"
evidence_level: L3
validation_status: S4-validated-Ableton-temporary-host
batch: B05
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# ValhallaPlate

## 身份与版本

- 厂商：Valhalla DSP, LLC
- 产品族：ValhallaPlate
- Family ID：efa4ad9005f3
- 本机观测版本：1.6.3
- 格式：VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：reverb-plate
- 次能力方向：vocal-plate;diffusion
- 当前证据等级：L3
- 验证状态：S4-validated-Ableton-temporary-host

## 能做什么

- 多种板式算法，以高密度、明亮尾部和可调金属/平滑模态为核心。
- Predelay、Decay、Size、Width、Low/High Shelf、Mod Rate/Depth 与 Mix Lock。
- Decay 显示主要对应约 2.9–3.6 kHz 的 RT60，不代表所有频率尾长。

## 不建议用来做什么

- 不要把显示 Decay 当全频统一 RT60。
- 不要在主唱 100% Insert 使用。
- 不要 Width >100% 后忽略 Mono。

## 信号流位置

- 100% Wet Aux；低切返回并缩短高频尾，必要时 duck。
- Plate 常提供密度，Predelay 保留主唱前景。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Mode | 改变板式模态、频率衰减和调制。 | 从 Smooth/Chrome 类候选逐个等响度，按本机模式名回读。 |
| Decay / Size | 中频 RT60 与模态密度；大 Size 更平滑。 | 先 Decay 配节奏，金属感强再加 Size。 |
| Predelay | 混响进入前间隔。 | 20–80 ms 分离词头。 |
| Low/High Shelf | 温和输出音色；行为会随 Decay/Mode 变化。 | 低频减量、高频按齿音和空间亮度调。 |
| Mod / Width / Mix Lock | 减金属并控制湿声宽度/干湿。 | 自然用低调制；Aux 100% Wet并锁。 |

## Gain Staging

按 Wet RMS 和 Send 电平记录；Mode/Size 比较时匹配湿声响度和 Decay。

## 延迟、相位与过采样

官方未列延迟/OS；调制目的之一是减金属而非制造明显 Chorus。S4 测脉冲与 PDC。

## Mono/Stereo

Width 100% 为典型双 Pickup；0%混合输出，>100%超宽。主唱 Aux 优先 70–100%，全程 Mono Fold-down。

## 适用场景

- 主唱密集明亮板式。
- Backing Vocal 更长更宽。
- 短板式增加存在感。

## 路由

- Stereo Aux 100% Wet。
- 链后 EQ/Duck。

## 参数起点

- Decay 0.8–1.8 s、Predelay 30–70 ms、Size 100–150%、Width 70–100%。
- Low Shelf 150–250 Hz 下减，高频按齿音调。

## 调整目标

- 尾部有密度但干声仍前。
- 高频光泽不复制完整齿音。

## 调整时听什么

- 金属 ring、齿音尾、低频长尾。
- Width 超宽相消。

## 何时停止

- 板式质感支持主唱而不独立成声源。
- 下一句被尾巴覆盖时缩 Decay/高频尾。

## 常见失败

- Decay 读数全频化。
- Width >100默认。
- Aux 不锁 Mix。
- 调制太深 Chorus。

## 替代方案

- VintageVerb Plate/Smooth Plate。
- Pro-R Decay Rate EQ。
- Abbey Road Chambers。

## 专业案例与工作流线索

- Valhalla 官方明确 Decay 是中频 RT60且频率曲线依 Mode；因此 L3 必须测分频尾长。

## 待执行测试

- 模式×Decay 的分频 RT60。
- Size/Mod 金属度与相关性。
- Width/Mono 和 Predelay 可懂度。

## 已测结果

- [[projects/p1-plugin-knowledge-base/validation/reports/efa4ad9005f3--ValhallaPlate|S4 默认 Chrome 全湿脉冲验证]]：本机 1.6.3、Mix 100%、Predelay 0 ms、Decay 3.0 s、Size/Width 100%。
- 首脉冲 onset 21.229 ms、拟合 T60 2.4174 s；全湿相关系数 0.027008、Side/Mid -0.2356 dB，旁通为 1.0、-92.7012 dB。
- 默认尾部跨过 2 s 间隔；Predelay=0 不等于算法瞬时输出。未做听感等响，Peak/RMS 不用于音质优劣判断。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | plate-reverb |
| mode | multi-plate |
| main_controls | mode,predelay,decay,size,width,eq,mod,mix |
| risk_flags | metallic-ring,sibilant-tail,mono-loss |
| validation | band-rt60-width |

## 来源

- [[sources/音乐制作/插件资料/Valhalla DSP, LLC/ValhallaPlate资料|ValhallaPlate 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]

## 开放问题

- 本机 1.6.3 模式列表与报告延迟？
