# 自动连接覆盖矩阵

本表区分“分析器自动触发”与“只有人工/报告证据才能触发”。卡片数量不等于自动诊断覆盖率。

## 人声参考模式

| Analyzer metric | 高于参考 | 低于参考 | P0 职责 |
|---|---|---|---|
| `integrated_lufs` / `rms_dbfs` | loudness gate | loudness gate | `p0-reference-level-gate` |
| `crest_factor_db` | `fast_peak_control` | `overcompressed_vocal` | 峰值控制 / 动态恢复 |
| `active_range_db` / `macro_range_db` | `macro_level_inconsistency` | `overcompressed_vocal` | 短语电平 / 动态恢复 |
| `micro_range_db` | `fast_peak_control` | `overcompressed_vocal` | 峰值控制 / 动态恢复 |
| `presence_db` | `harshness` | `presence_dullness` | 动态频谱 / Presence |
| `air_db` | `sibilance` | `lack_of_air` | 去齿 / Air |
| `low_mid_masking_db` | `mud` | `vocal_weight_deficit` | 减法分诊 / 重量恢复 |
| `upper_harmonic_share` | `harsh_consonants` | `harmonic_density` | 去齿 / 并行谐波 |
| `harmonic_concentration` | `harshness` | `harmonic_density` | 共振 / 并行谐波 |
| `spectral_flatness` | `broadband_stationary_noise` | — | 修复 |
| `side_mid_db` | `vocal_width_excess` | `vocal_width_deficit` | 宽度安全 / 辅助层宽化 |
| `lr_correlation` | — | `mono_translation_risk` | 宽度安全 |
| `width_tails_db` | `vocal_width_excess` | `vocal_depth` | 宽度安全 / 空间 |
| `width_core_db` | `vocal_width_excess` | `vocal_width_deficit` | 宽度安全 / 辅助层宽化 |

## 完整 Mix/Master 模式

| Analyzer metric | 高于参考 | 低于参考 | Scope / P0 职责 |
|---|---|---|---|
| `LUFS-I` | loudness gate | loudness gate | reference / monitoring |
| `PLR` | `master_peak_excess` | `master_overlimited` | mix-master / 削峰或恢复动态 |
| `Sub` | `master_low_end_excess` | `master_low_end_deficit` | mix-master / 总线安全低频 |
| `Presence` | `master_presence_excess` | `master_presence_deficit` | mix-master / 总线安全 Presence |
| `High Side` | `master_high_side_excess` | `master_high_side_deficit` | mix-master / 宽度翻译 |
| `Mono Loss` | `mono_translation_risk` | 不触发 | mix-master / Mono 安全 |

Master-only 卡禁止套用人声高通、单轨压缩、修音或从 Master 反推 Stem。只有 `records.*.stems` 对 Target 与 References 均存在时，才产生以下关系 finding：

| Stem metric | Canonical finding | Scope | 可靠性 |
|---|---|---|---|
| `presence_mask_risk` / `hat_sibilance_mask_risk` | `frequency_masking` | vocal-instrument-relationship | 取最弱 Stem 来源等级 |
| `vir_median_db` 偏低 | `presence_dullness` | vocal-instrument-relationship | 同上 |
| `spatial_width_gap_db` 偏高 | `vocal_instrument_width_gap` | vocal-instrument-relationship | 绝对差值只触发判别，不直接决定加宽哪侧 |
| `bass.side_mid_db` 偏高 | `low_frequency_mono` | bass-stem | 同上 |

`source_separated` 的置信度上限为 0.45，因此会抑制精确 P1 旋钮，只保留可回滚实验。

## 仍是 manual/report-only

以下领域已有 P0 卡与 P1 能力，但旧分析器尚无稳定自动检测器：音高校正、逐音编辑、呼吸、爆破、嘴声/点击、具体 Delay/Reverb 类型、句尾 Throw、细粒度瞬态、段落自动化、真实双轨识别、交付规格选择。它们必须来自用户确认、人工审听或后续事件检测器，不计入自动覆盖率。

