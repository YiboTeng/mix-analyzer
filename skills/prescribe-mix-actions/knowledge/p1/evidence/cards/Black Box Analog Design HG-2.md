---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: 1994a7f7d443
vendor: "Plugin Alliance"
product: "Black Box Analog Design HG-2"
evidence_level: L3
validation_status: S4-host-validated-passed
batch: B04
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Black Box Analog Design HG-2

## 身份与版本

- 厂商：Plugin Alliance
- 产品族：Black Box Analog Design HG-2
- Family ID：1994a7f7d443
- 本机观测版本：1.3.0.0
- 格式：VST2 | VST3
- Studio One 可用性：current-filesystem-match
- 主能力方向：saturation-tube-parallel
- 次能力方向：harmonics;air
- 当前证据等级：L3
- 验证状态：S4-host-validated-passed

## 能做什么

- 串联 Pentode/Triode 6U8A 管级与输入/输出变压器，并含可选两种 12AX7 Parallel Saturation。
- Density 同比例加推 Pentode/Triode 而尽量不改变相对平衡和输出；Calibration 调 Dark/Normal/Bright。
- Air 增加 10 kHz 以上光泽，Mix 回添干声。

## 不建议用来做什么

- 不要把当前 1.10 产品页功能完全写回本机 1.3；S4 必须回读。
- 不要同时推 Pentode、Triode、Density、Parallel 和 Air。
- 不要因相同峰值下更响就直接判定更好。

## 信号流位置

- 压缩后轻度管色；Air 后复查齿音。
- Vocal Bus 小幅统一密度；极端 Parallel 用 Aux。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Pentode / Triode | 串联两级不同管饱和量。 | 逐级单独推，先找到哪一级改善主体。 |
| Density | 一起加推两级而尽量保持平衡/输出。 | 基础比例确定后小幅增加整体密度。 |
| Parallel Saturation | 选择较柔/较激进 12AX7 并行谐波。 | 从关闭或低量起，注意中高频毛刺。 |
| Calibration / Air | 整体高频校准与 10 kHz 以上光泽。 | 先 Normal/Air 0；主链平衡后再加 Air。 |
| Mix / Input / Output | 并行和增益结构。 | 先全湿调色，再回 Mix；输出严格匹配。 |

## Gain Staging

产品定位包含“相同峰值更响”，正是潜在偏差。以 Active RMS/LUFS、Peak、THD 同时记录，用 Output 匹配主观响度后判断谐波/动态。

## 延迟、相位与过采样

本机 1.3.0.0 VST3 在 Ableton Live 11.3.43 中报告 32 samples / 0.67 ms；离线 PDC 后三次脉冲峰值均为 0-sample 对齐。本轮旧版界面未发现可归因的 OS 或 TMT 数字控制，不把新版能力倒灌。

## Mono/Stereo

本卡和实测实例均为原版 HG-2，不是 HG-2MS。左右相同输入的默认导出相关为 0.999999998701，但这不等于已验证独立 M/S 控制或所有不对称输入。

## 适用场景

- 主唱温暖、密度与高频光泽。
- Vocal Bus 轻胶合。
- 并行管饱和角色。

## 路由

- 主唱/人声总线后段。
- Aux 进行更重 Parallel。

## 参数起点

- Pentode/Triode 低量、Density 0、Parallel Off、Air 0。
- 先选一个管级推到可感，再用 Density 小加。
- Mix 10–40% 或全湿轻驱；Output 等响度。

## 调整目标

- 中频更密、峰值更圆且不暗。
- Air 增加光泽不突出齿音。

## 调整时听什么

- 相同峰值但 RMS 上升的偏差。
- 管级叠加导致低中频拥挤。
- Air/Parallel 增加沙亮。

## 何时停止

- 等响度下主体更稳定且细节保留。
- 再推 Density 只让声音变扁/糊时回退。

## 常见失败

- 把 HG-2MS 功能倒灌。
- 所有级同时推动。
- Output 未匹配。
- Air 与去齿互相抵消。

## 替代方案

- Decapitator：更显著性格。
- Saturn 2：频段/OS 可控。
- VTM：磁带式频响和压缩。

## 专业案例与工作流线索

- 官方把 Pentode/Triode 描述为串联、12AX7 为并行；实验必须分别消融，而不是把所有旋钮当同类 Drive。

## 待执行测试

- Pentode/Triode/Density/Parallel 单变量 THD。
- Calibration/Air 频响与齿音数据集。
- VST2/VST3、旧版/当前文档功能差异。

## 已测结果

Ableton Live 11.3.43 / HG-2 1.3.0.0 VST3 默认原版实例：Calibration 为 FLAT，界面其余旋钮保持默认；宿主报告 32 samples / 0.67 ms。三档输入 -1.938/-6.021/-12.041 dBFS 对应输出 -3.109/-6.946/-12.830 dBFS，峰值增益 -1.170/-0.925/-0.789 dB，范围 0.381 dB；三次局部峰值均 0 samples。直接相关 0.972700、RMS 电平差 -0.839411 dB、左右相关 0.999999998701。默认路径为温和且电平相关的削峰/管色，不是透明旁通。

本轮使用三电平脉冲，只覆盖默认路径瞬态传输、宿主延迟、短响应和通道一致性；Pentode/Triode/Density/并行管/Air 单变量、稳态 THD、别名、频响、VST2 与音乐盲听仍待后续扩展。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | tube-transformer-saturator |
| mode | serial-plus-parallel |
| main_controls | pentode,triode,density,parallel,calibration,air,mix |
| risk_flags | version-gap,loudness-bias,mud,sibilance |
| validation | stage-ablation-thd |

## 来源

- [[sources/音乐制作/插件资料/Plugin Alliance/Black Box Analog Design HG-2资料|Black Box Analog Design HG-2 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]
- [[projects/p1-plugin-knowledge-base/validation/reports/1994a7f7d443--Plugin-Alliance-Black-Box-HG-2|HG-2 默认路径 L3 验证]]

## 开放问题

- 本机 1.3 的 Density/Air/Mix 可见，但精确数值范围、单变量谐波和频响映射仍未量化；新版 HG-2/HG-2MS 专属能力不得外推。
