# Stable label registry

## Sections

| Label | Source heading | Level |
|---|---|---|
| `sec:introduction` | 引言 | `section*` |
| `sec:rod-model` | 多物理载荷下的几何精确弯曲---扭转导管动力学 | `section` |
| `sec:rod-1-1` | 建模框架 | `subsection` |
| `sec:rod-1-1-1` | 模型层级与计算分支 | `subsubsection` |
| `sec:rod-1-2` | 几何与运动学描述 | `subsection` |
| `sec:rod-1-2-1` | 中心线与截面标架 | `subsubsection` |
| `sec:rod-1-2-2` | 反对称算子 | `subsubsection` |
| `sec:rod-1-2-3` | 剪切---拉伸应变 | `subsubsection` |
| `sec:rod-1-2-4` | 曲率---扭转运动学 | `subsubsection` |
| `sec:rod-1-2-5` | 截面角速度与相容条件 | `subsubsection` |
| `sec:rod-1-2-6` | 截面内材料点运动 | `subsubsection` |
| `sec:rod-1-3` | 完整动能、弹性势能与本构关系 | `subsection` |
| `sec:rod-1-3-1` | 截面质量参数与质量中心线约定 | `subsubsection` |
| `sec:rod-1-3-2` | 完整结构动能 | `subsubsection` |
| `sec:rod-1-3-3` | 弹性势能密度 | `subsubsection` |
| `sec:rod-1-3-4` | 内力与内力矩本构 | `subsubsection` |
| `sec:rod-1-4` | 动量平衡与多物理载荷 | `subsection` |
| `sec:rod-1-4-1` | 平动平衡 | `subsubsection` |
| `sec:rod-1-4-2` | 转动平衡 | `subsubsection` |
| `sec:rod-1-4-3` | Maxwell 应力张量下的磁力与磁力矩 | `subsubsection` |
| `sec:rod-1-4-4` | 修正 Morison 流体作用力与能量一致附加质量 | `subsubsection` |
| `sec:rod-1-4-5` | 导管---血管壁接触力与接触力矩 | `subsubsection` |
| `sec:rod-1-4-6` | 微重力项 | `subsubsection` |
| `sec:rod-1-4-7` | 完整强形式方程组 | `subsubsection` |
| `sec:rod-1-5` | 变分形式与完整弱形式 | `subsection` |
| `sec:rod-1-5-1` | 虚位移与虚转角 | `subsubsection` |
| `sec:rod-1-5-2` | 内部虚功 | `subsubsection` |
| `sec:rod-1-5-3` | 惯性虚功与外力虚功 | `subsubsection` |
| `sec:rod-1-5-4` | 联合弱形式 | `subsubsection` |
| `sec:rod-1-5-5` | 边界项与边界条件 | `subsubsection` |
| `sec:rod-1-6` | Kirchhoff 无剪切约束 | `subsection` |
| `sec:rod-1-7` | 连续能量平衡 | `subsection` |
| `sec:rod-1-7-1` | 结构能量与扩展惯性能量 | `subsubsection` |
| `sec:rod-1-7-2` | 功率平衡 | `subsubsection` |
| `sec:rod-1-8` | 本章小结 | `subsection` |
| `sec:galerkin-discretization` | 平移---转动联合 Galerkin 离散 | `section` |
| `sec:galerkin-2-1` | 离散化原则 | `subsection` |
| `sec:galerkin-2-2` | 联合有限维近似 | `subsection` |
| `sec:galerkin-2-2-1` | 平移近似 | `subsubsection` |
| `sec:galerkin-2-2-2` | 截面姿态近似 | `subsubsection` |
| `sec:galerkin-2-2-3` | 右 Jacobian 与角速度 | `subsubsection` |
| `sec:galerkin-2-2-4` | 联合广义坐标与虚变量 | `subsubsection` |
| `sec:galerkin-2-3` | 离散应变与势能 | `subsection` |
| `sec:galerkin-2-3-1` | 剪切---拉伸应变 | `subsubsection` |
| `sec:galerkin-2-3-2` | 曲率---扭转应变 | `subsubsection` |
| `sec:galerkin-2-3-3` | 离散内部势能 | `subsubsection` |
| `sec:galerkin-2-4` | 完整离散动能与质量---惯性矩阵 | `subsection` |
| `sec:galerkin-2-4-1` | 材料点速度矩阵 | `subsubsection` |
| `sec:galerkin-2-4-2` | 质量---惯性矩阵 \(\mathbf{M}\left( \mathbf{q} \right)\) 的严格定义\textbackslash left( \textbackslash mathbf\{q\} \textbackslash right) 的严格定义} | `subsubsection` |
| `sec:galerkin-2-4-3` | 质量---惯性矩阵的分块形式 | `subsubsection` |
| `sec:galerkin-2-4-4` | 质量中心线与偏心部件 | `subsubsection` |
| `sec:galerkin-2-4-5` | 小转角常质量近似的适用范围 | `subsubsection` |
| `sec:galerkin-2-4-6` | 流体附加质量的能量一致离散 | `subsubsection` |
| `sec:galerkin-2-4-7` | 对称性与正定性 | `subsubsection` |
| `sec:galerkin-2-5` | 联合 Galerkin 投影 | `subsection` |
| `sec:galerkin-2-5-1` | 惯性项 | `subsubsection` |
| `sec:galerkin-2-5-2` | 内力项 | `subsubsection` |
| `sec:galerkin-2-5-3` | 分布力和分布力矩的联合投影 | `subsubsection` |
| `sec:galerkin-2-5-4` | 边界广义力 | `subsubsection` |
| `sec:galerkin-2-5-5` | 保守与非保守外载荷 | `subsubsection` |
| `sec:galerkin-2-6` | 广义动量与几何惯性项的严格推导 | `subsection` |
| `sec:galerkin-2-6-1` | 一般广义动量 | `subsubsection` |
| `sec:galerkin-2-6-2` | 质量度量产生的几何惯性 | `subsubsection` |
| `sec:galerkin-2-6-3` | 规定流场交叉项产生的附加作用 | `subsubsection` |
| `sec:galerkin-2-6-4` | 常质量矩阵特例 | `subsubsection` |
| `sec:galerkin-2-7` | Kirchhoff 无剪切约束的离散处理 | `subsection` |
| `sec:galerkin-2-7-1` | 离散约束 | `subsubsection` |
| `sec:galerkin-2-7-2` | 拉格朗日乘子形式 | `subsubsection` |
| `sec:galerkin-2-7-3` | 有限剪切刚度形式 | `subsubsection` |
| `sec:galerkin-2-8` | 全局有限维动力学方程 | `subsection` |
| `sec:galerkin-2-8-1` | 无显式约束形式 | `subsubsection` |
| `sec:galerkin-2-8-2` | 受约束形式 | `subsubsection` |
| `sec:galerkin-2-9` | 离散能量与功率恒等式 | `subsection` |
| `sec:galerkin-2-9-1` | 保守惯性骨架的离散机械能 | `subsubsection` |
| `sec:galerkin-2-9-2` | 一般端口功率平衡 | `subsubsection` |
| `sec:galerkin-2-9-3` | 一致切线矩阵 | `subsubsection` |
| `sec:galerkin-2-10` | 局部线性化与工程约化 | `subsection` |
| `sec:galerkin-2-10-1` | 平衡构形附近的局部线性化 | `subsubsection` |
| `sec:galerkin-2-10-2` | 工程约化的适用范围 | `subsubsection` |
| `sec:galerkin-2-10-3` | 模态截断与主计算阶数的确定 | `subsubsection` |
| `sec:galerkin-2-11` | 数值实现与有限维模型输出 | `subsection` |
| `sec:galerkin-2-11-1` | COMSOL 模型层级、投影与验证 | `subsubsection` |
| `sec:galerkin-2-11-2` | 有限维状态、能量、端口与结构学习输出 | `subsubsection` |
| `sec:galerkin-2-11-3` | 训练数据分层与模型标签 | `subsubsection` |
| `sec:galerkin-2-12` | 本章小结 | `subsection` |
| `sec:hamiltonian-structure` | 有限维 Hamiltonian 结构与正则化 | `section` |
| `sec:hamiltonian-3-1` | 有限维相空间变量与 Hamilton 表述 | `subsection` |
| `sec:hamiltonian-3-1-1` | 联合广义坐标 | `subsubsection` |
| `sec:hamiltonian-3-1-2` | Hamilton 表述的基本框架 | `subsubsection` |
| `sec:hamiltonian-3-2` | 自治保守骨架的 Lagrangian、动量与 Hamiltonian | `subsection` |
| `sec:hamiltonian-3-2-1` | 自治势能的选取 | `subsubsection` |
| `sec:hamiltonian-3-2-2` | 自治骨架 Lagrangian 与广义动量 | `subsubsection` |
| `sec:hamiltonian-3-2-3` | Legendre 正则性 | `subsubsection` |
| `sec:hamiltonian-3-2-4` | Hamiltonian 的构造 | `subsubsection` |
| `sec:hamiltonian-3-2-5` | 非线性势能与恢复力 | `subsubsection` |
| `sec:hamiltonian-3-3` | 正则 Hamilton 方程与几何惯性 | `subsection` |
| `sec:hamiltonian-3-3-1` | 标准辛结构 | `subsubsection` |
| `sec:hamiltonian-3-3-2` | 构形相关质量矩阵产生的项 | `subsubsection` |
| `sec:hamiltonian-3-3-3` | 与 Euler--Lagrange 方程的等价性 | `subsubsection` |
| `sec:hamiltonian-3-3-4` | 能量守恒 | `subsubsection` |
| `sec:hamiltonian-3-4` | 受迫---耗散 Hamilton 结构 | `subsection` |
| `sec:hamiltonian-3-4-1` | 非保守广义力的统一入口 | `subsubsection` |
| `sec:hamiltonian-3-4-2` | 等效黏性阻尼特例 | `subsubsection` |
| `sec:hamiltonian-3-4-3` | 能量变化率 | `subsubsection` |
| `sec:hamiltonian-3-4-4` | 完整受迫系统的相空间形式 | `subsubsection` |
| `sec:hamiltonian-3-5` | 一般规定流场下的正则动量与 Hamiltonian | `subsection` |
| `sec:hamiltonian-3-5-1` | 一般离散 Lagrangian | `subsubsection` |
| `sec:hamiltonian-3-5-2` | 一般正则动量与 Hamiltonian | `subsubsection` |
| `sec:hamiltonian-3-5-3` | 与一般 Euler--Lagrange 方程的等价性 | `subsubsection` |
| `sec:hamiltonian-3-5-4` | 精确表示与骨架---端口表示 | `subsubsection` |
| `sec:hamiltonian-3-5-5` | 一般能量变化率 | `subsubsection` |
| `sec:hamiltonian-3-6` | 适用范围与严格 Kirchhoff 约束分支 | `subsection` |
| `sec:hamiltonian-3-6-1` | 局部姿态坐标 | `subsubsection` |
| `sec:hamiltonian-3-6-2` | 严格 Kirchhoff 主分支与有限剪切验证分支 | `subsubsection` |
| `sec:hamiltonian-3-7` | CHNN、KAM 与结构保持离散接口 | `subsection` |
| `sec:hamiltonian-3-7-1` | 正则无量纲化、复坐标与物理 Hamiltonian 基线 | `subsubsection` |
| `sec:hamiltonian-3-7-2` | 骨架---端口结构与表示一致的数据对象 | `subsubsection` |
| `sec:hamiltonian-3-7-3` | 稳定平衡点、模态正则化与可积参考系统 | `subsubsection` |
| `sec:hamiltonian-3-7-4` | 学习误差、离散误差与 KAM 小量预算 | `subsubsection` |
| `sec:hamiltonian-3-7-5` | 辛映射、Birkhoff 结构与环面方程 | `subsubsection` |
| `sec:hamiltonian-3-7-6` | COMSOL 主训练模型与高保真模型差异的结构分解 | `subsubsection` |
| `sec:hamiltonian-3-7-7` | 结构化学习与稳定性分析接口 | `subsubsection` |
| `sec:hamiltonian-3-8` | 本章小结 | `subsection` |
| `sec:chnn-model` | 复值表示增强的结构化 Hamiltonian 神经网络 | `section` |
| `sec:chnn-4-1` | 研究对象与上游接口 | `subsection` |
| `sec:chnn-4-2` | 保守 Hamiltonian 头与复值内部表示 | `subsection` |
| `sec:chnn-4-2-1` | 实值物理 Hamiltonian | `subsubsection` |
| `sec:chnn-4-2-2` | 复值主干与实值读出 | `subsubsection` |
| `sec:chnn-4-2-3` | 广义复线性层与实仿射完备性 | `subsubsection` |
| `sec:chnn-4-2-4` | 实 MLP 嵌入与条件性 Sobolev 逼近继承 | `subsubsection` |
| `sec:chnn-4-2-5` | 复值表示的物理边界 | `subsubsection` |
| `sec:chnn-4-3` | 开放端口动力学与分支网络 | `subsection` |
| `sec:chnn-4-4` | COMSOL 数据体系与训练对象 | `subsection` |
| `sec:chnn-4-4-1` | Kirchhoff 一致主训练集 | `subsubsection` |
| `sec:chnn-4-4-2` | 严格弱形式和高保真对照 | `subsubsection` |
| `sec:chnn-4-5` | 损失函数与分阶段训练 | `subsection` |
| `sec:chnn-4-5-1` | 保守导数监督 | `subsubsection` |
| `sec:chnn-4-5-2` | 端口与能量平衡监督 | `subsubsection` |
| `sec:chnn-4-5-3` | 轨迹、规范与辛结构损失 | `subsubsection` |
| `sec:chnn-4-5-4` | CHNN 的实现基础与结构检验 | `subsubsection` |
| `sec:chnn-4-6` | 从 CHNN 学习误差到 KAM 小量条件 | `subsection` |
| `sec:chnn-4-6-1` | 可积参考系统不是网络实部的自动结果 | `subsubsection` |
| `sec:chnn-4-6-2` | 保守训练数据、函数类与加性规范 | `subsubsection` |
| `sec:chnn-4-6-3` | 覆盖数与 Rademacher 复杂度接口 | `subsubsection` |
| `sec:chnn-4-6-4` | 从梯度风险到 Hamiltonian 一致误差 | `subsubsection` |
| `sec:chnn-4-6-5` | 高阶 Sobolev 或解析误差证书 | `subsubsection` |
| `sec:chnn-4-6-6` | 可积参考、既有物理摄动与学习误差分账 | `subsubsection` |
| `sec:chnn-4-6-7` | 学习误差证书向 KAM 条件的概率传递 | `subsubsection` |
| `sec:chnn-4-6-8` | 连续和离散误差预算 | `subsubsection` |
| `sec:chnn-4-7` | 三类离散动力学分支 | `subsection` |
| `sec:chnn-4-8` | 面向不变环面分析的输出对象 | `subsection` |
| `sec:symplectic-kam` | 辛离散、Birkhoff 结构与不变环面核验 | `section` |
| `sec:symplectic-kam-5-1` | 分析分支 | `subsection` |
| `sec:symplectic-kam-5-2` | 标准辛分支与生成函数 | `subsection` |
| `sec:symplectic-kam-5-3` | Birkhoff 系统自伴表示 | `subsection` |
| `sec:symplectic-kam-5-4` | 剩余向量场的 Birkhoff 结构辨识 | `subsection` |
| `sec:symplectic-kam-5-5` | Birkhoff 系统的 \(K\left( \mathbf{z},t \right)\)-辛离散格式,t \textbackslash right)-辛离散格式} | `subsection` |
| `sec:symplectic-kam-5-6` | 参数化方法计算不变环面 | `subsection` |
| `sec:symplectic-kam-5-7` | 参数延拓与安全操控域 | `subsection` |
| `sec:numerical-results` | 数值实验与结果 | `section` |
| `sec:numerical-6-1` | 实验层级、数据划分与比较基线 | `subsection` |
| `sec:numerical-6-2` | 软件实现与结构一致性检验 | `subsection` |
| `sec:numerical-6-3` | 保守分支辨识结果 | `subsection` |
| `sec:numerical-6-4` | 开放端口辨识结果 | `subsection` |
| `sec:numerical-6-5` | 高阶误差证书与 KAM 数值核验 | `subsection` |
| `sec:numerical-6-6` | 参数延拓、模型偏差与安全操控域 | `subsection` |
| `sec:discussion` | 讨论与适用范围 | `section` |
| `sec:discussion-7-1` | 理论依据与方法边界 | `subsection` |
| `sec:discussion-7-2` | 研究边界与待验证条件 | `subsection` |
| `sec:discussion-7-3` | 非主线模型与扩展方向 | `subsection` |
| `sec:conclusion` | 结论 | `section` |

## Equations

| Label | Word number | Nearest source lead-in |
|---|---:|---|
| `eq:rod-1-1` | 1.1 | 设参考材料坐标为 |
| `eq:rod-1-2` | 1.2 | 设导管中心线的位置矢量为 |
| `eq:rod-1-3` | 1.3 | 在每个横截面上引入右手正交标架 |
| `eq:rod-1-4` | 1.4 | 并定义旋转矩阵 |
| `eq:rod-1-5` | 1.5 | 满足 |
| `eq:rod-1-6` | 1.6 | 完整模型中不预先令 d_{3} 与中心线切向平行，因此允许横向剪切。中心线的伸长率和单位切向量分别定义为 |
| `eq:rod-1-7` | 1.7 | 对任意 a \in R^{3}，定义反对称矩阵 \widehat{a} \in so(3)，使得Sola2018MicroLie,MarsdenRatiu1999MechanicsSymmetry |
| `eq:rod-1-8` | 1.8 | 定义材料坐标系中的剪切---拉伸应变矢量 |
| `eq:rod-1-9` | 1.9 | 其中，\nu_{1} 和 \nu_{2} 为两个横向剪切应变分量，\nu_{3} 为沿截面第三方向的轴向伸长分量。参考应变记为 |
| `eq:rod-1-10` | 1.10 | 对于无初始剪切且参考长度未伸长的直杆，可取 |
| `eq:rod-1-11` | 1.11 | 在完整可剪切 Cosserat 母模型中，应区分截面第三方向的材料轴向应变分量与中心线伸长应变。前者定义为 |
| `eq:rod-1-12` | 1.12 | 另一方面，由 r_{,S} = R\nu 以及 R^{T}R = I 可得 \lambda = \parallel r_{,S} \parallel = \parallel \nu \parallel |
| `eq:rod-1-13` | 1.13 | 定义材料坐标系中的曲率---扭转矢量 |
| `eq:rod-1-14` | 1.14 | 其中，\kappa_{1} 和 \kappa_{2} 为两个主方向的弯曲曲率，\kappa_{3} 为独立扭转率。局部标架沿参考坐标的变化满足 |
| `eq:rod-1-15` | 1.15 | 参考曲率---扭转矢量记为 |
| `eq:rod-1-16` | 1.16 | 定义材料坐标系中的截面角速度 |
| `eq:rod-1-17` | 1.17 | 空间坐标系中的角速度为 |
| `eq:rod-1-18` | 1.18 | 由 r_{,St} = r_{,tS} 和 R_{,St} = R_{,tS} 得到运动学相容关系Simo1985FiniteStrainBeam,Antman2005Elasticity,Sola2 |
| `eq:rod-1-19` | 1.19 |  |
| `eq:rod-1-20` | 1.20 | 设截面内材料坐标为 |
| `eq:rod-1-21` | 1.21 | 则杆内材料点的空间位置写为 |
| `eq:rod-1-22` | 1.22 | 其速度为 |
| `eq:rod-1-23` | 1.23 | 设材料密度为 \rho\left( S,\xi \right)。定义单位参考长度质量 |
| `eq:rod-1-24` | 1.24 | 截面一阶质量矩 |
| `eq:rod-1-25` | 1.25 | 以及材料坐标系中的单位参考长度质量惯性张量 |
| `eq:rod-1-26` | 1.26 | 上述定义首先保留一般截面质量分布。为使后续连续动量平衡、弱形式和离散质量矩阵使用同一惯性基线，本文从第 1.4 节起将基础导管中心线 r(S,t) 选为各截面的质量中心线，因而分布杆体满足 |
| `eq:rod-1-27` | 1.27 | 若截面主轴与 e_{1},e_{2},e_{3} 一致，则 |
| `eq:rod-1-28` | 1.28 | 由材料点速度得到基础杆体的三维结构动能 |
| `eq:rod-1-29` | 1.29 | 对截面积分后，一般形式为 |
| `eq:rod-1-30` | 1.30 | 采用第 1.3.1 节的质量中心线约定后，c_{\rho} = 0，从而基础杆体动能化为 |
| `eq:rod-1-31` | 1.31 | 设剪切---拉伸刚度矩阵和弯曲---扭转刚度矩阵分别为 |
| `eq:rod-1-32` | 1.32 |  |
| `eq:rod-1-33` | 1.33 | 单位参考长度弹性势能密度定义为 |
| `eq:rod-1-34` | 1.34 | 内部弹性势能为 |
| `eq:rod-1-35` | 1.35 | 材料坐标系中的截面合内力和合内力矩由势能密度的梯度给出： |
| `eq:rod-1-36` | 1.36 |  |
| `eq:rod-1-37` | 1.37 | 空间坐标系中的内力和内力矩分别为 |
| `eq:rod-1-38` | 1.38 | 以下连续平衡方程采用第 1.3.1 节规定的质量中心线作为基础导管中心线。单位参考长度的线动量平衡为 |
| `eq:rod-1-39` | 1.39 | 其中 |
| `eq:rod-1-40` | 1.40 | 以中心线为矩心的角动量平衡写为 |
| `eq:rod-1-41` | 1.41 | 其中 |
| `eq:rod-1-42` | 1.42 | 利用 \dot{R} = R\widehat{\omega}，可得展开形式 |
| `eq:rod-1-43` | 1.43 | 在包围磁性导管微段的空气或真空区域中，Maxwell 应力张量写为Jackson1998Electrodynamics,Abbott2020MagneticRobotics |
| `eq:rod-1-44` | 1.44 | 其中，B 为磁感应强度，\mu_{0} 为真空磁导率。对参考长度为 \Delta S 的微段，单位参考长度磁力和关于中心线的磁力矩分别定义为 |
| `eq:rod-1-45` | 1.45 |  |
| `eq:rod-1-46` | 1.46 | 当磁性微段可由磁偶极近似描述时，设材料坐标系中的单位参考长度磁矩为 \mu_{0}^{b}(S)，空间磁矩为Jackson1998Electrodynamics,Abbott2020MagneticR |
| `eq:rod-1-47` | 1.47 | 给定外磁场 B\left( r,t \right) 时，磁势能可写为 |
| `eq:rod-1-48` | 1.48 | 相应磁力和磁力矩为 |
| `eq:rod-1-49` | 1.49 | 设流体速度为 v_{f}\left( r,t \right)，流体质点加速度为 |
| `eq:rod-1-50` | 1.50 | 定义流体相对于导管的速度 |
| `eq:rod-1-51` | 1.51 | 若仅保留相对于当前中心线的法向作用，定义 |
| `eq:rod-1-52` | 1.52 | 工程 Morison 验证分支可写为Morison1950,Newman1977MarineHydrodynamics,Faltinsen1990SeaLoads |
| `eq:rod-1-53` | 1.53 | 其中 |
| `eq:rod-1-54` | 1.54 |  |
| `eq:rod-1-55` | 1.55 |  |
| `eq:rod-1-56` | 1.56 | 为将构形相关附加质量纳入完整惯性结构，理论主线改由速度型附加流体惯性泛函定义。令Newman1977MarineHydrodynamics,Faltinsen1990SeaLoads |
| `eq:rod-1-57` | 1.57 | 并取 |
| `eq:rod-1-58` | 1.58 | 其对应惯性作用由泛函 Euler--Lagrange 导数 |
| `eq:rod-1-59` | 1.59 | 统一产生。冻结 P_{\bot} 时，主项为 |
| `eq:rod-1-60` | 1.60 | 而 P_{\bot} 的构形变化及流场的空间变化还会产生附加几何项。启用 T_{A} 的理论主线时，右端显式流体加速度输入仅保留纯 Froude--Krylov 项 |
| `eq:rod-1-61` | 1.61 | 并取 |
| `eq:rod-1-62` | 1.62 | 对于二次拖曳，定义非负的瞬时状态相关系数 |
| `eq:rod-1-63` | 1.63 | 则拖曳力必须按被动耗散核与背景流输入排他分解为 |
| `eq:rod-1-64` | 1.64 | 其中只有被动核对导管机械能具有确定耗散号： |
| `eq:rod-1-65` | 1.65 | 而 {\dot{r}}^{T}f_{drag,flow} 一般不定号，应进入流场输入端口。完整拖曳还满足相对运动被动性恒等式 |
| `eq:rod-1-66` | 1.66 | 若需要考虑流体对截面自转的阻尼，可另外引入单位参考长度流体力矩，例如 |
| `eq:rod-1-67` | 1.67 | 设导管表面与血管壁之间的间隙函数为 g(S,t)，接触判定阈值为 g_{0}。定义侵入量 |
| `eq:rod-1-68` | 1.68 | 为同时表示 Hertz 弹性、法向冲击耗散和正则化摩擦，令 {\delta}_{c} 表示接触点侵入量的物质时间导数。接触激活 \delta_{c} > 0 时，法向力取为Johnson1985Con |
| `eq:rod-1-69` | 1.69 | 当上述表达式为负或 \delta_{c} = 0 时，规定 f_{n} = 0；这等价于对法向力采用非负截断，从而避免未接触和分离阶段产生非物理拉力。切向摩擦力和总接触力分别为 |
| `eq:rod-1-70` | 1.70 |  |
| `eq:rod-1-71` | 1.71 | 若接触力作用点相对于中心线的偏置矢量为 \rho_{c}，则接触力矩为 |
| `eq:rod-1-72` | 1.72 | 若空间站内存在残余加速度 g_{res}(t)，则单位参考长度残余重力为 |
| `eq:rod-1-73` | 1.73 | 在理想微重力近似下，取 |
| `eq:rod-1-74` | 1.74 | 将运动学、平衡方程和本构关系统一整理，得到基础杆体的几何精确系统： |
| `eq:rod-1-75` | 1.75 | 并满足相容条件 |
| `eq:rod-1-76` | 1.76 | 取中心线虚位移 \deltar，并以材料虚转角 \eta 表示姿态变分： |
| `eq:rod-1-77` | 1.77 | 对应的空间虚转角为 |
| `eq:rod-1-78` | 1.78 | 由应变定义得到 |
| `eq:rod-1-79` | 1.79 |  |
| `eq:rod-1-80` | 1.80 | 内部虚功为 |
| `eq:rod-1-81` | 1.81 | 代入应变变分并对空间导数分部积分，得到 |
| `eq:rod-1-82` | 1.82 | 其中 |
| `eq:rod-1-83` | 1.83 |  |
| `eq:rod-1-84` | 1.84 | 其中，材料形式的转动平衡项满足 |
| `eq:rod-1-85` | 1.85 | 基础杆体的惯性虚功为 |
| `eq:rod-1-86` | 1.86 | 若采用第 1.4.4 节的能量一致附加质量，附加惯性虚功写为 |
| `eq:rod-1-87` | 1.87 | 其中 \langle \cdot , \cdot \rangle 表示沿杆长的对偶配对。若存在偏心附加部件，其惯性虚功由对应刚体动能 T_{e} 的 Euler---Lagrange 导数给出。因此总 |
| `eq:rod-1-88` | 1.88 | 外部分布载荷虚功为 |
| `eq:rod-1-89` | 1.89 | 其中 f_{ext,rem} 不再包含已经通过 T_{A} 计入的附加惯性；在能量一致流体主线中，流体部分仅保留 f_{FK}、拖曳及其他未由 T_{A} 表示的输入。由于 \eta_{s} = R\ |
| `eq:rod-1-90` | 1.90 | 根据 D'Alembert 原理，任意满足本质边界条件的 \deltar 和 \eta 均满足 |
| `eq:rod-1-91` | 1.91 | 展开后得到完整平移---转动联合弱形式： |
| `eq:rod-1-92` | 1.92 | 分部积分产生的自然边界项为 |
| `eq:rod-1-93` | 1.93 | 在端点 S = S_{e} 上，可以指定以下两类边界条件之一： |
| `eq:rod-1-94` | 1.94 |  |
| `eq:rod-1-95` | 1.95 | 完整动力学初边值问题还需给定初始条件 |
| `eq:rod-1-96` | 1.96 |  |
| `eq:rod-1-97` | 1.97 | 对于细长导管，可施加可伸长 Kirchhoff 无剪切约束 |
| `eq:rod-1-98` | 1.98 | 于是 |
| `eq:rod-1-99` | 1.99 | 基础杆体结构机械能定义为 |
| `eq:rod-1-100` | 1.100 | 若存在偏心附加部件，加入其动能 T_{e}。在静止流场 v_{f} = 0 且 m_{A} 不显含时间的能量一致附加质量分支中，定义总动能 |
| `eq:rod-1-101` | 1.101 | 若磁作用、无摩擦接触或残余重力可由势能表示，则定义 |
| `eq:rod-1-102` | 1.102 | 以及扩展机械能 |
| `eq:rod-1-103` | 1.103 | 将平动方程与 \dot{r} 点乘，将转动方程与空间角速度 \omega_{s} 点乘并积分，可写成 |
| `eq:rod-1-104` | 1.104 | 其中边界功率为 |
| `eq:rod-1-105` | 1.105 | 将所有保守外载荷并入 V 后，得到 |
| `eq:galerkin-2-1` | 2.1 | 取满足平移本质边界条件的矩阵值基函数 N(S)，中心线近似写为 |
| `eq:galerkin-2-2` | 2.2 | 其中，a(t) \in R^{n_{a}} 为平移广义坐标。于是 |
| `eq:galerkin-2-3` | 2.3 | 设参考姿态为 R_{0}(S)。在参考姿态附近采用旋转向量的指数坐标： |
| `eq:galerkin-2-4` | 2.4 |  |
| `eq:galerkin-2-5` | 2.5 | 其中，b(t) \in R^{n_{b}} 为转动广义坐标，\Psi(S) 为满足转动本质边界条件的矩阵值基函数。定义 |
| `eq:galerkin-2-6` | 2.6 | 因此 |
| `eq:galerkin-2-7` | 2.7 | 令 \theta = \parallel \theta_{h} \parallel。旋转向量的右 Jacobian 定义为 |
| `eq:galerkin-2-8` | 2.8 | 当 \theta \rightarrow 0 时，按连续延拓有 |
| `eq:galerkin-2-9` | 2.9 | 由指数映射的精确微分关系，材料角速度为 |
| `eq:galerkin-2-10` | 2.10 | 定义角速度矩阵 |
| `eq:galerkin-2-11` | 2.11 | 则 |
| `eq:galerkin-2-12` | 2.12 | 定义总广义坐标 |
| `eq:galerkin-2-13` | 2.13 | 平移虚位移为 |
| `eq:galerkin-2-14` | 2.14 | 由 \deltaR_{h} = R_{h}\widehat{\eta_{h}}，材料虚转角满足 |
| `eq:galerkin-2-15` | 2.15 | 为使 q = 0 对应无应力参考构形，参考中心线、参考姿态和参考应变必须满足相容关系 |
| `eq:galerkin-2-16` | 2.16 |  |
| `eq:galerkin-2-17` | 2.17 | 离散剪切---拉伸应变为 |
| `eq:galerkin-2-18` | 2.18 | 其虚变分可写为 |
| `eq:galerkin-2-19` | 2.19 | 从而存在应变---广义坐标矩阵 B_{\nu}\left( S,q \right)，使得 |
| `eq:galerkin-2-20` | 2.20 | 显式写为 |
| `eq:galerkin-2-21` | 2.21 | 定义参考姿态的曲率---扭转矢量 |
| `eq:galerkin-2-22` | 2.22 | 由 R_{h} = R_{0}E_{h} 得 |
| `eq:galerkin-2-23` | 2.23 | 因此，离散曲率---扭转矢量为 |
| `eq:galerkin-2-24` | 2.24 | 其中 |
| `eq:galerkin-2-25` | 2.25 | 相应虚变分满足 |
| `eq:galerkin-2-26` | 2.26 | 因此存在 B_{\kappa}\left( S,q \right)，使得 |
| `eq:galerkin-2-27` | 2.27 | 将离散应变代入第 1 章的势能，可将离散内部势能分解为 |
| `eq:galerkin-2-28` | 2.28 | 其中 |
| `eq:galerkin-2-29` | 2.29 |  |
| `eq:galerkin-2-30` | 2.30 | 离散内部广义力为 |
| `eq:galerkin-2-31` | 2.31 | 利用虚功表达，可写为 |
| `eq:galerkin-2-32` | 2.32 | 离散材料点位置为 |
| `eq:galerkin-2-33` | 2.33 | 其速度为 |
| `eq:galerkin-2-34` | 2.34 | 定义材料点速度矩阵 |
| `eq:galerkin-2-35` | 2.35 | 则 |
| `eq:galerkin-2-36` | 2.36 | 离散动能为 |
| `eq:galerkin-2-37` | 2.37 | 代入速度矩阵，得到 |
| `eq:galerkin-2-38` | 2.38 | 其中 |
| `eq:galerkin-2-39` | 2.39 | 按照 q = \left( a^{T},b^{T} \right)^{T}，写成 |
| `eq:galerkin-2-40` | 2.40 | 利用第 1 章定义的 \mu,c_{\rho},J_{c}，各分块为 |
| `eq:galerkin-2-41` | 2.41 |  |
| `eq:galerkin-2-42` | 2.42 |  |
| `eq:galerkin-2-43` | 2.43 |  |
| `eq:galerkin-2-44` | 2.44 | 即 |
| `eq:galerkin-2-45` | 2.45 | 与第 1 章保持一致，基础导管中心线取为各截面的质量中心线，因此分布杆体满足 |
| `eq:galerkin-2-46` | 2.46 | 从而杆体本身的平移---转动交叉块消失： |
| `eq:galerkin-2-47` | 2.47 | 此时 |
| `eq:galerkin-2-48` | 2.48 | 若磁性头端、传感器或其他附加部件的质心相对于中心线存在偏置，则其动能应单独加入。设附加部件质心位置为 |
| `eq:galerkin-2-49` | 2.49 | 其质量为 m_{e}、材料坐标转动惯量为 J_{e}，则 |
| `eq:galerkin-2-50` | 2.50 | 令 B_{e}\left( q \right) 为该部件速度关于 \dot{q} 的映射，则 |
| `eq:galerkin-2-51` | 2.51 | 当 \parallel \theta_{h} \parallel \ll 1 时，若仅保留 |
| `eq:galerkin-2-52` | 2.52 | 则 |
| `eq:galerkin-2-53` | 2.53 | 定义联合平移速度矩阵 |
| `eq:galerkin-2-54` | 2.54 | 使得 {\dot{r}}_{h} = N_{q}\dot{q}。令 |
| `eq:galerkin-2-55` | 2.55 | 第 1 章的附加流体惯性泛函离散为（静止流场下即为附加动能） |
| `eq:galerkin-2-56` | 2.56 | 展开可写为 |
| `eq:galerkin-2-57` | 2.57 | 其中 |
| `eq:galerkin-2-58` | 2.58 |  |
| `eq:galerkin-2-59` | 2.59 |  |
| `eq:galerkin-2-60` | 2.60 | 因此，将结构动能、偏心部件动能和附加流体项统一记为速度型惯性泛函 |
| `eq:galerkin-2-61` | 2.61 | 其关于广义速度的 Hessian 给出总有效质量---惯性矩阵 |
| `eq:galerkin-2-62` | 2.62 | 由动能 Hessian 的定义可知 |
| `eq:galerkin-2-63` | 2.63 | 若材料与附加质量参数为正，姿态坐标位于 J_{r} 非奇异的局部坐标域内，且联合速度映射对任意非零广义速度均不会在几乎处处同时退化，即 |
| `eq:galerkin-2-64` | 2.64 | 则 |
| `eq:galerkin-2-65` | 2.65 | 将有限维近似代入第 1 章的总惯性虚功，有 |
| `eq:galerkin-2-66` | 2.66 | 对于静止流场，或在明确将规定流场交叉项的完整 Euler--Lagrange 作用划入 Q_{flow} 后选取的自治保守惯性骨架， |
| `eq:galerkin-2-67` | 2.67 | 惯性广义力可整理为 |
| `eq:galerkin-2-68` | 2.68 | 一般规定流场下，T_{h} 还包含 - {\dot{q}}^{T}b_{A} + c_{A}，对应附加项记为 g_{f}\left( q,\dot{q},t \right)。因此统一写成 |
| `eq:galerkin-2-69` | 2.69 | 离散内部虚功为 |
| `eq:galerkin-2-70` | 2.70 | 因此 |
| `eq:galerkin-2-71` | 2.71 | 首先将仍位于外力端口中的分布载荷作排他分解 |
| `eq:galerkin-2-72` | 2.72 | 其中保守部分在第 2.5.5 节通过外势能处理，只有非保守部分直接投影到右端。空间分布力矩先转换为材料坐标 l_{nc}^{b} = R_{h}^{T}l_{nc}，从而非保守分布广义力为 |
| `eq:galerkin-2-73` | 2.73 | 对只作用于中心线平移速度的法向二次拖曳，定义联合速度矩阵 |
| `eq:galerkin-2-74` | 2.74 | 其一致广义力投影为 |
| `eq:galerkin-2-75` | 2.75 | 其中 |
| `eq:galerkin-2-76` | 2.76 | 对任意 y \in R^{n}，有 |
| `eq:galerkin-2-77` | 2.77 | 第 1 章的边界虚功为 |
| `eq:galerkin-2-78` | 2.78 | 代入有限维虚变量，得到 |
| `eq:galerkin-2-79` | 2.79 | 若保守分布载荷和保守边界载荷存在离散外势能 V_{ext,h}\left( q,t \right)，则其总保守广义力为 |
| `eq:galerkin-2-80` | 2.80 | 并定义 |
| `eq:galerkin-2-81` | 2.81 | 非保守广义力统一记为 |
| `eq:galerkin-2-82` | 2.82 | 对第 2.4.6 节的速度型惯性泛函 |
| `eq:galerkin-2-83` | 2.83 | 定义广义动量 |
| `eq:galerkin-2-84` | 2.84 | 因此，一般规定流场下不能无条件写成 p = M\dot{q}。只有在静止流场中，或在人为选取的自治保守骨架中将 b_{A} 的完整作用移入 Q_{flow} 后，才定义骨架动量 |
| `eq:galerkin-2-85` | 2.85 | 对纯二次速度部分求 Euler---Lagrange 导数，得到 |
| `eq:galerkin-2-86` | 2.86 | 其中 |
| `eq:galerkin-2-87` | 2.87 | 定义 |
| `eq:galerkin-2-88` | 2.88 | 则 |
| `eq:galerkin-2-89` | 2.89 | 由 - {\dot{q}}^{T}b_{A} + c_{A} 得到 |
| `eq:galerkin-2-90` | 2.90 | 这里 {\dot{b}}_{A} 为沿轨道的全导数。于是总惯性作用为 |
| `eq:galerkin-2-91` | 2.91 | 若在特定小转角、无偏心、冻结法向投影和固定附加质量近似下有 |
| `eq:galerkin-2-92` | 2.92 | 严格 Kirchhoff 模型要求MarsdenRatiu1999MechanicsSymmetry,HairerLubichWanner2006GNI |
| `eq:galerkin-2-93` | 2.93 | 将所有离散约束写成 |
| `eq:galerkin-2-94` | 2.94 | 定义约束 Jacobian |
| `eq:galerkin-2-95` | 2.95 | 引入拉格朗日乘子 \lambda_{c}，约束反力对应的广义力为 |
| `eq:galerkin-2-96` | 2.96 | 完整受约束离散系统写为 |
| `eq:galerkin-2-97` | 2.97 | 将惯性项、内部保守力、保守外势、非保守分布载荷和边界载荷组装，得到 |
| `eq:galerkin-2-98` | 2.98 | 若把规定流场交叉项整体移至输入端口，并将耗散与控制输入分开，可写为 |
| `eq:galerkin-2-99` | 2.99 | 严格 Kirchhoff 无剪切模型最终写为 |
| `eq:galerkin-2-100` | 2.100 |  |
| `eq:galerkin-2-101` | 2.101 | 在静止流场 b_{A} = 0 且 c_{A} = 0，或已将规定流场交叉项完整移入 Q_{flow} 后选取的自治保守骨架中，定义 |
| `eq:galerkin-2-102` | 2.102 | 由于 g_{M} 由完整二次动能的 Euler---Lagrange 导数产生，有 |
| `eq:galerkin-2-103` | 2.103 | 对全局方程左乘 {\dot{q}}^{T}，得到 |
| `eq:galerkin-2-104` | 2.104 | 若将规定流场交叉作用的完整 Euler--Lagrange 贡献定义为流场输入的一部分，则 |
| `eq:galerkin-2-105` | 2.105 | 这里 Q_{diss} 只含拆分后的被动耗散核，满足 {\dot{q}}^{T}Q_{diss} \leq 0；Q_{flow} 同时收纳 Q_{drag,flow}、Froude--Krylov 输 |
| `eq:galerkin-2-106` | 2.106 | 因此 |
| `eq:galerkin-2-107` | 2.107 | 在非线性求解或局部线性化中，内部一致切线矩阵定义为 |
| `eq:galerkin-2-108` | 2.108 | 采用耗散---输入分解 |
| `eq:galerkin-2-109` | 2.109 | 这里的``静态平衡构形''要求系统在 t = t_{e} 处已冻结显式时间输入、控制参数和规定流场，或本身为自治系统。若磁场或流场为周期驱动，应围绕周期轨道采用 Floquet 线性化，而不能直接使用 |
| `eq:galerkin-2-110` | 2.110 | 通常 Q_{diss}\left( q,0 \right) = 0。令 q = q_{e} + \eta，忽略二阶及以上扰动项。对无约束系统有 |
| `eq:galerkin-2-111` | 2.111 | 其中 |
| `eq:galerkin-2-112` | 2.112 |  |
| `eq:galerkin-2-113` | 2.113 |  |
| `eq:galerkin-2-114` | 2.114 | 在纯保守、无边界随形载荷的情形下，直接化为 |
| `eq:galerkin-2-115` | 2.115 | CHNN 和 KAM 分析必须基于固定维数的有限维系统，不能长期停留在抽象模态数 n。对候选截断阶数 n = 1,2,\ldots,n_{max}，至少计算：前若干固有频率、末端位移、结构能量、扭转响 |
| `eq:galerkin-2-116` | 2.116 | 定义平移 Gram 矩阵 |
| `eq:galerkin-2-117` | 2.117 | 则 COMSOL 中心线场投影为 |
| `eq:galerkin-2-118` | 2.118 | 姿态不能直接对 Euler 角分量线性投影。应先计算相对旋转的对数坐标 |
| `eq:galerkin-2-119` | 2.119 | 再令 |
| `eq:galerkin-2-120` | 2.120 | 经联合 Galerkin 离散和第 3 章的一致 Legendre 后处理后，数值实现应输出统一的有限维状态、能量、端口和表示标签： |
| `eq:galerkin-2-121` | 2.121 | 第 3 章应据此构造两类不混用的数据对象。自治骨架数据为 |
| `eq:galerkin-2-122` | 2.122 | 精确非自治数据为 |
| `eq:galerkin-2-123` | 2.123 | 每个样本必须同时保存 |
| `eq:galerkin-2-124` | 2.124 | 用于保守 CHNN 与统计学习---KAM 的数据集限定为 |
| `eq:galerkin-2-125` | 2.125 | 开放端口训练集为 |
| `eq:galerkin-2-126` | 2.126 | 高保真对照集为 |
| `eq:galerkin-2-127` | 2.127 | 本章直接从完整平移---转动弱形式出发，采用中心线展开和截面姿态指数映射构造联合 Galerkin 近似。参考构形与参考应变的相容条件、初始条件、接触活动集以及保守---非保守载荷的排他记账均已明确； |
| `eq:galerkin-2-128` | 2.128 | 对于一般规定流场，广义动量严格为 |
| `eq:hamiltonian-3-1` | 3.1 | 第 2 章通过中心线位置与截面姿态的联合 Galerkin 投影得到 |
| `eq:hamiltonian-3-2` | 3.2 | 有限剪切刚度 Cosserat 几何精确母模型的离散动力学可写为 |
| `eq:hamiltonian-3-3` | 3.3 | 质量---惯性矩阵 |
| `eq:hamiltonian-3-4` | 3.4 | 有限维 Hamilton 表述采用如下推导链：MarsdenRatiu1999MechanicsSymmetry,Arnold1989ClassicalMechanics |
| `eq:hamiltonian-3-5` | 3.5 | 设外部驱动由参数 \lambda(t) 控制，选择参考参数 \bar{\lambda}。将离散势能写成 |
| `eq:hamiltonian-3-6` | 3.6 | 并规定 |
| `eq:hamiltonian-3-7` | 3.7 | 参考参数冻结后不再残留显含时间项，因此 |
| `eq:hamiltonian-3-8` | 3.8 | 在自治、无端口骨架中，Lagrangian 为 |
| `eq:hamiltonian-3-9` | 3.9 | 与 q 共轭的正则动量定义为MarsdenRatiu1999MechanicsSymmetry,Arnold1989ClassicalMechanics |
| `eq:hamiltonian-3-10` | 3.10 | 由此得到正则动量与广义速度之间的关系 |
| `eq:hamiltonian-3-11` | 3.11 | 速度 Hessian 为MarsdenRatiu1999MechanicsSymmetry,Arnold1989ClassicalMechanics |
| `eq:hamiltonian-3-12` | 3.12 | 若联合基函数不存在速度冗余，材料密度、转动惯量和附加质量参数满足物理正性，并且在所考察构形域内 |
| `eq:hamiltonian-3-13` | 3.13 | Hamiltonian 定义为 |
| `eq:hamiltonian-3-14` | 3.14 | 代入 \dot{q} = M^{- 1}p_{0} 得 |
| `eq:hamiltonian-3-15` | 3.15 | Cosserat 杆的离散内势由第 2 章的应变能泛函确定。定义 |
| `eq:hamiltonian-3-16` | 3.16 | 相对于参考构形 q_{*}，保守势能也可写成路径无关线积分 |
| `eq:hamiltonian-3-17` | 3.17 | 由此，保守势能可以表示为恢复力沿构形路径的线积分。一般情况下，不能无条件令 f_{int} = K_{tan}\left( q \right)q；仅在线性化邻域或恢复力确实具有该因子分解时，才可采用二 |
| `eq:hamiltonian-3-18` | 3.18 | 定义相空间变量和标准辛矩阵 |
| `eq:hamiltonian-3-19` | 3.19 | 自治保守骨架满足 |
| `eq:hamiltonian-3-20` | 3.20 | 即 |
| `eq:hamiltonian-3-21` | 3.21 | 相应标准 Poisson 括号为 |
| `eq:hamiltonian-3-22` | 3.22 | 对第 i 个构形分量，有 |
| `eq:hamiltonian-3-23` | 3.23 | 因此动量方程为 |
| `eq:hamiltonian-3-24` | 3.24 | 利用矩阵逆的导数恒等式 |
| `eq:hamiltonian-3-25` | 3.25 | 可得 |
| `eq:hamiltonian-3-26` | 3.26 | 由 |
| `eq:hamiltonian-3-27` | 3.27 | 以及前述 Hamilton 动量方程，得到 |
| `eq:hamiltonian-3-28` | 3.28 | 其中 |
| `eq:hamiltonian-3-29` | 3.29 | 由于 J 反对称且 H_{cons} 不显含时间， |
| `eq:hamiltonian-3-30` | 3.30 | 故 |
| `eq:hamiltonian-3-31` | 3.31 | 非保守广义力通过 Hamilton 动量方程的右端统一引入： |
| `eq:hamiltonian-3-32` | 3.32 | 根据第 1、2 章建立的排他功率记账，写成 |
| `eq:hamiltonian-3-33` | 3.33 | 若某一工况下非保守力可等效写为 |
| `eq:hamiltonian-3-34` | 3.34 | 则由 \dot{q} = \nabla_{p_{0}}H_{cons} 得 |
| `eq:hamiltonian-3-35` | 3.35 | 若磁力和弹性接触力未写入势能，则可令 |
| `eq:hamiltonian-3-36` | 3.36 | 对自治 Hamiltonian，有MarsdenRatiu1999MechanicsSymmetry,Zhong2020Dissipative,Desai2021PHNN |
| `eq:hamiltonian-3-37` | 3.37 | 代入受迫正则方程，辛结构项相消，得到 |
| `eq:hamiltonian-3-38` | 3.38 | 在第 3.4.2 节的等效阻尼条件下，有 |
| `eq:hamiltonian-3-39` | 3.39 | 其中 |
| `eq:hamiltonian-3-40` | 3.40 | 定义 |
| `eq:hamiltonian-3-41` | 3.41 | 则自治骨架上的完整受迫---耗散系统写为 |
| `eq:hamiltonian-3-42` | 3.42 | 第 1、2 章的能量一致规定流场表述会产生速度线性项。一般离散 Lagrangian 为MarsdenRatiu1999MechanicsSymmetry,Arnold1989ClassicalMec |
| `eq:hamiltonian-3-43` | 3.43 | 由定义 |
| `eq:hamiltonian-3-44` | 3.44 | 得到 |
| `eq:hamiltonian-3-45` | 3.45 | Legendre 变换给出 |
| `eq:hamiltonian-3-46` | 3.46 | 其中 - c_{A} 是 Legendre 变换的直接结果。若 M = M\left( q \right) 不显含时间，则 |
| `eq:hamiltonian-3-47` | 3.47 |  |
| `eq:hamiltonian-3-48` | 3.48 | 以及固定 \left( q,p \right) 时 |
| `eq:hamiltonian-3-49` | 3.49 | 无外部端口时仍满足标准非自治正则方程 |
| `eq:hamiltonian-3-50` | 3.50 | 由 |
| `eq:hamiltonian-3-51` | 3.51 | 可恢复 |
| `eq:hamiltonian-3-52` | 3.52 | 其中 |
| `eq:hamiltonian-3-53` | 3.53 | 保留 b_{A},c_{A} 时，定义MarsdenRatiu1999MechanicsSymmetry,Arnold1989ClassicalMechanics |
| `eq:hamiltonian-3-54` | 3.54 | 完整受迫系统为 |
| `eq:hamiltonian-3-55` | 3.55 | 在骨架---端口表示中，取 |
| `eq:hamiltonian-3-56` | 3.56 | 并定义 |
| `eq:hamiltonian-3-57` | 3.57 | 则规定流场交叉项整体转入端口： |
| `eq:hamiltonian-3-58` | 3.58 | 两种表示产生相同的构形轨道，但必须成套使用： |
| `eq:hamiltonian-3-59` | 3.59 | 精确表示满足 |
| `eq:hamiltonian-3-60` | 3.60 | 骨架---端口表示满足 |
| `eq:hamiltonian-3-61` | 3.61 | 指数坐标是 SO(3) 上的局部坐标。为使用标准正则变量，可在当前坐标图内要求对任意 S \in \lbrack 0,L\rbrack 均有 |
| `eq:hamiltonian-3-62` | 3.62 | 第 1 章以有限剪切 Cosserat 杆作为几何精确母模型，为与 Kirchhoff 细长导管假设保持一致，并向第 4、5 章提供无冗余的正则状态，主结构学习与 KAM 分支优先采用严格无剪切约束的 |
| `eq:hamiltonian-3-63` | 3.63 | 若 G 在研究域内保持常秩，则约束集合局部构成光滑流形。全坐标下的方程为 |
| `eq:hamiltonian-3-64` | 3.64 | 理想约束反力满足 {\dot{q}}^{T}G^{T}\lambda_{c} = 0。为获得可直接用于 CHNN 与标准辛分析的正则系统，取局部独立坐标 q = \chi\left( y \right |
| `eq:hamiltonian-3-65` | 3.65 | 后续复值表示不能直接把具有不同量纲和不同尺度的 q 与 p 相加。选定稳定参考状态 \left( q_{*},p_{*} \right)、坐标尺度矩阵 S_{q}、动量尺度矩阵 S_{p}、时间尺度  |
| `eq:hamiltonian-3-66` | 3.66 | 定义 |
| `eq:hamiltonian-3-67` | 3.67 | 由上述尺度相容条件可得 |
| `eq:hamiltonian-3-68` | 3.68 | 故无量纲变量仍满足标准正则 Hamilton 方程。随后定义复坐标MarsdenRatiu1999MechanicsSymmetry,Arnold1989ClassicalMechanics |
| `eq:hamiltonian-3-69` | 3.69 | 第 3 章向第 4 章提供解析物理基线 |
| `eq:hamiltonian-3-70` | 3.70 | 第 4 章的实值读出宜采用物理残差形式 |
| `eq:hamiltonian-3-71` | 3.71 | 在冻结驱动参数 \lambda(t) \equiv \overline{\lambda} 的自治骨架表示中， |
| `eq:hamiltonian-3-72` | 3.72 | 且 |
| `eq:hamiltonian-3-73` | 3.73 | 第 4 章应分别参数化或监督各端口，而不是让一个无结构残差同时吸收全部物理作用： |
| `eq:hamiltonian-3-74` | 3.74 | 一般规定流场下使用 p = M\dot{q} - b_{A} 和相应非自治 Hamiltonian；自治骨架使用 p_{0} = M\dot{q}。两类数据必须由 representation 标签区 |
| `eq:hamiltonian-3-75` | 3.75 |  |
| `eq:hamiltonian-3-76` | 3.76 | 后续 KAM 分析以自治保守骨架 H_{cons}\left( q,p_{0} \right) 为起点，但不预设其整体可积。选择平衡点 \left( q_{*},0 \right)，要求 |
| `eq:hamiltonian-3-77` | 3.77 | 求解广义特征值问题 |
| `eq:hamiltonian-3-78` | 3.78 | 并取模态矩阵 \Phi 满足 |
| `eq:hamiltonian-3-79` | 3.79 | 线性正则变换 |
| `eq:hamiltonian-3-80` | 3.80 | 将二次 Hamiltonian 化为 |
| `eq:hamiltonian-3-81` | 3.81 | 其中 |
| `eq:hamiltonian-3-82` | 3.82 | 仅有二次项时频率与作用量无关，故 |
| `eq:hamiltonian-3-83` | 3.83 | 若 H_{cons} 在研究邻域内解析（或满足所选有限光滑 KAM 定理的正则性），且线性频率在所需阶数内避开低阶共振，则可构造有限阶 Birkhoff 正规形HairerLubichWanner20 |
| `eq:hamiltonian-3-84` | 3.84 | 定义 |
| `eq:hamiltonian-3-85` | 3.85 | 最低非平凡情形常有 |
| `eq:hamiltonian-3-86` | 3.86 | 此时 Kolmogorov 非退化条件在所考察作用量域内要求 |
| `eq:hamiltonian-3-87` | 3.87 | 在固定复邻域或 Sobolev 域 D 和统一函数范数 \parallel \cdot \parallel_{X\left( D \right)} 下，将无量纲 Hamiltonian 写成 |
| `eq:hamiltonian-3-88` | 3.88 | 并定义 |
| `eq:hamiltonian-3-89` | 3.89 | 为了使第 4 章的学习误差和第 5 章的辛离散误差真正进入同一数学链，所有误差必须在同一研究域和相容的函数范数中计量。连续 Hamiltonian 层首先定义 |
| `eq:hamiltonian-3-90` | 3.90 | 从而 |
| `eq:hamiltonian-3-91` | 3.91 | 离散层不无条件假设存在一个全局精确的``离散 Hamiltonian''。令 \Phi_{h}^{H} 表示 Hamiltonian H 的精确时间 h 流，令 F_{\lambda,h} 表示第 5 |
| `eq:hamiltonian-3-92` | 3.92 | 由三角不等式有 |
| `eq:hamiltonian-3-93` | 3.93 | 在向量场关于 Hamiltonian 扰动局部 Lipschitz 且流在所考察时间内保持于同一域的条件下，后两项可分别由 C_{learn}(h)\delta_{learn} 和 C_{model} |
| `eq:hamiltonian-3-94` | 3.94 | 对自治保守分支，由结构保持积分器得到一步映射 |
| `eq:hamiltonian-3-95` | 3.95 | 第 5 章首先验证 F_{h} 是否为精确辛映射，再使用 Shang 的辛映射／辛算法 KAM 条件和 Haro 等人的参数化方法FengQin2010,Shang1999KAMAlgorithms, |
| `eq:hamiltonian-3-96` | 3.96 | 数值近似 K_{N} 的不变性残差为 |
| `eq:hamiltonian-3-97` | 3.97 | 对完整数据向量场，必须先扣除已知保守主体和已知端口： |
| `eq:hamiltonian-3-98` | 3.98 | 第 3 章将 Kirchhoff 一致 COMSOL 分支视为主训练动力学 X_{K}，将 Weak Form、Timoshenko 或实体模型视为高保真对照 X_{HF}。定义配对工况下的模型差异 |
| `eq:hamiltonian-3-99` | 3.99 | 该差异不能整体加入 Hamiltonian。首先检验其在正则变量中的保守闭合性；若存在实值 \Delta H_{HF} 使 |
| `eq:hamiltonian-3-100` | 3.100 | 则该部分可进入第 4 章的保守修正头。若某一动量端口满足 |
| `eq:hamiltonian-3-101` | 3.101 | 则可进入耗散修正头。其余不满足闭合性、功率符号或光滑性条件的部分保留为一般模型残差 r_{HF}。因此 |
| `eq:hamiltonian-3-102` | 3.102 | 由上述推导可得到后续结构学习与稳定性分析所需的三个接口： |
| `eq:hamiltonian-3-103` | 3.103 |  |
| `eq:hamiltonian-3-104` | 3.104 |  |
| `eq:hamiltonian-3-105` | 3.105 | 基于完整平移---截面姿态联合坐标，自治保守骨架的正则动量与 Hamiltonian 为 |
| `eq:hamiltonian-3-106` | 3.106 | 以及受迫---耗散正则方程 |
| `eq:hamiltonian-3-107` | 3.107 | 一般规定流场下，正则动量和 Hamiltonian 分别推广为 |
| `eq:chnn-4-1` | 4.1 | 设约化后的无量纲正则状态为 |
| `eq:chnn-4-2` | 4.2 | 并定义复坐标 |
| `eq:chnn-4-3` | 4.3 | COMSOL 数据同时携带 |
| `eq:chnn-4-4` | 4.4 | 标准 HNN 通过实值标量 Hamiltonian 的梯度生成保守向量场Greydanus2019HNN。本文采用 |
| `eq:chnn-4-5` | 4.5 | 其中 {H}_{phys} 由第 3 章的质量矩阵、Cosserat／Kirchhoff 应变能、已确定的保守磁势和固定活动集内的弹性接触势给出；网络只学习材料参数偏差、Galerkin 截断造成的保 |
| `eq:chnn-4-6` | 4.6 | 令 |
| `eq:chnn-4-7` | 4.7 | 理论主分支采用关于实部、虚部足够光滑的激活函数，例如 |
| `eq:chnn-4-8` | 4.8 | 为使复值主干既保留幅值---相位耦合的结构偏置，又具有与一般实网络相容的表达能力，采用广义复线性层。令 |
| `eq:chnn-4-9` | 4.9 | 其中 z = x + iy、W = A + iB、V = C + iD、b = b_{R} + ib_{I}。于是 |
| `eq:chnn-4-10` | 4.10 |  |
| `eq:chnn-4-11` | 4.11 |  |
| `eq:chnn-4-12` | 4.12 |  |
| `eq:chnn-4-13` | 4.13 | 存在唯一的 W,V,b 使广义复线性层与之完全等价，其显式构造为 |
| `eq:chnn-4-14` | 4.14 |  |
| `eq:chnn-4-15` | 4.15 |  |
| `eq:chnn-4-16` | 4.16 | 考虑复值标量表示 |
| `eq:chnn-4-17` | 4.17 | 自治骨架上的完整结构化模型写为 |
| `eq:chnn-4-18` | 4.18 | 其中 |
| `eq:chnn-4-19` | 4.19 | 各分支具有不同物理含义。 |
| `eq:chnn-4-20` | 4.20 | 保守训练集限定为 |
| `eq:chnn-4-21` | 4.21 | 开放端口训练集为 |
| `eq:chnn-4-22` | 4.22 | 当需要逐项复现本文联合弱形式时，采用 Weak Form PDE 或 Weak Contribution 输入试验函数、边界贡献和辅助变量COMSOLWeakFormPDE2025,COMSOLWea |
| `eq:chnn-4-23` | 4.23 | 对 D_{K}^{cons}，定义 |
| `eq:chnn-4-24` | 4.24 | 若已知物理 Hamiltonian，则增加能量修正监督 |
| `eq:chnn-4-25` | 4.25 | 定义端口残差 |
| `eq:chnn-4-26` | 4.26 | 能量平衡损失为 |
| `eq:chnn-4-27` | 4.27 | 耗散符号约束只施加于 {\widehat{Q}}_{diss,\mu}： |
| `eq:chnn-4-28` | 4.28 | 轨迹损失为 |
| `eq:chnn-4-29` | 4.29 | 加性规范损失取 |
| `eq:chnn-4-30` | 4.30 | 辛结构损失只作用于保守子映射 F_{h,\lambda}^{cons}： |
| `eq:chnn-4-31` | 4.31 | 为实现上述数学结构，本文构建了与统一接口对应的独立 CHNN 软件系统。该实现不把既有 HNN、CVNN 和 KAM--HNN 复现工程直接拼接，而是保留经单元测试核验的复值算子，并按照本文的正则状态 |
| `eq:chnn-4-32` | 4.32 |  |
| `eq:chnn-4-33` | 4.33 | 被动耗散头采用 |
| `eq:chnn-4-34` | 4.34 | 从而在代码结构层面保证 |
| `eq:chnn-4-35` | 4.35 | 第 3 章通过稳定平衡点、模态正则化和 Hamiltonian Birkhoff 正规形构造 |
| `eq:chnn-4-36` | 4.36 | 以下统计学习结论只针对保守训练集 D_{K}^{cons}。设 \Omega \subset R^{2d} 为有界、连通的 Lipschitz 区域，真实保守 Hamiltonian 为 H_{\st |
| `eq:chnn-4-37` | 4.37 | 把 Hamiltonian 头的全部复参数实化为 \vartheta \in \Theta = \lbrack - B,B\rbrack^{P}，记学习误差 |
| `eq:chnn-4-38` | 4.38 | 仅由状态导数不能识别 Hamiltonian 的绝对常数，因此在理论域上固定 |
| `eq:chnn-4-39` | 4.39 | 或使用已知能量锚点固定同一加性等价类代表。取统计指数 r > 2d，定义标量梯度损失 |
| `eq:chnn-4-40` | 4.40 | 对样本 S = \left( Z_{1},\ldots,Z_{N} \right)，定义归一化经验度量 |
| `eq:chnn-4-41` | 4.41 |  |
| `eq:chnn-4-42` | 4.42 | 当输入域和参数集有界、网络深度有限且激活的一阶、二阶导数在相关范围内有界时，该假设可在紧参数集上成立；L_{S} 一般随深度、宽度、权重界和导数界增长。 |
| `eq:chnn-4-43` | 4.43 | 由于参数集紧且参数到损失连续，上确界可取到。经验 Rademacher 复杂度定义为 |
| `eq:chnn-4-44` | 4.44 | 令 |
| `eq:chnn-4-45` | 4.45 | Dudley 熵积分给出Dudley1999UCLT |
| `eq:chnn-4-46` | 4.46 | 假设损失类在抽样前固定。由标准 Rademacher 统一泛化界，以至少 1 - \delta 的概率，对所有 \vartheta \in \Theta 同时有 |
| `eq:chnn-4-47` | 4.47 | 进一步假设 P_{Z} 关于 Lebesgue 测度具有密度 f_{Z}，且在 \Omega 上 |
| `eq:chnn-4-48` | 4.48 | 则在上述统一事件上 |
| `eq:chnn-4-49` | 4.49 | 由加性规范和 Poincaré 不等式，再由 r > 2d 时的 Morrey--Sobolev 嵌入AdamsFournier2003SobolevSpaces，得到： |
| `eq:chnn-4-50` | 4.50 | 设第 3 章已在局部作用量---角区域 |
| `eq:chnn-4-51` | 4.51 | 建立可积参考和坐标变换。若原始训练数据位于物理正则坐标，则必须把学习误差拉回 A，并把坐标变换及其逆的高阶导数界计入常数。取整数 s,\ell 与统计指数 r 满足 |
| `eq:chnn-4-52` | 4.52 | 令训练算法输出 \widehat{\vartheta}。除定理 4.2 的一阶统计证书外，另要求一个针对该训练输出的高阶证书：在概率至少 1 - \eta 的事件上， |
| `eq:chnn-4-53` | 4.53 | 该证书控制的必须是真实学习误差的高阶导数，而不只是网络自身导数的大小。由周期 Sobolev 嵌入，在两个事件的交集上 |
| `eq:chnn-4-54` | 4.54 | 其中可以取 |
| `eq:chnn-4-55` | 4.55 | 固定第 3 章构造并验证的可积参考 Hamiltonian h\left( I \right)。真实保守系统和学习系统分别写为 |
| `eq:chnn-4-56` | 4.56 | 其中 |
| `eq:chnn-4-57` | 4.57 | 因此，在同一 C^{\ell}\left( A \right) 范数下 |
| `eq:chnn-4-58` | 4.58 | 预先选定一个外部 KAM 定理。用 A_{KAM}(h,P) 表示该定理除扰动小性以外的全部结构假设，包括作用量---角区域、正则阶数、非退化类型、Diophantine 条件、边界距离和允许的扰动类 |
| `eq:chnn-4-59` | 4.59 | 在统一解析域 D_{\rho} 上定义 |
| `eq:chnn-4-60` | 4.60 | 令 \Phi_{h}^{0} 为 X_{0} 的精确时间-h 映射，\Psi_{h,\lambda} 为施加于学习 Hamiltonian 的 s_{a} 阶辛算法。若向量场及其一阶导数一致有界，且轨 |
| `eq:chnn-4-61` | 4.61 | 这里 h^{s_{a}} 来自局部算法误差；该预算不无条件假设存在全局精确``离散 Hamiltonian''。只有当 |
| `eq:chnn-4-62` | 4.62 | 由此可得到第 5 章不变环面分析所需的对象： |
| `eq:chnn-4-63` | 4.63 | 其中 |
| `eq:symplectic-kam-5-1` | 5.1 | 对自治保守 CHNN |
| `eq:symplectic-kam-5-2` | 5.2 | 精确流满足 |
| `eq:symplectic-kam-5-3` | 5.3 | 若一步映射 F_{h}^{cons} 为近恒等的精确辛映射，且所选投影的 Jacobi 分块非退化，则局部存在生成函数。对中心型生成函数取首项可得隐式中点格式 |
| `eq:symplectic-kam-5-4` | 5.4 | 对于非自治 H\left( Z,t \right)，引入扩展相空间 |
| `eq:symplectic-kam-5-5` | 5.5 | 令 z \in R^{2n}，F_{i}\left( z,t \right) 为 Birkhoff 函数组，B\left( z,t \right) 为 Birkhoff 函数，并定义 |
| `eq:symplectic-kam-5-6` | 5.6 | Birkhoff 方程写为 |
| `eq:symplectic-kam-5-7` | 5.7 | 设一般系统写成 |
| `eq:symplectic-kam-5-8` | 5.8 | 在局部星形区域内，若 K 非退化并满足反对称性、空间闭合条件和时间相容条件，则系统具有正则、自伴 Birkhoff 表示；等价地，可找到 F_{i} 与 B 使上述方程成立COMSOLWeakCont |
| `eq:symplectic-kam-5-9` | 5.9 | 其相流满足时变结构保持关系 |
| `eq:symplectic-kam-5-10` | 5.10 | 分析仅针对第 4 章定义的 X_{res} 展开。直接参数化一形式 |
| `eq:symplectic-kam-5-11` | 5.11 | 并引入 B_{\beta}，定义候选向量场 |
| `eq:symplectic-kam-5-12` | 5.12 | 训练损失取 |
| `eq:symplectic-kam-5-13` | 5.13 | 在研究域 D 上定义 Birkhoff 系统自伴表示缺陷 |
| `eq:symplectic-kam-5-14` | 5.14 | 在正则、自伴、解析和非退化条件下，Birkhoff 相流在适当局部投影中具有梯度映射和标量生成函数。若生成函数关于步长解析，可展开为 |
| `eq:symplectic-kam-5-15` | 5.15 | 截断至 m 阶得到隐式 m 阶 K\left( z,t \right)-辛格式，并满足 |
| `eq:symplectic-kam-5-16` | 5.16 | 对自治保守分支的精确辛步进映射 F_{h}^{cons}，寻找嵌入 |
| `eq:symplectic-kam-5-17` | 5.17 | 满足 |
| `eq:symplectic-kam-5-18` | 5.18 | 采用 Fourier 截断 |
| `eq:symplectic-kam-5-19` | 5.19 | 并定义不变性残差 |
| `eq:symplectic-kam-5-20` | 5.20 | 定义 KAM 理论保证域 |
| `eq:symplectic-kam-5-21` | 5.21 | 完整工程安全域定义为 |
