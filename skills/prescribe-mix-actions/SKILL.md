---
name: prescribe-mix-actions
description: 将 Mix Analyzer 的干声/人声或完整混音参考分析指标、已有分析报告或人工诊断，转换为分优先级、可回滚和可复测的具体混音操作；输出路由、插件候选、版本化参数起点、监听目标、停止条件、副作用与复测指标。用户只要求测量对比而不需要处理建议时不要调用。
---

# 生成混音处方

本 Skill 是 P0 决策与 P1 插件映射的薄工作流层。确定性逻辑由脚本执行，知识不写进本文件。

## 输入选择

- 用户提供 `reference-set-metrics.json`：按人声模式规范化。
- 用户提供 `mix-reference-metrics.json`：按完整混音模式规范化。
- 用户只提供报告或口头问题：先把可确认问题写成 `diagnosis-evidence.json`，对无法从证据确认的因果标记 `calibration_required: true`；不要把假设写成测量事实。
- 需要重新分析音频时，先分别使用 `$compare-vocal-references` 或 `$compare-mix-references`。不要把干声与完整 Mix 放进同一个统计集。
- 只有一首参考时，保留等响门控，并允许输出低置信度条件处方；每项必须标为 `conditional-hypothesis`，不得把单参考差值称为稳健偏差、参考共性或固定处理量。
- 用户要求逐旋钮建议但未提供运行时信息时，在运行前一次性说明需要 DAW/Host、插件格式、采样率和已安装插件版本。用户没有要求暂停时继续生成 P0 与能力级 P1 候选，但明确抑制精确旋钮。

规范化输入与输出字段见 [references/contracts.md](references/contracts.md)。处方的证据和安全边界见 [references/decision-policy.md](references/decision-policy.md)。

## 运行

从插件根目录执行：

```powershell
$env:PYTHONPATH = "C:\Projects\mix-analyzer\src"
python -m mix_analyzer.cli `
  --input "C:\path\to\reference-set-metrics.json" `
  --out-dir "C:\Projects\work\mix-prescription" `
  --require-jsonschema
```

默认会推荐能力和插件候选，但在没有当前运行时版本证据时抑制 P1 精确旋钮。优先提供当前 Inventory/版本：

```powershell
python -m mix_analyzer.cli `
  --input "C:\path\to\diagnosis-evidence.json" `
  --out-dir "C:\Projects\work\mix-prescription" `
  --installed-version "497c2536aeff=3.2.3.0" `
  --host "Ableton Live 11.3.43" --format VST3 --sample-rate-hz 48000 `
  --require-jsonschema
```

只有在明确接受打包快照的验证日期/宿主边界、尚未做实时重扫时，才使用 `--trust-catalog-snapshot`；报告必须保留该警告。复杂 Inventory、偏好和插件模式用 `--context-json` 输入。

实时监听或跟唱时同时传入延迟预算：

```powershell
python -m mix_analyzer.cli `
  --input "C:\path\to\diagnosis-evidence.json" `
  --out-dir "C:\Projects\work\mix-prescription" `
  --realtime --latency-budget-ms 10
```

脚本输出：

- `diagnosis-evidence.json`
- `treatment-plan.json`
- `treatment-plan.md`

## 交付要求

在回复中先给优先级最高的 3–6 项操作，再提供文件路径。每项都必须包含：

1. 为什么触发，以及测量事实与假设的边界。
2. 先做什么判别测试。
3. Insert/Send/Parallel/Sidechain/Mid-Side 路由。
4. 已验证版本的插件候选与参数起点；版本不匹配时抑制确定性旋钮映射。
5. 调整时听什么、副作用、停止/回滚条件。
6. 处理后重新测什么。

没有 P1 插件候选时，保留 P0 通用方法或显式退路，不要臆造插件。自动阈值尚未经过大型标注语料校准；即使脚本触发，也要表述为可证伪起点，禁止直接操作用户 DAW 或覆盖音频。

## 维护路由

- 修改 P0 卡：编辑 `knowledge/p0/decision-cards.json`，随后运行知识校验和测试。
- 更新 P1：运行插件根目录 `scripts/import_p1_snapshot.py`，不要手工复制 1.386 GB 的渲染目录。
- P1 参数来源需要深入核对时，读取相应 `knowledge/p1/evidence/cards/`、`sources/` 和 `validation/` 文件，不要一次加载全部 40 款。
