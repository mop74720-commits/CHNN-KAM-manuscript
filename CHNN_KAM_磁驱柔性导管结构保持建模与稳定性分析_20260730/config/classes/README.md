# 文档类适配层

`main.tex` 只通过 `config/classes/<profile>.tex` 选择文档类。当前正式可编译配置为 `internal`，用于中文理论稿审阅。

切换期刊模板时：

1. 复制相应 `.tex.example` 为新的配置文件，例如 `elsevier.tex`；
2. 在 `main.tex` 顶部将 `\ProjectClassProfile` 改为该文件名；
3. 同时新增或调整 `config/frontmatter/<profile>.tex`，只映射题名、作者、单位、摘要和关键词；
4. 不在 `manuscript/` 中写期刊专属命令。

示例仅说明接口，不包含或替代期刊官方模板。最终应以目标期刊最新 author guidelines 和官方类文件为准。
