# Translation terminology

The verified Chinese LaTeX manuscript is authoritative. This glossary fixes preferred English renderings for the bilingual manuscript.

- 磁驱柔性导管: magnetically actuated flexible catheter
- 几何精确杆 / 几何精确 Cosserat 杆: geometrically exact rod / geometrically exact Cosserat rod
- 截面姿态: cross-sectional orientation
- 平移--转动联合 Galerkin 离散: joint translational--rotational Galerkin discretization
- 构形相关质量--惯性矩阵: configuration-dependent mass--inertia matrix
- 质量中心线: mass centerline
- 保守骨架: conservative backbone
- 自治保守骨架: autonomous conservative backbone
- 开放端口系统: open-port system
- 被动耗散核: passive dissipative kernel
- 规定流场: prescribed flow field
- 流场输入端口: flow-input port
- 排他能量分账: mutually exclusive energy accounting
- 正则 Hamiltonian 系统: canonical Hamiltonian system
- 复值表示增强的结构化 Hamiltonian 神经网络: complex-representation-enhanced structured Hamiltonian neural network
- 实值物理 Hamiltonian 读出: real-valued physical Hamiltonian readout
- 后验不变环面核验: a posteriori invariant-torus validation
- KAM 小量预算: KAM smallness budget
- 安全操控域: safe operating domain
- 高保真对照: high-fidelity reference/validation model
- Kirchhoff 无剪切约束: Kirchhoff shear-free constraint

## Symbol contract

- B_mag: magnetic induction or magnetic field quantity; do not reuse it for a port or basis matrix.
- B_port: port embedding matrix; in the reduced state, B_port maps u in R^d to U_port in R^(2d) and acts only in the momentum channel.
- B_N: configuration-dependent modal or canonical pullback matrix; its dimension is m_f by N_diag.
- L_full: full-order load rate, defined as dot P_full when that definition is explicitly active; it is not the generic unqualified L in the canonical momentum-rate equation.
- N_diag: diagnostic order only; the current diagnostic basis uses N_diag = 2.
- n_main: production order to be selected by a formal convergence study; it is not fixed by the diagnostic basis.
- Q_diss and Q_contact: bulk passive dissipation and nonpotential contact channels are separate contracts; a formal implementation must not merge or double-count them.

Generic B, L, N, J, or n occurrences in local algebra, sample-count sums, historical reports, or literature quotations are retained when their local meaning is explicit. Historical and review files are not current implementation contracts.
