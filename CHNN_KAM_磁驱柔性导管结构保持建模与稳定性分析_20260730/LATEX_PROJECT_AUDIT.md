# LaTeX 工程与回写资产审计

审计日期：2026-07-30  
科学结论截止点：P2-B0-R2  
正文工作对象：本目录（由 `CHNN_KAM_Word基线完整迁移版_v2_清理核验版` 原样复制后建立的独立回写副本）

## 1. 范围与只读边界

- 原 LaTeX 工程、`../paper_evidence` 与 `../bridge_conservative` 均作为只读输入。
- 不查找、合并或修改其他旧 LaTeX、DOCX、PDF 稿件。
- 不运行实验、训练、COMSOL 求解或 KAM；只允许读取证据库登记的正式小型报告、CSV、JSON、manifest 和机器 gate。
- `bridge_conservative/outputs/p2_a1_amplitude_sentinel_scan_20260729/` 未同时出现正式最终报告、final status、manifest、完成标记和稳定交付包，故保持 `RES-A1-001 = running_not_yet_accepted`。
- 当前论文可写的最高资格结论严格限定为 `canonical_contract_qualified_for_A1_sentinel`。

## 2. 顶层结构与职责

| 路径 | 职责 |
|---|---|
| `main.tex` | 公共主入口；加载类、项目配置、前置页、正文、可选附录和参考文献 |
| `main-zh.tex` | 中文入口；设置 `ProjectLanguage=zh` 后加载 `main.tex` |
| `main-en.tex` | 英文入口；设置 `ProjectLanguage=en` 后加载 `main.tex` |
| `config/` | 类配置、项目开关、宏包、定理与前置页配置 |
| `frontmatter/zh/`、`frontmatter/en/` | 中英文标题元数据、摘要和关键词 |
| `manuscript/zh/`、`manuscript/en/` | 中英文正文分发器与章节文件 |
| `backmatter/` | 附录分发与参考文献 |
| `bibliography/` | BibTeX 数据库与引用顺序 |
| `figures/` | 图件与图数据；基线仅有说明文件 |
| `tables/` | 可复用表格；基线仅有说明文件 |
| `tools/` | 语义审计、双语一致性、书目检查与构建脚本 |
| `release/` | 构建后的中英文 PDF |
| `docs/`、`translation/`、`code/` | 迁移说明、翻译辅助和代码清单 |

原工程不是 Git 仓库，因此本轮采用独立副本而不是新 Git 分支。复制前后文件数均为 91，未覆盖既有目录。

## 3. 主入口、正文分发与章节文件

`main.tex` 的主要加载顺序为：

1. `config/classes/\ProjectClassProfile`
2. `config/project`
3. `config/preamble`
4. `frontmatter/\ProjectLanguage/metadata`
5. `config/frontmatter/\ProjectClassProfile`
6. `frontmatter/title-block`
7. `bibliography/order`
8. `manuscript/\ProjectLanguage/body`
9. 可选 `backmatter/appendices`
10. `backmatter/references`

中英文正文均由八个同构章节组成：

| 序号 | 中文文件 | 英文文件 | 主题 |
|---|---|---|---|
| 00 | `manuscript/zh/sections/00-introduction.tex` | `manuscript/en/sections/00-introduction.tex` | 引言与贡献 |
| 01 | `.../01-rod-model.tex` | `.../01-rod-model.tex` | 连续 Cosserat/Kirchhoff 杆模型 |
| 02 | `.../02-galerkin-discretization.tex` | `.../02-galerkin-discretization.tex` | 平移—转动联合 Galerkin 离散与 COMSOL bridge |
| 03 | `.../03-hamiltonian-structure.tex` | `.../03-hamiltonian-structure.tex` | Hamiltonian、构形/切/余切空间与 canonical contract |
| 04 | `.../04-chnn-model.tex` | `.../04-chnn-model.tex` | CHNN/HNN、数据与训练接口 |
| 05 | `.../05-symplectic-kam.tex` | `.../05-symplectic-kam.tex` | 辛/Birkhoff/KAM 方法和待验证对象 |
| 06 | `.../06-numerical-results.tex` | `.../06-numerical-results.tex` | 已冻结结果和待回填结果 |
| 07 | `.../07-discussion.tex` | `.../07-discussion.tex` | 讨论、边界和适用范围 |
| 08 | `.../08-conclusion.tex` | `.../08-conclusion.tex` | 截止 P2-B0-R2 的结论 |

## 4. BibTeX、图表和宏包资产

- BibTeX：`bibliography/references.bib`，37 个条目。
- 基线 SHA-256：`F17F7A12F07EB3B89DF4F2834CE10086B0A7A61BCAD1C3315E77205EB472C60D`。
- 已加载 `graphicx`、`booktabs`、`array`、`multirow`、`tabularx` 和 `longtable`，足以承载本轮新增图表，无需引入新宏包。
- 基线 `figures/` 与 `tables/` 无正式稿图表；本轮图表必须由登记的机器结果生成，并在交付清单中登记源路径和 SHA-256。
- 基线附录文件为空且 `ProjectIncludeAppendices=false`；本轮将启用附录，用于放置 A0–B0-R2 诊断链、证据路径和复现边界，不删除正文研究范围。

## 5. 编译方式与基线产物

工程声明的标准流程为：

```bash
python tools/audit_semantics.py --language zh
python tools/audit_semantics.py --language en
python tools/audit_bilingual.py
python tools/check_bibliography.py
python tools/build.py --language both --clean
```

构建脚本使用 `latexmk` 驱动 XeLaTeX，并生成：

- `release/CHNN_KAM_Manuscript_ZH.pdf`
- `release/CHNN_KAM_Manuscript_EN.pdf`

基线 PDF 分别为 51 页和 61 页。最终交付前需执行三轮验证：语义/双语/书目审计，完整编译与日志审计，PDF 渲染抽查与结论边界复核。

## 6. 已识别的正文缺口

- 中文摘要基线仅含单字占位，英文摘要亦为占位；需重写为“已冻结结果 + 明确待回填范围”的摘要。
- 第 6 节尚无正式数字表、Bridge 图、R2 收敛图和结果证据绑定。
- 第 3 节虽有正则动量理论，但缺少 COMSOL 输出到冻结 \(N=2\) reduced canonical labels 的明确机器数据合同。
- 第 5 节需要明确 BDF 只承担 solver-step 状态采样和向量场标签生成，不构成辛性证明。
- 第 6.4–6.6 节和 KAM/高保真/开放端口部分必须保留为待回填槽位，不能因本轮无结果而删除。
- 附录需补入 A0–A0.8、B0、B0-R1、B0-R2 的审计链与 supersession 边界。

## 7. 证据库核验结论

九项核心证据文件均已读取：文件清单、结果登记表、claim–evidence 矩阵、替代关系、待回填表、图表计划、回写映射、复现索引和冲突/不确定性清单。正式小型证据补读确认：

- `RES-P1-001`、`RES-P15-001`、`RES-P16-001` 已完成；
- A0–A0.8 是 canonical 数据合同的诊断链；
- B0 与 B0-R1 是应保留历史状态的中间资格结果；
- `RES-B0-R2-001` 的最终状态为 `canonical_contract_qualified_for_A1_sentinel`；
- P2-A1 尚未形成可接受论文结果；
- 正式 96 轨迹、正式 P2 训练和数值 KAM 均未完成。

## 8. 结论红线

本轮不得写成：正式 P2 已完成、BDF 已证明辛、已取得 KAM 资格、正式 P2 已证明 CHNN 优于 Real HNN、已获得不变环面或安全域。不同 Bridge 能量门和 force gate 必须分开呈现；seed 只能解释为算法重复，不能当作独立物理样本。
