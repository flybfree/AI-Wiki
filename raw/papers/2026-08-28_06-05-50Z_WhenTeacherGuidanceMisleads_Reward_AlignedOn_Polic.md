---
title: When Teacher Guidance Misleads: Reward-Aligned On-Policy Distillation
published: 2026-08-28T06:05:50Z
authors: Siyuan Gan, Yuhan Li, Xiran Wang, Linjian Meng, Boyan Wang, Zhen Zhao, Jing Huo, Yang Gao
url: http://arxiv.org/abs/2608.27960v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Teacher Guidance Misleads: Reward-Aligned On-Policy Distillation

## Abstract
On-policy distillation (OPD) has recently emerged as a popular post-training paradigm for large language models (LLMs), providing an efficient way to transfer the knowledge and capabilities of teacher models into student models. However, teacher guidance on student-generated prefixes is not always reliable. Training should optimize the model to generate responses that are more likely to be correct, or equivalently, to get higher outcome rewards. But during OPD, the teacher model may provide guidance that discourages the student from moving toward correct trajectories or moves the student toward incorrect ones, which is misaligned with outcome reward. Such misaligned guidance is unreliable, as it would mislead the optimization process and ultimately degrade model performance. To mitigate misaligned teacher guidance, we propose Reward-Aligned On-Policy Distillation (RA-OPD). The key insight is to keep only trajectories whose induced updates move the student toward correct trajectories or discourage the student from moving toward incorrect ones. Specifically, for each sampled trajectory, RA-OPD checks whether its trajectory-level distillation return is consistent with its outcome reward and then filters out the misaligned trajectories. RA-OPD selects more reliable trajectories to improve student model performance without requiring additional computational cost. We evaluate RA-OPD on math and code benchmarks using models from the Qwen3 family and the DeepSeek-R1 family. Across seven math benchmarks and three code benchmarks, RA-OPD significantly outperforms standard OPD and other tested OPD variants.

## Metadata
- **Published**: 2026-08-28T06:05:50Z
- **Authors**: Siyuan Gan, Yuhan Li, Xiran Wang, Linjian Meng, Boyan Wang, Zhen Zhao, Jing Huo, Yang Gao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27960v1)