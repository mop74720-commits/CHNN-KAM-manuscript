# 去审计语言专项清理报告

> **历史审计记录。** 本文件记录去审计语言专项的历史结果；当前符号合同以 `translation/terminology.md` 和最新双语正文为准，本文不构成正式源码接口或维度已核验的证明。

日期：2026-07-30  
工作对象：磁驱柔性导管结构保持建模与稳定性分析论文工程  
结论：专项清理完成，中英文 PDF 均通过严格构建、文本扫描和关键页视觉检查。

## 1. 范围与保护措施

- 修改前创建了完整备份：
  `C:/Users/GW/Downloads/bridge_latest/CHNN_KAM_Word基线完整迁移版_v2_清理核验版_P2B0R2回写副本_20260730_去审计语言前完整备份`
- 备份含 141 个文件、共 7,244,104 bytes；主入口、配置、中英文数值章节及 PDF 抽样哈希一致。
- 仅修改当前回写副本。未修改原论文工程、`paper_evidence`、`bridge_conservative` 或 P2-A1 目录。
- 未运行实验、训练、COMSOL 或 KAM，未读取或吸收 P2-A1 临时结果。
- P2-A1 在内部项目材料中继续按 `running_not_yet_accepted` 管理；该内部状态不显示在论文 PDF 中。

## 2. 清理结果

初始扫描命中为文本命中数，各类别可能重叠：

| 类别 | 清理前 | 清理后可编译 TeX |
|---|---:|---:|
| `RES-*` result ID | 189 | 0 |
| `resultplaceholder` | 22 | 0 |
| `SHA-256` | 34 | 0 |
| `manifest` | 14 | 0 |
| `verification` | 13 | 0 |
| receipt/checksum | 4 | 0 |
| 实验内部路径 | 24 | 0 |
| A1 原始运行状态 | 11 | 0 |
| canonical qualified 原始状态 | 11 | 0 |
| failed/blocked 原始状态 | 4 | 0 |
| 回填/待回填 | 29 | 0 |
| 审计/验收/资格链等 | 18 | 0 |
| 证据路径/哈希说明 | 13 | 0 |
| 交付工作流语言 | 9 | 0 |

最终递归源码扫描还确认：

- 本地绝对路径：0；
- `bridge_conservative/outputs/...`：0；
- 可见 TODO、核查框和问题框调用：0；
- raw status code：0；
- 旧证据附录引用：0。

作者注宏 `\todo`、`\checkeq`、`\question` 已改为无条件不渲染；`resultplaceholder` 环境定义已删除。

## 3. 学术化重写

- 数值实验章改按“实验目的—数值模型与数据—对照方法—评价指标与阈值—结果—科学解释—适用边界”组织。
- 原阶段式诊断改写为：
  1. 初始异常；
  2. 误差来源隔离；
  3. 余切投影合同识别；
  4. solver/output 语义比较；
  5. fixed-basis 初值一致性修正；
  6. 三层时间步收敛；
  7. \(1\,\mathrm{s}\) canonical 验证。
- 表格只保留工况、指标、数值、阈值/判据和适用范围；图注只说明物理量、方法、工况与科学结论。
- 附录删除路径、文件清单、哈希表、更新协议和操作说明，改为诊断方法、canonical 方程、指标定义、阈值、数值设置及后续实例化方法。
- 未完成内容改写为正常的后续数值验证方案，不再显示回填框、内部 TODO 或状态提示。

详细逐文件记录见 `AUDIT_LANGUAGE_REMOVAL_CHANGELOG.md`，删除/改写/保留对照见 `AUDIT_LANGUAGE_REMOVAL_COMPARISON.md`。

## 4. 科学内容保留

以下内容作为当前仓库文本合同记录；本轮不重新生成 release PDF，历史 PDF 验收结论不因本节文字收口而变化：

- canonical contract（当前文本合同）：
  \(q_N=\Pi_{\mathrm{conf},N}(U)\)、
  \(p_N=B_N(q_N)^{T}P_{\mathrm{full}}\)、
  \(\dot q_N=M_N(q_N)^{-1}p_N\)、
  \(\dot p_N=\dot B_N(q_N)^{T}P_{\mathrm{full}}+B_N(q_N)^{T}L_{\mathrm{full}}\)，其中
  \(L_{\mathrm{full}}:=\dot P_{\mathrm{full}}\) 仅在该定义明确激活时使用；
- 三层观察收敛阶：\(1.64186\)--\(2.00088\)；
- \(1\,\mathrm{s}\) G2：\(0.00146226\)；
- G3 点态：\(0.000221162\)；
- G3 impulse：\(0.0000563606\)；
- 扰动能量峰峰漂移：\(0.00307057<0.005\)；
- P0、P1、P1.5、P1.6 的全部已写入数值和方法学负结果；
- Bridge \(0.5\%\) 扰动能量判据、探索性 \(1\%\) 判据和独立 force-v2 \(2\%\) 判据保持分离；
- seed 明确为算法重复，不等于独立物理样本。

结论边界继续明确：

- BDF 未被证明为辛积分器；
- 当前结果不构成数值 KAM 认证；
- 完整 96 轨迹和 P2 模型比较尚未完成；
- 尚未证明 CHNN 在完整 P2 任务上普遍优于 Real HNN；
- 尚未获得不变环面或工程安全域；
- P2、KAM、开放端口、高保真和安全域研究范围均未删减。

## 5. PDF 验收

| PDF | 页数 | 禁用项扫描 | SHA-256 |
|---|---:|---:|---|
| `release/CHNN_KAM_Manuscript_ZH.pdf` | 55 | 0 | `6C1063A7006EFA539E8FFCB53327B97CEFC49BD55AA0324BAA9EF9825275EE5E` |
| `release/CHNN_KAM_Manuscript_EN.pdf` | 67 | 0 | `2044BA068B8C9C2B90B1E73094BDE4A90BFC263FCB5E8F3294F608427B0CB3AC` |

PDF 文本扫描对以下九类均为 0：本地路径、result ID、SHA/checksum、manifest/receipt、raw status code、placeholder/backfill、工作流指令、内部阶段码、`verification`。

已目视检查全部页面缩略图，以及中英文摘要、数值实验、表格、图注、讨论、结论和附录关键页。未发现裁切、重叠、可见占位框或附录浮动顺序错误。

## 6. 图表数据来源与哈希

图表数据、矢量图及生成脚本未在本轮修改：

| 图 | 数据 | 数据 SHA-256 | 图 SHA-256 |
|---|---|---|---|
| `figures/fig_bridge_gate_separation.pdf` | `figures/data/bridge_gate_separation.csv` | `BB6E8038EAC2B7F834BBA457137A0A61058D797EF50A8E01236783599594CFB8` | `A7C97769D1BBD31AF3DB7B9EF131467A56D0088C74002E8EA236A770B8518B64` |
| `figures/fig_b0_r2_convergence_orders.pdf` | `figures/data/b0_r2_convergence_orders.csv` | `66472B3E538105A5B8AC4EF62F13057B5A5C2692EA5114AFB3D6BDC3A49663A9` | `4D3C5D5CE89EA217F9902B175A5C62949CBB1A664E2D2D23FF3DC28BEE680F17` |

内部 result ID、证据路径和生成溯源继续保留在 `FIGURE_TABLE_PROVENANCE.csv`、`RESULT_ID_TO_TEX_MAP.csv`、原 changelog 和只读证据库中，不显示在论文 PDF。

## 7. 交付状态

- 修改后的完整工程：当前目录；
- 中文 PDF：`release/CHNN_KAM_Manuscript_ZH.pdf`；
- 英文 PDF：`release/CHNN_KAM_Manuscript_EN.pdf`；
- 逐文件 changelog：`AUDIT_LANGUAGE_REMOVAL_CHANGELOG.md`；
- 删除/改写/保留对照：`AUDIT_LANGUAGE_REMOVAL_COMPARISON.md`；
- 编译、引用、标签、公式与结论边界审计：`AUDIT_LANGUAGE_REMOVAL_BUILD_AUDIT.md`。
