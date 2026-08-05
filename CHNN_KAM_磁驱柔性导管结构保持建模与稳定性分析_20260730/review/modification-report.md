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
| A-11 | Birkhoff 定理引用 COMSOL；\(O(h^{m+1})\) 缺陷仍称精确 K-辛 | 双语第 05 章式 (5-7)、(5-15) | 改引 FengQin2010、HairerLubichWanner2006GNI；改称近似 K-辛并给出精确成立条件 | BibTeX 审计、双语公式审计、编译 | FIXED | 尚无具体 Birkhoff 结构或不变环面数值证书 |
| A-12 | 单一 1 s mode1 哨兵外推为多幅值资格 | 双语摘要、引言、第 06--08 章 | 统一收窄为“后续 A1 资格实验的候选输入”，明确不认证跨 mode、幅值或工况 | 全文固定短语检索、双语审计 | FIXED | A-01 重算前连 A1 资格也未完成 |
| A-13 | build 不验 provenance 和资源，不能区分 PDF 与科学门 | tools/build.py | 增加缺失资源和 provenance fail-closed 门；诊断构建必须显式放行；保留语义、双语和 BibTeX 检查 | 默认门失败、诊断构建成功 | PARTIAL | 仍缺 raw 到 metrics 到图表的正式重算流水线和科学断言 |
| A-14 | \(Q_c\) 定义与方程左端乘子符号不一致 | 双语第 02 章式 (2-95)--(2-96) | 定义统一为 \(Q_c:=-G^T\lambda_c\)，方程左端保留 \(+G^T\lambda_c\) | 双语公式审计、编译 | PARTIAL | 具体约束 residual 和代码符号仍未交付，无法完成实现级验收 |
| A-15 | 接触阻尼/摩擦在耗散和 contact 端口间重复或遗漏 | 双语第 01--04 章 | 定义 \(Q_{\rm diss}^{bulk}/P_{\rm diss}^{bulk}\) 不含接触；未进入势能的接触弹性及接触阻尼、摩擦、冲击只进入 \(Q_{\rm contact}/P_{\rm contact}\)；同步修正能量式、平衡与线性化、Hamiltonian 端口、residual 和数据接口 | 双语公式审计、全文端口检索、编译 | PARTIAL | 正式实现未交付，无法核对代码是否遵循排他合同 |
| A-16 | \(B,J,L,N,n,d\) 等复用，控制输入维度不清 | 双语第 03、04 章 | 注册 B_mag、B_port、L_full、N_diag、n_main 和关键维度；将端口嵌入统一为 \(B_{\rm port}\)，明确 \(u\in\mathbb R^d\)、\(U_{\rm port}=B_{\rm port}u\in\mathbb R^{2d}\) 且端口只进入动量通道；区分数据、控制和 Birkhoff 三类步长，并声明当前无可核验的离散控制器或自适应律 | 双语公式审计、全文 B_port/步长/regressor 检索 | PARTIAL | 历史章节中的局部 \(J,L\) 尚未全量重命名；正式控制器、自适应律和代码接口缺失 |
| A-17 | README 引用不存在的源码归档 | code/README.md | 明确归档缺失；列出实际存在的 skeleton/JSON，并声明骨架不是正式 CHNN/Bridge/force-v2 实现 | 文件存在性核查 | FIXED | 正式复现包仍未交付 |

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
