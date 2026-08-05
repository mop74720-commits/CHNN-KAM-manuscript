# 第一次审查修改执行报告

## 1. 基线与分支

- 基线提交：295df72
- 修改分支：fix/first-review
- 原始审查结论：review/first-review.md 未修改。
- 问题矩阵：review/issue-matrix.md 未标记 VERIFIED；本报告状态仅表示本轮修改执行程度。

## 2. 问题处理表

| 编号 | 修改前的问题 | 修改文件与位置 | 实际修改内容 | 证据与验证方法 | 状态 | 剩余风险 |
|---|---|---|---|---|---|---|
| A-01 | 构形相关 \(B_N(q_N)\) 的动量率遗漏输运项 | 双语摘要；双语第 03 章 canonical data contract | 改为 \(\dot p_N=\dot B_N^TP_{\rm full}+B_N^T\dot P_{\rm full}\)，说明 \(L_{\rm full}:=\dot P_{\rm full}\) 的条件简写及既有 force-v2/G3 必须重算 | 链式法则；双语公式审计和 XeLaTeX 编译 | PARTIAL | 缺 \(U,B_N,E,P_{\rm full}\)、输运项源码与原始数组，无法重算标签和门 |
| A-02 | P0/P1/P1.5/P1.6、Bridge、R2 正式源码和原始输出缺失 | 双语第 06 章；code/README.md | 明确当前交付物缺原始数组、指标函数、日志和正式实现；不把骨架当正式代码 | 文件树、RESULT_ID_TO_TEX_MAP.csv 路径核查 | BLOCKED | 外部证据路径未交付，clean checkout 无法重建结果 |
| A-03 | provenance 中结果表哈希失配 | tools/build.py | 新增资源存在性和 SHA-256 检查；默认拒绝失配，仅诊断开关可放行 | 默认构建实测拒绝 12 个失配资产 | PARTIAL | 缺原始机器指标和生成日志，不能合法刷新 provenance |
| A-04 | relative L2、rollout、force-v2、G0--G6 等定义不可独立复算 | 双语第 06 章 | 明确指标名称和历史摘录不能替代数组轴、切片、零分母、聚合和阈值来源 | 正文语义审计；交付文件核查 | BLOCKED | 缺原始数组和正式指标实现 |
| A-05 | whole-trajectory 划分缺 val、早停、归一化和 fold manifest | 双语第 06 章 | 保留“完整轨迹划分”含义，同时明确 manifest、早停和归一化日志未交付 | 文件树和日志路径核查 | BLOCKED | 无法证明或排除验证/预处理泄漏 |
| A-06 | 四模型比较缺参数量、预算、硬件和绝对时间 | 本报告 | 不改写历史比较结果，不将相对时间写成公平性证据 | 表格及证据目录核查 | BLOCKED | 缺 model card、逐 seed 配置和运行日志 |
| A-07 | 相邻阶轨迹误差跨维相减 | 双语第 02 章式 (2-115) | 改为 \(q^{(n)}-\Pi_{n+1\to n}q^{(n+1)}\)，补空间、投影维度、同工况/时间网格及零分母处理；统一 N_diag/n_main | 双语公式审计、编译 | PARTIAL | 尚无正式代码/机器输出执行 \(n_{\rm main}\) 收敛选择 |
| A-08 | 数值映射 \(F_h\) 被等同于精确流 \(\Phi_h\) | 双语第 03 章式 (3-94) 及相邻说明 | 分离 \(F_h^{cons}\)、\(\Phi_h^{cons}\) 和 \(\delta_{\rm alg}\)，明确一般数值积分器不等于精确流 | 双语公式审计、编译 | PARTIAL | 具体辛映射、代码接口和算法误差仍待数值实例化 |
| A-09 | 约束局部坐标与固定 pilot 的对应缺证据 | 双语第 03 章 Kirchhoff 约束分支 | 明确秩、约束残差、独立坐标和 pilot 正则性记录未交付，理论构造不等于 pilot 认证 | 文件树核查、双语审计 | PARTIAL | 缺约束 Jacobian、秩和残差数值 |
| A-10 | 条件泛化定理被用于三条相关轨迹的风险 | 双语第 04 章统计学习假设 | 明确 i.i.d.、全维密度下界和统一正则性均未由 pilot 验证，三条固定轨迹不能直接代入定理 | 双语审计、定理上下文核查 | FIXED | 若要获得保证，需独立全维采样或轨迹依赖理论 |
| A-11 | Birkhoff 理论条件、生成函数阶、结构缺陷阶和 KAM 小量未充分分离 | 双语第 03、05 章；`bibliography/references.bib` | 区分 \(r_{\rm alg}\)、\(m_{\rm gen}\)、\(\Delta_K\)、轨迹误差和 KAM 小量；补充定义域、正则性、闭合性、时间相容、非退化、余项范数与条件性结论 | 双语语义/数学骨架审计、BibTeX 审计、双语诊断编译 | FIXED（文本层） | 无不变环面、频率映射、Diophantine 条件和非退化常数的完整数值证书 |
| A-12 | 单一 1 s mode1 哨兵外推为多幅值资格 | 双语摘要、引言、第 06--08 章 | 统一收窄为“后续 A1 资格实验的候选输入”，明确不认证跨 mode、幅值或工况 | 全文固定短语检索、双语审计 | FIXED | A-01 重算前连 A1 资格也未完成 |
| A-13 | build 不验 provenance 和资源，不能区分 PDF 与科学门 | tools/build.py | 增加缺失资源和 provenance fail-closed 门；诊断构建必须显式放行；保留语义、双语和 BibTeX 检查 | 默认门失败、诊断构建成功 | PARTIAL | 仍缺 raw 到 metrics 到图表的正式重算流水线和科学断言 |
| A-14 | \(Q_c\) 定义与方程左端乘子符号不一致 | 双语第 02 章式 (2-95)--(2-96) | 定义统一为 \(Q_c:=-G^T\lambda_c\)，方程左端保留 \(+G^T\lambda_c\) | 双语公式审计、编译 | PARTIAL | 具体约束 residual 和代码符号仍未交付，无法完成实现级验收 |
| A-15 | 接触阻尼/摩擦在耗散和 contact 端口间重复或遗漏 | 双语第 01--04 章 | 定义 \(Q_{\rm diss}^{bulk}/P_{\rm diss}^{bulk}\) 不含接触；未进入势能的接触弹性及接触阻尼、摩擦、冲击只进入 \(Q_{\rm contact}/P_{\rm contact}\)；同步修正能量式、平衡与线性化、Hamiltonian 端口、residual 和数据接口 | 双语公式审计、全文端口检索、编译 | PARTIAL | 正式实现未交付，无法核对代码是否遵循排他合同 |
| A-16 | \(B,J,L,N,n,d\) 等复用，控制输入维度不清 | 双语第 03、04 章；附录、摘要、表格、README、审计文档 | 注册 B_mag、B_port、L_full、N_diag、n_main 和关键维度；标明历史/审查文件中的旧符号不构成当前合同；声明代码接口仍未核验 | 双语公式审计、全仓库语义检索、双语诊断编译 | PARTIAL（文本层完成） | 正式控制器、自适应律、源码对象和维度接口缺失 |
| A-17 | README 和正文对 verification skeleton 与正式实现边界不一致 | 双语第 04、07、08 章；附录；README；KNOWN_ISSUES；`code/README.md`；骨架 JSON | 统一声明 skeleton 仅为接口示例、回归测试骨架、数值流程演示和构建门测试对象；JSON 只描述 skeleton 运行；列出解除边界所需材料 | 骨架执行、双语语义/结构审计、双语诊断编译 | PARTIAL | 正式 CHNN/bridge/force-v2 源码、原始数组、manifest、clean-run 日志、生成物和 provenance 记录仍缺失 |

## 3. 数学公式与实现对应关系

- 全阶到诊断空间：\(q_N=\Pi_{\mathrm{conf},N}(U)\)，\(p_N=B_N(q_N)^TP_{\mathrm{full}}\)。
- 动量率：\(\dot p_N=\dot B_N^TP_{\mathrm{full}}+B_N^T\dot P_{\mathrm{full}}\)。当前没有实现证据，不能验证 force-v2/G3。
- 诊断质量：\(M_N=B_N^TEB_N\in\mathbb R^{N_{\mathrm{diag}}\times N_{\mathrm{diag}}}\)，其中 \(N_{\mathrm{diag}}=2\) 不等于待定生产阶数 \(n_{\mathrm{main}}\)。
- CHNN 状态与端口：\(Z=[Q;P]\in\mathbb R^{2d}\)，物理输入 \(u\in\mathbb R^d\)，全状态嵌入 \(U_{\mathrm{port}}=B_{\mathrm{port}}u\in\mathbb R^{2d}\)；B_port=[0;I] 只作用于动量更新。
- 接触通道：体内/拖曳被动耗散与非势接触端口互斥；未进入势能的接触项只通过 \(Q_{contact}\) 进入，当前只能验证论文合同，不能验证未交付实现。
- 控制与自适应边界：BDF 数据输出间隔 \(\Delta t_{data}\)、未来控制采样周期 \(\Delta t_{ctrl}\) 和 Birkhoff 映射步长 \(h_{Birk}\) 是独立量；当前未提供 regressor、参数律、转置/外积约定、投影约束或实现，故不形成自适应稳定性结论。

## 4. 中英文一致性

- tools/audit_bilingual.py：通过。
- 双语各 174 个章节标签、425 个公式标签、608 个唯一标签、86 个 Cref 调用。
- 关键公式、状态、数字和实验边界已同步；mode1、mode2、mixed12 均保持为轨迹族名称。

## 5. 编译与验证

- 中文 clean build：成功，生成 release/CHNN_KAM_Manuscript_ZH.pdf（57 页，A4）。
- 英文 clean build：成功，生成 release/CHNN_KAM_Manuscript_EN.pdf（69 页，A4）。
- 最终日志：无未解析 citation/reference、无重复 label、无缺失图片/表格、无 Overfull/缺字/致命错误；英文最终日志保留 3 处 Underfull \\hbox（第 02 章 2 处、第 04 章 1 处），属于松散行排版警告。已渲染并抽查中英文修改集中页，未见裁切、重叠或不可读公式。
- BibTeX：37 个条目，37 个活动引用，0 个未使用条目。
- provenance：默认门失败；诊断构建显式放行后成功。当前共 12 个资产哈希失配，其中包含 10 个中英文结果表和 2 个轻量 CSV。
- MiKTeX：宿主报告“unsupported version of Windows”并返回非零状态，但在无 TeX fatal error且 PDF 已生成时构建脚本继续；该宿主警告不被解释为科学验证。

## 6. 本轮未修改内容及原因

- 未修改 review/first-review.md 和 review/issue-matrix.md 的结论或状态。
- 未刷新 FIGURE_TABLE_PROVENANCE.csv：没有原始机器指标和生成日志，刷新哈希会掩盖证据链断裂。
- 未改写历史结果表中的数值：现有数字只能作为历史摘录，A-01 修复后必须从正式原始数组重算。
- 未创建正式 P2、96 轨迹、开放端口或 KAM 实验结果：相关代码、数据和配置未交付。
- 未声称 KAM 证明、工程安全域、模态充分性或完整任务上的 CHNN 优势。

## 7. 独立审查重点

1. canonical pullback 的输运项是否在正式实现中正确离散，并重算 force-v2、G3 和所有训练标签。
2. 12 个 provenance 失配资产能否从原始结果一键重建。
3. P1/P2 的 fold manifest、归一化、早停、参数量、预算和硬件记录。
4. 约束 Jacobian 秩、约束残差与 \(N_{\mathrm{diag}}=2\) pilot 的正则坐标对应。
5. 接触端口和控制输入在正式代码中是否仅进入动量通道且不重复计功。

## 8. 第二轮返工（PR #1 第一次独立复审后）

### 8.1 基线与编号说明

- 返工基线：`fix/first-review@04596a741daa62ceece61d87f46105562901d3fd`。
- PR：#1，保持 Draft；未创建新 PR，未修改或合并 `main`。
- 本节保留第 1--7 节的第一次修改记录，不覆盖历史状态。
- 用户第二轮指令将 provenance release 门列为 A-12、bulk/contact 分账列为 A-13；PR 独立复审正文分别将这两项列为 A-13、A-15。本节按用户给出的五个 FAIL 任务名报告，并在证据栏保留实际对象，避免用编号差异掩盖内容。

### 8.2 五个 FAIL 的返工记录

| 返工项 | 修改文件与位置 | 实际修改内容 | 验证命令与结果 | 当前状态 | 剩余风险 |
|---|---|---|---|---|---|
| A-01 canonical 合同 | `frontmatter/zh/abstract-en.tex`；双语第 01--04、06 章；`backmatter/appendices-{zh,en}.tex`；`tables/tab_canonical_diagnostic_chain_{zh,en}.tex`；`tables/tab_r2_qualification_{zh,en}.tex` | 全部有效输入统一为 `p=B_N(q)^T P_full` 与 `dot p=dot B_N(q)^T P_full+B_N(q)^T dot P_full`；定义空间和维度；删除一般情形下的 `B^T L`；将旧 G3/R2 数值明确标为待原始数组重算的冻结历史记录 | `rg` 全源检索旧 `B^T L`、裸 `N=2` 和旧资格句：0 命中；双语审计通过；诊断编译通过 | PARTIAL | 缺 `B_N,dot B_N,P_full`、force-v2/G3 原始数组和正式实现，不能完成机器重算 |
| A-12 provenance release 门 | `tools/build.py` | `--allow-provenance-mismatch` 与 `--no-check` 均只能用于显式诊断构建；诊断 PDF 仅写 `build/diagnostic/{zh,en}`；正式双语 PDF 在全部检查通过后才原子提升；编译器非零仅允许精确匹配的 MiKTeX 宿主告警；增加 formal source path/hash 检查 | 正式门 `python tools/build.py --language both --clean`：exit 4，release 哈希不变；绕过尝试仅加 allow 开关：exit 2，release 哈希不变；隔离诊断门：exit 0，release 哈希不变 | FIXED | release/diagnostic 隔离和 fail-closed 行为已验证；12 个资产哈希及上游 source 问题仍由 A-03 保持 PARTIAL |
| A-13 bulk/contact 分账 | 双语第 04 章式 (4-25)--(4-27)、(4-32)--(4-34) | 动力学和能量损失统一使用 `Q_diss^bulk+Q_contact+Q_in+Q_flow+Q_partial+r_eta`；`L_pass` 只约束 `Q_diss^bulk`；接触阻尼、摩擦和冲击功率只进入独立 contact 通道一次 | 双语语义审计通过；全文检索确认式 (4-26)/(4-27) 不再使用旧 `Q_diss`；双语诊断编译通过 | PARTIAL | 正式端口实现和逐样本功率数组未交付，无法执行机器单计功断言 |
| A-15 双语合同唯一性 | `frontmatter/{zh,en}/abstract.tex`、`frontmatter/zh/abstract-en.tex`；双语第 01--06 章；双语附录和诊断表 | 磁场统一为 `B_mag`、端口嵌入统一为 `B_port`、载荷率为 `L_full`、诊断阶数为 `N_diag`、正式阶数为待定 `n_main`；删除“前 12 个生产模态”和多幅值资格平行定义 | `audit_semantics.py --language zh/en`、`audit_bilingual.py` 均 exit 0；旧合同语义检索 0 命中；双语 PDF 构建成功 | PARTIAL | 审计工具不证明未交付代码对象一致；`n_main` 仍未由正式收敛实验选择 |
| A-16 失败位置及联动 | 双语第 03 章式 (3-91)/(3-94)；双语第 05 章式 (5-7) 附近；双语第 06 章及表格 | 明确 `F_h^cons:=F_{lambda,h}`，消除 `delta_alg` 的二次对象；写出 Birkhoff 空间闭合和时间相容条件；同步 canonical、bulk/contact 和符号迁移的联动位置 | 双语语义/结构审计与编译通过；无重复 label、未解析引用或 Overfull | PARTIAL | 具体辛映射、Birkhoff 结构、余项范数及实现记录仍未交付 |

### 8.3 独立复审中的 PARTIAL 与 BLOCKED

- PARTIAL 保持：A-03、A-07、A-08、A-11、A-14、A-17。A-08 已统一数值映射对象；A-11 已补写闭合/相容公式；A-17 已修正 README/KNOWN_ISSUES，验证骨架增加断言、有限差分步长扫描并原子生成 JSON。缺正式机器输出或实现的验收条件仍未关闭。
- BLOCKED 保持：A-02、A-04、A-05、A-06、A-09。未交付正式源码、原始数组、指标函数、fold manifest、model card、约束秩/残差和坐标变换记录，未虚构数据解除阻塞。
- A-10 保持独立复审的 VERIFIED 结论，本轮未改动其定理边界。

### 8.4 第二轮构建与门结果

- 正式 provenance 门：exit 4；检测到 12 个资产哈希失配，未刷新；失败前后 `release/CHNN_KAM_Manuscript_{ZH,EN}.pdf` 哈希均不变。
- 非诊断绕过尝试：`--allow-provenance-mismatch` 未配 `--diagnostic` 时 exit 2；release 哈希不变。
- 诊断 provenance 门：`python tools/build.py --language both --clean --diagnostic --allow-provenance-mismatch` exit 0；中文 PDF 57 页，英文 PDF 69 页，均位于 `build/diagnostic`；release 哈希不变。
- 日志检查：无未解析 citation/reference、重复 label、缺失图片/表格、Overfull、缺字或致命错误；BibTeX 无警告；英文保留 3 处 Underfull `\\hbox`。
- 骨架验证：`python code/verification_skeleton.py` exit 0；断言通过，并原子更新 `code/verification_results.json`。有限差分缺陷在过小步长受舍入放大，未作单调下降结论。

## 9. 第三轮返工：A-13 数量一致性门

### 9.1 基线与缺陷

- 复审 head：`faea830574255284d798ae235e49b159814fa5a7`。
- 缺陷位置：`tools/build.py` 中 `formal_source_paths` 与 `formal_source_sha256` 的解析和配对逻辑。
- 原问题：旧逻辑仅在 `index < len(source_hashes)` 时校验 hash；两侧数量不一致时，缺失的 hash 会被静默跳过，无法建立 provenance source 的一一对应关系。

### 9.2 本轮修改

- 修改文件：`tools/build.py`；新增 `tests/test_build_provenance_structure.py`；本报告。
- 在使用或配对 source 列表前，按 manifest 行检查两侧数量；错误信息包含 manifest 路径、行号、asset path、两侧数量以及“cannot establish one-to-one correspondence”原因。
- 数量相等后才使用直接索引访问 `source_hashes[index]`，不使用截断式配对，不忽略多余 path 或 hash。
- 该结构检查位于正式/诊断构建共用的 provenance 前置门中；未修改正式 provenance CSV、未刷新 hash，也不受诊断开关绕过。

### 9.3 回归测试

测试均使用临时 manifest 和临时 build 目录；正式 manifest 与 release 文件不作为写入目标。

| 测试 | 命令 | 退出码 | 结果 |
|---|---|---:|---|
| T1：数量相等 | `python -m unittest tests.test_build_provenance_structure.FormalProvenanceStructureTests.test_t1_equal_lists_reach_existing_provenance_gate` | 0 | 数量门通过，随后由原有 asset hash 门拒绝 |
| T2：paths 多 1 项 | `python -m unittest tests.test_build_provenance_structure.FormalProvenanceStructureTests.test_t2_extra_path_is_rejected` | 0 | 构建返回非零；报告 paths=2、sha256=1 和一一对应失败 |
| T3：hashes 多 1 项 | `python -m unittest tests.test_build_provenance_structure.FormalProvenanceStructureTests.test_t3_extra_hash_is_rejected` | 0 | 构建返回非零；报告 paths=1、sha256=2 和一一对应失败 |
| T4：一侧为空 | `python -m unittest tests.test_build_provenance_structure.FormalProvenanceStructureTests.test_t4_empty_path_list_with_hash_is_rejected` | 0 | 构建返回非零；报告 paths=0、sha256=1 和一一对应失败 |
| T5：诊断模式不绕过 | `python -m unittest tests.test_build_provenance_structure.FormalProvenanceStructureTests.test_t5_diagnostic_mode_cannot_bypass_structure_gate` | 0 | 诊断构建同样返回非零；报告 paths=2、sha256=0 和一一对应失败 |

测试套件命令 `python -m unittest discover -s tests -p 'test_*.py' -v` 共运行 5 项，exit 0。

### 9.4 Release 与 provenance 记录

- 正式 release 修改前 SHA-256：ZH `C3B2B3948FB67F12D91A7437147614E13F396AB68FA2DF67337858B63BC0F162`；EN `7F76C275B1937E74F91593AFD93829B7EB55E5698710D77E149312767B2BB1D5`。
- T1--T5 及正式失败门之后 SHA-256：ZH `C3B2B3948FB67F12D91A7437147614E13F396AB68FA2DF67337858B63BC0F162`；EN `7F76C275B1937E74F91593AFD93829B7EB55E5698710D77E149312767B2BB1D5`。
- 正式构建 `python tools/build.py --language both --clean` exit 4；现有 12 个 provenance 资产失配仍原样保留，未刷新、补齐或生成新的正式 hash。
- 本轮只处理 A-13 数量一致性门，没有声称关闭其他 PARTIAL 或 BLOCKED 项。

## 10. 第四轮返工：A-13 空 provenance entry 与测试可发现性

### 10.1 复审绑定与范围

- 复审 head：`dd88904c7c52d1debef996e37f68cc625ee7a303`。
- 剩余问题：`tests/__init__.py` 缺失使标准 unittest 模块命令不能直接运行；`formal_source_paths` 和 `formal_source_sha256` 的分隔字段使用 `if item.strip()` 静默丢弃空项。
- 本轮修改文件：`tools/build.py`、`tests/__init__.py`、`tests/test_build_provenance_structure.py`、`review/modification-report.md`。
- 未修改正文、release PDF、`FIGURE_TABLE_PROVENANCE.csv`、`review/first-review.md`、`review/issue-matrix.md` 或 `main`。

### 10.2 新增检查逻辑与空字段合同

- 新增 `parse_provenance_entries()`，对非空字段保留原始 `split(";")` 结果并逐项检查，不在结构校验前过滤空元素。
- 前导分隔符、尾随分隔符、连续分隔符以及仅含空白的元素均立即失败；错误信息包含字段名、从 0 开始的空元素索引、manifest/config 路径和 `empty provenance entry`，并说明无法建立一一对应关系。
- 整个字段为 `""` 时解析为空列表；因此当前正式合同允许 `formal_source_paths=""` 且 `formal_source_sha256=""` 的双空声明。该合同依据现有 manifest 解析语义：双空不触发结构错误，但随后仍由现有 asset/provenance 门决定构建结果。
- 空项检查和数量检查位于 source hash 配对、staging 及 release promote 之前；正式和诊断构建共用，诊断开关不能绕过。
- 数量相等时仍由原有 hash/provenance 门决定后续成功或失败；不使用截断式 `zip`，不忽略多余 path/hash，不生成、刷新或修改 provenance hash。

### 10.3 回归测试

以下每条命令均已从项目根目录实际执行，unittest 命令退出码均为 `0`；测试内部临时构建按预期返回 `4` 时由断言验证其失败原因。

| 测试 | 实际命令 | unittest 退出码 | 结果 |
|---|---|---:|---|
| T1：paths/hashes 数量相等 | `python -m unittest tests.test_build_provenance_structure.FormalProvenanceStructureTests.test_t1_equal_lists_reach_existing_provenance_gate` | 0 | 数量合同通过；随后原有 provenance 门拒绝，构建返回 4 |
| T2：paths 多 1 项 | `python -m unittest tests.test_build_provenance_structure.FormalProvenanceStructureTests.test_t2_extra_path_is_rejected` | 0 | 构建返回 4；报告 paths=2、sha256=1 和一一对应失败 |
| T3：hashes 多 1 项 | `python -m unittest tests.test_build_provenance_structure.FormalProvenanceStructureTests.test_t3_extra_hash_is_rejected` | 0 | 构建返回 4；报告 paths=1、sha256=2 和一一对应失败 |
| T4：paths 为空、hashes 非空 | `python -m unittest tests.test_build_provenance_structure.FormalProvenanceStructureTests.test_t4_empty_path_list_with_hash_is_rejected` | 0 | 构建返回 4；数量不一致被拒绝 |
| T5：诊断模式不能绕过数量门 | `python -m unittest tests.test_build_provenance_structure.FormalProvenanceStructureTests.test_t5_diagnostic_mode_cannot_bypass_structure_gate` | 0 | 诊断构建返回 4；数量不一致仍被拒绝 |
| T6：paths 连续分隔符 | `python -m unittest tests.test_build_provenance_structure.FormalProvenanceStructureTests.test_t6_consecutive_empty_path_entry_is_rejected` | 0 | 构建返回 4；报告 `formal_source_paths` 的空项 index 1 |
| T7：hashes 连续分隔符 | `python -m unittest tests.test_build_provenance_structure.FormalProvenanceStructureTests.test_t7_consecutive_empty_hash_entry_is_rejected` | 0 | 构建返回 4；报告 `formal_source_sha256` 的空项 index 1 |
| T8：paths 前导分隔符 | `python -m unittest tests.test_build_provenance_structure.FormalProvenanceStructureTests.test_t8_leading_empty_path_entry_is_rejected` | 0 | 构建返回 4；报告 `formal_source_paths` 的空项 index 0 |
| T9：hashes 尾随分隔符 | `python -m unittest tests.test_build_provenance_structure.FormalProvenanceStructureTests.test_t9_trailing_empty_hash_entry_is_rejected` | 0 | 构建返回 4；报告 `formal_source_sha256` 的空项 index 1 |
| T10：仅空白元素 | `python -m unittest tests.test_build_provenance_structure.FormalProvenanceStructureTests.test_t10_whitespace_only_entry_is_rejected` | 0 | 构建返回 4；报告 `formal_source_paths` 的空项 index 1 |
| T11：正式/诊断均拒绝空项 | `python -m unittest tests.test_build_provenance_structure.FormalProvenanceStructureTests.test_t11_formal_and_diagnostic_modes_reject_empty_entries` | 0 | 两种模式均返回 4；诊断开关不能绕过 |
| T12：双方同时为空 | `python -m unittest tests.test_build_provenance_structure.FormalProvenanceStructureTests.test_t12_both_lists_empty_are_allowed_by_current_contract` | 0 | 双空通过结构门；随后原有 provenance 门返回 4，未触发 empty entry 或数量错误 |

标准模块和发现命令也均已从项目根目录实际执行并退出 `0`：

```text
python -m unittest tests.test_build_provenance_structure
Ran 12 tests ... OK

python -m unittest discover -s tests -p "test_build_provenance_structure.py"
Ran 12 tests ... OK
```

### 10.4 正式构建与文件哈希

- 正式命令：`python tools/build.py --language both --clean`，退出码 `4`；失败发生在正式 release staging/promote 前。
- `release/CHNN_KAM_Manuscript_ZH.pdf` 修改前后均为 `C3B2B3948FB67F12D91A7437147614E13F396AB68FA2DF67337858B63BC0F162`。
- `release/CHNN_KAM_Manuscript_EN.pdf` 修改前后均为 `7F76C275B1937E74F91593AFD93829B7EB55E5698710D77E149312767B2BB1D5`。
- `FIGURE_TABLE_PROVENANCE.csv` 修改前后均为 `8AB2E3729A2A41259C05D19819A3E96EF9F70674F36E04ADD588C4C63CF78574`。
- 现有 12 个 provenance 失配仍未刷新、补齐或生成新 hash；本轮没有改变正式 provenance CSV。
- 本轮只修复 A-13 的测试可发现性和空 provenance entry 结构门，没有声称关闭其他 PARTIAL 或 BLOCKED 项。

## 11. 第四轮返工：A-11、A-16、A-17

### 11.1 绑定基线与范围

- 本轮起始 head：`5416616ab5543da027c722d2df791cbb019875c9`。
- 分支：`fix/first-review`；PR #1 继续保持 Draft；不修改 `main`，不创建新 PR，不合并。
- 本轮只处理 A-11、A-16、A-17；没有通过文字修改声称关闭 A-01、A-03、A-07、A-08、A-14、A-15。
- 未虚构正式源码、原始数组、机器日志、KAM 数值证书或工程安全域；未刷新 12 个 provenance 失配哈希。

### 11.2 A-11：近似 K-辛理论与推导

- 修改文件和位置：`manuscript/zh/sections/03-hamiltonian-structure.tex:847`、`manuscript/en/sections/03-hamiltonian-structure.tex:847`；`manuscript/{zh,en}/sections/05-symplectic-kam.tex:81-171`。
- 修改前问题：原文本容易把数值方法阶、生成函数截断阶、结构缺陷、轨迹误差和 KAM 小扰动混为同一个 \(O(h^{m+1})\) 量，并把条件性理论写成近似结构的直接证明。
- 实际修改：
  - 明确区分数值代数阶 \(r_{\rm alg}\)、生成函数截断阶 \(m_{\rm gen}\)、局部一步映射误差、固定时间区间轨迹误差和离散结构缺陷 \(\Delta_K\)。
  - 在同一局部域 \(\mathcal{D}'\Subset\mathcal{D}\) 上定义 \(\Delta_K\) 的 \(C^0\) 范数；明确生成函数余项 \(R_S\) 需要在 \(C^2\) 或解析范数中估计。
  - 给出条件链：局部域与正则性、\(K_{ij}=-K_{ji}\)、二形式 \(\Omega_K\) 的空间闭合、时间相容条件、\(\inf_{\mathcal D}\sigma_{\min}(K)>0\) 的非退化性、时间相容离散映射、生成函数截断及其余项，最后才把 \(C^1\) 映射误差传递为结构缺陷上界。
  - 明确不能未经上述传递证明直接把代数阶写成 \(O(h^{m+1})\) 的辛结构缺陷；KAM 小扰动还必须合并模型、学习、截断、映射和结构误差，并满足选定定理的解析域、Diophantine、非退化、维数和步长非共振条件。
  - 明确“近似 K-辛”不等于数值 KAM 认证；当前没有不变环面、频率映射、Diophantine 条件和非退化常数的完整数值证书，当前结果只支持结构保持数值框架，不支持工程安全域结论。
- 数学和文献依据：Birkhoff 自伴表示、闭合性和时间相容条件引用 `FengQin2010` 与 `HairerLubichWanner2006GNI`；辛算法 KAM 和辛映射 KAM 分别引用 `Shang1999KAMAlgorithms`（Numerische Mathematik 83:477--496）和 `Shang2000KAMMappings`（Journal of Dynamics and Differential Equations 12(2):357--383）。书籍条目和文章页码已在 `bibliography/references.bib:150-230` 核对。引用只提供理论来源，不表示本稿已完成对应证明或数值证书。
- 当前状态：`FIXED`（文本层）；具体 Birkhoff 结构、离散映射误差常数和 KAM 数值证书仍需正式实现与机器数据，最终审查状态不在本报告自行提升。

### 11.3 A-16：符号和旧合同清理

- 修改文件和位置：`translation/terminology.md` 的 Symbol contract；双语摘要、正文第 03/04/06/07/08 章和附录中的当前合同声明；`README_CN.md`、`code/README.md`、`KNOWN_ISSUES.md`、`CHANGELOG_P2_B0_R2_WRITEBACK.md`；本报告本节及问题总表。
- 修改前问题：磁场、端口嵌入、canonical pullback、诊断阶数和待定生产阶数在仓库文字中存在复用或语义漂移；旧 `B^T L` 仍可在回写历史记录中被误读为当前合同。
- 实际修改：当前文本统一使用 `B_mag`（磁场）、`B_port`（端口嵌入）、`B_N`（模态/canonical 映射）、`L_full`（全空间载荷率）、`N_diag`（诊断阶数）和 `n_main`（待正式收敛研究选择的生产阶数），并保持 `Q_diss` 与 `Q_contact` 为分离通道。当前正文只做文字合同统一，不声称正式源码对象、维度和接口已经核验。
- 历史保留：`CHANGELOG_P2_B0_R2_WRITEBACK.md` 已增加 **Historical / superseded record** 标记；`review/first-review.md`、`review/issue-matrix.md`、审查报告和本报告中的旧符号只作为审查证据或历史问题描述，不是当前实现合同。
- 当前状态：文本层完成；代码接口、正式控制器、自适应律、正式输入数组和对象维度仍为 `PARTIAL`，没有因符号表更新而声称实现级闭合。

### 11.4 A-16 语义检索记录

检索覆盖 `*.tex`、`*.md`、`*.py`、`*.json`、`*.csv` 和 `*.txt`，排除生成目录 `build/`、正式 PDF 目录 `release/`。搜索词包含下列显式形式及其 LaTeX 变体（如 `B_{N}`、`\mathbf{B}_{port}`、`Q_{diss}`、`\dot{p}`）：

| 搜索词 | 命中文件（按当前文本、审计/历史记录分组） | 保留原因与修改结果 | 剩余未核验项 |
|---|---|---|---|
| `B_N`、`B_{N}` | 当前：双语第 03、06 章、双语附录、双语摘要、canonical 诊断表、`translation/terminology.md`；历史/审查：`review/*`、`FINAL_BUILD_AND_BOUNDARY_AUDIT.md`、`WRITEBACK_EXECUTION_PLAN.md`、`审查报告_20260804_第01次.md` | 当前 canonical pullback 保留 `B_N`；历史命中不改写为新数据，并在本记录中标注为历史/审查语境 | 正式源码中的矩阵维度、输运项和原始数组未核验 |
| `B_port`、`B_{port}` | 双语第 04 章、`translation/terminology.md`、`review/*`、`审查报告_20260804_第01次.md` | 当前端口嵌入统一为 `B_port`，只进入动量通道；审查文件中的旧写法保留为证据 | 正式控制器和端口代码接口未交付 |
| `B_mag`、`B_{mag}` | `translation/terminology.md`、本报告；正文中的磁场多为语义文字 | 仅注册磁场对象，避免与端口或基矩阵复用；没有虚构未交付代码对象 | 正式源码是否使用同一对象和维度未核验 |
| `L`、`L_full`、`\dot p` | 双语第 03 章、双语附录、摘要、数值表、审查/审计记录；`translation/terminology.md` | 当前有效载荷率明确为 `L_full=\dot P_full` 的条件性记号；动量率保留输运项；裸 `L` 只在局部代数或历史语境中保留 | 正式 force-v2/G3 标签和代码命名未核验 |
| `N`、`N_diag`、`n_main` | 双语摘要、第 02/03/04/06/07 章、canonical 表、附录、`translation/terminology.md`、审查记录 | `N_diag=2` 仅为诊断基；`n_main` 明确为待正式收敛研究选择的生产阶数；求和索引 `N` 按局部数学含义保留 | 生产阶数尚无正式收敛结果，模态充分性未验证 |
| `B^T L` | `CHANGELOG_P2_B0_R2_WRITEBACK.md`、`review/modification-report.md` 的历史记录 | changelog 已标为 Historical / superseded；报告中的命中是旧问题和修复证据，不是当前正文合同；当前合同使用 `B_N^T\dot P_full` 并含输运项 | 正式实现是否已采用当前链式法则仍需源码和重算证据 |
| `Q_diss` | 双语第 01--04 章、`docs/reference/LABEL_REGISTRY.md`、`translation/terminology.md`、审查/报告文件 | 当前分离体内被动耗散 `Q_diss^bulk` 与非势接触 `Q_contact`；文档/审查命中保留其局部定义或历史引用 | 正式端口实现是否单计功率未核验 |
| `Q_contact` | 双语第 01--04 章、`translation/terminology.md`、审查/报告文件 | 接触阻尼、摩擦和冲击保持独立 contact 通道；不改写文献引用和审查证据 | 正式 contact 代码、事件轨迹和功率数组未交付 |

### 11.5 A-17：verification skeleton 与正式实现边界

- 修改文件和位置：`code/verification_skeleton.py` 模块说明和 JSON 输出；`code/verification_results.json` 生成结果；`code/README.md`、`README_CN.md`、`KNOWN_ISSUES.md`；双语第 04、07、08 章和附录。
- 修改前问题：README、正文和 JSON 容易让 V1--V3 skeleton 与正式 CHNN、COMSOL--Galerkin bridge、force-v2、P0/P1/P2、控制器或 KAM 证书混淆。
- 实际修改：所有相关描述统一为接口示例、回归测试骨架、数值流程演示和构建门测试对象。`verification_results.json` 增加 `artifact_type`、`scope`、`formal_implementation=false`、`formal_experiment=false`、`numerical_kam_certificate=false` 和 `required_formal_materials`；结果只描述 skeleton 运行，不能作为论文正式实验结果。
- 解除边界所需材料：正式源码、配置、环境锁、原始数组、manifest、clean-run 日志、自动生成的表格和图、provenance 一致性记录。
- 当前状态：`PARTIAL`。边界已强化，但材料仍缺失；没有将 skeleton 描述为正式 CHNN、bridge、force-v2、生产实验、控制器、自适应律或 KAM 数值证书。

### 11.6 检索和验证结果

- `python code/verification_skeleton.py`：exit `0`；生成 JSON 的 skeleton 范围字段和三个 `false` 边界标志。
- `python -m unittest discover -s tests -v`：exit `0`，共 12 项结构门测试通过。
- `python tools/audit_semantics.py --language zh`：exit `0`，174 个 section label、424 个 equation label、607 个唯一 label。
- `python tools/audit_semantics.py --language en`：exit `0`，同上；`python tools/audit_bilingual.py`：exit `0`；`python tools/check_bibliography.py`：exit `0`，37 个 BibTeX 条目、37 个活动引用、0 个未使用条目。
- `python tools/build.py --language both --clean --diagnostic --allow-provenance-mismatch`：exit `0`；中文诊断 PDF 58 页，英文诊断 PDF 71 页，均位于 `build/diagnostic/{zh,en}`；日志无 `Overfull`、未解析引用、缺失图片/表格或 LaTeX 致命错误。MiKTeX 宿主的 Windows 版本警告不被解释为科学验证。
- `python tools/build.py --language both --clean`：本次在正式 provenance 前置门处 exit `1`，报告同一 12 个资产/源失配；失败发生在正式 release staging/promote 前，未写入正式 release。
- `git diff --check` 和最终文件范围检查在提交前执行；正文、附录和表格只发生本节列出的文本边界/理论修改，没有新增正式实验声明。

### 11.7 文件和证据状态

- 本轮修改文件：`CHANGELOG_P2_B0_R2_WRITEBACK.md`、`KNOWN_ISSUES.md`、`README_CN.md`、`backmatter/appendices-{zh,en}.tex`、`code/README.md`、`code/verification_skeleton.py`、`code/verification_results.json`、`manuscript/{zh,en}/sections/{03-hamiltonian-structure,04-chnn-model,05-symplectic-kam,07-discussion,08-conclusion}.tex`、`translation/terminology.md`、本报告。
- 未修改 `FIGURE_TABLE_PROVENANCE.csv`、正式 release PDF、`review/first-review.md`、`review/issue-matrix.md`、`main`；12 个 provenance 失配仍未刷新。
- 正式 release SHA-256（修改前后相同）：ZH `C3B2B3948FB67F12D91A7437147614E13F396AB68FA2DF67337858B63BC0F162`；EN `7F76C275B1937E74F91593AFD93829B7EB55E5698710D77E149312767B2BB1D5`。
- 正式 provenance CSV SHA-256（修改前后相同）：`8AB2E3729A2A41259C05D19819A3E96EF9F70674F36E04ADD588C4C63CF78574`。
- 本轮没有声称关闭 A-01、A-03、A-07、A-08、A-14、A-15，也没有因 A-11 的文本修订声称完成 KAM 认证、正式模型验证或工程安全域。
