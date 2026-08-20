# 自审记录

## 已发现并修复

1. 不能按旧仓库 HEAD 迁移：完整 Mix 与路由 Skill 尚未提交。已按当前工作树复制，并记录 HEAD、porcelain 状态和文件哈希。
2. P1 Adapter 没有足够的逐旋钮数值。已从 40 张 L3 卡提取参数起点、控件语义、监听与停止信息生成 Profile。
3. P1 证据路径原本依赖知识库根目录。已打包小型证据并保存原路径、打包路径与 SHA-256。
4. 实时呼吸处理可能误选高延迟 DeBreath。已把 Host 延迟与音乐性 Delay 分成结构化运行时约束、执行预算过滤，并用测试固定 Clip Gain 退路。
5. 爆破可能误选 WNS。已按诊断设置 capability override，只允许动态 EQ/Clip Gain 路径；测试禁止 WNS。
6. 插件版本不匹配仍可能泄露精确参数。已保留能力候选但清空 start points/control table，并输出 warning。
7. P0 卡同时含多个职责时，preferred capability 可能误匹配。已支持 diagnosis-specific capability mapping。
8. 系统 Python 缺少 PyYAML 且默认 GBK 读取中文失败。验证依赖安装在任务级目录，并用 UTF-8 模式运行；未修改系统 Python。
9. Master-only 曾可误用人声卡，低方向会继续削减/压缩。已加入严格 mode/scope、方向专用诊断与 11 张恢复/总线安全卡，并增加反例测试。
10. 单参考曾用固定分母产生伪稳健偏差，且门控后只有等响动作。现单参考只保留原始差值、严重度上限与条件处方，Outlier 明示证据不足，并始终抑制精确 P1 旋钮；重复、低兼容等门控失败仍只保留参考修正。
11. Mono fold loss 曾把“损失更小”映射成风险。现仅在 Target 数值更低/更负且超过初始差值阈值时生成 `mono_translation_risk`，并加入正反例测试。
12. Markdown 曾丢失用户证据、假设、校准状态和 provenance。现已完整呈现 P0/P1 证据、风险、拒绝原因、逐旋钮表与复测。
13. 完整 Mix 曾以 24 kHz 分析且静默截断多声道。现改为 48 kHz/20 kHz 上限，并拒绝重复、静音、过短和 >2 声道输入。
14. P1 能力匹配曾把整张插件卡的人声起点泄漏给 Master。现只有 diagnosis recipe 精确命中才开放控件；Master 保留 P0 总线安全起点与能力级插件候选。
15. 参考模式 canonical 输入曾可省略 gate，单个 Stem 参考也可形成关系结论。现非 manual 强制 gate，分离参考限制置信度，关系判断至少需要两个 Stem 参考。
16. 仅版本号曾可解锁控件，空 Inventory 也被当作未提供。现精确控件要求版本+Host+格式+采样率全部确认或显式快照；空 Inventory 明确拒绝。
17. Top-K 曾可能保留失真、暂缓低优先去齿。现 `deessing → harmonic-tone` 与 `reference-gate → clip-limit` 是硬前置，预算不足时暂缓下游。
18. 7 个 L2 supplemental 曾未进入 Schema/hash 审计。现使用独立 L2 Schema、Profile/证据哈希验证，并排除 manifest 被误读为 Profile。

## 仍保留的高风险项

- 自动诊断阈值未完成大型标定，所有自动触发保留 `calibration_required`。
- legacy 分析器缺少真实音频回归 fixture；当前只做 AST 和新处方端到端测试。
- 完整 Mix 的 Stem 对齐、Stem Sum/Master 一致性与真实音频 golden fixture 尚待完成。
- P1 L3 的 Ableton/48 kHz 证据不能外推为 Studio One 或所有模式行为。
- 参考兼容度与所有自动阈值仍是工程代理，不是工业常模。
