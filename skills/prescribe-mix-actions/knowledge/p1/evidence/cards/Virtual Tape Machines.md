---
type: plugin-card
status: active
created: 2026-08-20
updated: 2026-08-20
family_id: 6d808184e53c
vendor: "Slate Digital"
product: "Virtual Tape Machines"
evidence_level: L3
validation_status: S4-host-validated-passed
batch: B04
tags:
  - music-production
  - vocal-mixing
  - plugin-knowledge
---

# Virtual Tape Machines

## 身份与版本

- 厂商：Slate Digital
- 产品族：Virtual Tape Machines
- Family ID：6d808184e53c
- 本机文件系统版本：1.1.11.1 | 1.2.1.1
- 已验证格式/宿主：VST3 / Ableton Live 11.3.43
- 格式库存：VST2 | VST3
- 主能力方向：saturation-tape
- 当前证据等级：L3
- 验证状态：S4-host-validated-passed

## 机器、磁带与速度

- 2-inch 16-track 模拟 Studer A827，适合单轨/多轨录带角色；1/2-inch 2-track 模拟 Studer A80 RC，常作为总线/母带机角色。
- FG456 是约 +6 参考磁带；FG9/GP9 是约 +9，约多 3 dB headroom，能在更高输入下保持较少饱和。
- 30 ips 通常噪声更低、频响更平直、高频更延伸；15 ips 更非线性并改变低频/中频和高频衰减。实际“厚/紧”不能脱离具体机器、磁带、Bias 和输入电平判断。
- Bias High 让高频更早饱和，Low 让高频更晚饱和并更动态；Normal 是本机默认。

## 能做什么

- 用两种磁带机、两种磁带、两档速度、三档 Bias 与可推驱输入塑造频响、相位、峰值、谐波、噪声和时基稳定性。
- 既可在单轨模拟多轨录带，也可在总线模拟 1/2-inch 双轨机；Groups 可联动同用途实例。

## 不建议用来做什么

- 不把默认实例当透明增益；不把 15 ips 固定写成“更多低频”；不在未记录全局状态时批量 Group。

## 信号流位置

- 主唱可放在去齿之后、EQ/压缩之前塑造录带角色；Vocal Bus 可放在后段胶合。机器/速度会改变后级触发，链序固定后再比较。

## 已验证默认态

- Process On、Ungrouped、Input/Output 0.00 dB。
- Machine 2-inch 16-track、Tape FG456、Speed 30 ips、Bias Normal。
- Global Calibration -15.0 dB、Noise Reduction -24.0 dB、Wow & Flutter 25%、Bass Alignment 0.00 dB、Hiss Automute 开、Default Group Ungrouped。
- Ableton 报告延迟 1882 samples / 39.2 ms。

## 控制语义

| 控制 | 含义 | 调整动作 |
|---|---|---|
| Machine 2-inch / 1/2-inch | A827 多轨机与 A80 RC 双轨机模型。 | 单轨先试 2-inch；总线试 1/2-inch，但必须等响。 |
| Tape FG456 / FG9 | +6 与 +9 参考磁带，headroom 相差约 3 dB。 | 更早色彩试 FG456；更紧/更高 headroom 试 FG9。 |
| 15 / 30 ips | 改变噪声、频响、相位和非线性。 | 一次只切速度；回配 Output 后比较 55–300 Hz 与 8–16 kHz。 |
| Bias High/Normal/Low | 改变高频饱和与动态。 | Normal 基线；High 更早柔化高频，Low 更开放动态。 |
| Input / Output | Input 推磁带，Output 做电平回配。 | 推到失真刚明显再回约 0.5 dB；按 Active RMS 等响。 |
| Calibration | 定义 VU 参考与工作电平；全局共享。 | 会话开始记录；不要在 A/B 中途无记录地改。 |
| Noise Reduction / Hiss Automute | 降低建模 hiss；无输入时自动静音 hiss。 | 现代主唱保持默认或更安静；复古目标才主动加噪。 |
| Wow & Flutter | 时基不稳程度；0 关、25 调校、50 常规、100 较差机器。 | 默认 25% 已非零；清晰主唱先与 0% 对照。 |
| Bass Alignment | 按机器/磁带/速度调整低频对齐。 | 0 dB 基线；不要把它当普通低架 EQ。 |
| Group 1–8 / Ungrouped | 同组实例共享主参数；全局设置另行共享。 | 只给同用途实例分组，避免误改全工程。 |

## Gain Staging

1. 固定 Machine、Tape、Speed、Bias 和 Calibration，先记录 Advanced 全局值。
2. 从 Input 0 dB 开始逐步推高，找到失真/压缩刚明显点，再回约 0.5 dB。
3. 用 Output 匹配旁路 Active RMS，同时记录 Peak、低频、齿音和后级压缩触发变化。
4. 只切一个变量；速度比较时尤其检查 80–300 Hz、1–4 kHz 与 8–16 kHz。
5. 最后复查 Hiss、Wow、Group、自动化与 Mono/Stereo 路由状态。

VU 是校准后的平均工作电平，不是峰值表。Input/Output Link 只是界面联动；自动化应分别验证。0 VU 可作为噪声/饱和平衡起点，但不是普遍最佳音色。

## 延迟、相位与过采样

- 本机 VST3 在 Ableton 报告 1882 samples / 39.2 ms；周期多音的相关偏移不等于 PDC。官方资料未给当前旧版本的过采样规格。

## Mono/Stereo

- 机器型号不是通道格式。主唱 Mono 与 Stereo Bus 都要分别检查；本轮双单声道输入左右残差约 -141.49 dBFS，证明当前默认/速度变体保持通道一致。

## 适用场景

- 主唱柔化数字边缘、Vocal Bus 胶合、复古暗化和效果化录带角色。

## 路由

- 主唱 Insert 轻用；总线与单轨不要同时无差别叠加。Group 只分配给确需联动的同用途实例。

## 参数起点

- 本机默认 2-inch/FG456/30 ips/Normal 可作观察起点；较干净试 FG9 或降低 Input，复古暗化才单独试 15 ips/High Bias。

## 调整目标

- 等响后峰值更圆、边缘更合适、后级更易控制，同时不损 1–4 kHz可懂度、8–16 kHz空气和低中频清晰。

## 调整时听什么

- 低频隆起或箱体感、最高频滚降、齿音谐波、爆破失真、建模 hiss、Wow/Flutter 和后级压缩触发变化。

## 何时停止

- 达到目标且等响后仍优于旁路即停；继续推只增加糊、暗、噪声或延迟负担时回退。

## 常见失败

- 默认 30 ips 当透明；未匹配 +1.55 dB RMS 就判断更好；Machine/Tape/Speed/Bias 同时切；把 Group/Global 混为实例参数；忘记默认 Wow 25%。

## 替代方案

- FabFilter Saturn 2：需要多段、过采样与精细调制；Abbey Road Saturator：需要更强 TG/REDD 角色；Black Box HG-2：需要管/变压器密度。

## 专业案例与工作流线索

- 官方人声链示例 De-esser → VTM → EQ → VCC，2-inch/FG456/30 ips/High Bias 可作测试起点；Input 可推到失真刚明显再回约 0.5 dB。

## 本机实测

- 默认 30 ips 相对旁路：RMS +1.552950 dB、Peak +3.019170 dB；55 Hz +3.15 dB，220–1760 Hz约 +1.35 至 +1.44 dB，12/16 kHz约 -0.69/-0.68 dB。
- 15 ips 相对旁路：RMS +0.728860 dB、Peak +2.404451 dB；55 Hz +1.39 dB，220–1760 Hz约 +0.78 至 +0.96 dB，12/16 kHz -2.22/-4.84 dB。
- 15 相对 30 ips：RMS -0.824133 dB；55 Hz -1.76 dB，12 kHz -1.58 dB，16 kHz -4.23 dB。本轮不能把 15 ips 简写为“更多低频”；主要差异是整体稍低和最高频更暗。
- 左右处理一致，L-R 残差约 -141.49 dBFS。周期多音相关偏移不是 PDC；实时延迟记录为宿主报告 1882 samples。

## 主唱工作流

- 清晰现代主唱：2-inch、30 ips、Normal，先比较 FG9 与降低 Input；Noise Reduction 保持默认，Wow 先与 0% 对照。
- 需要柔化数字边缘：FG456、30 ips，小幅推 Input；若齿音被新谐波激发，在 VTM 后复查 De-esser。
- 复古/暗化：15 ips 或 High Bias 单变量试验；先等响再判断，不用“更厚”标签替代频谱检查。
- Vocal Bus：可试 1/2-inch，但不要与单轨 2-inch 同时默认开启；Group 仅用于确需联动的同用途实例。
- 官方示例链 De-esser → VTM → EQ → VCC，2-inch/FG456/30 ips/High Bias 可作为起点，不是固定模板。

## 边界与待扩展

- L3 只覆盖本机可达 VST3 的 2-inch/FG456/Normal/Input 0 dB、30/15 ips。
- 待测：1/2-inch、FG9、Bias、Input 驱动、Noise/Wow/Bass/Calibration/Group、VST2、其它采样率、自动化、CPU、脉冲/扫频 PDC 与连续人声盲听。
- 本机文件版本早于 1.2.6.0；官方新版修复的异常低频噪声/失真与 Ableton Bias 自动化已知问题不能无条件外推。

## 待执行测试

- 1/2-inch、FG9、Bias、Input 驱动、Noise/Wow/Bass/Calibration/Group、VST2、其它采样率、自动化、CPU、脉冲/扫频 PDC 与连续人声盲听。

## 已测结果

- 已完成旁路、默认 30 ips、仅改 15 ips 的 48 kHz/24-bit 固定多音验证；核心结果见“本机实测”和 L3 报告。

## P0 映射

| P0 字段 | 值 |
|---|---|
| processor_class | tape-emulation |
| mode | machine-tape-speed-bias |
| main_controls | machine,tape,speed,bias,input,output,calibration,noise,wow,bass,group |
| risk_flags | noise,head-bump,phase,global-group,loudness-bias,latency |
| validation | multitone-speed-transfer;host-latency;channel-consistency |

## 来源

- [[sources/音乐制作/插件资料/Slate Digital/Virtual Tape Machines资料|Virtual Tape Machines 资料]]
- [[projects/p1-plugin-knowledge-base/validation/reports/6d808184e53c--Slate-Digital-Virtual-Tape-Machines|VTM L3 验证报告]]
- `validation/results/6d808184e53c--multitone-tape-machine.json`
- `validation/scripts/analyze_tape_machine.py`

## 开放问题

- Ableton 实际加载 1.1.11.1 还是 1.2.1.1？1.2.6.0 修复会怎样改变低频结果？其它格式/采样率的延迟与频谱是否一致？
