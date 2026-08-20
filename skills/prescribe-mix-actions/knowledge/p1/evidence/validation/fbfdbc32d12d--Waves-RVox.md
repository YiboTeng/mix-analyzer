---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: fbfdbc32d12d
product: RVox
evidence_level: L3
test_id: dynamics-steps-rvox-compression
---

# Waves RVox：Compression -20 动态收敛验证

## 结论

本机 Waves `RVox` 12.7.0.209 VST3 Stereo 已在 Ableton Live 11.3.43、48 kHz 中真实加载；宿主设备栏报告 `Latency: 64 samples (1.3 ms)`，与 Waves 对 44.1/48 kHz 的官方延迟表一致。本轮保持 Gate `-Inf`、Gain `0.0`，比较旁路、Compression `0.0` 与 `-20.0`。

Compression `0.0` 相对旁路是相关系数 1.0 的线性 -0.0873 dB 偏移；它在本轮可作为近似中性控制，但不是数学上的 0 dB 直通。Compression `-20.0` 则把低电平显著抬高、把高电平抬高得更少：五档相对中性稳态增益从 +17.834 dB 收敛到 +5.178 dB，输出对输入斜率为 0.471931，对应当前五档的局部有效比率约 2.119:1。最高档处理峰值达到 -0.911 dBFS，说明该旋钮同时带来显著回补/上靠 Ceiling 的效果，不能把面板 `-20` 直接当作“20 dB 向下压缩”或纯 GR。

四个持续音阶梯在本分析窗内进入稳态 ±1 dB 需要约 28–80 ms；五个隔离脉冲相对中性均高约 1.21 dB。因为脉冲出现在前段持续音之后，结果包含检测器与释放记忆，不能反推隐藏 Attack/Release 常数。它能可靠支持的工作流是：先用 Compression 获得目标密度，立即检查峰值余量和低电平噪声，再在插件外做旁路等响，而不是依赖旋钮数字或更响听感。

## 固定状态与量化

- 插件：Waves `RVox` 12.7.0.209，VST3 Stereo。
- 宿主：Ableton Live 11.3.43；160 BPM；48 kHz；报告延迟 64 samples / 1.3 ms。
- 中性控制：Gate `-Inf`、Compression `0.0`、Gain `0.0`。
- 单变量：Compression `0.0` → `-20.0`；Gate 与 Gain 固定。
- 导出：Master、42.1.1–50.1.1、12 s、48 kHz/24-bit WAV、Normalize Off、Triangular dither。
- 夹具：`dynamics_steps_48k.wav`；Ableton 自动 Warp 为 160 BPM 下 8 bars/12 s。
- 工程快照：`validation/host/snapshots/0072a637f389--FabFilter-Saturn-2 Project/fbfdbc32d12d--Waves-RVox.als`。

| 输入峰值 | 中性 RMS | -20 RMS | -20 相对中性稳态增益 | -20 峰值 |
|---:|---:|---:|---:|---:|
| -30 dBFS | -33.098 | -15.264 | +17.834 dB | -12.264 dBFS |
| -24 dBFS | -27.098 | -10.996 | +16.102 dB | -7.995 dBFS |
| -18 dBFS | -21.098 | -7.672 | +13.426 dB | -4.667 dBFS |
| -12 dBFS | -15.111 | -5.372 | +9.738 dB | -2.353 dBFS |
| -6 dBFS | -9.098 | -3.920 | +5.178 dB | -0.911 dBFS |

| 静态指标 | Compression -20 vs 中性 |
|---|---:|
| 输出对输入斜率 | 0.471931 |
| 当前五档局部有效比率 | 2.118953:1 |
| 最低到最高档增益变化 | -12.656577 dB |
| 全文件 RMS 差 | +7.734796 dB |
| 全文件峰值差 | +2.029548 dB |
| 直接相关 | 0.925210363 |

> 局部有效比率只是五档稳态回归；内部能量检测、Knee、时间积分与 Ceiling/回补共同影响结果，不能把它当成隐藏固定 Ratio 的标定。

| 持续音起点 | 进入稳态 ±1 dB |
|---:|---:|
| -24 dBFS | 80.02 ms |
| -18 dBFS | 54.58 ms |
| -12 dBFS | 28.21 ms |
| -6 dBFS | 51.85 ms |

五个隔离脉冲相对中性的峰值增益为 +1.211 至 +1.213 dB。两种处理态的 L-R 残差约 -141.47 dBFS；夹具是双单声道，因此只支持当前输入下左右输出一致，不能替代不等电平 Stereo Link 测试。

## 操作观察与工作流

- 先把 Gate 保持 `-Inf`，只拉 Compression；以 Total Compression/能量显示找动作区，但用字头、轻句、噪声和峰值表确认。
- `-20` 在本轮不是“衰减 20 dB”：低档被抬约 17.8 dB，最高档仍抬约 5.2 dB。旋钮越深越要预留下游 Headroom，并用外部 Utility/通道增益做旁路等响。
- 实用主唱从较浅位置开始，以响句约 3–6 dB 总压缩为听感起点；若轻句、呼吸和房间声同时前冲，先减 Compression，不要用更高 Gate 粗暴补救。
- Gate 应独立验证：从关闭缓慢推高，只做句间噪声轻退；词尾、气声或弱辅音被切即回退。本轮没有执行 Gate 音频测试。
- 需要明确 Attack、Release、Ratio、Range 或 Sidechain 时改用 Pro-C 2；需要更平滑的宏动态可用 CL 1B；需要更强瞬态性格可用 CLA-76。

## 边界与未验证项

- L3 覆盖本机 VST3 Stereo、48 kHz、Gate -Inf、Gain 0.0、Compression 0.0→-20.0、一个阶梯/脉冲历史与 64-sample 宿主报告。
- Ableton 对导出做 PDC；64 samples 是宿主报告与官方表的交叉核对，不是本轮从文件间测得的裸延迟。
- 未验证 Gate 对词尾/呼吸/噪声的效果、隐藏检测器常数、Output/Ceiling 边界、Mono、Stereo Link、VST2、其它版本/采样率/输入节目、自动化、CPU 或真实主唱等响盲听。
- Compression -20 的大幅增益变化会造成听感偏差；本报告量化其电平行为，但不把更响等同更好。

## 证据

- 旁路 SHA-256：`dc8379ba04fe00155a24266321d6c08c11bd3877c383f39c23b360d446708132`。
- 中性 SHA-256：`19d91a4d4a687912cdde55a0c1362b8962717438b1ec1df8cffb70fc19c40e09`。
- Compression -20 SHA-256：`88208944a008cadac2b2bd6ca38208af609118ee78b7c916a2504161517fc5d0`。
- 工程快照 SHA-256：`e58373ab2711552e4e61dfdd5d36ef768a8249bff3d4d1015070bee0fc55cb9a`。
- 量化：`validation/results/fbfdbc32d12d--dynamics-rvox-compression.json`。
- 测量脚本：`validation/scripts/analyze_rvox.py`。
