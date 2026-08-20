# 补充调研来源

本文件只列本次为 P0 工程缺口补充的权威来源；40 款插件的逐款来源位于 P1 Profile 的 `evidence.packaged`。

- ITU-R BS.1770-5：节目响度与 True Peak 测量算法。<https://www.itu.int/rec/R-REC-BS.1770-5-202311-I/en>
- EBU R 128 v5.0：广播响度归一化与最大允许电平。<https://tech.ebu.ch/publications/r128>
- EBU Tech 3343：R128 实施与监听实践。<https://tech.ebu.ch/publications/tech3343>
- EBU R128 S2：Streaming 响度指导。<https://tech.ebu.ch/publications/r128s2>
- SIR Audio Tools StandardCLIP Manual：削波、Soft Clip、Oversampling、最小/线性相位边界。<https://www.siraudiotools.com/StandardCLIP_manual.php>
- FabFilter Pro-L 2 True Peak：True Peak Limiting、Metering、Lookahead 与 ISP。<https://www.fabfilter.com/help/pro-l/using/truepeaklimiting>
- FabFilter Pro-L 2 Oversampling：混叠、CPU 与轻微 pre-ring 的权衡。<https://www.fabfilter.com/help/pro-l/using/oversampling>

注意：广播 R128 的 `-23 LUFS / -1 dBTP` 是特定交付标准，不是商业说唱母带的统一创作目标；平台规范可能变化，实际交付前必须重新核对目标平台。

