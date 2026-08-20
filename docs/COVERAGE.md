# 当前覆盖与缺口

## 已落地

| 层 | 当前制品 |
|---|---:|
| 分析入口 | 干声/人声、完整 Mix/Master 2 种 |
| 路由 Skill | 1 |
| 处方 Skill | 1 |
| P0 决策卡 | 28 |
| P0 打包来源 | 19（缺失 0） |
| P1 正式 Profile | 40 L3 + 7 L2/deferred |
| P1 能力/诊断索引键 | 208（继承源快照） |
| P1 小型证据文件 | 164 + 14 份 L2 卡/来源 |
| 自动化测试 | 47（当前） |

P0 首批覆盖：参考等响、低频/低中频三分法、固定/移动共振、齿音、宏观电平、峰值动态、过压缩恢复、Presence/Air、并行颗粒、宽度与 Mono 安全、空间、Delay、噪声修复、修音、Beat 遮蔽、Vocal/Instrument 宽度关系、Master 低频/存在感高低方向、Master 高低 PLR、Clipper/Limiter、呼吸/爆破。

P1 覆盖：校音、逐音编辑、呼吸/点击/噪声、EQ/动态 EQ/去齿/共振、多种压缩/骑乘/门限/多段/限制/包络、饱和/磁带/激励、移调/宽化/M-S、混响、延迟、参考 A/B 与计量。

## 尚未完成

### P0 标定

- `practical_floor` 和 robust deviation 只是分析器工程阈值，不是大规模听感诊断阈值。
- 缺少带标签真实人声/混音语料、盲听记录和 ground truth。
- 修音、节奏、可懂度、爆破、口水音、噪声和房间声仍需事件检测器及标定。
- 说唱子风格、年代、段落职责的参考正常区间仍不足。

### 完整混音

- 现有知识明显偏现代说唱人声；Beat 内部鼓组、808/Bass、采样、合成器、吉他、键盘的职责卡不均衡。
- Mix 模式已拒绝重复 Mix 路径与未声明的多声道截断，并提升为 48 kHz/20 kHz 上限；Stem 对齐、Stem Sum 与 Master 一致性仍需门禁与真实音频回归。

### P1

- 40 款是 L3 固定夹具，不是所有模式、采样率、Mono/VST2、自动化和 Studio One 行为全覆盖。
- L4 为 0；需要用户真实工程的多轮渲染、复测与反馈。
- SoundToys Decapitator/MicroShift/LittleAlterBoy 只有 L2 卡；已作为低优先级 supplemental Profile，可在用户明确指定时使用，但必须显示未达 L3 警告。
- StandardCLIP 当前磁盘缺失，仅保留官方手册支持的通用 Clipper 方法，不推荐为已安装插件。
- RX Breath Control/De-plosive/Mouth De-click 的本机 VST3 曾出现依赖错误，不能作为正式候选。

### 工程化

- 尚未把 legacy 音频脚本抽成共享 Python 包。
- 尚无真实音频 golden fixture、CI、依赖锁和跨平台测试。
- 尚未直连 DAW/VST 参数 ID；当前输出是人工可执行处方。
