# 编译、引用、标签、公式与结论边界审计

> **历史审计记录。** 本文件保留专项构建审计的历史统计；当前符号合同以 `translation/terminology.md` 和最新双语正文为准，不据此声称正式源码接口或维度已经核验。

日期：2026-07-30

## 1. 构建命令与结果

最终执行：

```powershell
python tools/build.py --language both --clean
```

构建流程为：

1. 语义结构检查；
2. BibTeX 数据库检查；
3. 中英文骨架一致性检查；
4. XeLaTeX；
5. BibTeX；
6. XeLaTeX 多轮运行至交叉引用稳定；
7. 构建后日志检查；
8. 发布 PDF。

最终结果：

| 项目 | 中文 | 英文 |
|---|---:|---:|
| sections / `sec:` labels | 174 / 174 | 174 / 174 |
| equations / `eq:` labels | 425 / 425 | 425 / 425 |
| unique labels | 608 | 608 |
| `\Cref` calls | 87 | 87 |
| citation calls / unique keys | 63 / 37 | 63 / 37 |
| structured result placeholders | 0 | 0 |
| BibTeX entries / active / unused | 37 / 37 / 0 | 37 / 37 / 0 |
| PDF pages | 55 | 67 |

中英文 9 个组装文件的语义骨架一致。

## 2. 最终日志审计

最终 `build/zh/main-zh.log` 和 `build/en/main-en.log` 中：

- LaTeX/Package Error：0；
- Overfull box：0；
- undefined citation：0；
- undefined reference：0；
- multiply defined label：0；
- rerun required：0；
- float specifier changed：0。

中文 Underfull hbox：0。  
英文 Underfull hbox：3，均为原有长英文术语的松排版提示，不造成裁切、重叠或构建失败；严格构建器接受。

## 3. 源码禁用项审计

对所有可编译 `*.tex` 递归扫描，下列项目均为 0：

- result ID / `RES-*`；
- SHA-256 / checksum；
- manifest / verification / receipt；
- 本地绝对路径；
- `bridge_conservative/outputs/...`；
- raw status code；
- 审计、验收、资格链、冻结点、唯一状态等工作流语言；
- backfill / 回填 / 待回填；
- machine record/gate/summary；
- delivery chain/package；
- `resultplaceholder`；
- 可见 TODO、核查和问题宏调用。

## 4. PDF 文本审计

使用 PyMuPDF 提取两份最终 PDF 全文。九类禁用项的命中总数均为 0：

| 类别 | 中文 PDF | 英文 PDF |
|---|---:|---:|
| local path | 0 | 0 |
| result ID | 0 | 0 |
| SHA/checksum | 0 | 0 |
| manifest/receipt | 0 | 0 |
| raw status code | 0 | 0 |
| placeholder/backfill | 0 | 0 |
| workflow instructions | 0 | 0 |
| internal A0/B0 stage codes | 0 | 0 |
| `verification` | 0 | 0 |

## 5. 公式与定量结果审计

当前源码文本合同记录为（本轮不重新生成 release PDF）：

- \(q_N=\Pi_{\mathrm{conf},N}(U)\)；
- \(p_N=B_N(q_N)^{T}P_{\mathrm{full}}\)；
- \(\dot q_N=M_N(q_N)^{-1}p_N\)；
- \(\dot p_N=\dot B_N(q_N)^{T}P_{\mathrm{full}}+B_N(q_N)^{T}L_{\mathrm{full}}\)，其中
  \(L_{\mathrm{full}}:=\dot P_{\mathrm{full}}\) 仅在该定义明确激活时使用；
- \(1.64186\)、\(2.00088\)；
- \(0.00146226\)；
- \(0.000221162\)；
- \(0.0000563606\)；
- \(0.00307057\) 和阈值 \(0.005\)；
- P0：\(0.0109144\)；
- P1：\(0.1417\%\)；
- P1.5：\(97.29\%\)；
- P1.6 负结果：\(2.872\times10^{-2}\)。

## 6. 结论边界审计

中英文摘要、数值实验、讨论和结论均保留并一致表达：

- BDF 未被证明为辛；
- 当前结果不构成 KAM 数值认证；
- 完整 96 轨迹和 P2 模型比较尚待完成；
- 未证明完整 P2 上 CHNN 普遍优于 Real HNN；
- 未获得不变环面和工程安全域；
- seed 不等于独立物理样本；
- Bridge 能量判据与 force-v2 判据不合并。

同时检出 P2、KAM、open-port、high-fidelity、invariant torus 和 safe domain，确认研究范围未被删减。

## 7. 视觉检查

- 对中文 55 页和英文 67 页生成并检查了全页缩略图。
- 逐页放大检查摘要、数值实验、Bridge 图表、canonical 收敛图表、讨论、结论和附录。
- 修正英文附录中浮动表先于附录标题的问题。
- 最终未见文字裁切、图表重叠、孤立占位框或可见内部操作说明。

## 8. 发布文件

| 文件 | Size (bytes) | SHA-256 |
|---|---:|---|
| `release/CHNN_KAM_Manuscript_ZH.pdf` | 957291 | `6C1063A7006EFA539E8FFCB53327B97CEFC49BD55AA0324BAA9EF9825275EE5E` |
| `release/CHNN_KAM_Manuscript_EN.pdf` | 432864 | `2044BA068B8C9C2B90B1E73094BDE4A90BFC263FCB5E8F3294F608427B0CB3AC` |
