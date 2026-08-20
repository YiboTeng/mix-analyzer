from __future__ import annotations

from copy import deepcopy
from pathlib import Path
from typing import Any

from .catalog import load_profiles, select_profiles
from .constants import CHAIN_STAGE_ORDER, DECISION_ENGINE_VERSION, PLUGIN_ID, TREATMENT_SCHEMA_VERSION
from .io import read_json


def load_cards(knowledge_root: Path) -> list[dict[str, Any]]:
    payload = read_json(knowledge_root / "p0" / "decision-cards.json")
    return payload["cards"]


def load_p0_provenance(knowledge_root: Path) -> dict[str, dict[str, Any]]:
    path = knowledge_root / "p0" / "source-manifest.json"
    if not path.is_file():
        return {}
    payload = read_json(path)
    return {entry["source_path"]: entry for entry in payload.get("entries", [])}


def _card_index(cards: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    result: dict[str, list[dict[str, Any]]] = {}
    for card in cards:
        for diagnosis in card.get("diagnoses", []):
            result.setdefault(diagnosis, []).append(card)
    return result


def _confidence_label(score: float) -> str:
    if score >= 0.85:
        return "高"
    if score >= 0.7:
        return "中高"
    if score >= 0.5:
        return "中"
    if score >= 0.35:
        return "中低"
    return "低"


def _make_action(
    finding: dict[str, Any], card: dict[str, Any], profiles: list[dict[str, Any]],
    rejected: list[dict[str, Any]], provenance_index: dict[str, dict[str, Any]],
    conditional_only: bool = False,
) -> dict[str, Any]:
    action = deepcopy(card["action"])
    evidence_tests = _evidence_conditioned_tests(finding)
    confidence = min(float(finding.get("confidence", 0.5)), float(card.get("evidence_weight", 0.6)))
    plugin_options = []
    for profile in profiles[:2]:
        warnings = list(profile.get("runtime_warnings", []))
        if float(finding.get("confidence", 0.0)) < 0.5:
            warnings.append("source_confidence_below_0.5_exact_controls_suppressed")
        if finding["diagnosis_id"] not in profile.get("capabilities", {}).get("diagnoses", []):
            warnings.append("capability_match_without_diagnosis_recipe_exact_controls_suppressed")
        if finding.get("scope") == "vocal-instrument-relationship":
            warnings.append("relationship_scope_recipe_unavailable_exact_controls_suppressed")
        if conditional_only:
            warnings.append("single_reference_conditional_exact_controls_suppressed")
        exact_controls_allowed = not any("exact_controls_suppressed" in warning for warning in warnings)
        start_points = list(profile.get("local_guidance", {}).get("parameter_start_points", [])) if exact_controls_allowed else []
        if card["id"] == "p0-parallel-grain" and exact_controls_allowed:
            start_points = [
                item for item in start_points
                if "mix" not in item.casefold()
            ]
            start_points.insert(0, "当前选定 Parallel Aux：插件 Mix/Wet=100%；用 Return Fader 控制混合比例。")
        control_table = deepcopy(profile.get("local_guidance", {}).get("controls", [])) if exact_controls_allowed else []
        control_actions = deepcopy(profile.get("parameter_strategy", {}).get("controls", [])) if exact_controls_allowed else []
        if card["id"] == "p0-parallel-grain" and exact_controls_allowed:
            for control in [*control_table, *control_actions]:
                if "mix" in str(control.get("name", "")).casefold():
                    control["action"] = "当前 Parallel Aux 路由固定 100% Wet；不用此旋钮混合，改用 Return Fader。"
        plugin_options.append({
            "adapter_id": profile.get("adapter_id"),
            "family_id": profile.get("family_id"),
            "vendor": profile.get("identity", {}).get("vendor"),
            "product": profile.get("identity", {}).get("product"),
            "version_range": profile.get("identity", {}).get("version_range"),
            "tested_host": profile.get("identity", {}).get("tested_host"),
            "route_options": [
                route for route in profile.get("routing", [])
                if route.get("when") == finding["diagnosis_id"]
            ],
            "control_actions": control_actions,
            "parameter_targets": profile.get("parameter_strategy", {}).get("targets", []),
            "start_points": start_points,
            "control_table": control_table,
            "listen_for": profile.get("local_guidance", {}).get("listen_for", []),
            "stop_conditions": profile.get("stop_conditions", []),
            "risks": profile.get("risks", []),
            "alternatives": profile.get("alternatives", []),
            "runtime_warnings": warnings,
            "runtime_constraints": profile.get("runtime_constraints", {}),
            "runtime_confirmation": profile.get("runtime_confirmation", {}),
            "estimated_latency_ms": profile.get("estimated_latency_ms"),
            "exact_controls_allowed": exact_controls_allowed,
            "evidence": profile.get("evidence", {}),
        })
    provenance = deepcopy(card["provenance"])
    grade_parts = str(provenance.get("evidence_grade", "E")).split("+")
    p0_grades = [item for item in grade_parts[0] if item in "ABCDE"]
    provenance["p0_action_suitability_grade"] = max(p0_grades, default="E")
    provenance["p1_control_validation_level"] = next(
        (item for item in grade_parts[1:] if item.startswith("P1-")), None
    )
    candidate_levels = sorted({
        str(item.get("evidence", {}).get("level")) for item in plugin_options
        if item.get("evidence", {}).get("level")
    })
    if candidate_levels:
        provenance["p1_control_validation_level"] = (
            candidate_levels[0] if len(candidate_levels) == 1 else "mixed:" + "/".join(candidate_levels)
        )
    provenance["packaged_sources"] = [
        provenance_index[path] for path in provenance.get("source_paths", []) if path in provenance_index
    ]
    return {
        "action_id": f"{finding['diagnosis_id']}::{card['id']}",
        "card_id": card["id"],
        "diagnosis_id": finding["diagnosis_id"],
        "diagnosis_ids": [finding["diagnosis_id"]],
        "title": card["title"],
        "action_status": "conditional-hypothesis" if conditional_only else "standard",
        "priority_score": round(float(finding.get("severity", 0.5)) * 0.6 + confidence * 0.4, 4),
        "confidence": {"score": round(confidence, 4), "label": _confidence_label(confidence)},
        "chain_stage": card["chain_stage"],
        "scope": finding.get("scope"),
        "routing_type": _routing_type(action.get("routing", "")),
        "routing_contract": _routing_contract(card, finding, _routing_type(action.get("routing", ""))),
        "why": {"finding": finding, "hypotheses": card.get("hypotheses", [])},
        "disambiguation_tests": [*evidence_tests, *card.get("disambiguation_tests", [])],
        "operation": action,
        "plugin_options": plugin_options,
        "rejected_plugins": rejected,
        "verification": card["verification"],
        "verification_protocol": _verification_protocol(card, finding),
        "provenance": provenance,
        "calibration_required": bool(finding.get("calibration_required", False) or card.get("calibration_required", False)),
        "chain_warnings": ([
            "单参考条件处方：必须先完成等响、同职责段落的重复 A/B；不得把原始差值直接复制成处理量。"
        ] if conditional_only else []),
    }


def _routing_type(routing: str) -> str:
    value = routing.casefold()
    if "监听" in routing or "monitor" in value:
        return "monitoring-only"
    if "aux" in value or "发送" in routing or "返回" in routing:
        return "send-return"
    if "clip gain" in value or "事件" in routing or "编辑" in routing:
        return "event-edit"
    if "总线" in routing or "master" in value or "bus" in value:
        return "bus-insert"
    return "track-insert-or-upstream-correction"


def _routing_contract(card: dict[str, Any], finding: dict[str, Any], routing_type: str) -> dict[str, Any]:
    contract = {
        "routing_type": routing_type,
        "source_scope": finding.get("scope"),
        "target_bus": finding.get("scope"),
        "wet_policy": "按通用步骤设置并做输出等响",
        "detector": None,
    }
    if card["id"] == "p0-sibilance-harshness":
        contract.update({
            "target_bus": f"{finding.get('scope')} insert",
            "wet_policy": "Insert 主处理；先限 Range，再用 Threshold/Sensitivity 控制触发",
            "detector": "插件内部侧链；用 Audition 确认只抓目标辅音",
        })
    elif card["id"] == "p0-parallel-grain":
        contract.update({
            "target_bus": "filtered-grain-aux",
            "wet_policy": "Aux 内失真/饱和保持 100% Wet；只用 Return Fader 混合，忽略 Insert Mix 起点",
            "detector": "无；必要时由干净主唱侧链控制返回动态",
        })
    elif card["id"] == "p0-vocal-width":
        contract.update({
            "target_bus": "chorus-adlib-width-aux" if finding.get("scope") == "chorus-adlib" else "vocal-width-aux",
            "wet_policy": "宽化 Aux 100% Wet；Lead Vocal Dry/Mid 保持不变",
            "detector": "无；按段落自动化 Send/Return",
        })
    return contract


def _reported_band(finding: dict[str, Any]) -> tuple[float, float] | None:
    for evidence in finding.get("evidence", []):
        band = evidence.get("reported_band_hz") if isinstance(evidence, dict) else None
        if isinstance(band, list) and len(band) == 2:
            return float(band[0]), float(band[1])
    return None


def _evidence_conditioned_tests(finding: dict[str, Any]) -> list[str]:
    band = _reported_band(finding)
    if not band:
        return []
    low, high = band
    return [
        f"用户报告的 {low:g}–{high:g} Hz 仅作首个 Audition/Detector 搜索窗；先确认命中目标事件而非元音，再向外扩展。"
    ]


def _verification_protocol(card: dict[str, Any], finding: dict[str, Any]) -> dict[str, Any]:
    protocol = {
        "baseline": "保存处理前设置或渲染；处理后输出补偿至等响",
        "measurement_window": "使用与触发证据相同的段落/事件窗口",
        "comparison": "单变量处理前后 A/B，并同时复测 verification.remeasure_metrics",
        "acceptance": "至少一个目标听感/指标改善，且 failure_signs 无新增恶化",
        "rollback": "命中任一 stop_condition 或收益只来自更响时恢复基线",
    }
    if card["id"] == "p0-sibilance-harshness":
        band = _reported_band(finding)
        window = f"{band[0]:g}–{band[1]:g} Hz" if band else "已确认的齿音带"
        protocol.update({
            "measurement_window": f"固定 3–5 个最坏 S/T/CH 事件与 2 个非齿音元音；先检查 {window}",
            "comparison": "比较事件能量、最大/中位 GR，并确认非齿音元音高频没有持续下降",
            "acceptance": "最坏齿音下降且非齿音元音亮度基本不变",
        })
    elif card["id"] == "p0-parallel-grain":
        protocol.update({
            "measurement_window": "固定 10–20 秒主唱活跃段，并包含最坏齿音",
            "comparison": "处理前后 LUFS-S 匹配在约 ±0.2 dB，再比较谐波份额与 6–12 kHz 事件能量",
            "acceptance": "中频支撑/颗粒增加，齿音事件、噪声、峰值与 Mono 不恶化",
        })
    elif card["id"] == "p0-vocal-width":
        protocol.update({
            "measurement_window": "只在副歌 Ad-lib 活跃窗测量，并保留一个 Lead-only 对照窗",
            "comparison": "比较 Side/Mid、LR correlation、Mono fold loss，并确认 Lead Vocal Mid 电平/清晰度不变",
            "acceptance": "Ad-lib 宽度增加，Mono 与 Lead 中心均保持",
        })
    return protocol


def _resolve_dependencies(actions: list[dict[str, Any]]) -> list[dict[str, Any]]:
    # A failed reference gate and a loudness-bias observation are two pieces of
    # evidence for the same gate operation. Their findings legitimately use
    # different scopes (reference-set vs mix-master), so the normal card/scope
    # deduplication below cannot merge them. Keep the explicit gate action and
    # fold the loudness evidence into it instead of asking the user to perform
    # the same equal-loudness check twice.
    reference_gate = next(
        (
            item for item in actions
            if item["card_id"] == "p0-reference-level-gate"
            and "reference_mismatch" in item.get("diagnosis_ids", [])
        ),
        None,
    )
    if reference_gate is not None:
        retained: list[dict[str, Any]] = []
        for action in actions:
            duplicate_loudness_gate = (
                action is not reference_gate
                and action["card_id"] == "p0-reference-level-gate"
                and "loudness_bias_check" in action.get("diagnosis_ids", [])
            )
            if not duplicate_loudness_gate:
                retained.append(action)
                continue
            reference_gate["diagnosis_ids"] = sorted(set(
                reference_gate.get("diagnosis_ids", []) + action.get("diagnosis_ids", [])
            ))
            reference_gate["why"]["finding"].setdefault("evidence", []).extend(
                action.get("why", {}).get("finding", {}).get("evidence", [])
            )
            reference_gate["priority_score"] = max(
                reference_gate["priority_score"], action["priority_score"]
            )
            reference_gate["calibration_required"] = bool(
                reference_gate.get("calibration_required") or action.get("calibration_required")
            )
        actions = retained

    # One responsibility per card/scope; merge evidence from multiple metrics.
    unique: dict[tuple[str, str], dict[str, Any]] = {}
    for action in actions:
        key = (action["card_id"], action["scope"])
        if key not in unique:
            unique[key] = action
            continue
        current = unique[key]
        merged_ids = sorted(set(current["diagnosis_ids"] + action["diagnosis_ids"]))
        merged_evidence = [
            *current["why"]["finding"].get("evidence", []),
            *action["why"]["finding"].get("evidence", []),
        ]
        if action["priority_score"] > current["priority_score"]:
            action["diagnosis_ids"] = merged_ids
            action["why"]["finding"]["evidence"] = merged_evidence
            unique[key] = action
        else:
            current["diagnosis_ids"] = merged_ids
            current["why"]["finding"]["evidence"] = merged_evidence
    result = list(unique.values())

    # Resolve mutually exclusive directional responsibilities within one scope.
    conflict_groups = [
        {"vocal_width_deficit", "vocal_width_excess", "mono_translation_risk"},
        {"master_low_end_excess", "master_low_end_deficit"},
        {"master_presence_excess", "master_presence_deficit"},
        {"master_high_side_excess", "master_high_side_deficit", "mono_translation_risk"},
        {"master_peak_excess", "master_overlimited"},
    ]
    suppressed: set[str] = set()
    for group in conflict_groups:
        for scope in {item["scope"] for item in result}:
            matches = [item for item in result if item["scope"] == scope and group.intersection(item["diagnosis_ids"])]
            if len(matches) < 2:
                continue
            winner = max(matches, key=lambda item: item["priority_score"])
            for item in matches:
                if item is winner:
                    continue
                suppressed.add(item["action_id"])
                winner.setdefault("chain_warnings", []).append(
                    f"方向冲突：已暂缓 {item['diagnosis_id']}；先用单变量实验确认 {winner['diagnosis_id']}。"
                )
    result = [item for item in result if item["action_id"] not in suppressed]
    # Add explicit chain warnings for common destructive combinations.
    diagnoses = {item["diagnosis_id"] for item in result}
    for item in result:
        warnings = item.setdefault("chain_warnings", [])
        if item["chain_stage"] == "harmonic-tone" and ("sibilance" in diagnoses or "harsh_consonants" in diagnoses):
            warnings.append("先控制齿音/刺耳，再推饱和或并行失真；失真后重新检查新生高次谐波。")
        if item["chain_stage"] == "clip-limit" and "loudness_bias_check" in diagnoses:
            warnings.append("先完成等响参考校准，再判断是否需要削波/限制；不要用更响掩盖音色问题。")
        if item["chain_stage"] == "width-layering":
            warnings.append("主唱主体保持中心；宽度优先放在辅助层/返回，并复核 Mono Fold-down。")
    return result


def _select_with_prerequisites(
    ranked: list[dict[str, Any]], max_actions: int
) -> tuple[list[dict[str, Any]], list[tuple[dict[str, Any], str]]]:
    selected: list[dict[str, Any]] = []
    deferred: list[tuple[dict[str, Any], str]] = []
    selected_ids: set[str] = set()
    deferred_ids: set[str] = set()

    def prerequisite_for(action: dict[str, Any]) -> list[dict[str, Any]]:
        requirements: list[dict[str, Any]] = []
        if action["chain_stage"] == "harmonic-tone":
            deess = [
                item for item in ranked
                if item["chain_stage"] == "deessing" and item.get("scope") == action.get("scope")
            ]
            if deess:
                requirements.append(max(deess, key=lambda item: item["priority_score"]))
        if action["chain_stage"] == "clip-limit":
            gates = [item for item in ranked if item["chain_stage"] == "reference-gate"]
            if gates:
                requirements.append(max(gates, key=lambda item: item["priority_score"]))
        return requirements

    for action in ranked:
        if action["action_id"] in selected_ids or action["action_id"] in deferred_ids:
            continue
        prerequisites = [item for item in prerequisite_for(action) if item["action_id"] not in selected_ids]
        action["prerequisite_action_ids"] = [item["action_id"] for item in prerequisites]
        if len(selected) + len(prerequisites) + 1 <= max_actions:
            for prerequisite in prerequisites:
                if prerequisite["action_id"] not in selected_ids:
                    selected.append(prerequisite)
                    selected_ids.add(prerequisite["action_id"])
            selected.append(action)
            selected_ids.add(action["action_id"])
            continue
        if prerequisites:
            for prerequisite in prerequisites:
                if len(selected) >= max_actions:
                    break
                if prerequisite["action_id"] not in selected_ids:
                    selected.append(prerequisite)
                    selected_ids.add(prerequisite["action_id"])
            deferred.append((action, "prerequisite_not_delivered_within_action_budget"))
            deferred_ids.add(action["action_id"])
        elif len(selected) < max_actions:
            selected.append(action)
            selected_ids.add(action["action_id"])
        else:
            deferred.append((action, "below_top_k_cutoff"))
            deferred_ids.add(action["action_id"])

    for action in ranked:
        if action["action_id"] not in selected_ids and action["action_id"] not in deferred_ids:
            deferred.append((action, "below_top_k_cutoff"))
    return selected, deferred


def _validate_plan_contract(plan: dict[str, Any]) -> None:
    if plan.get("analysis_mode") not in {"manual", "vocal-reference", "mix-reference"}:
        raise ValueError("Treatment plan has an invalid analysis_mode")
    if plan["analysis_mode"] != "manual":
        gate = plan.get("context", {}).get("reference_gate")
        if not isinstance(gate, dict) or not isinstance(gate.get("passed"), bool):
            raise ValueError("Reference-mode plan is missing a valid reference_gate")
    for action in plan.get("actions", []):
        protocol = action.get("verification_protocol", {})
        if not all(str(protocol.get(key, "")).strip() for key in ("baseline", "measurement_window", "comparison", "acceptance", "rollback")):
            raise ValueError(f"Action {action.get('action_id')} has an incomplete verification protocol")
        provenance = action.get("provenance", {})
        if not provenance.get("p0_action_suitability_grade") or "packaged_sources" not in provenance:
            raise ValueError(f"Action {action.get('action_id')} has incomplete provenance")
        for plugin in action.get("plugin_options", []):
            if plugin.get("exact_controls_allowed"):
                status = plugin.get("runtime_confirmation", {}).get("status")
                if status not in {"live-context-confirmed", "snapshot-explicit"}:
                    raise ValueError(
                        f"Plugin {plugin.get('family_id')} exposes exact controls without runtime confirmation"
                    )


def prescribe(
    diagnosis: dict[str, Any], knowledge_root: Path, context_override: dict[str, Any] | None = None
) -> dict[str, Any]:
    cards = load_cards(knowledge_root)
    provenance_index = load_p0_provenance(knowledge_root)
    profiles = load_profiles(knowledge_root)
    indexed = _card_index(cards)
    context = {**diagnosis.get("context", {}), **(context_override or {})}
    mode = diagnosis.get("analysis_mode", "manual")
    reference_gate = context.get("reference_gate")
    if mode != "manual" and (not isinstance(reference_gate, dict) or "passed" not in reference_gate):
        reference_gate = {"passed": False, "reasons": ["missing_reference_gate"]}
        context["reference_gate"] = reference_gate
    elif mode == "manual" and not isinstance(reference_gate, dict):
        reference_gate = {"passed": True, "reasons": []}
    actions = []
    unresolved = []
    gate_reasons = set(reference_gate.get("reasons", []))
    conditional_single_reference = (
        mode != "manual"
        and not reference_gate.get("passed", True)
        and int(reference_gate.get("reference_count") or 0) == 1
        and gate_reasons == {"fewer_than_two_independent_references"}
    )
    for finding in diagnosis.get("findings", []):
        candidate_cards = indexed.get(finding["diagnosis_id"], [])
        compatible = [
            card for card in candidate_cards
            if mode in card.get("modes", [])
            and ("*" in card.get("scopes", []) or finding.get("scope") in card.get("scopes", []))
            and (not card.get("requires_stems") or bool(context.get("stems_available")))
        ]
        conditional_only = False
        if mode != "manual" and not reference_gate.get("passed", True):
            if conditional_single_reference and finding["diagnosis_id"] != "reference_mismatch":
                conditional_only = True
            else:
                compatible = [
                    card for card in compatible
                    if card["id"] == "p0-reference-level-gate" and finding["diagnosis_id"] == "reference_mismatch"
                ]
        if not compatible:
            reason = (
                "reference_gate_failed"
                if mode != "manual" and not reference_gate.get("passed", True) and not conditional_only
                else "no_mode_and_scope_safe_p0_card"
            )
            unresolved.append({
                "diagnosis_id": finding["diagnosis_id"],
                "reason": reason,
                "fallback": "保留该诊断为待验证假设；先做等响监听、单变量实验和复测，不输出固定插件数值。",
            })
            continue
        for card in compatible:
            preferred = card.get("capability_by_diagnosis", {}).get(
                finding["diagnosis_id"], card.get("preferred_capabilities", [])
            )
            candidates, rejected = select_profiles(finding["diagnosis_id"], preferred, profiles, context)
            actions.append(_make_action(
                finding, card, candidates, rejected, provenance_index,
                conditional_only=conditional_only,
            ))
    actions = _resolve_dependencies(actions)
    max_actions = int(context.get("max_actions", 6))
    ranked = sorted(actions, key=lambda item: (-item["priority_score"], CHAIN_STAGE_ORDER.get(item["chain_stage"], 999)))
    actions, deferred = _select_with_prerequisites(ranked, max_actions)
    actions.sort(key=lambda item: (CHAIN_STAGE_ORDER.get(item["chain_stage"], 999), -item["priority_score"]))
    plan = {
        "schema_version": TREATMENT_SCHEMA_VERSION,
        "plugin_id": PLUGIN_ID,
        "decision_engine_version": DECISION_ENGINE_VERSION,
        "analysis_mode": mode,
        "source_diagnosis_schema": diagnosis.get("schema_version"),
        "context": context,
        "summary": {
            "finding_count": len(diagnosis.get("findings", [])),
            "action_count": len(actions),
            "deferred_count": len(deferred),
            "unresolved_count": len(unresolved),
            "automatic_thresholds_calibrated": False,
        },
        "actions": actions,
        "deferred_actions": [
            {"action_id": item["action_id"], "priority_score": item["priority_score"], "reason": reason}
            for item, reason in deferred
        ],
        "unresolved": unresolved,
        "global_verification": [
            "每次只改一个职责层，输出补偿后做等响旁路 A/B。",
            "保留原始版本或可回滚设置；若收益只在 Solo、频谱图或更响条件下成立，回退。",
            "处理后重新运行原分析指标，并同时检查主观副作用、Mono、峰值与延迟。",
            "自动阈值尚未经过大型标注语料校准；数值触发只生成可证伪的起点，不是自动执行授权。",
        ],
    }
    _validate_plan_contract(plan)
    return plan
