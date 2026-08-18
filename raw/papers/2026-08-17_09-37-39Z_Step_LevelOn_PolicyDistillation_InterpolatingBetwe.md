---
title: Step-Level On-Policy Distillation: Interpolating Between On-Policy Distillation and Supervised Fine-Tuning
published: 2026-08-17T09:37:39Z
authors: Changhui Sun, Lanbo Liu, Hang Lei, Tong Ling, Jiahang Xie, Zhiyong Zheng, Yujia Wang, Hao Liu, Feng Xiao, Lu Liu, Yanlong Du, Zifeng Cheng, Ziwei Jiang, Qing Gu
url: http://arxiv.org/abs/2608.16333v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Step-Level On-Policy Distillation: Interpolating Between On-Policy Distillation and Supervised Fine-Tuning

## Abstract
On-policy distillation (OPD) aligns a student model with a teacher's logit distribution on student-generated trajectories. This approach has achieved strong empirical gains and can often surpass conventional off-policy distillation with substantially less data. However, standard token-level OPD can provide only fragmented corrections along an erroneous student trajectory and cannot unfold a complete and correct repair path. Motivated by this limitation, we propose \emph{Step-Level On-Policy Distillation} (SOPD), which combines the long-horizon correction of supervised fine-tuning (SFT) with the on-policy advantage of OPD to provide step-level supervision over complete student-generated trajectories. We show that, at different limits of step length, SOPD reduces to SFT or approximates OPD. Compared with SFT, the teacher responses in SOPD are conditioned on student trajectories and therefore align more closely with student-visited states; compared with OPD, SOPD provides longer-horizon corrections rather than fragmented token-level guidance. Across both reasoning and agent tasks, SOPD substantially outperforms conventional SFT and OPD. For example, on ALFWorld, SOPD improves the average success rate by 13.4 points over Vanilla OPD. We hope this work offers a new perspective for future research on distillation methods.

## Metadata
- **Published**: 2026-08-17T09:37:39Z
- **Authors**: Changhui Sun, Lanbo Liu, Hang Lei, Tong Ling, Jiahang Xie, Zhiyong Zheng, Yujia Wang, Hao Liu, Feng Xiao, Lu Liu, Yanlong Du, Zifeng Cheng, Ziwei Jiang, Qing Gu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16333v1)