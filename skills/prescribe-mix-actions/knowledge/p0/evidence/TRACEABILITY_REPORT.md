---
type: traceability-report
status: passed
created: 2026-08-20
updated: 2026-08-20
---

# P1 v1 可追溯性报告

## 结论

最终 Shortlist、S4 Matrix 和 Adapter Manifest 均为 40 个唯一 Family ID，三个集合完全相同。每个 Family ID 都有本机 Inventory 来源、选择理由、L3 知识卡、官方/可信来源笔记、验证报告、量化结果和机器可读 Adapter；40/40 链路通过。

```text
Inventory component(s)
  → normalized product family
  → scored Shortlist record
  → L3 knowledge card + source note
  → validation report + result JSON + host snapshot/render
  → P1 Adapter
  → capability/version/routing/availability indexes
  → offline P0 prescription + retest contract
```

完整逐款路径表位于 `audit/results/traceability.csv`；它包含 Family ID、厂商、产品、主能力、Card、Source、Validation、Result 和 Adapter 路径，SHA-256 由 `audit/results/final-audit.json` 记录。

## 层间门禁

| 层 | 门禁 | 审计结果 |
|---|---|---|
| Inventory → Family | 原始组件不丢失；变体可回查 | 3459 → 656，通过 |
| Family → Shortlist | 统一评分与能力分类 | 40，通过 |
| Shortlist → Card/Source | 每款 L2 字段和来源完整 | 40/40，通过 |
| Card → Validation | 每款达到与边界相称的 L3 | 40/40，通过 |
| Validation → Adapter | 只采纳 L3 事实；证据路径存在 | 40/40，通过 |
| Adapter → P0 | 输出插件/路由/目标/停止/副作用/复测 | 12 Fixture，通过 |

## P0 诊断到证据的示例

### Sibilance

`sibilance` 从能力索引返回 Pro-DS 与 Eiosis E2Deesser 等候选；版本和可用性筛选后，处方输出路由、Threshold/Range 或 Mode/Sensitivity 的调节目标、lisping/暗化风险、停止条件和复测的齿音带能量/Voiced Tone；证据指针直达对应 Card、Source、L3 报告和 Result JSON。

### Mouth click / short impulse

`mouth_click_or_short_impulse` 返回 X-Click；Adapter 要求 Difference 只包含缺陷、使用最低工作 Threshold，并在 Difference 出现辅音/鼓击时停止。L3 报告明确当前无带标签嘴部点击，因此 P0 不得输出准确率或“一键 Mouth De-click”等确定性承诺。

### Plosive low-frequency event

该诊断没有被候选数量掩盖：WNS 的 `not_for` 与冲突规则拒绝选择，Fixture F11 返回 Clip Gain + Pro-Q 3/F6 动态低频。此退路在处方快照和测试中固定。

### Realtime loud breath

DeBreath 能处理呼吸，但本机 35248 samples / 734 ms；Fixture F12 带 `realtime_tracking=true` 时触发延迟冲突，改用 Clip Gain 呼吸自动化。非实时编辑仍可通过 Breath Monitor、停止条件和复测指标使用 DeBreath。

## 最终审计摘要

- JSON：115 个，语法全部通过。
- CSV：7 个，列形状全部通过。
- Scoped Markdown：150 个，本地链接未解析数 0。
- Traceability：40 行，缺失路径 0。
- Schema：40/40；处方快照：12/12。
- Adapter 测试：15/15。

新增最终文档后又执行了同一全量审计；最终权威结果为 `audit/results/final-audit.json`。
