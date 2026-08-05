# 代码材料说明

本目录区分“原稿保全”和“已检查骨架”，避免把 PDF 中的代码页误当作已经复现的程序。

- `original_prototype_archive.txt`：原稿第 77--116 页的版式化文本抽取。它保留章节、注释和大部分代码，但可能含分页符、Unicode 负号、断行和缩进损失。仅用于追溯。
- `verification_skeleton.py`：只依赖 NumPy 的 V1--V3 最小测试，覆盖复坐标往返、保守中点法阶数、二次能量、阻尼离散功率平衡及共形辛缺陷。

建议环境：Python 3.10+、NumPy 1.24+。运行：

在工程根目录运行：

```bash
python code/verification_skeleton.py
```

本次审阅运行的机器可读输出保存在 `verification_results.json`。

通过标准不是某个预填的固定数值，而是：复坐标往返误差接近机器精度；保守中点法观测阶数接近 2；二次能量漂移接近舍入误差；阻尼功率平衡与两类共形辛缺陷随有限差分步长稳定下降。

尚未纳入此骨架的内容：COMSOL 数据读取、Galerkin 投影、CHNN 训练、Birkhoff 高阶生成函数递推、接触事件和控制器实验。这些模块应在相应理论部分逐项审阅后再加入。
