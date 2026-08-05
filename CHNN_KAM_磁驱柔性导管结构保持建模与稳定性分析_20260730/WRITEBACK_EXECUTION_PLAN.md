# 截至 P2-B0-R2 的论文回写执行计划

状态：前置审计完成，正文尚未修改。  
证据冻结点：`RES-B0-R2-001`。  
回写原则：只写正式证据支持的局部结论，保留论文完整研究范围和所有未完成槽位。

## 1. 文件级执行映射

| 写入对象 | 章节/位置 | 动作 | 证据与结论边界 |
|---|---|---|---|
| `frontmatter/zh/abstract.tex`、`frontmatter/en/abstract.tex`、`frontmatter/zh/abstract-en.tex` | 摘要 | 替换占位；概述理论链、P0/P1 系列、Bridge 与 B0-R2；明确 P2/KAM 未完成 | 数字绑定 `RES-P0-001`、`RES-P1-001`、`RES-P15-001`、`RES-P16-001`、`RES-BRIDGE-001`、`RES-FORCE-V2-001`、`RES-B0-R2-001` |
| `manuscript/*/sections/00-introduction.tex` | 贡献和范围 | 新增证据冻结点及完成/待回填分层，不删除原研究问题 | 不把设计目标写成已完成结果 |
| `manuscript/*/sections/02-galerkin-discretization.tex` | §2.11 | 新增 COMSOL–Galerkin bridge、冻结 \(N=2\) 资格基、严格能量门/候选门/force-v2 分离 | `RES-BRIDGE-001`、`RES-FORCE-V1-001`、`RES-FORCE-V2-001` |
| `manuscript/*/sections/03-hamiltonian-structure.tex` | §3.1–3.3、§3.7 | 新增构形/切/余切空间解释与 canonical contract 四式；区分 projected momentum 与 mass diagnostic | `RES-A06-001`、`RES-A08-001`、`RES-B0-R2-001` |
| `manuscript/*/sections/04-chnn-model.tex` | §4.4–4.6 | 新增历史 pilot 的数据划分边界、whole-trajectory folds 与 seed 解释；保留正式 P2 训练方案 | `RES-P1-001`、`RES-P15-001`、`RES-P16-001` |
| `manuscript/*/sections/05-symplectic-kam.tex` | §5.1–5.2、§5.6–5.7 | 新增 BDF 角色边界与 KAM 待回填声明 | `RES-A08-001`、`RES-B0-R2-001`；不得声称数值 KAM 已完成 |
| `manuscript/*/sections/06-numerical-results.tex` | §6.1–6.3 | 用正式结果替换空占位：P0、Bridge/force、P1/P1.5/P1.6、R2 | 所有数字带 result ID；保留 §6.4–6.6 |
| 同上 | §6.4–6.6 | 保留并细化槽位 | `RES-P2-TRAIN-001`、`RES-KAM-001`、`RES-PORT-HF-001` 仍未完成 |
| `manuscript/*/sections/07-discussion.tex` | §7.1–7.3 | 讨论方法学负结果、资格演进、样本与外推边界 | B0/R1 不覆盖，R2 只资格 A1 sentinel |
| `manuscript/*/sections/08-conclusion.tex` | 结论 | 替换空结果占位；列已完成贡献和未完成研究计划 | 截止语严格为 `canonical_contract_qualified_for_A1_sentinel` |
| `backmatter/appendices.tex` 及双语附录文件 | 附录审计链 | 新增 A0–A0.8、B0/R1/R2、证据路径/哈希与复现边界 | 历史失败按 supersession 显示，不与当前结论混淆 |
| `config/project.tex` | 项目开关 | 启用附录 | 不改变论文类别与其他研究范围 |

## 2. 图表计划与数据来源

| 资产 | 类型 | 数据源 | 写入位置 | 允许表达 |
|---|---|---|---|---|
| `figures/fig_bridge_gate_separation.*` | 双面板图 | `RES-BRIDGE-001` manifest；`RES-FORCE-V2-001` metrics CSV | §6.2 | 严格 0.5% 能量门、候选 1% 门和 force-v2 2% 门分离 |
| `figures/fig_b0_r2_convergence_orders.*` | 收敛阶图 | `RES-B0-R2-001` 正式结果和 canonical gates | §6.3 | 观察阶范围 1.64186–2.00088；仅 canonical contract 时间离散资格 |
| `tables/tab_bridge_gate_summary_*` | 双语表 | Bridge manifest 与 force-v2 CSV | §6.2 | 三轨迹逐项状态，不合并门 |
| `tables/tab_p0_summary_*` | 双语表 | P0 ZIP 内正式 machine summary | §6.3 | 仅低维合成系统基线 |
| `tables/tab_p1_series_summary_*` | 双语表 | P1/P1.5/P1.6 正式报告 | §6.3 | 三条轨迹 pilot；seed 非物理样本 |
| `tables/tab_r2_qualification_*` | 双语表 | R2 report/gates/run state | §6.3 | 1 s G2/G3/G4 与严格截止状态 |
| `tables/tab_canonical_diagnostic_chain_*` | 双语表 | A0–A0.8、B0/R1/R2 正式报告 | 附录 | 方法学诊断与替代关系 |

生成脚本只读取本轮新增的轻量 CSV，不访问实验大文件；源 CSV 保存于 `figures/data/`，脚本和所有生成资产均登记 SHA-256。

## 3. 新增、替换与保留规则

- 新增：evidence scope、COMSOL–Galerkin bridge、冻结 \(N=2\) 资格基、canonical contract、诊断链、已完成 pilot 结果、R2 资格与证据索引。
- 替换：空摘要和第 6.3/结论中的无内容结果占位。
- 保留：连续模型、Galerkin、CHNN、开放端口、辛/Birkhoff、KAM、高保真、参数延拓和安全域的完整方法与研究目标。
- 保留并标记待回填：P2-A1、正式 96 轨迹、正式 P2 训练、数值 KAM、开放端口与高保真。
- 不扩张：P1 系列只在三条固定小轨迹与 whole-trajectory folds 上成立；P0 只证明低维基线；R2 只获得 A1 sentinel 的设计/运行资格。

## 4. 固定公式与术语

正文采用同一冻结合同：

\[
q_N=\Pi_{\mathrm{conf},N}(U),\qquad
p_N=B_N(q_N)^\mathsf{T}P_{\mathrm{full}},\qquad
\dot q_N=M_N(q_N)^{-1}p_N,\qquad
\dot p_N=B_N(q_N)^\mathsf{T}L.
\]

其中 \(q_N\in\mathcal Q_N\)，\(\dot q_N\in T_{q_N}\mathcal Q_N\)，\(p_N,\dot p_N\) 按 paired-coordinate contract 解释为余切量。`p_mass=M_N*dq_native` 只作诊断；只有全场速度位于冻结切空间且离散/投影一致时才可与 projected momentum 等同。

## 5. A1、正式 P2 与数值 KAM 回填槽位

- A1：§6.3 的 amplitude sentinel 小节、附录增量审计行、摘要/讨论/结论中的状态句。
- 正式 96 轨迹与正式 P2 训练：§4.4–4.6 的正式数据/训练合同，§6.3–6.4 的主要比较表和图，§7/§8 的外推结论。
- 数值 KAM：§5.6–5.7 的算法输出，§6.5–6.6 的不变环面、后验误差、延拓和安全域图表。
- 开放端口与高保真：§4.3、§6.4、§6.6。

A1 完成后的增量读取仅限：

1. `bridge_conservative/outputs/p2_a1_amplitude_sentinel_scan_20260729/` 内新增的正式最终报告、final status、机器 gates、manifest、verification 与完成标记；
2. `bridge_conservative/deliverables/P2_A1*` 及项目顶层/交付目录中的稳定 ZIP、receipt 和 checksum；
3. 随正式 A1 交付更新的 `PROJECT_STATE.md`、`EXPERIMENT_HISTORY.md`、`ASSUMPTION_REGISTRY.md`、`NEXT_STAGE.md`；
4. manifest 明确绑定的轻量 CSV/JSON/NPZ；不读取临时 CSV、中间日志或在写大型 MPH/ZIP。

需要增量更新：结果登记表、claim–evidence 矩阵、替代关系图、待回填表、图表计划、回写映射、复现索引、冲突清单、`RESULT_ID_TO_TEX_MAP.csv` 及正文 A1 槽位。

## 6. 验证与交付

1. 第一轮：运行中英文语义审计、双语审计与 BibTeX 检查；修复硬错误。
2. 第二轮：完整构建中英文 PDF；审计 undefined citation/reference、duplicate label、overfull/underfull、数学公式和编码。
3. 第三轮：渲染 PDF 关键页并目视检查摘要、图表、公式、附录和待回填框；执行禁止结论全文检索。
4. 交付逐文件 changelog、最终结果映射、图表数据/哈希清单、未回填槽位清单和构建审计报告。
