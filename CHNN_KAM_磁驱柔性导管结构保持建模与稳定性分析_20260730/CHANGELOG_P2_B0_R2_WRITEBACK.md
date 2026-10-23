# P2-B0-R2 论文回写逐文件 Changelog

日期：2026-07-30  
当前论文工程：`CHNN_KAM_磁驱柔性导管结构保持建模与稳定性分析_20260730`  
基线目录：`CHNN_KAM_Word基线完整迁移版_v2_清理核验版`（未修改）

> **Historical / superseded record.** 本 changelog 记录 A-01 canonical 合同修订前的 P2-B0-R2 回写状态；其中出现的旧符号（包括 `B^T P_full`、`B^T L`）仅作为历史变更证据，不是当前实现合同。当前文本合同以 `translation/terminology.md` 和本分支最新双语正文为准。

## 1. 项目入口与构建

| 文件 | 变更 |
|---|---|
| `config/project.tex` | 启用双语附录；未改变文档类、语言或研究范围开关。 |
| `backmatter/appendices.tex` | 按 `ProjectLanguage` 分发中英文证据附录。 |
| `tools/build.py` | 保留原审计流程；当 `latexmk` 或 Perl 不可用时，加入 `XeLaTeX → BibTeX → XeLaTeX` 至交叉引用稳定的回退构建链，并把重跑提示纳入严格检查。 |
| `release/CHNN_KAM_Manuscript_ZH.pdf` | 中文论文 PDF。 |
| `release/CHNN_KAM_Manuscript_EN.pdf` | 英文论文 PDF。 |

## 2. 摘要

| 文件 | 变更 |
|---|---|
| `frontmatter/zh/abstract.tex` | 回写 Bridge/force 门分离、P0/P1/P1.5/P1.6、A0–B0-R2 资格链、R2 正式数值与 A1/P2/KAM 边界。 |
| `frontmatter/zh/abstract-en.tex` | 同步英文摘要，使用相同 result ID、数值和结论边界。 |
| `frontmatter/en/abstract.tex` | 英文工程摘要与中文权威版本语义对齐。 |

## 3. 中文正文

| 文件 | 变更 |
|---|---|
| `manuscript/zh/sections/00-introduction.tex` | 增加证据冻结点、已完成/诊断/待回填三层范围声明。 |
| `manuscript/zh/sections/02-galerkin-discretization.tex` | 增加 frozen \(N=2\) qualification basis、COMSOL–Galerkin bridge、严格 0.5%/候选 1% 能量门与独立 force-v2 2% 门。 |
| `manuscript/zh/sections/03-hamiltonian-structure.tex` | 明确构形空间、切空间、余切空间及 `q=Pi_conf(U)`、`p=B^T P_full`、`dq=M_N^{-1}p`、`dp=B^T L` canonical contract；限定 BDF 用途。 |
| `manuscript/zh/sections/04-chnn-model.tex` | 加入 P1 系列的 whole-trajectory folds、三条物理轨迹和五个算法 seed 边界；保留正式 P2 方案。 |
| `manuscript/zh/sections/05-symplectic-kam.tex` | 声明 BDF 只用于采样/标签，B0-R2 不证明辛性或 KAM；保留完整 KAM 回填接口。 |
| `manuscript/zh/sections/06-numerical-results.tex` | 回写 P0、Smoke、Bridge/force、P1/P1.5/P1.6、A0–A0.8、B0/R1/R2；插入五类表和两张图；保留 A1、正式 P2、KAM、高保真和开放端口槽位。 |
| `manuscript/zh/sections/07-discussion.tex` | 增加方法学负结果、资格替代、样本与外推边界讨论。 |
| `manuscript/zh/sections/08-conclusion.tex` | 将结论冻结在 `canonical_contract_qualified_for_A1_sentinel`，明确所有未完成结果。 |

`manuscript/zh/sections/01-rod-model.tex` 未修改。

## 4. 英文正文

| 文件 | 变更 |
|---|---|
| `manuscript/en/sections/00-introduction.tex` | 与中文引言的证据范围和冻结点对齐。 |
| `manuscript/en/sections/02-galerkin-discretization.tex` | 与中文的 frozen basis 和 Bridge/force 门分离对齐。 |
| `manuscript/en/sections/03-hamiltonian-structure.tex` | 与中文的构形/切/余切空间和 canonical contract 对齐。 |
| `manuscript/en/sections/04-chnn-model.tex` | 与中文的 P1 数据划分和 seed 边界对齐。 |
| `manuscript/en/sections/05-symplectic-kam.tex` | 与中文的 BDF/KAM 结论边界对齐。 |
| `manuscript/en/sections/06-numerical-results.tex` | 回写与中文同源的结果、表、图和未完成槽位；对长状态字符串使用可断行排版。 |
| `manuscript/en/sections/07-discussion.tex` | 与中文方法学和外推边界对齐。 |
| `manuscript/en/sections/08-conclusion.tex` | 与中文截止状态和未完成槽位对齐。 |

`manuscript/en/sections/01-rod-model.tex` 未修改。

## 5. 附录

| 文件 | 变更 |
|---|---|
| `backmatter/appendices-zh.tex` | 新增 A0–B0-R2 supersession 诊断链、正式证据路径/SHA-256、force 修订链、A1 增量更新协议。 |
| `backmatter/appendices-en.tex` | 新增英文镜像附录；科学状态、路径和哈希与中文一致。 |

## 6. 表格

| 文件 | 变更 |
|---|---|
| `tables/tab_bridge_gate_summary_zh.tex` | 新增中文 Bridge/force 三门逐轨迹表。 |
| `tables/tab_bridge_gate_summary_en.tex` | 新增英文镜像。 |
| `tables/tab_p0_summary_zh.tex` | 新增中文 P0 quadratic-physics machine summary。 |
| `tables/tab_p0_summary_en.tex` | 新增英文镜像。 |
| `tables/tab_p1_series_summary_zh.tex` | 新增中文 P1/P1.5/P1.6 结果与解释边界表。 |
| `tables/tab_p1_series_summary_en.tex` | 新增英文镜像。 |
| `tables/tab_r2_qualification_zh.tex` | 新增中文 B0-R2 三层观察阶与 1 s sentinel 表。 |
| `tables/tab_r2_qualification_en.tex` | 新增英文镜像。 |
| `tables/tab_canonical_diagnostic_chain_zh.tex` | 新增中文 A0–B0-R2 诊断/资格链表。 |
| `tables/tab_canonical_diagnostic_chain_en.tex` | 新增英文镜像。 |

## 7. 图、图源与生成脚本

| 文件 | 变更 |
|---|---|
| `figures/data/bridge_gate_separation.csv` | 新增 Bridge 严格/候选能量门和 force-v2 的冻结轻量图源。 |
| `figures/data/b0_r2_convergence_orders.csv` | 新增 B0-R2 五个观察收敛阶的冻结轻量图源。 |
| `tools/generate_writeback_figures.py` | 新增确定性图件生成脚本；只读取上述两项轻量 CSV。 |
| `figures/fig_bridge_gate_separation.pdf` | 新增正文用矢量图。 |
| `figures/fig_bridge_gate_separation.png` | 新增审阅用 PNG。 |
| `figures/fig_b0_r2_convergence_orders.pdf` | 新增正文用矢量图。 |
| `figures/fig_b0_r2_convergence_orders.png` | 新增审阅用 PNG。 |

## 8. 审计与交付索引

| 文件 | 变更 |
|---|---|
| `LATEX_PROJECT_AUDIT.md` | 修改前生成的工程结构、入口、章节、BibTeX、图表和构建审计。 |
| `WRITEBACK_EXECUTION_PLAN.md` | 修改前生成的文件级执行计划、图表计划、边界和回填槽位。 |
| `RESULT_ID_TO_TEX_MAP.csv` | 23 个 result ID 的证据路径、目标 `.tex`、章节、动作、允许/禁止结论与执行状态。 |
| `FIGURE_TABLE_PROVENANCE.csv` | 图、图源、表、脚本、正式源路径和 SHA-256 的来源链。 |
| `UNFILLED_BACKFILL_SLOTS.md` | A1、正式 96 轨迹、正式 P2、数值 KAM、开放端口/高保真待回填清单。 |
| `FINAL_BUILD_AND_BOUNDARY_AUDIT.md` | 双语构建、引用/标签/公式、PDF 目视和结论边界的最终验收记录。 |
| `CHANGELOG_P2_B0_R2_WRITEBACK.md` | 本逐文件变更记录。 |

`build/` 中的 AUX、BBL、日志和 `pdf_visual_audit/` PNG 是可重建审计产物，不是新的科学证据。
