---
title: Learning from Interaction Experience via Localized Context Distillation
published: 2026-10-15T07:39:09Z
authors: Zhezheng Hao, Yongkang Yang, Xilin Xia, Jiarui Yu, Yi Liu, Fanjunduo Wei, Peijie Dong, Tianfu Wang, Qiang Lin, Can Wang, Hande Dong, Jiawei Chen
url: http://arxiv.org/abs/2610.21427v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Learning from Interaction Experience via Localized Context Distillation

## Abstract
Learning from interaction experience is essential for enabling large language models to continually improve during deployment. Context distillation offers a promising path: privileged information extracted from experience is provided to a teacher, whose behavior is then distilled into a student model that has no access to it. However, both existing forms of context distillation have limitations. Off-policy context distillation trains the student on teacher-generated trajectories and thus suffers from exposure bias; whereas on-policy context distillation trains on the student's own rollouts, whose states are often uninformative and fail to convey behaviors the student cannot yet produce. To resolve this dilemma, we introduce Localized Context Distillation (LoCD). LoCD first localizes the critical spans of a student trajectory that require revision. The teacher then regenerates only these spans from the student's own prefix, and the student is trained on the regenerated segments. LoCD thereby concentrates learning on the most informative states while keeping exposure bias low. Extensive experiments across math reasoning, code generation, and agent tasks demonstrate that LoCD consistently outperforms strong baselines and achieves more stable training with smaller and sparser parameter updates.

## Metadata
- **Published**: 2026-10-15T07:39:09Z
- **Authors**: Zhezheng Hao, Yongkang Yang, Xilin Xia, Jiarui Yu, Yi Liu, Fanjunduo Wei, Peijie Dong, Tianfu Wang, Qiang Lin, Can Wang, Hande Dong, Jiawei Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.21427v1)