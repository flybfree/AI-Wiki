---
title: Understanding Machine Unlearning Through the Lens of Mode Connectivity
published: 2026-07-27T03:39:03Z
authors: Jiali Cheng, Hadi Amiri
url: http://arxiv.org/abs/2607.23970v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Understanding Machine Unlearning Through the Lens of Mode Connectivity

## Abstract
Machine Unlearning aims to remove undesired information from trained models without full retraining from scratch. Despite recent progress, the loss landscape and optimization geometry of unlearning are poorly understood. In this paper, we study machine unlearning through the lens of mode connectivity--the phenomenon that independently trained models can often be connected by smooth low-loss paths in parameter space. We introduce {\em mode connectivity in unlearning} (MCU) and evaluate it across a range of settings, including curriculum learning, second-order optimization, and connectivity across different unlearning methods. We find that many unlearned models lie in connected basins with smooth retain/forget behavior, while changes in training dynamics can move solutions into different basins. MCU also reveals that models within the same basin can differ substantially on privacy metrics, and that unlearning progresses nonlinearly from the original model to the unlearned model. In addition, linear connectivity suggests that most approximate unlearning methods are mechanistically distinct from retraining. Finally, MCU-based ensembling can improve generalization and robustness to relearning attacks, and MCU smoothness correlates with unlearning difficulty. To our knowledge, this is the first study of machine unlearning through the lens of mode connectivity.

## Metadata
- **Published**: 2026-07-27T03:39:03Z
- **Authors**: Jiali Cheng, Hadi Amiri
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23970v1)