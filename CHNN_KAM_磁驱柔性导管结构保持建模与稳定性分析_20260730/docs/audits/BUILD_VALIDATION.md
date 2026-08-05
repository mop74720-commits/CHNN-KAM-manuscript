# 清理核验版构建与交付审计

## 1. 本轮修改

- 删除英文首页可见的内部状态/审计提示，并移除对应 staging 开关；
- 保留实验结果占位，但不再在首页显示“工作稿”“非投稿稿”等状态文字；
- 核验并修正 5 条 COMSOL 6.3 官方文档记录；
- 将第 [6] 条题名修正为 `Theory for Section Stiffness`；
- 根据 COMSOL 官方发布记录，将版本 6.3 的年份规范为 2024；
- 增加官方页面 URL 与访问日期；
- 保留原有 BibTeX key，避免中英文引用结构变化；
- 修正英文稿参考文献标题为 `References`；
- 删除旧英文 staging PDF、Python 缓存和构建中间文件；
- 将顶层说明压缩为 `README_CN.md`、`KNOWN_ISSUES.md`，其余审计和历史文档迁入 `docs/`。

## 2. COMSOL 文献核验结果

| Key | 规范题名 | 官方文档位置 |
|---|---|---|
| `COMSOLBeamInterface2025` | The Beam Interface | COMSOL 6.3 Beam Interface documentation |
| `COMSOLGeometricNonlinearity2025` | Geometric Nonlinearity | COMSOL 6.3 Beam interface theory |
| `COMSOLSectionStiffness2025` | Theory for Section Stiffness | COMSOL 6.3 Beam interface theory |
| `COMSOLWeakFormPDE2025` | The Weak Form PDE | COMSOL 6.3 equation-based modeling documentation |
| `COMSOLWeakContribution2025` | Weak Contribution (PDEs and Physics) | COMSOL 6.3 equation-based modeling documentation |

BibTeX key 中的 `2025` 为既有内部标识，未随年份字段改名，以保持全部 `\cite` 调用稳定。

## 3. 结构审计

- 章节/章节标签：171 / 171；
- 编号公式/公式标签：424 / 424；
- 唯一标签：602；
- 交叉引用调用：79；
- BibTeX 条目：37；
- 活动文献键：37；
- 未用文献：0；
- 结构化实验占位：5。

## 4. 构建结果

| 稿件 | 页数 | 未定义引用 | Overfull | Missing character | BibTeX warning |
|---|---:|---:|---:|---:|---:|
| 中文 | 51 | 0 | 0 | 0 | 0 |
| 英文 | 61 | 0 | 0 | 0 | 0 |

英文日志保留 3 处轻微 `Underfull \hbox`，未造成越界、裁切或内容缺失。

## 5. PDF 检查

- 英文首页不再含内部审计、基线或投稿状态提示；
- 英文参考文献标题为 `References`；
- COMSOL 第 [6] 条题名已经修正；
- COMSOL URL 可正常换行，无 Overfull；
- 中文参考文献标题保持为“参考文献”；
- 两份 PDF 均无可见裁切、重叠、黑块或断字。

## 6. 交付包结构

- 根目录仅保留主要入口、总说明和当前遗留问题；
- 当前审计位于 `docs/audits/`；
- 标签注册表位于 `docs/reference/`；
- 早期迁移和 staging 阶段记录位于 `docs/history/`，并标注为历史资料；
- `release/` 仅保留当前中文和英文 PDF。
