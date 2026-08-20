---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: 0c0769036773
vendor: "Slate Digital"
product: "Fresh Air"
evidence_level: L3
validation_status: S4-passed-l3
batch: B02
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Fresh Air

## 身份与版本

- 厂商：Slate Digital
- 产品族：Fresh Air
- Family ID：0c0769036773
- 本机观测版本：1.1.1
- 格式：VST2 | VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：exciter-air
- 次能力方向：presence;parallel-brightness
- 当前证据等级：L3
- 验证状态：S4-passed-l3

## 能做什么

- 以 Mid Air 提升高频中段存在感、High Air 提升超高频细节；两旋钮可 Link 联动。
- 基于多级并行动态过程和经典 Dolby-A 改装式激励思路，不等同于普通 Shelf EQ。
- Trim 用于补偿动态处理造成的整体增益，输出表同时显示 Peak 与 RMS 并提供削波指示。

## 不建议用来做什么

- 不要用它修复单一窄共振或尖锐齿音。
- 不要因界面简单就忽略电平、噪声、点击和齿音被抬高。
- 不要把旋钮百分比解释为固定 dB Shelf。

## 信号流位置

- 通常放在基础清理与第一阶段去齿后；若 Mid/High Air 重新激发齿音，在其后补轻度 De-esser。
- 可在压缩后作为颜色，避免高频激励先改变压缩器触发；也可前置做实验但要重新调压缩。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Mid Air | 动态提升高频中段和 Presence。 | 从 5–15% 起，咬字不足才上推；鼻尖/硬感出现则回退。 |
| High Air | 动态提升更高频细节和空气。 | 从 5–20% 起，关注 S、底噪和嘴部点击。 |
| Link | 锁定两 Air 旋钮一起移动。 | 先分别找边界；只有需要整体联动微调时 Link。 |
| Trim | 补偿动态处理带来的输出增益。 | 以旁通 Peak/RMS 和感知响度回调，避免超过 0 dBFS。 |

## Gain Staging

官方明确提示提升 Air 会增加整体输出。每次设置后用 Trim 匹配旁通 RMS/感知响度并确保 Peak 不削波；同时记录高频段能量，避免 Trim 降低后仍把频谱倾斜误当响度。

## 延迟、相位与过采样

官方简版文档未给出算法延迟、过采样或相位数据。本机 VST3 在 Ableton Live 11.3.43、48 kHz 下报告 `0 samples`；三个独立导出最佳整数偏移均为 0 samples。该结果只覆盖当前宿主、格式与采样率，不从第三方开发信息推断内部实现。

## Mono/Stereo

适用于单轨和全混；主唱 Mono/Stereo 组件不重复建卡。立体声总线上若动态处理左右不同，需实测相关性与声像；官方文档未说明 Link 是声道链接，它只链接两个旋钮。

## 适用场景

- 录音偏暗但主体已经平衡的主唱。
- Backing Vocal Bus 的统一光泽。
- 并行 Send 做更可控的亮度层。

## 路由

- 主唱链后段，压缩后、链尾去齿前。
- 并行 Aux 100% 插件处理，用 Send 控量并高通/去齿返回。

## 参数起点

- Mid Air 5–15%、High Air 5–20%、先不 Link。
- Trim 降到旁通等 RMS；任何百分比仅为试点。
- 并行返回从比干声低 15–25 dB 起推到刚可感。

## 调整目标

- 人声更靠前、更开阔但不变薄。
- High Air 增加空气，不让齿音、口水音和底噪成为新焦点。

## 调整时听什么

- S/T/CH、嘴部点击、耳机底噪是否被放大。
- Mid Air 是否把 2–5 kHz 推成刺耳或电话感。
- Trim 前后响度偏差。

## 何时停止

- 在混音中关掉会略失光泽，打开又不显处理。
- 齿音先于元音变亮或主体变薄时停止。

## 常见失败

- Mid/High 同时大推。
- 不做 Trim 等响度。
- 用后级重度去齿抵消过量激励。
- 把 Link 误认为声道链接。

## 替代方案

- Maag EQ4：宽幅 Air Shelf 与模拟色彩。
- Pro-Q 3 Shelf：更线性可测的透明亮度。
- 饱和器高频并行：需要更明确谐波角色时。

## 专业案例与工作流线索

- Slate 官方文档把 Trim 和 Peak/RMS 表列为必要配套；Air 的判断必须在补偿增益后完成。

## 待执行测试

- Mid、High 分离变量的复合夹具传输已完成；仍需单音/扫频、真实音素、瞬态-only 与更多百分比映射。
- 与 Maag Air、Pro-Q Shelf 的等响度盲听。
- 去齿前后链序、VST2/VST3 输出与延迟一致性。

## 已测结果

- Ableton Live 11.3.43 / 48 kHz / Fresh Air 1.1.1 VST3 真实加载；界面确认 Mid Air、High Air、Link、Trim、Power、Peak/RMS 表，宿主报告 `0 samples`。
- 相对同实例 `Mid 0 / High 0 / Trim 0` 基线，`Mid 21 / High 0` 使稳定多音整体 `+0.651 dB`，12/16 kHz `+0.75/+0.80 dB`；峰值由 `-1.918` 升至 `-0.708 dBFS`。
- `Mid 0 / High 21` 使稳定多音整体 `+0.911 dB`，12/16 kHz `+1.57/+2.34 dB`；峰值达到 `-0.000001 dBFS`，是余量风险端点而非推荐起点。
- 两处理态对中性基线最佳整数偏移均 0 samples，稳定区相关 `0.9999947/0.9999986`。十音拟合残差比例未见明显变化，但谐波相关多音不足以证明无失真或无混叠。
- 主结论使用同实例中性态作基线；较早共享旁路只用于辅助边界，不声称逐比特透明。详见 [[projects/p1-plugin-knowledge-base/validation/reports/0c0769036773--Slate-Digital-Fresh-Air|Fresh Air L3 验证]]。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | dynamic-air-exciter |
| mode | mid-and-high-air |
| main_controls | mid_air,high_air,link,trim |
| risk_flags | sibilance,noise-lift,loudness-bias,clipping |
| validation | harmonic-dynamic-air-level-match |

## 来源

- [[sources/音乐制作/插件资料/Slate Digital/Fresh Air资料|Fresh Air 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]

## 开放问题

- Link 的精确联动比例、声道行为与更完整动态映射？
- VST2/VST3 是否完全相同输出？
