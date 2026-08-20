---
type: plugin-validation
status: passed
created: 2026-08-20
updated: 2026-08-20
family_id: 6756edefac77
product: WNS
evidence_level: L3
test_id: composite-wns-neutral-broad-reduction
---

# Waves WNS：六段宽带降噪与零延迟边界验证

## 结论

本机 Waves WNS Stereo 12.7.0.209 VST3 已在 Ableton Live 11.3.43 / 48 kHz 真实加载，宿主报告 0 samples。默认 Threshold -20 dB、六段 Gain 0 dB、Smoothing 50；默认输出与独立保存的共享旁路全段 RMS 相差约 0 dB，但因宿主状态/时间对齐差异不能可靠 Null，因此只记为电平中性，不声称逐比特透明。

把六段设为 -9.4/-6.7/-6.7/-6.7/-6.7/-6.7 dB 的宽带压力状态后，相对同一 WNS 默认渲染，固定人声、稳定多音、空间与动态区域分别降低 13.91、13.99、11.28、12.55 dB。这证明六段 Gain 不是静态 EQ 增益：它在 Threshold 与语音检测约束下形成内容相关的抑制，并清楚展示过量时会吞掉有效节目。

WNS 是对白宽带噪声抑制器，不是 De-plosive。它作为 RX De-plosive 无法加载后的“修复/降噪槽位”可验证替代被纳入最终 40 款，但爆破音专用能力仍明确缺口，处方应回退到 Clip Gain、动态低频 EQ 或手工自动化。

## 固定状态

- 默认：Threshold -20 dB；六段 0 dB；Smoothing 50。
- 频带中心：30、99、330、1094、3627、12027 Hz。
- 压力：第一段 -9.4 dB，其余五段 -6.7 dB；Threshold/Smoothing 不变。
- 宿主：Ableton Live 11.3.43，48 kHz；0 samples。
- 隔离：只启用 WNS；此前链上设备全部停用。

| Composite 区域 | Broad reduction vs neutral |
|---|---:|
| 0–6 s 脉冲列 | -7.221 dB |
| 8–20 s 稳定多音 | -13.992 dB |
| 21–42 s 固定人声 | -13.915 dB |
| 45–57 s 空间夹具 | -11.278 dB |
| 60–72 s 动态夹具 | -12.546 dB |

## 操作工作流

1. 放在压缩、响度骑乘、激励和饱和之前，不先放大噪声。
2. 循环纯噪声、最弱字尾、正常语句和擦音；把 Threshold 放在对白主体下方、噪声可被识别的位置。
3. 只降低真正含噪的频带；用低/高边界限制处理区，Smoothing 在自然过渡与频段独立性之间折中。
4. 以“噪声退入编曲、弱字尾仍完整”为停止条件。有效语句上持续大幅衰减、齿音变水或空间尾断裂时回退。
5. Suggest 只能提供起点，必须用当前说话者、话筒和环境复核。

## 边界与未验证项

- Composite 没有已知 SNR 的稳定噪声床，不报告 SNR 改善量、噪声分类准确率或主观伪影阈值。
- 未验证 Mono、VST2、其它采样率、自动 Suggest、HP/LP、实时/离线差异或盲听。
- 独立保存宿主状态不能可靠 Null；默认只记电平中性。
- 不把 WNS 写成 De-plosive；爆破音低频事件需要独立手段。

## 证据

- Default Neutral SHA-256：`dd1bad827e1b8fb21e0ee3ba08faa0601a7c1626ee81540f7ca54f875d0899d7`。
- Broad Reduction SHA-256：`e2d1569a471a682f1847a1ca016cacb7236f34264e179e9087b4d4275346fa05`。
- 工程快照 SHA-256：`2b06997b900f5f264aff5043725a004650ea2310341102ddbbb25fa5211c5b96`。
- 量化：`validation/results/6756edefac77--composite-wns.json`（SHA-256 `d205ac3ee1b3af9b16568e1e6d2a8b6c8ca0bd8dc76627e8ea933eb816ac4ee7`）。
- 测量脚本：`validation/scripts/analyze_wns.py`。

