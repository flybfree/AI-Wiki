---
title: WAM-OPD: On-Policy Distillation for World Action Models
published: 2026-08-23T11:06:45Z
authors: Liuhaichen Yang, Zhuang Jiang, Chenchao Sheng, Zezhi Tang
url: http://arxiv.org/abs/2608.22364v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WAM-OPD: On-Policy Distillation for World Action Models

## Abstract
World action models (WAMs) couple visual future prediction with robot action generation, but accelerated students can lose task capabilities during distillation and later encounter states that are poorly represented by offline data. We study whether on-policy distillation (OPD) can repair such a student without requiring sparse-reward reinforcement learning. We introduce WAM-OPD, a deployment-consistent post-training recipe for a video-first WAM. The student acts in the environment and therefore determines the history distribution. A frozen teacher labels those student histories with coherent video and action targets, while the student action branch is trained under its own generated video plan, as it is at deployment. Joint video and action losses update lightweight adapters in the shared backbone, together with an action flow-matching regularizer. In preliminary RoboTwin 2.0 studies on two tasks, the released one-video/one-action-step Flash-WAM improves from 0.0% to 58.3% success on HANDOVER MIC, and from 16.7% to 33.3% on PUT OBJECT CABINET. These task-specific results are an initial capability proof rather than evidence of broad or uniform generalization. They nevertheless suggest that dense teacher supervision on student-induced histories is a promising post-training interface for video-first WAMs.

## Metadata
- **Published**: 2026-08-23T11:06:45Z
- **Authors**: Liuhaichen Yang, Zhuang Jiang, Chenchao Sheng, Zezhi Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22364v1)