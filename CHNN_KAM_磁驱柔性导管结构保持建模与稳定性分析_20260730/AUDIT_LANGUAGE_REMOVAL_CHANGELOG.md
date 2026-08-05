# 去审计语言专项逐文件 Changelog

本轮共修改 35 个既有 LaTeX 文件，并新增 4 个内部 Markdown 报告。未修改实验工程、证据库、图表数据或图形文件。

| 文件 | 修改内容 |
|---|---|
| `frontmatter/zh/abstract.tex` | 删除状态码、result ID 和资格/冻结语言；以学术语言保留 Bridge、P0/P1 系列、canonical 收敛数值和研究边界。 |
| `frontmatter/zh/abstract-en.tex` | 同步改写中文稿内英文摘要。 |
| `frontmatter/en/abstract.tex` | 同步改写英文稿摘要。 |
| `manuscript/zh/sections/00-introduction.tex` | 将证据截止点和回填表述改为当前数值范围与后续研究范围。 |
| `manuscript/en/sections/00-introduction.tex` | 同步英文引言范围表述。 |
| `manuscript/zh/sections/02-galerkin-discretization.tex` | 将“冻结资格基、机器检查、证据路径”改为固定 \(N=2\) 映射基及学术数值说明。 |
| `manuscript/en/sections/02-galerkin-discretization.tex` | 同步英文；将 `verification` 改为科学性的 term-by-term check。 |
| `manuscript/zh/sections/03-hamiltonian-structure.tex` | 删除阶段码、审计与证据索引语言；保留 canonical 方程、余切动量和 BDF 适用边界。 |
| `manuscript/en/sections/03-hamiltonian-structure.tex` | 同步英文并将工程 verification 改为 convergence analysis。 |
| `manuscript/zh/sections/04-chnn-model.tex` | 将阶段登记和回填语言改为小样本结果及未来完整 P2 研究方案。 |
| `manuscript/en/sections/04-chnn-model.tex` | 同步英文，章节名改为 Structural Validation，并移除 qualification 措辞。 |
| `manuscript/zh/sections/05-symplectic-kam.tex` | 删除资格/回填措辞；保留 BDF 非辛边界、KAM 条件和后续实例化要求。 |
| `manuscript/en/sections/05-symplectic-kam.tex` | 同步英文 KAM 边界。 |
| `manuscript/zh/sections/06-numerical-results.tex` | 按学术实验结构重写全章；移除阶段标题、状态码、result ID、路径、哈希、manifest、机器记录和可见占位框。 |
| `manuscript/en/sections/06-numerical-results.tex` | 同步英文数值实验章。 |
| `manuscript/zh/sections/07-discussion.tex` | 将历史资格链改写为误差来源和可复用诊断方法；保留全部适用边界和扩展方向。 |
| `manuscript/en/sections/07-discussion.tex` | 同步英文讨论。 |
| `manuscript/zh/sections/08-conclusion.tex` | 删除冻结点、唯一状态和未完成结果框；以论文语言总结数值结果和限制。 |
| `manuscript/en/sections/08-conclusion.tex` | 同步英文结论。 |
| `backmatter/appendices.tex` | 将内部注释改为 scientific appendices。 |
| `backmatter/appendices-zh.tex` | 删除路径、哈希、文件清单和增量操作协议；重写为诊断方法、方程、指标、阈值与数值设置。 |
| `backmatter/appendices-en.tex` | 同步英文附录，并修正附录标题与浮动表顺序。 |
| `tables/tab_bridge_gate_summary_zh.tex` | 删除 result ID 和内部门控术语；保留轨迹、能量、force-v2、阈值及判定。 |
| `tables/tab_bridge_gate_summary_en.tex` | 同步英文表。 |
| `tables/tab_p0_summary_zh.tex` | 删除 machine summary、登记和 result ID；保留四模型数值。 |
| `tables/tab_p0_summary_en.tex` | 同步英文表。 |
| `tables/tab_p1_series_summary_zh.tex` | 删除 result ID、“正式结果”等字段；改为实验、数值结果和适用范围。 |
| `tables/tab_p1_series_summary_en.tex` | 同步英文表。 |
| `tables/tab_r2_qualification_zh.tex` | 表题改为 canonical 三层收敛与 \(1\,\mathrm{s}\) 验证；删除阶段码和数据 ID。 |
| `tables/tab_r2_qualification_en.tex` | 同步英文表。 |
| `tables/tab_canonical_diagnostic_chain_zh.tex` | 将阶段/result ID/论文用途表改为诊断步骤、观察分析和科学解释。 |
| `tables/tab_canonical_diagnostic_chain_en.tex` | 同步英文诊断表。 |
| `config/theorems/zh.tex` | 删除可见 `resultplaceholder` 环境。 |
| `config/theorems/en.tex` | 删除英文可见 `resultplaceholder` 环境。 |
| `config/macros.tex` | 将 TODO、核查和问题宏设为无条件不渲染，避免 draft 模式泄漏到 PDF。 |

## 新增内部交付文件

| 文件 | 用途 |
|---|---|
| `AUDIT_LANGUAGE_REMOVAL_REPORT.md` | 总体清理、科学保留和 PDF 验收报告。 |
| `AUDIT_LANGUAGE_REMOVAL_CHANGELOG.md` | 本逐文件 changelog。 |
| `AUDIT_LANGUAGE_REMOVAL_COMPARISON.md` | 删除、改写与保留项目对照。 |
| `AUDIT_LANGUAGE_REMOVAL_BUILD_AUDIT.md` | 编译、引用、标签、公式、关键词及结论边界审计。 |

