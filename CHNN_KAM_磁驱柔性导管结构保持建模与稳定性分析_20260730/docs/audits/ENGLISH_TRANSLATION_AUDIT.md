# 英文全文翻译与结构审计报告

## 1. 工作范围

本轮以已经完成 DOCX--LaTeX 基线核验的 `manuscript/zh/` 为唯一内容权威源，对 `manuscript/en/` 完成全文语言层翻译。此前英文 DOCX 仅用于术语和表达对照，没有覆盖中文 LaTeX 主稿。

已翻译文件：

- `00-introduction.tex`
- `01-rod-model.tex`
- `02-galerkin-discretization.tex`
- `03-hamiltonian-structure.tex`
- `04-chnn-model.tex`
- `05-symplectic-kam.tex`
- `06-numerical-results.tex`
- `07-discussion.tex`
- `08-conclusion.tex`

翻译覆盖章节标题、正文、列表文字、定理与证明文字、公式中的文字注释、实验占位和结论占位。没有改写中文正文，也没有补写尚未得到实验支持的结果。

## 2. 保持不变的结构对象

中英文结构审计通过，以下对象保持同构：

- 9 个章节文件及其装配顺序；
- 171 个章节层级与章节标签；
- 424 个编号公式及公式标签；
- 行内数学结构；
- 602 个唯一标签；
- 79 次交叉引用调用及其目标；
- 37 个 BibTeX 文献键；
- 定理、命题、引理、假设、推论和证明环境的类型与顺序；
- 5 个结构化实验结果占位环境；
- 摘要中的实验结果占位；
- 数学主张、限定条件和结论边界。

增强后的 `tools/audit_bilingual.py` 还会检查：

- 章节命令类型和顺序；
- 英文正文是否仍残留 CJK 中文字符；
- 中英文显示公式和行内数学签名；
- 标签、引用目标、文献键和定理环境序列。

## 3. 构建结果

从零构建结果：

- 中文稿：51 页；
- 英文稿：61 页；
- 未定义引用：0；
- 缺失文献：0；
- 重复标签：0；
- Missing character：0；
- Overfull box：0；
- BibTeX warning：0。

英文日志仍有 3 处轻微 `Underfull \hbox`，属于个别英文段落行间伸缩提示，没有造成内容缺失、越界、重叠或裁切。

英文 PDF 已对 61 页全部渲染检查。标题页、目录、公式、定理、实验占位、讨论、结论和参考文献页面均可正常显示。

## 4. 中文基线保护

新生成的中文 PDF 与双语结构实施前的冻结中文 PDF 进行了 51 页逐页像素比较：

- 变化页数：0；
- 中文正文、公式、编号和版面未发生变化。

因此，本轮英文翻译没有反向污染中文基线。

## 5. 翻译口径

英文采用 SCI 学术表达方式进行等义改写，而不是机械逐词替换。主要术语已经固定在 `translation/terminology.md`，包括：

- magnetically actuated flexible catheter；
- geometrically exact Cosserat rod；
- Kirchhoff shear-free constraint；
- joint translational--rotational Galerkin discretization；
- configuration-dependent mass--inertia matrix；
- autonomous conservative backbone；
- structured Hamiltonian neural network with complex-valued representations；
- real-valued physical Hamiltonian readout；
- a posteriori invariant-torus validation；
- safe operating domain。

## 6. 当前稿件定位

当前英文稿是完整的英文语言层工作稿，但还不是最终投稿稿，原因不是正文未翻译，而是：

1. 数值实验尚未冻结，摘要、第 6 节和结论仍保留实验占位；
2. 尚未选定目标 SCI 期刊；
3. 尚未执行目标期刊模板、文献样式和声明模块适配；
4. 最终实验回填后仍需进行一次结合目标期刊风格的英文精修和母语级校对。

后续应先把稳定实验结果回填中文主稿，再同步更新英文对应段落并运行双语审计。不要直接修改公式、标签和文献键。
