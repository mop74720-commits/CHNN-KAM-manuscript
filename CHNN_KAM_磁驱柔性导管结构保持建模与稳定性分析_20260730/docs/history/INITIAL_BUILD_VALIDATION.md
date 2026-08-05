> **历史记录：** 本文档反映早期迁移或双语搭建阶段，不代表当前工程状态。当前说明以根目录 `README_CN.md` 和 `docs/audits/BUILD_VALIDATION.md` 为准。

# 构建与语义验证

验证日期：2026-07-29

## 构建结果

- 正式入口：`main.tex`；
- 构建命令：`python tools/build.py --clean`；
- 引擎：XeLaTeX + xdvipdfmx，由 latexmk 驱动；
- 输出：`release/CHNN_KAM_Manuscript_ZH.pdf`；
- 页数：51；
- 页面：A4，PDF 1.7；
- 页面样式：仅保留页码，不显示作者姓名或短标题页眉。

## 结构审计

- 活动章节命令：171；
- 活动章节标签：171；
- 编号公式环境：424；
- 公式标签：424；
- 定理类环境/标签：7/7；
- 证明环境：4；
- `\Cref`/`\cref` 调用：79；
- 文献调用：63 处，覆盖 37 个唯一 BibTeX key；
- 重复标签：0；
- Word 数字引用残留：0；
- 硬编码正文章节/公式编号引用：0；
- 活动 figure/table 环境：0/0，与 Word 源一致。

## 编号边界校验

- `eq:rod-1-1`--`eq:rod-1-105`：1.1--1.105；
- `eq:galerkin-2-1`--`eq:galerkin-2-128`：2.1--2.128；
- `eq:hamiltonian-3-1`--`eq:hamiltonian-3-107`：3.1--3.107；
- `eq:chnn-4-1`--`eq:chnn-4-63`：4.1--4.63；
- `eq:symplectic-kam-5-1`--`eq:symplectic-kam-5-21`：5.1--5.21。

## 日志检查

- 未定义引用：0；
- 未定义文献：0；
- 重复标签或 PDF 锚点：0；
- Missing character：0；
- Overfull hbox：0；
- Underfull hbox/vbox：0；
- BibTeX warning：0；
- BibTeX 条目：37；
- 活动引用键：37；
- 未使用数据库条目：0。
