# 第一轮问题矩阵

- 基线：`main@e53016b`
- 来源：第一轮科学与代码审查结果
- 范围：仅整理已完成结论；不新增问题，不对修改分支作判断
- 文件约束：本文件只记录审查意见；未修改论文正文、参考文献、图片、脚本或实验文件

| 编号 | 级别 | 位置 | 问题 | 依据 | 建议 | 验收条件 |
|---|---|---|---|---|---|---|
| A-01 | S0 | `manuscript/zh/sections/03-hamiltonian-structure.tex:120-131` | 对 (p_N=B_N(q_N)^\top P_{\rm full}) 直接写 (dot p_N=B_N^\top L)，遗漏构形相关基的输运项。 | 若 (B_N=B_N(q_N))，一般有 (dot p_N=\dot B_N^\top P_{\rm full}+B_N^\top\dot P_{\rm full})。正文未证明 (B_N) 常数，也未定义 (L) 为含补偿量。 | 重新推导 canonical pullback；定义 (U,B_N,E,P_{\rm full},L)，并重算 (dot p)、force-v2、G3 和训练标签。 | 论文给出完整链式法则；代码实现包含输运项或严格证明其已吸收；独立复算的 canonical 闭合与表格结果一致。 |
| A-02 | S1 | `RESULT_ID_TO_TEX_MAP.csv:2-19`；`code/README.md:20` | P0/P1/P1.5/P1.6、Bridge、R2 的正式源码、原始输出和报告不在交付目录。 | 登记的 ZIP、`bridge_conservative/...`、CHNN 训练和逐运行输出路径全部无法在当前项目解析。 | 提供可运行源码、配置、原始数组、manifest、日志、环境锁和哈希。 | 每个 `result_id` 的 evidence path 在 clean checkout 中存在；一条命令可从原始输出重建指标。 |
| A-03 | S1 | `FIGURE_TABLE_PROVENANCE.csv:5-17` | 10/10 个中英文 TeX 结果表的 SHA-256 与登记值不一致。 | 轻量 CSV 和 4 个图件哈希匹配，但 10 个表格全部失配，说明 provenance 冻结后表格被改写。 | 从机器指标自动生成表格，更新 provenance，禁止手工改表后保留旧哈希。 | 构建前哈希检查全部通过；表格源、生成命令和 provenance 记录一一对应。 |
| A-04 | S1 | `manuscript/zh/sections/06-numerical-results.tex:8`；`05-symplectic-kam.tex:56` | relative L2、rollout、linearization、force-v2、G2/G3、energy drift 及 G0-G6 缺完整定义。 | 文本主要给出名称、最终数值和阈值，没有分子、分母、分量、时间支持、索引和聚合；G0-G6 没有完整机器门。 | 为每个指标提供公式、数组轴、切片、零分母处理、聚合和阈值来源。 | 任何指标均可从原始数组独立重算；公式、代码函数和机器 JSON 通过逐项映射。 |
| A-05 | S1 | `manuscript/zh/sections/04-chnn-model.tex:243`；`06-numerical-results.tex:6-8` | P1 只说明 leave-one-whole-trajectory-out，未说明验证轨迹、early stopping、超参数选择和归一化范围。 | 没有 fold manifest、预处理日志和模型选择日志；当前无法证明或排除验证/预处理泄漏。 | 冻结每个 fold 的 train/val/test trajectory ID；所有预处理和选择只使用 train/val。 | 自动断言三集合 trajectory ID 无交集；test 只在最终评估调用。 |
| A-06 | S1 | `manuscript/zh/sections/06-numerical-results.tex:29-39` | 比较模型的参数量、网络配置、优化器、积分器、训练预算、早停和选择规则未报告。 | P1.5 仅报告相对训练/评估时间，没有绝对时间、硬件或参数量。 | 建立逐模型 model card，做参数量匹配或明确预算差异。 | 每个模型有固定配置、参数量、训练/推理时间、硬件和相同模型选择规则。 |
| A-07 | S1 | `manuscript/zh/sections/02-galerkin-discretization.tex:964-975` | (e_n^{traj}) 的相减对象维度不一致，且没有使用 (q^{(n)})。 | (q^{(n+1)}\in\mathbb R^{n+1})，(Pi_{n+1\to n}q^{(n+1)}\in\mathbb R^n)；现式不合法。 | 定义相邻阶比较为 (q^{(n)}-Pi q^{(n+1)})，或回嵌到共同全阶空间。 | (n_*) 判据的每一项在同一空间、同一时间网格上可计算，并有机器输出。 |
| A-08 | S1 | `manuscript/zh/sections/03-hamiltonian-structure.tex:820-856` | 前文区分精确流 (Phi_h) 与数值映射 (F_h)，后文却写 (F_h=Phi_h^{cons})。 | 一般数值辛映射不等于连续系统精确流，该等式会使 (delta_{alg}) 失去意义。 | 重新命名数值映射并给出局部误差/算法误差。 | (F_h) 与 (Phi_h) 在定义、代码和误差预算中保持不同对象；(delta_{alg}) 可非零复算。 |
| A-09 | S1 | `manuscript/zh/sections/03-hamiltonian-structure.tex:574-599`；`04-chnn-model.tex:4-37` | 理论要求在 Kirchhoff 约束流形上使用独立坐标，但未给出 (chi(y))、切空间基、秩或余切变换。 | 未证明固定 (N=2) pilot 数据与理论正则 Hamiltonian 对象相同。 | 实现约束坐标、约束 Jacobian、切/余切映射和残差检查。 | 约束残差、秩、坐标变换和 canonical 数据生成均有代码与数值记录。 |
| A-10 | S1 | `manuscript/zh/sections/04-chnn-model.tex:395-501` | CHNN 泛化定理的 i.i.d.、密度下界和高阶正则性假设未在 pilot 数据上验证。 | 三条固定轨迹的时间点相关，且不能直接提供全维相空间密度下界。 | 将定理明确为条件命题；若要应用，改变采样协议或建立轨迹依赖数据理论。 | 论文明确列出未验证假设；任何数值结论不再调用该定理作为已满足保证。 |
| A-11 | S1 | `manuscript/zh/sections/05-symplectic-kam.tex:81,138-145`；`bibliography/references.bib:67-74` | Birkhoff 自伴表示引用 COMSOL Weak Contribution 文档；近似 (K)-结构误差被称为 (K)-辛。 | 官方 COMSOL 文档只描述弱贡献功能，不支撑 Birkhoff 存在性定理；式 (5-15) 只有 (O(h^{m+1}))。 | 替换为真正的 Birkhoff/自伴理论来源，并区分精确与近似结构。 | 定理条件逐项给出；若仅近似保持，则不将其作为精确辛 KAM 输入。 |
| A-12 | S1 | `manuscript/zh/sections/06-numerical-results.tex:49`；`08-conclusion.tex:10` | 单一 (1\,s) mode1 哨兵被推广为一般多幅值数据生成资格。 | Bridge 严格 (0.5\%) 能量门仍有 2/3 失败；单哨兵不能认证跨 mode/幅值。 | 收窄为允许进入 A1 sentinel 的条件性观察，或补充独立多幅值资格实验。 | 至少完成预注册的跨 mode、幅值和工况资格集；否则结论保持局部。 |
| A-13 | S1 | `tools/build.py:97-152`；`code/verification_skeleton.py:187-190` | 构建不重建科学资产、不校验 provenance；骨架没有断言，坏结果仍 exit 0。 | 旧表、旧图、旧 JSON 可继续进入 PDF；失败门不是可执行门。 | 建立 raw→metrics→tables/figures→provenance→PDF 的冷构建链，门失败时非零退出。 | clean build 不依赖旧科学资产；所有失败门都有机器断言和失败日志。 |
| A-14 | S2 | `manuscript/zh/sections/02-galerkin-discretization.tex:779-796` | 约束力定义 (Q_c=+G^\top\lambda_c)，系统方程又将同一项正号置于左端。 | 乘子可重命名，但当前定义与方程符号未统一。 | 统一乘子符号或调整方程。 | 从定义到离散方程、代码 residual、能量功率符号完全一致。 |
| A-15 | S2 | `manuscript/zh/sections/01-rod-model.tex:574-602`；`04-chnn-model.tex:170,337` | 接触阻尼/摩擦在连续能量层归入耗散，但 CHNN 实现层又单列 (Q_{contact})。 | 未定义排他集合时可能重复计入或漏计接触功率。 | 明确接触弹性、阻尼、摩擦、冲击的唯一通道。 | 功率账满足 (Q_{diss}\cap Q_{contact}=\varnothing)，且代码只调用一次。 |
| A-16 | S2 | 多章节符号表缺失 | (B,J,L,M_e,N,n,d) 复用多个含义，阶数关系未唯一登记。 | 同一论文对象无法稳定映射到代码对象。 | 建立全局符号注册表并改名。 | 定义、推导、损失、标签、代码、表格和结论中的同一对象保持单一含义。 |
| A-17 | S3 | `code/README.md:5`；`KNOWN_ISSUES.md` | 文档引用不存在的 `original_prototype_archive.txt`，部分 README 与当前资产状态不一致。 | 增加复现者定位成本，可能误把归档说明当证据。 | 更新文档并加入打包完整性检查。 | clean checkout 中 README 所列文件全部存在或明确标记缺失。 |

## 当前审查门

| Gate | 第一轮状态 | 验收依据 |
|---|---|---|
| Gate A：正式数据生成 | FAIL | canonical 动量率公式和正式标签链未闭合。 |
| Gate B：正式模型比较 | BLOCKED | 正式数据、split、代码、公平预算未冻结。 |
| Gate C：结构优势声明 | FAIL | 仅有缺失原始证据的低维/三轨迹汇总。 |
| Gate D：KAM 数值认证 | BLOCKED | 精确辛映射、生产阶数、非退化和高阶证书未实例化。 |
| Gate E：工程安全域 | BLOCKED | 开放端口、高保真、接触、控制和实验验证未完成。 |

## 说明

本矩阵是第一轮审查的固定记录，不代表对 `fix/first-review` 的复审结果。修改分支创建 Pull Request 后，应另行对比 `main@e53016b`，逐项输出 `PASS`、`FAIL` 或 `BLOCKED`，并记录对应代码、数据、测试和 provenance 证据。
