---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: 0072a637f389
vendor: "FabFilter"
product: "Saturn 2"
evidence_level: L3
validation_status: S4-host-validated-passed
batch: B04
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Saturn 2

## 身份与版本

- 厂商：FabFilter
- 产品族：Saturn 2
- Family ID：0072a637f389
- 本机观测版本：2.0.8.0
- 格式：VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：saturation-multiband
- 次能力方向：modulation;parallel
- 当前证据等级：L3
- 验证状态：S4-host-validated-passed

## 能做什么

- 最多 6 个自由频段，每段独立 Style、Drive、Mix、Feedback、Dynamics、Tone、Level。
- 覆盖 Tube/Tape/Transformer/Amp 到 Foldback/Bitcrush 等大量风格，并可用 Envelope/LFO/XY/MIDI 调制。
- Good 8x、Superb 32x OS 降低混叠；Linear Phase 作用于分频与 HQ 路径。

## 不建议用来做什么

- 不要默认多段比单段更好；分频增加相位/延迟变量。
- 不要开 Unrestricted Feedback 后离线无人监控。
- 不要把 Drive 自动补偿当严格等响度。

## 信号流位置

- 单段轻饱和先作为基准；只在需要分频定向失真时加 Band。
- 高频激励/饱和后复查去齿；低频段 Drive 需防胸腔和爆破失真。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Style / Drive | 选择非线性算法并推驱；Drive 自动一定程度回调输出。 | 先单段 Subtle Tube/Tape 低 Drive，固定响度再换 Style。 |
| Band Mix / Tone / Level | 每段并行、谐波频谱与输出。 | 先 Mix 100%识别，再回比例；Level 只校准。 |
| Feedback / Dynamics | 反馈产生共振；Dynamics 向右压缩、向左扩展。 | 混音轻用或关闭，创意效果另建轨。 |
| HQ / Linear Phase | 8x/32x OS 与线性相位分频。 | 实时先 Off/Good，导出比较；Linear 只在相位叠加有证据时。 |
| M/S / Modulation | 以中侧通道和调制改变参数。 | 主唱默认 L/R 无调制；效果返回才逐项引入并测 Mono。 |

## Gain Staging

Drive 有自动输出调节但不保证 LUFS 一致。关闭/固定 Global Mix，用 Input/Output 匹配旁通；多段分别测 THD、频响和段间总电平。

## 延迟、相位与过采样

Good=8x、Superb=32x，增加 CPU/延迟；Linear Phase 处理分频和 HQ OS，但其他 Tone/模型仍保留角色相位。本机 VST3 默认 Warm Tape、HQ/Linear 关闭时，Ableton 设备栏实测 `Latency: 0 samples`；Good/Superb/Linear 仍待单独量化。

## Mono/Stereo

L/R 与 M/S 可选。单声道主唱不要无意义 M/S；立体声 M/S Drive/Pan 必须检查相关性和声像。

## 适用场景

- 单段透明/暖管增稠。
- 只对 2–8 kHz 增加谐波、保持低频稳定。
- Ad-lib 多段极端角色。

## 路由

- 主唱 Insert 轻饱和。
- 效果 Aux 或复制轨做多段/调制。

## 参数起点

- 单段 Subtle Tube/Tape，Drive 1–3 dB，Mix 10–40%。
- 多段仅两段：低频近干，高中频轻 Drive。
- HQ Good 作为导出候选，先与 Off 盲听。

## 调整目标

- 指定频段增加密度，不把齿音和底噪变前景。
- OS 收益超过 CPU/延迟代价。

## 调整时听什么

- 分频相位、前振铃、别名。
- Dynamics/Feedback 意外泵动或自激。
- M/S 声像漂移。

## 何时停止

- 单段已达目标就不加频段。
- 继续复杂化只增加参数而无盲听收益时停止。

## 常见失败

- 全频多段重饱和。
- 32x 默认。
- Unrestricted Feedback 遗留。
- M/S/调制无法归因。

## 替代方案

- Decapitator：更快五风格。
- HG-2：管式串并联。
- Fresh Air：只做高频激励。

## 专业案例与工作流线索

- FabFilter 官方说明 Linear Phase 只覆盖分频/HQ 而非所有内部滤波；不能把它描述为全插件线性相位。

## 待执行测试

- 默认单段 Warm Tape 脉冲传输已完成；继续补双段与 Linear 分频脉冲和 Null。
- Style/Drive THD、别名、动态映射。
- 8x/32x CPU、延迟和盲听。

## 已测结果

Ableton Live 11.3.43 / Saturn 2 2.0.8 VST3 默认单段 Warm Tape、Mix 100%、Output 0 dB、HQ/Linear 关闭：宿主报告 0 samples 延迟；三档输入脉冲 -1.938/-6.021/-12.041 dBFS 对应输出 -8.530/-10.371/-15.424 dBFS，峰值增益 -6.591/-4.351/-3.382 dB，范围 3.209 dB；最佳整数偏移均为 0 samples，直接相关 0.673004。说明默认状态已经对强瞬态做电平依赖软化，不能视为中性旁通。证据见 [[projects/p1-plugin-knowledge-base/validation/reports/0072a637f389--FabFilter-Saturn-2|Saturn 2 L3 验证]]。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | multiband-saturator |
| mode | single-or-multiband |
| main_controls | bands,style,drive,mix,feedback,dynamics,tone,hq |
| risk_flags | aliasing,crossover-phase,feedback,complexity |
| validation | thd-os-crossover |

## 来源

- [[sources/音乐制作/插件资料/FabFilter/Saturn 2资料|Saturn 2 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]
- [[projects/p1-plugin-knowledge-base/validation/reports/0072a637f389--FabFilter-Saturn-2|Saturn 2 L3 验证]]

## 开放问题

- 本机 2.0.8.0 各 HQ/Linear 报告延迟和 CPU？
