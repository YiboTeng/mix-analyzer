# Mix Analyzer 架构

## 目标

把“分析发现不足”变成一条可验证的数据管线，而不是在报告末尾追加固定插件链：

```text
音频/项目清单
  → 双模式参考分析
  → 统一诊断证据
  → P0 通用处理决策
  → P1 本机插件与版本映射
  → 链序/冲突/延迟求解
  → JSON + Markdown 处方
  → 等响 A/B 与重新测量
```

## 模块边界

### 分析器

- `compare-vocal-references`：干声、处理后独唱、Vocal Stem、分离参考。
- `compare-mix-references`：完整 Mix/Master；有可靠 Stems 才启用人声/伴奏、鼓、Bass、Lead/Pad 关系诊断。
- 输出仍保持 legacy schema，`mix_analyzer.normalize` 负责兼容。首版只对完整 Mix 的输入门禁与分析带宽做安全修正：拒绝重复/静音/过短/未声明多声道截断，并以 48 kHz 分析到 20 kHz。

### P0 决策层

- 输入：带 `severity/confidence/scope/evidence` 的 canonical finding。
- 知识：`skills/prescribe-mix-actions/knowledge/p0/decision-cards.json`。
- 输出：抽象路由、操作步骤、参数搜索范围、判别测试、失败/停止条件和复测指标。
- P0 不绑定品牌；它可以在没有 P1 候选时仍返回 Clip Gain、Automation、Dynamic EQ、Parallel Aux 等通用方法。

### P1 插件层

- 40 个正式 L3 Profile 源自 Aizen P1 v1 Adapter 和知识卡。
- Profile 同时保留 Adapter 原始字段与从 Markdown 卡提取的 `parameter_start_points`、控制语义、监听目标和延迟文本。
- 未确认当前版本或版本不匹配时保留能力级候选，但删除精确起点与控件表；使用打包快照必须显式选择并保留警告。
- 运行时可用性、版本、宿主、格式、采样率、模式化 Host 延迟和显式拒绝规则先于候选排序；音乐性 Delay 时间不当作 PDC。

### 处方层

- 链序按职责依赖排序，不按插件品牌排序。
- 同一职责/Scope 合并多条证据；互斥方向先求解，再按价值取 Top-K，最后按链序展示。
- 齿音→饱和、参考等响→削波限制、主体中心→宽度返回等冲突产生显式警告。
- 默认只交付 3–6 个最高价值动作；其余进入 deferred，不一次堆满整条链。

## 为什么保留旧分析脚本

首版以“行为兼容 + 新契约”为目标。直接重写音频算法会同时改变测量、阈值和处方，无法区分回归来源。当前先把旧脚本作为 legacy baseline，新增 AST、Schema、决策与端到端测试；后续再把共享音频 I/O、分帧、绘图、可信度和日志逐步抽到 `src/mix_analyzer/analyzers`。

## 可部署数据

P1 验证工程约 1.386 GB，插件只打包：

- Adapter/Profile JSON；
- capability/version/routing/availability 索引；
- 40 张知识卡、40 份来源笔记、40 份验证摘要和小型结果 JSON；
- SHA-256 与源审计状态。

不打包 WAV、ALS、渲染和用户 DAW 工程。

## 安全边界

- 引擎只生成计划，不直接控制 DAW、不覆盖音频、不自动渲染。
- 自动指标阈值未完成语料标定时必须 `calibration_required=true`。
- Master-only 不反推具体 Stem、Preset 或单轨参数；只允许总线安全的宽带判别和小幅起点。
- Source Separation 结果限制诊断置信度。
- L3 不升级为真实工程 L4。
