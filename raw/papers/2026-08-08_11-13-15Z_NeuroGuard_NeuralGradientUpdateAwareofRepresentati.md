---
title: NeuroGuard: Neural Gradient Update Aware of Representation Damage
published: 2026-08-08T11:13:15Z
authors: Taigo Sakai, Kazuhito Hotta
url: http://arxiv.org/abs/2608.08068v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NeuroGuard: Neural Gradient Update Aware of Representation Damage

## Abstract
Long-tailed class-incremental learning (LT-CIL) must learn new classes from imbalanced streams while retaining old classes. Existing methods mainly change replay, classifiers, or losses. We study a different factor, namely how strongly the feature representation should be updated at each task boundary. We propose NeuroGuard, an update-control method added to DGR, a replay-based LT-CIL baseline, without adding learnable parameters. NeuroGuard preserves DGR's replay memory, classifier, and set of loss terms. Adaptive Gradient Scaling (AGS) converts teacher uncertainty into one task-wise gradient scale. Confidence-Ranked Knowledge Distillation Reweighting (CRK) gives larger knowledge-distillation weights to replay samples that the teacher predicts less decisively. Fragility-Blended Entropy Gate (FBE) adds old-memory leakage to the scale decision. Across five LT-CIL settings, NeuroGuard improves over DGR in every setting. In the four main benchmark comparisons, it achieves the best task-agnostic accuracy among the compared methods. The gains extend to both old- and new-class accuracy, while medium-frequency accuracy improves consistently across all five settings. Controlled comparisons show that the gain does not come from generic gradient suppression: AGS outperforms a matched fixed-scale control in all five settings, demonstrating that boundary-specific scaling is more effective than applying the same average scale throughout learning.

## Metadata
- **Published**: 2026-08-08T11:13:15Z
- **Authors**: Taigo Sakai, Kazuhito Hotta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08068v1)