> **历史记录：** 本文档反映早期迁移或双语搭建阶段，不代表当前工程状态。当前说明以根目录 `README_CN.md` 和 `docs/audits/BUILD_VALIDATION.md` 为准。

# Word-to-LaTeX 迁移报告

## 唯一内容基线

- 文件：`磁驱柔性导管_期刊投稿预备版(4).docx`
- 本轮没有使用旧 LaTeX 正文补写、改写或纠正 Word 内容。
- 标题、中英文摘要、关键词、正文、定理陈述、结果占位和参考文献均按 Word 基线迁入。

## 迁移覆盖

- Word 段落：1281；
- 顶层编号章节：8；
- 二级标题：52；
- 三级标题：110；
- 活动章节标签：171；
- 编号公式：424；
- 定理/命题/引理/假设/推论环境：7；
- 证明环境：4；
- 结构化结果占位环境：5；
- 参考文献：37；
- Word 源图：0；
- Word 源表：0；
- Word 源附录：0。

## 语义结构

1. Word 标题层级保持为 `section/subsection/subsubsection`，引言使用不编号章节。
2. 所有活动章节均建立稳定英文 `sec:` 标签。
3. 424 个公式保持 Word 的 1.1--5.21 编号序列，并建立稳定 `eq:` 标签。
4. Word 中显式的章节、公式和定理引用已改为 `\Cref`/`\cref`，不再依赖硬编码编号。
5. 定理类环境使用语义标签，并分别保留 Word 中的命题、定理、推论、假设和引理编号。
6. Word 数字引用已映射为 37 个稳定 BibTeX key；`bibliography/order.tex` 固定 Word 参考文献编号顺序。
7. 中文稿与后续英文稿共用相同 label 和 BibTeX key，不需要在翻译时改动引用接口。
8. Word 不含图、表或附录，因此本轮只建立 `fig:`、`tab:` 与附录接入规范，没有虚构任何内容。

## 关键文件

- `manuscript/zh/body.tex`：中文正文装配；
- `manuscript/zh/sections/`：引言与第 1--8 节；
- `frontmatter/zh/`：中英文题名、摘要和关键词；
- `bibliography/references.bib`：37 条 Word 参考文献；
- `bibliography/order.tex`：固定 Word 文献编号顺序；
- `LABEL_REGISTRY.md`：章节和公式标签映射；
- `figures/README.md`、`tables/README.md`：图表接口；
- `backmatter/appendices/README.md`：附录接口。
