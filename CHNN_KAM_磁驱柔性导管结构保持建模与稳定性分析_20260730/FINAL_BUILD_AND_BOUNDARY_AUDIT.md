# 最终构建、引用、公式与结论边界审计

审计日期：2026-07-30  
科学结论截止点：P2-B0-R2  
验收状态：通过

## 1. 独立副本与只读边界

- 本轮只修改 `CHNN_KAM_磁驱柔性导管结构保持建模与稳定性分析_20260730`。
- 原工程 `CHNN_KAM_Word基线完整迁移版_v2_清理核验版` 仍为 91 个文件，附录开关仍为关闭，且不存在本轮最终审计文件。
- `paper_evidence` 与 `bridge_conservative` 仅作为只读证据输入；没有运行实验、训练、COMSOL 求解或 KAM。
- 对 P2-A1 只做了顶层名称级元数据检查：活动目录顶层有 8 个文件，但没有名称包含 final、status、manifest、completion 或 delivery 的文件；正式 `P2_A1*` 交付项也不存在。没有读取或哈希活跃 A1 的大型 MPH、NPZ 或 ZIP。
- 因此 `RES-A1-001` 继续登记为 `running_not_yet_accepted`。

## 2. 构建方法与产物

执行命令：

```bash
python tools/build.py --language both --clean
```

构建脚本先执行语义、书目和双语骨架审计；当前环境的 `latexmk` 缺少 Perl，因此采用：

```text
XeLaTeX → BibTeX → XeLaTeX（至少两遍，并按日志迭代至交叉引用稳定，最多四遍）
```

| 产物 | 页数 | 字节数 | SHA-256 |
|---|---:|---:|---|
| `release/CHNN_KAM_Manuscript_ZH.pdf` | 55 | 957291 | `6C1063A7006EFA539E8FFCB53327B97CEFC49BD55AA0324BAA9EF9825275EE5E` |
| `release/CHNN_KAM_Manuscript_EN.pdf` | 67 | 432864 | `2044BA068B8C9C2B90B1E73094BDE4A90BFC263FCB5E8F3294F608427B0CB3AC` |
| `build/zh/main-zh.log` | — | 41382 | `36754209444F0C03674AAA46BABABBE4EBC5DCC43D6DC7112D439E3CC1B887FB` |
| `build/en/main-en.log` | — | 43436 | `9E3699CF54009343071FA2ABC0D67640B5120725D4B33873534FF36F871BE73F` |

## 3. 语义、引用、标签与公式审计

中英文审计结果一致：

| 检查项 | 中文 | 英文 |
|---|---:|---:|
| sections / section labels | 174 / 174 | 174 / 174 |
| equations / equation labels | 425 / 425 | 425 / 425 |
| unique labels | 608 | 608 |
| `\Cref` calls | 91 | 91 |
| citation calls / unique keys | 63 / 37 | 63 / 37 |
| structured pending-result slots | 5 | 5 |

- 双语骨架：9 个章节文件、9 个正文装配项，检查一致。
- BibTeX：37 个条目，37 个均被激活，无未使用条目；中英文 `.blg` 均为 0 个 `Warning--`。
- 最终中英文日志均为：
  - undefined citation/reference：0；
  - multiply defined label：0；
  - missing character：0；
  - overfull box：0；
  - “rerun cross-references”或“labels may have changed”：0。
- 保留 9 个中文和 16 个英文 underfull box，来自附录长路径/哈希及少量英文断行；关键页目视检查未发现裁切、重叠或越界。
- 两份日志各有 2 个字体提示：Latin Modern Mono 无粗体字形时退回常规字形；不存在字符缺失。

Canonical contract 在中英文 `manuscript/*/sections/03-hamiltonian-structure.tex` 的同一位置和同一公式标签
`eq:hamiltonian-canonical-data-contract` 下固定为：

\[
q_N=\Pi_{\mathrm{conf},N}(U),\qquad
p_N=B_N(q_N)^T P_{\mathrm{full}},\qquad
\dot q_N=M_N(q_N)^{-1}p_N,\qquad
\dot p_N=B_N(q_N)^T L .
\]

相邻正文同时定义了构形空间、切空间和余切空间，并明确 `p_mass=M_N*dq_native` 仅为诊断量；BDF order-2 仅承担同一 solver-step 状态采样和向量场标签生成。

## 4. 正式数值与 result ID 绑定

`RESULT_ID_TO_TEX_MAP.csv` 验证结果：

- 23 行、23 个唯一 result ID；
- 23 行回写执行状态均为 `completed_as_planned`；
- 其中 5 行是“保留待回填槽位”，并不表示科学结果完成。

`RES-B0-R2-001` 在正文、摘要、结论、表和附录中统一绑定以下正式值：

| 指标 | 数值 |
|---|---:|
| 三层观察收敛阶范围 | `1.64186–2.00088` |
| 1 s G2 | `0.00146226` |
| G3 点态 | `0.000221162` |
| G3 impulse | `0.0000563606` |
| 扰动能量峰峰漂移 | `0.00307057 < 0.005` |

正文 `.tex` 中 `RES-B0-R2-001` 出现 25 次；最终状态以可编译转义形式出现 11 次。唯一允许的状态语义为：

```text
canonical_contract_qualified_for_A1_sentinel
```

## 5. 图表来源与哈希审计

- `FIGURE_TABLE_PROVENANCE.csv` 共 16 行。
- 所有 16 个本地图、图源和表格资产均存在，逐项重算 SHA-256 与登记值一致，错误数为 0。
- Bridge 图和表分别绑定 `RES-BRIDGE-001` 与 `RES-FORCE-V2-001` 的机器表；严格 0.5% 能量门、候选 1% 门与独立 2% force-v2 门保持分离。
- B0-R2 图和表绑定正式报告与 canonical gates；图注明确只支持 canonical data contract 的时间离散资格。
- 图件生成脚本只读取 `figures/data/` 下两项轻量 CSV，不访问实验工程。

## 6. PDF 页面级目视审计

使用 PDF 渲染库以 1.7 倍分辨率渲染并检查：

- 中文：第 1、48、50、53、54 页；
- 英文：第 1、59、61、64、65 页。

覆盖内容包括中英文摘要、Bridge/force 分门表与图、P0/P1 系列表、B0-R2 数值表、截止状态、结论、诊断链和证据路径/哈希。检查结果：

- 图例、阈值线、坐标轴和表格列均可读；
- result ID、长状态字符串、长路径和 SHA-256 均在版心内；
- 附录与参考文献衔接正常；
- 未发现空白页、图表裁切、文本重叠或乱码。

审计缩略图位于 `build/pdf_visual_audit/`，仅为可重建检查产物。

## 7. 结论边界审计

全文检索并逐处复核“正式 P2”“BDF 辛性”“KAM 资格”“不变环面”“安全域”“CHNN/Real HNN”相关语句。所有命中均属于：

1. 已完成的低维或三轨迹 pilot，并带局部适用范围；
2. 理论方法与未来验证接口；
3. 明确的否定、未完成或禁止外推声明。

论文没有声称：

- 正式 P2 已完成；
- BDF 已证明辛；
- 已取得 KAM 资格；
- 正式 P2 已证明 CHNN 优于 Real HNN；
- 已获得真实不变环面或工程安全域。

P1 的五个 seed 在双语方法、结果和讨论中均定义为同一物理轨迹上的算法重复；物理样本数仍为三条轨迹。B0 与 B0-R1 保留为历史中间资格结果，没有覆盖 B0-R2，也没有用旧失败否定当前截止状态。

## 8. 剩余非阻断项

- 作者、单位、通信作者和邮箱仍沿用基线空白栏，未擅自填造。
- A1、正式 96 轨迹、正式 P2、数值 KAM、开放端口和高保真仍为结构化待回填槽位；详见 `UNFILLED_BACKFILL_SLOTS.md`。
- 本轮至此停止，不自动吸收后续 A1 文件。
