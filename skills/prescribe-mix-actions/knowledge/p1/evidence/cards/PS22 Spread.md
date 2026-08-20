---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: 2035ec8dd8df
vendor: "Waves"
product: "PS22 Spread"
evidence_level: L3
validation_status: S4-host-validated-passed
batch: R01
tags: [music-production, vocal-mixing, plugin-knowledge]
---

# PS22 Spread

## 身份与版本

- 厂商/产品族：Waves / PS22 Spread；Family ID：2035ec8dd8df。
- 本机版本：12.7.0.209；格式：VST2 | VST3；Studio One：current-filesystem-match。
- Ableton 实测组件：`PS22 Spread Stereo` VST3。
- 主/次方向：width-psychoacoustic；mono-to-stereo;stereo-diffusion。
- 证据等级：L3；状态：S4-host-validated-passed。

## 能做什么

- 用频率相关的左右声像分配，把中央 Mono 变成从定位型到扩散型的 Stereo，而不是复制声部、加回声或调制延迟。
- 对已有 Stereo 输入保留原声像位置，再围绕原位置增加扩散；Width 与 Rotation 可先整理输入宽度和重心。
- 通过 Sweeps、FCenter、FDensity 与 Tweak，在“少数频段清晰定位”和“许多频段平滑扩散”之间取舍。

## 不建议用来做什么

- 不要把它当作 Doubler、MicroShift 或 Delay：它没有声部 Detune，也没有 PS22 Spread 的 Delay 参数。
- 不要在未监听 Mono、M/S 与扬声器时追求越宽越好；图中越过 L/R 的频段属于反相超宽区域。
- 不要把官方“保持总 Stereo 能量”误解为 Mono 折叠与原始 Mono 完全相同。

## 信号流位置

- Mono 人声、乐器或档案音源可直接 Insert；关键主唱更稳妥的路径是复制轨/并行返回，保留干燥中心。
- 已经很宽的 Stereo 源先用 Width 收窄，再加适量 Spread；需要偏左/偏右时用 Rotation。
- 下游可再做高通、去齿或 Duck，但必须重新检查 Stereo 与 Mono。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Input | 0 到 -24 dB 输入衰减。 | 处理可能抬高峰值；出现 Clip 时先降 Input。 |
| Width | 0=输入折成 Mono，1=保留原 Stereo 宽度。 | 宽 Stereo 输入先试 0.6–0.7，给 Spread 留空间。 |
| Rotation | -45° 到 +45°，移动输入重心但不靠左右电平差。 | 给非中央 Mono/窄 Stereo 定位，再加中等 Spread。 |
| Spread | 0=不展开，1=填满扬声器间，1.2=超宽。 | 从 0.25–0.6 起；切 Mono，并观察图形是否越过 L/R。 |
| Freq | 低频 Spread 开始作用的过渡频率，32 Hz–16 kHz。 | 想让低频更稳时提高过渡频率并降低 LFSpread。 |
| LFSpread | 1=低频与高频同宽，>1=低频更宽，趋近 0=低频居中。 | 主唱/总线通常先收窄低频。 |
| Sweeps | 全频左右往返次数；标准版 2–22，(10) 版 2–10。 | 2–4 做定位，约 8 折中，12–22 做扩散；先定它。 |
| FCenter | FDensity 集中/疏散 Sweeps 的中心频率。 | 把密度放到需要扩散的频段。 |
| FDensity | 0=大致均匀；正值集中到 FCenter，负值让中心附近更疏。 | 通常保持中等（手册建议约 0.6 以下）。 |
| Tweak | 移动各频率的左右位置。 | 最后在 -0.5 到 +0.5 一带细调平衡。 |
| L/R · M/S | 只改变表头显示，不改声音。 | S 长期高于 M 常意味着过宽或输入相位问题。 |

## Gain Staging

PS22 以保持总 Stereo 能量为设计目标，但频率相关相位/声像重分配仍会改变瞬时峰值；官方称常见峰值上升约 2–3 dB，极端可更高。先留余量，观察 Clip，再分别记录 Stereo RMS、Mid RMS 与 Mono Fold-down。

## 延迟、相位与过采样

- 官方把 PS-Spread/PS-Split 描述为线性、非时变的高阶低 Q IIR 交叉馈送系统；目标是低染色、低 phasey 感并避免基于时间延迟的伪立体声。
- 本机 Ableton 在 48 kHz 报告 2 samples / 0.042 ms PDC。默认脉冲双通道峰值均在事件阈值后 5 samples / 0.104167 ms 到达；波形峰值与宿主 PDC 不是同一指标。
- 没有 Oversampling 控制；本轮未测不同采样率或 VST2。

## Mono/Stereo

- 官方明确说 Mono 折叠不是原始 Mono 的精确复制；Spread=0.6 时手册给出的 Mono 频响波纹约 ±0.67 dB，Spread 增大时波纹也增大。
- 本机默认 Spread=0.60：三次宽带脉冲 L/R 相关均值 0.7113955，Side/Mid RMS -7.728248 dB，Mono Fold 相对每通道 Stereo RMS -0.677117 dB，Mono 峰值差约 -0.30035 dB。
- -0.677 dB 是宽带 RMS 指标，不是对官方 ±0.67 dB 频响波纹的直接复现；只能说明默认状态存在温和但可测的 Mono 变化。

## 适用场景

- Mono Ad-lib、叠唱、乐器或档案素材的伪立体声。
- 稀疏 Stereo 编排的空间填充，或对已定位声源做局部扩散。
- 主唱很低电平的并行宽化层；不替代显式多声部 Doubler。

## 路由

- Insert：对 Mono/窄 Stereo 音源直接构造空间。
- Parallel：复制轨/Aux 100% 处理，干声保留中心；返回可高通、去齿与 Duck。

## 参数起点

- 官方 Mono 教程起点：Sweeps=8、Spread=1.0、LFSpread=0、Freq≈200 Hz、FCenter≈2600 Hz、FDensity/Tweak=0；再把 FDensity 推到约 0.4，并用 FCenter/Tweak 找平衡。它不是通用最终值。
- 已有 Stereo：Width 0.6–0.7、Spread 0.25–0.5 起步。
- 主唱并行层：Spread 0.25–0.6、LFSpread 0–1；Sweeps 8 左右起步。

## 调整目标

- Stereo 中获得所需定位、扩散或空间感，Mono 中词义、中心重量和主要频段仍稳定。
- M/S 中 S 明显增加但不长期压过 M；左右峰值和重心可控。

## 调整时听什么

- Mono 频响起伏、中心变薄、某些音符或齿音突然偏向一侧。
- 高 Sweeps + 高 FDensity + 大 Spread 带来的梳状/机器人色彩。
- 超出扬声器的反相宽度在耳机上的疲劳感。

## 何时停止

- 目标宽度已可感，继续加 Spread 只增加 Mono 变化、疲劳或染色。
- Tweak 已使关键频段平衡；继续移动只是在音符间交换偏左/偏右问题。

## 常见失败

- 沿用错误的 Delay/MicroShift 思路寻找不存在的 Delay 参数。
- Sweeps、FCenter、FDensity、Tweak 同时乱动。
- 宽 Stereo 输入 Width=1 再叠大 Spread。
- 只看相关性数值，不听 Mono、扬声器、耳机与关键歌词。

## 替代方案

- Doubler：显式多声部 Detune、Delay、Pan，更像人声叠唱。
- bx_control V2：管理已有 Stereo 的 Width/Mono Maker，不生成频率分区伪立体声。
- PS22 Split：更接近方波式频率左右分割；Spread 更平滑。
- PS22 Spread(10)：同一控制体系但 Sweeps 上限 10、DSP 更低；不是另一套 Mono 算法。

## 专业案例与工作流线索

- 官方把目标分为频段定位、声像扩散和空间增强：低 Sweeps 偏定位，高 Sweeps 偏扩散，中等 Sweeps 折中。
- 高密度扩散与低染色存在取舍；先选 Sweeps，再定 Spread/LFSpread、Density/FCenter，最后用 Tweak 居中。

## 待执行测试

- 已完成标准 `PS22 Spread Stereo` 默认状态的组件确认、参数回读、宿主 PDC、三档宽带脉冲的 L/R 相关、Side/Mid、Mono Fold 与峰值到达测量。
- 已确认本机暴露 Split、Spread、Spread(10)、XSplit 的 Mono/Stereo 与 Stereo 组件；手册确认标准版最大 22 Sweeps、(10) 最大 10。
- 待补 Spread 0/0.6/1.0、Sweeps 4/8/16、LFSpread 0/1/1.5、FDensity 单变量、多音 Mono 频响波纹、连续人声盲听、VST2/Mono 与不同采样率。

## 已测结果

- 默认：Input 0.0 dB、Width 1.00、Rotation 0.0、L/R、No Clip、Spread 0.60、Freq 251 Hz、LFSpread 1.50、FCenter 724 Hz、FDensity 0、Tweak 0、Sweeps 16。
- 48 kHz 宿主 2 samples / 0.042 ms；三次脉冲左右峰值到达中位数均 5 samples，通道间峰值差 0。
- L/R 相关 0.711395513；Side/Mid -7.728248 dB；Mono Fold -0.677117 dB；左峰值增益约 -5.887 dB、右约 -5.276 dB，随输入电平稳定。
- 100 ms 全响应由直接 Mid 主导；Hann 窗频域尾部在 20–200 / 200–2000 / 2000–20000 Hz 的 Side/Mid 约 -0.36 / -0.55 / -0.85 dB。该指标不能替代稳态多音频响测试。
- 完整报告：[[projects/p1-plugin-knowledge-base/validation/reports/2035ec8dd8df--Waves-PS22-Spread|PS22 Spread L3 验证]]。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | stereo-generator |
| mode | frequency-dependent-iir-spread |
| main_controls | input,width,rotation,spread,freq,lfspread,sweeps,fcenter,fdensity,tweak |
| risk_flags | mono-ripple,comb-coloration,antiphase-width,center-thinning,sibilant-spread |
| validation | correlation,side-mid,mono-delta,impulse,multitone |

## 来源

- [[sources/音乐制作/插件资料/Waves/PS22 Spread资料|PS22 Spread 资料]]
- [[projects/p1-plugin-knowledge-base/selection/shortlist|P1 v1 正式插件短名单]]

## 开放问题

- Spread、Sweeps、LFSpread 与 FDensity 的单变量变化，在多音稳态下如何改变 Mono 频响波纹、梳状染色与主唱可懂度？
