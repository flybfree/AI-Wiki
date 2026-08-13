---
title: CoAdapt-GUI: Joint Workflow Context and Policy Adaptation for Unseen GUI Applications
published: 2026-08-12T02:55:50Z
authors: Linqiang Guo, Li Gu, Zihuan Jiang, Zhixiang Chi, Siobhan Reid, Ziqiang Wang, Yuanhao Yu, Wei Liu, Yang Wang,  Tse-Hsun,  Chen
url: http://arxiv.org/abs/2608.11588v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CoAdapt-GUI: Joint Workflow Context and Policy Adaptation for Unseen GUI Applications

## Abstract
Mobile GUI agents remain brittle when deployed to applications absent from source training. We study novel-app generalization under a limited target interaction budget and without target demonstrations. We introduce CoAdapt-GUI, a test-time adaptation (TTA) framework that jointly adapts structured workflow context and policy from the agent's own target-app rollouts and rewards. The workflow context retains transferable procedures, failure modes, and verification rules while excluding app-bound source details. This separation allows reusable workflow knowledge to guide adaptation without transferring source-interface state. For policy adaptation, task-context-matched group-relative optimization updates a LoRA adapter on a frozen vision-language model. Across two unseen-app evaluations, CoAdapt-GUI reaches 45.0% on AndroidWorld-Generalization, compared with 37.5% for the reported Policy-Only TTA baseline, and raises AndroidWorld Plus performance from 38.6% to 52.9%. These results show that transfer-constrained workflow context provides substantial gains and that joint policy adaptation further improves held-out performance.

## Metadata
- **Published**: 2026-08-12T02:55:50Z
- **Authors**: Linqiang Guo, Li Gu, Zihuan Jiang, Zhixiang Chi, Siobhan Reid, Ziqiang Wang, Yuanhao Yu, Wei Liu, Yang Wang,  Tse-Hsun,  Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11588v1)