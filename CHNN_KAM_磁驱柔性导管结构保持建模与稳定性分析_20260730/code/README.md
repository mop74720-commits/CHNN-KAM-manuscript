# 代码材料说明

本目录区分“原稿保全”和“已检查骨架”，避免把 PDF 中的代码页误当作已经复现的程序。

- `original_prototype_archive.txt` 当前缺失，不能作为复现证据或源码归档。
- `verification_skeleton.py`：只依赖 NumPy 的 V1--V3 最小测试，覆盖复坐标往返、保守中点法阶数、二次能量、阻尼离散功率平衡及共形辛缺陷；它不是正式 CHNN、COMSOL--Galerkin bridge 或 force-v2 实现。

建议环境：Python 3.10+、NumPy 1.24+。运行：

在工程根目录运行：

```bash
python code/verification_skeleton.py
```

本次审阅运行的机器可读输出保存在 `verification_results.json`；当前代码目录实际可追溯的结果仅限该骨架及其 JSON 输出。

脚本对复坐标往返、保守中点法阶数、二次能量漂移和阻尼功率平衡设置可执行断言，并输出 \(10^{-2}\) 至 \(10^{-9}\) 有限差分步长扫描。共形辛缺陷的扫描结果用于显示步长敏感性，不作“随步长稳定下降”的科学结论；该骨架不替代正式 CHNN、COMSOL--Galerkin bridge 或 force-v2 实现。

尚未纳入此骨架的内容：COMSOL 数据读取、Galerkin 投影、CHNN 训练、Birkhoff 高阶生成函数递推、接触事件和控制器实验。这些模块应在相应理论部分逐项审阅后再加入。

## 验证边界

verification_skeleton.py 只承担接口示例、回归测试骨架、数值流程演示和构建门测试对象。它不是正式 CHNN 训练代码、正式 COMSOL--Galerkin bridge、正式 force-v2 实现、P0/P1/P2 生产实验、正式控制器或自适应律，也不是 KAM 数值证书。verification_results.json 只能描述该 skeleton 的运行结果，不能作为论文正式实验结果。

解除 A-17 的 PARTIAL 边界至少需要正式源码、配置、环境锁、原始数组、manifest、clean-run 日志、自动生成的表格和图以及 provenance 一致性记录。当前这些材料缺失，因此本目录不声称完成正式复现或正式模型验证。
