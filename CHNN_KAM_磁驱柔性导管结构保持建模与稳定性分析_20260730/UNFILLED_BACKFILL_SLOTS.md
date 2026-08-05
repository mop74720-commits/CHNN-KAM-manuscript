# 未回填结果槽位

冻结日期：2026-07-30  
当前论文结论截止点：`RES-B0-R2-001`  
当前唯一允许的资格状态：`canonical_contract_qualified_for_A1_sentinel`

## 1. P2-A1 amplitude sentinel

- Result ID：`RES-A1-001`
- 当前状态：`running_not_yet_accepted`
- 正文槽位：
  - `frontmatter/zh/abstract.tex`
  - `frontmatter/zh/abstract-en.tex`
  - `frontmatter/en/abstract.tex`
  - `manuscript/zh/sections/06-numerical-results.tex`，§6.3
  - `manuscript/en/sections/06-numerical-results.tex`，§6.3
  - 双语讨论、结论和附录增量审计段
- 接受前置条件：正式最终报告、final status、机器 gates、manifest、verification、完成标记和稳定交付包必须同时存在。
- 禁止吸收：部分 gate、临时 CSV、中间日志、正在写入的 MPH/NPZ/ZIP，以及未被 manifest 绑定的文件。

A1 完成后只增量读取：

1. `bridge_conservative/outputs/p2_a1_amplitude_sentinel_scan_20260729/` 中新增且稳定的正式最终报告、final status、机器 gates、manifest、verification 和完成标记；
2. `bridge_conservative/deliverables/P2_A1*` 以及项目正式交付目录中的稳定 ZIP、receipt、checksum；
3. 正式更新后的 `PROJECT_STATE.md`、`EXPERIMENT_HISTORY.md`、`ASSUMPTION_REGISTRY.md`、`NEXT_STAGE.md`；
4. manifest 明确绑定的轻量 CSV、JSON、NPZ。

增量更新表项：

- `paper_evidence/00_registry/PAPER_FILE_INVENTORY.csv`
- `paper_evidence/00_registry/PAPER_RESULT_REGISTRY.csv`
- `paper_evidence/00_registry/PAPER_CLAIM_EVIDENCE_MATRIX.md`
- `paper_evidence/00_registry/PAPER_SUPERSESSION_MAP.md`
- `paper_evidence/00_registry/PAPER_PENDING_RESULTS.md`
- `paper_evidence/05_figures_tables/PAPER_FIGURE_TABLE_PLAN.md`
- `paper_evidence/06_writeback_drafts/PAPER_WRITEBACK_MAP.md`
- `paper_evidence/07_reproducibility/REPRODUCIBILITY_INDEX.md`
- `paper_evidence/SCAN_CONFLICTS_AND_UNCERTAINTIES.md`
- 本工程的 `RESULT_ID_TO_TEX_MAP.csv`、`FIGURE_TABLE_PROVENANCE.csv` 与上述 A1 正文槽位。

## 2. 正式 96 轨迹

- Result ID：`RES-P2-96-001`
- 当前状态：`not_started`
- 槽位：双语 §4.4–4.6 的正式数据合同，以及双语 §6.3 的正式数据结果。
- 必须报告：物理轨迹数量、whole-trajectory 划分、轨迹参数覆盖、状态/向量场标签质量、数据 manifest 和校验和。
- 边界：seed 只能作为算法重复，不能增加物理样本数；A1 也不能替代正式 96 轨迹。

## 3. 正式 P2 训练与比较

- Result ID：`RES-P2-TRAIN-001`
- 当前状态：`not_started`
- 槽位：双语 §4.4–4.6、§6.3、§7 和 §8。
- 必须报告：预注册模型、轨迹级划分、训练预算、seed、主指标、长时 rollout、线性化/结构指标、统计区间和失败案例。
- 边界：现有 P0/P1/P1.5/P1.6 不得写成正式 P2，也不得据此宣称 CHNN 已优于 Real HNN。

## 4. 数值 KAM 与不变环面

- Result ID：`RES-KAM-001`
- 当前状态：`not_started`
- 槽位：双语 §5.6–5.7、§6.5–6.6、§7 和 §8。
- 必须报告：积分参考系、normal form、非退化裕度、Diophantine 裕度、高阶/解析误差证书、辛映射缺陷、步长非共振条件、不变性残差和后验验证。
- 边界：B0-R2 不是 KAM 资格，不证明存在不变环面，也不产生安全域。

## 5. 开放端口、高保真与工程安全域

- Result ID：`RES-PORT-HF-001`
- 当前状态：`not_completed`
- 槽位：双语 §4.3、§6.4、§6.6、§7 和 §8。
- 必须报告：端口功率闭合、耗散符号、接触切换、高保真模型差异、实验数据和安全域组成条件。
- 边界：保守骨架的条件性稳定域不能替代完整工程安全域。

## 6. 本轮停止点

本轮没有运行实验、训练、COMSOL 或 KAM，也没有自动吸收 P2-A1。下一次论文回写必须由新的正式证据和新的 result ID/manifest 触发。
