# 数据契约

## 管线

```text
legacy analyzer metrics
  → diagnosis-evidence.json
  → P0 decision cards
  → P1 versioned profiles
  → treatment-plan.json + treatment-plan.md
```

`diagnosis-evidence.json` 的每个 finding 至少有 `diagnosis_id`、`severity`、`confidence`、`scope`、`direction` 和测量证据。`calibration_required=true` 表示触发阈值尚未被大型标注语料验证。

`context.reference_gate` 保存参考数量、重复项、兼容度、离群风险、可信度上限和是否通过。若唯一失败原因是只有一首独立参考，可在等响门控之外生成 `conditional-hypothesis` 条件处方，但只使用原始差值、有上限严重度和能力级插件候选，禁止精确 P1 旋钮。重复、低兼容或其他门控失败仍只允许参考修正。

运行时插件字段可放入 `context`：

- `available_family_ids`
- `installed_versions`
- `host`、`format`、`sample_rate_hz`
- `plugin_modes`
- `host_latency_ms`（按 family_id 提供当前宿主实测 PDC；不要填音乐性 Delay 时间）
- `latency_budget_ms`、`realtime`
- `trust_catalog_snapshot`（显式接受快照，不等同实时确认）

`treatment-plan.json` 的 action 包含通用策略和零至两个插件候选。没有插件候选不等于没有方法；必须返回通用路由或显式退路。

`scope` 是安全边界：`mix-master` 不得调用 `target-vocal`/`lead-vocal` 卡；`vocal-instrument-relationship` 仅在可靠 Stems 存在时产生；`source_separated` 的低置信度会抑制精确旋钮。

## 人工证据量表

人工输入不得凭直觉制造小数精度。CLI 会按证据种类限制 `confidence` 上限：

- `repeatable_measurement`：最高 0.80；必须含实际数值与可复跑窗口。
- `equal_loudness_listening_confirmation`：最高 0.70；至少在等响、同段落、重复 A/B 下成立。
- `user_report`：最高 0.55；是用户感受，尚未独立复核。
- 未分类人工证据：最高 0.45。

`severity` 表示当前作品中的主观影响/优先级，不表示诊断置信度。人工严重度建议只用 0.25/0.50/0.75/1.00 四档，并写 `severity_basis`；不要将 0.76 等小数伪装成测量精度。

用户报告具体频段时写 `reported_band_hz: [low, high]`。它会成为第一个 Audition/Detector 搜索窗，但仍标为待监听确认，不升级为仪器测量事实。

处方 provenance 把两层证据分开：`p0_action_suitability_grade` 判断动作是否适合当前问题，`p1_control_validation_level` 只判断插件控件/版本行为。P1 L3 不能提高 P0 适用性等级。

权威 Schema 位于插件根目录：

- `schemas/diagnosis-evidence.schema.json`
- `schemas/treatment-plan.schema.json`
- `schemas/p0-decision-card.schema.json`

## 人工诊断示例

```json
{
  "schema_version": "1.0",
  "analysis_mode": "manual",
  "context": {"realtime": false, "max_actions": 4},
  "findings": [
    {
      "diagnosis_id": "parallel_distortion",
      "direction": "missing",
      "severity": 0.75,
      "confidence": 0.70,
      "severity_basis": "用户认为是高影响问题；人工四档量表 0.75",
      "scope": "lead-vocal",
      "calibration_required": true,
      "evidence": [{"evidence_kind": "equal_loudness_listening_confirmation", "listening_confirmation": "等响后仍比参考缺少中频颗粒"}]
    }
  ]
}
```
