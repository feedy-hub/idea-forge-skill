# 领域知识地图：AI / 多模态 / 信号处理 v1.1

> 本文件只作为启发式背景与检查清单，不得替代最新检索。涉及 SOTA、数据集、leaderboard、投稿趋势、法律合规、开源协议、模型能力时，必须重新查新。

## 发表阵地分级与口味

| 阵地 | 级别 | 口味特征 |
|------|------|----------|
| NeurIPS / ICML / ICLR | 顶会 | 方法通用性、理论洞察，story 要“改变认知” |
| CVPR / ICCV / ECCV | 顶会 | 视觉效果、benchmark 强，工程完成度要求高 |
| ACL / EMNLP | 顶会 | 语言与多模态语言侧 |
| ACM MM | 顶会 | 多模态应用、融合机制、跨模态任务价值 |
| ICASSP / Interspeech | 会议 | 信号/语音，重 SP 严谨性，短文迭代快，适合试水占位 |
| TPAMI | 顶刊 | 完整体系性工作，常为顶会工作深化 |
| IEEE TSP / JSTSP | 顶刊 | 理论保证 + 算法推导，SP 先验 × DL 范式主场 |
| Nature Communications / NMI | 顶刊 | 跨学科影响力，需“AI × 科学 / 医疗”大 story |

标准打法：ICASSP / preprint 试水占位 → 顶会主力 → TPAMI / TSP 扩展。时效窗口“紧张”时，占位节点必须进时间线。

## 交叉区富矿

- 多模态 × 生理信号：情感计算、医疗监测。数据壁垒高，但合规风险也高。
- SP 理论 × 多模态融合：融合的理论解释（信息论 / 最优传输 / 子空间视角）长期欠缺。
- 基础模型 × 时序信号：窗口期，但拥挤度快速上升。
- 多模态缺失 / 不对齐鲁棒性：真实部署刚需；注意 attention 类方案已部分填占，差异化要落在机制层和极端条件。
- 音视频语音 × Codec / Foundation Model：有 prior transfer、target space、生成式/判别式混合等机会，但必须和既有神经 codec、speech enhancement、AVSE 工作清晰区分。

## 常用公开资源锚点

- 多模态：CMU-MOSEI、AVE、Ego4D、AudioSet。
- 音视频语音：LRS2 / LRS3、VoxCeleb2、AMI、EasyCom。
- 生理信号：PhysioNet 系列、DEAP、SEED。
- SOTA 核对：PapersWithCode、官方 benchmark 页面、论文附录与开源仓库。

## 领域雷区（L3 自动预警）

- “又一个 attention 变体”。
- 饱和 benchmark 刷点。
- 多模态“暴力拼接”式融合无机制解释。
- 声称通用但只在单一数据集验证。
- 装饰性理论：保证定义在 learned space，物理含义丢失。
- 把隐私、生物识别、医疗、监控类数据问题当作普通数据问题处理。
- 把静态领域知识当作最新 SOTA。

## 伦理合规敏感区

涉及以下方向时，L3 必须触发 Ethics Gate：

- 生物识别：声纹、人脸、步态、虹膜、唇形身份识别。
- 敏感属性推断：健康、情绪、心理状态、年龄、性别、种族、宗教、政治倾向等。
- 医疗与生理信号：ECG、EEG、EMG、睡眠、疾病诊断。
- 监控与执法：远程识别、群体行为分析、异常检测、安防场景。
- 未成年人数据。
- 未授权采集、爬取、录音、视频处理。
