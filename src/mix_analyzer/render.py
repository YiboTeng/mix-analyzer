from __future__ import annotations

from typing import Any


def _bullets(items: list[Any], indent: str = "") -> list[str]:
    return [f"{indent}- {item}" for item in items]


def _value(value: Any) -> str:
    if isinstance(value, dict):
        return "；".join(f"{key}={_value(item)}" for key, item in value.items())
    if isinstance(value, list):
        return "、".join(_value(item) for item in value)
    return str(value)


def render_markdown(plan: dict[str, Any]) -> str:
    lines = [
        "# 混音优化处方",
        "",
        f"- 模式：`{plan['analysis_mode']}`",
        f"- 处方引擎：`{plan['decision_engine_version']}`",
        f"- 已选动作：{plan['summary']['action_count']}；未解析：{plan['summary']['unresolved_count']}",
        "- 重要边界：自动指标阈值尚未完成大规模语料校准，以下参数是可回滚起点。",
        "- 可信度量表：0.85–1.00 高；0.70–0.84 中高；0.50–0.69 中；0.35–0.49 中低；低于 0.35 低。",
        "",
    ]
    gate = plan.get("context", {}).get("reference_gate")
    if gate:
        compatibility = gate.get("median_compatibility")
        if isinstance(compatibility, (int, float)):
            compatibility = f"{compatibility:.1f}"
        lines += [
            "## 参考门控",
            "",
            f"- 状态：{'通过' if gate.get('passed') else '未通过'}",
            f"- 参考数量：{gate.get('reference_count')}；可信度上限：{gate.get('confidence_cap')}",
            f"- 兼容度中位数：{compatibility}",
        ]
        lines += _bullets([f"门控原因：{item}" for item in gate.get("reasons", [])])
        lines.append("")

    for index, action in enumerate(plan.get("actions", []), 1):
        finding = action.get("why", {}).get("finding", {})
        lines += [
            f"## {index}. {action['title']}",
            "",
            f"- 诊断：`{action['diagnosis_id']}`",
            f"- 合并诊断：{', '.join(action.get('diagnosis_ids', [action['diagnosis_id']]))}",
            f"- 作用范围：`{action.get('scope')}`",
            f"- 链路阶段：`{action['chain_stage']}`",
            f"- 路由类型：`{action.get('routing_type')}`",
            f"- 动作状态：`{action.get('action_status', 'standard')}`",
            f"- 优先级：{action['priority_score']:.2f}",
            f"- 建议可信度：{action['confidence']['label']}（{action['confidence']['score']:.2f}）",
            f"- 需要语料校准：{'是' if action.get('calibration_required') else '否'}",
            "",
            "### 证据与待验证假设",
            "",
            f"- 方向：`{finding.get('direction')}`；严重度：{finding.get('severity')}；原始置信度：{finding.get('confidence')}",
        ]
        if finding.get("confidence_basis"):
            lines += [f"- 置信度依据：`{finding.get('confidence_basis')}`；严重度依据：{finding.get('severity_basis')}"]
        lines += _bullets([f"用户/分析证据：{_value(item)}" for item in finding.get("evidence", [])])
        lines += _bullets([f"假设：{item}" for item in action.get("why", {}).get("hypotheses", [])])
        lines += ["", "### 先做判别", ""]
        lines += _bullets(action.get("disambiguation_tests", [])) or ["- 无额外判别测试。"]

        operation = action["operation"]
        routing = action.get("routing_contract", {})
        lines += [
            "", "### 通用操作", "",
            f"- 路由（{action.get('routing_type')}）：{operation.get('routing')}",
            f"- 来源 Scope：`{routing.get('source_scope')}`；目标轨/Bus：`{routing.get('target_bus')}`",
            f"- Wet 策略：{routing.get('wet_policy')}",
        ]
        if routing.get("detector"):
            lines += [f"- Detector/Sidechain：{routing.get('detector')}"]
        lines += _bullets(operation.get("steps", []))
        if operation.get("parameter_start_ranges"):
            lines += ["", "参数起点：", ""] + _bullets(operation["parameter_start_ranges"])

        if action.get("plugin_options"):
            lines += ["", "### 插件映射", ""]
        for plugin in action.get("plugin_options", []):
            product = plugin["product"]
            vendor = plugin["vendor"]
            display_name = product if product.lower().startswith(vendor.lower()) else f"{vendor} {product}"
            lines += [f"#### {display_name}（验证版本 {plugin['version_range']}）", ""]
            if plugin.get("runtime_warnings"):
                lines += _bullets([f"运行时警告：{item}" for item in plugin["runtime_warnings"]])
            confirmation = plugin.get("runtime_confirmation", {})
            if confirmation:
                lines += [
                    f"- 运行时确认：`{confirmation.get('status')}`；版本={confirmation.get('installed_version')}；Host={confirmation.get('host')}；格式={confirmation.get('format')}；采样率={confirmation.get('sample_rate_hz')}"
                ]
            if not plugin.get("exact_controls_allowed"):
                lines += ["- 精确旋钮已抑制：先确认当前安装版本、格式、宿主与采样率；以下仅保留能力级目标。"]
            if plugin.get("route_options"):
                lines += _bullets([f"路由：{item['position']}；条件：{item['when']}" for item in plugin["route_options"]])
            if plugin.get("parameter_targets"):
                lines += _bullets([f"参数目标：{item}" for item in plugin["parameter_targets"]])
            if plugin.get("start_points"):
                lines += _bullets([f"起点：{item}" for item in plugin["start_points"]])
            if plugin.get("control_table"):
                lines += _bullets([
                    f"旋钮 {item.get('name')}：含义={item.get('meaning')}；操作={item.get('action')}"
                    for item in plugin["control_table"]
                ])
            if plugin.get("control_actions"):
                lines += _bullets([f"{item['name']}：{item['action']}" for item in plugin["control_actions"]])
            if plugin.get("listen_for"):
                lines += _bullets([f"插件监听点：{item}" for item in plugin["listen_for"]])
            if plugin.get("risks"):
                lines += _bullets([f"风险：{item}" for item in plugin["risks"]])
            if plugin.get("stop_conditions"):
                lines += _bullets([f"停止：{item}" for item in plugin["stop_conditions"]])
            if plugin.get("alternatives"):
                lines += _bullets([f"替代：{_value(item)}" for item in plugin["alternatives"]])
            evidence = plugin.get("evidence", {})
            if evidence:
                lines += [f"- 插件证据等级：`{evidence.get('level')}`"]
                packaged = evidence.get("packaged", {})
                paths = []
                for key in ("card", "source_note", "validation_report"):
                    if packaged.get(key):
                        paths.append(packaged[key].get("packaged_path"))
                paths += [item.get("packaged_path") for item in packaged.get("result_files", [])]
                lines += _bullets([f"插件证据：{path}" for path in paths if path])
            lines.append("")

        if action.get("rejected_plugins"):
            lines += ["### 被拒绝的插件候选", ""]
            lines += _bullets([
                f"{item.get('adapter_id')}：{', '.join(item.get('reasons', []))}"
                for item in action["rejected_plugins"]
            ])
            lines.append("")

        lines += ["### 复测与停止", ""]
        verification = action["verification"]
        lines += _bullets([f"听：{item}" for item in verification.get("listen_for", [])])
        lines += _bullets([f"失败信号：{item}" for item in verification.get("failure_signs", [])])
        lines += _bullets([f"停止：{item}" for item in verification.get("stop_conditions", [])])
        lines += _bullets([f"复测：{item}" for item in verification.get("remeasure_metrics", [])])
        protocol = action.get("verification_protocol", {})
        if protocol:
            lines += ["", "操作化验收：", ""]
            lines += _bullets([
                f"基线：{protocol.get('baseline')}",
                f"测量窗口：{protocol.get('measurement_window')}",
                f"比较方法：{protocol.get('comparison')}",
                f"通过条件：{protocol.get('acceptance')}",
                f"回滚：{protocol.get('rollback')}",
            ])
        if action.get("chain_warnings"):
            lines += ["", "链路警告：", ""] + _bullets(action["chain_warnings"])

        provenance = action.get("provenance", {})
        lines += [
            "", "### 证据来源", "",
            f"- 原始复合等级：`{provenance.get('evidence_grade')}`",
            f"- P0 动作适用性：`{provenance.get('p0_action_suitability_grade')}`",
            f"- P1 控件验证：`{provenance.get('p1_control_validation_level')}`",
        ]
        lines += _bullets([
            f"打包来源：{item.get('packaged_path')}（SHA-256 {item.get('sha256')}）"
            for item in provenance.get("packaged_sources", [])
        ])
        lines += _bullets([f"官方资料：{url}" for url in provenance.get("official_urls", [])])
        lines.append("")

    if plan.get("unresolved"):
        lines += ["## 尚未覆盖或被门控的诊断", ""]
        lines += _bullets([f"{item['diagnosis_id']}（{item['reason']}）：{item['fallback']}" for item in plan["unresolved"]])
        lines.append("")
    lines += ["## 全局复核", ""] + _bullets(plan.get("global_verification", []))
    return "\n".join(lines) + "\n"
