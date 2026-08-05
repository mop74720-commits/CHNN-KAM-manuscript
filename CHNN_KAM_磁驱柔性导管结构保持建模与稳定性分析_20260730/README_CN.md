# CHNN--KAM 双语 LaTeX 主工程

本工程以已核验的中文 LaTeX 稿为内容基线，同时维护结构同构的英文 SCI 语言层。中文与英文正文共用公式、标签、交叉引用和 BibTeX 键；实验结果尚未冻结的部分继续保留结构化占位。

## 入口与正文

- `main.tex`：共享装配核心；
- `main-zh.tex`：中文构建入口；
- `main-en.tex`：英文构建入口；
- `manuscript/zh/`：中文权威主稿；
- `manuscript/en/`：英文对应稿；
- `bibliography/references.bib`：中英文共用文献库；
- `translation/terminology.md`：固定术语表。

## 构建与审计

```bash
python tools/audit_semantics.py --language zh
python tools/audit_semantics.py --language en
python tools/audit_bilingual.py
python tools/check_bibliography.py
python tools/build.py --language both --clean
```

当前输出：

- `release/CHNN_KAM_Manuscript_ZH.pdf`；
- `release/CHNN_KAM_Manuscript_EN.pdf`。

PDF 首页不显示内部审计、阶段或工作稿状态文字。实验占位只保留在对应摘要、结果和结论位置。

## 文档组织

- `docs/audits/`：当前有效的基线、英文翻译和构建审计；
- `docs/reference/`：标签等长期参考资料；
- `docs/history/`：迁移和双语搭建阶段的历史记录，不代表当前状态；
- `KNOWN_ISSUES.md`：仍需后续处理的问题。

## 维护原则

1. 中文稿是实验回填和内容修订的首要基线；
2. 英文稿只做等义语言转换，不改变公式、标签和文献键；
3. 中英文修改后必须运行双语审计；
4. 期刊切换只调整类文件、前置信息、声明和文献样式；
5. 不在 PDF 中加入内部审计提示、版本声明或工作稿水印，除非明确要求。
