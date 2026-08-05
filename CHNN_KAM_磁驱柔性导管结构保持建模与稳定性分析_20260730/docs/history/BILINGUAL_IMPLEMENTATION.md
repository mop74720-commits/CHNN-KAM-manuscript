> **历史记录：** 本文档反映早期迁移或双语搭建阶段，不代表当前工程状态。当前说明以根目录 `README_CN.md` 和 `docs/audits/BUILD_VALIDATION.md` 为准。

# 中英文同构写作层实施说明

## 实施目标

在不修改已核验中文正文的前提下，将工程扩展为同一结构下的中文基线与英文翻译工作稿。英文目录不是新的内容源，而是中文主稿的语言层镜像。

## 新增结构

```text
main.tex                  # 共享核心入口
main-zh.tex               # 中文 profile
main-en.tex               # 英文 profile
manuscript/zh/            # 已核验中文主稿
manuscript/en/            # 英文翻译工作副本
frontmatter/zh/           # 中文工作稿前置信息
frontmatter/en/           # 英文工作稿前置信息
config/fonts/{zh,en}.tex
config/theorems/{zh,en}.tex
config/localization/{zh,en}.tex
tools/audit_bilingual.py
TRANSLATION_STATUS.md
```

## 当前英文目录状态

英文正文文件已从中文基线逐文件建立同构副本，目前仍保留中文自然语言。这样可以从翻译开始前就固定：

- 章节文件及装配顺序；
- 章节、公式、定理和其他标签；
- 显示公式与行内数学；
- 定理、证明和实验占位环境；
- 交叉引用目标；
- BibTeX 文献键。

英文 profile 的首页会显示“translation working copy”提示，防止误作为投稿稿。

## 自动一致性门禁

`tools/audit_bilingual.py` 对每对中英文文件检查：

1. 文件集合和 `body.tex` 装配顺序；
2. 标签集合及出现顺序；
3. 章节命令数量；
4. 显示公式的规范化数学结构；
5. 行内数学的规范化数学结构；
6. 定理、证明、实验占位环境顺序；
7. 文献键多重集；
8. 交叉引用目标多重集。

公式中的 `\text{...}` 内容允许从中文翻译成英文，比较时被抽象为语言文本占位；公式其余结构必须一致。

## 使用方法

```bash
# 只检查双语结构
python tools/audit_bilingual.py

# 中文主稿
python tools/build.py --language zh --clean

# 英文翻译工作稿
python tools/build.py --language en --clean

# 同时审计并构建两种语言
python tools/build.py --language both --clean
```

## 翻译操作规则

每次只编辑 `manuscript/en/` 和 `frontmatter/en/`。完成一节后先运行双语审计，再分别构建中英文稿。中文正文需要因实验结果或理论修订而改变时，应先修改中文主稿，再将同一结构性改动同步到英文目录，最后通过审计。
