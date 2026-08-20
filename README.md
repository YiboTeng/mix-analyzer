# Mix Analyzer

面向 Codex 的双模式混音分析与处方插件。它继承 `mix-reference-comparator` 当前工作树的干声/人声分析与完整 Mix/Master 分析，并新增：

- P0：把分析指标规范化为诊断证据，调用结构化决策卡，生成可回滚的处理策略。
- P1：导入 40 款本机插件的 L3 Adapter、版本边界、参数起点、风险和证据摘要。
- 处方闭环：判别测试 → 路由 → 插件/参数起点 → 监听目标 → 停止条件 → 复测。

## 三种入口

1. `compare-vocal-references`：干声、独唱、Vocal Stem 或人声分离参考。
2. `compare-mix-references`：包含 Vocal 与 Beat/Instrumental 的完整 Mix/Master；有可靠 Stems 时启用关系诊断。
3. `prescribe-mix-actions`：读取以上指标、规范化诊断并生成插件级处方。

干声与完整 Mix 不进入同一个参考统计集。Master-only 不反推具体 Stem、插件、Preset 或精确单轨参数。

## 快速运行处方引擎

```powershell
Set-Location "C:\Projects\mix-analyzer"
$env:PYTHONPATH = "C:\Projects\mix-analyzer\src"

python -m mix_analyzer.cli `
  --input "C:\path\to\reference-set-metrics.json" `
  --out-dir "C:\Projects\work\mix-prescription"
```

默认在未确认当前安装版本、宿主、格式与采样率时抑制精确 P1 旋钮。可以传 `--context-json`，或使用 `--installed-version FAMILY_ID=VERSION --host ... --format VST3 --sample-rate-hz 48000`。仅明确接受打包 P1 快照边界时使用 `--trust-catalog-snapshot`。生产式交付建议同时传 `--require-jsonschema`。

输出：

```text
diagnosis-evidence.json
treatment-plan.json
treatment-plan.md
```

## 知识边界

- P0 当前是首批高频决策卡，不是完整音乐制作百科。
- 旧分析器 `practical_floor` 和稳健偏差阈值尚未在大型标注语料上校准，因此自动触发只是一条可证伪建议。
- P1 的 L3 表示指定版本、宿主、采样率和固定夹具下已验证主要行为；不等于真实作品 L4。
- 版本不匹配时只保留能力级建议，抑制确定性旋钮映射。
- 自动参考模式会先检查参考数量、重复项、兼容度与离群风险；单参考只使用原始差值并可给低置信度条件处方，其他门控失败只给参考修正，所有失败门控都禁止精确插件旋钮。
- P0 卡按 `mode + scope` 双重隔离；Master-only 不会套用人声高通、修音或单轨压缩参数。
- 破坏性下游动作有硬前置：存在齿音动作时，饱和/失真不能挤掉去齿；存在参考门控动作时，削波/限制不能越过门控。
- 所有动作都要求等响 A/B、全混音监听、Mono/峰值/延迟检查和回滚条件。

## P1 快照

`scripts/import_p1_snapshot.py` 从 `C:\Projects\aizen-knowledge-base` 导入小型运行时快照：40 个 Adapter、索引、卡片、来源、验证报告和小型结果 JSON。不会复制约 1.386 GB 的 WAV、渲染和 DAW 工程。

```powershell
python .\scripts\import_p1_snapshot.py
```

## 验证

```powershell
$env:PYTHONPATH = "C:\Projects\mix-analyzer\src"
python -m pip install -e ".[dev]"
python -m unittest discover -s .\tests -p "test_*.py" -v
python .\scripts\validate_runtime.py
python "C:\Users\Administrator\.codex\skills\.system\skill-creator\scripts\quick_validate.py" .\skills\prescribe-mix-actions
python "C:\Users\Administrator\.codex\skills\.system\plugin-creator\scripts\validate_plugin.py" .
```

这是 Codex 插件源码树，不发布为独立 wheel；运行时知识位于 `skills/prescribe-mix-actions/knowledge`，因此应从插件根目录运行或显式传 `--knowledge-root`。

## 目录

```text
mix-analyzer/
├─ .codex-plugin/plugin.json
├─ skills/
│  ├─ select-reference-analysis-mode/
│  ├─ compare-vocal-references/
│  ├─ compare-mix-references/
│  └─ prescribe-mix-actions/
│     ├─ knowledge/p0/
│     ├─ knowledge/p1/
│     ├─ references/
│     └─ SKILL.md
├─ src/mix_analyzer/
├─ schemas/
├─ scripts/
├─ tests/
└─ docs/
```

迁移来源、当前旧工作树提交和文件哈希见 `docs/provenance/comparator-working-tree.json`。

自动指标到诊断、Scope 与 P0 职责的连接范围见 `docs/COVERAGE_MATRIX.md`；manual-only 卡不会伪装成自动覆盖。
