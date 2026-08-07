---
title: Beyond Full-Model Rollback: AuroSFT for Adapter-State Multi-Task Fine-Tuning
published: 2026-08-05T15:57:43Z
authors: Yue Han, Ziniu Liu
url: http://arxiv.org/abs/2608.05250v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Full-Model Rollback: AuroSFT for Adapter-State Multi-Task Fine-Tuning

## Abstract
Multi-task supervised fine-tuning (SFT) often casts a heterogeneous data mixture as a single optimization problem, even though different tasks may reach their best generalization at different times. msft exposes this mismatch through task-wise roll-out, exclusion, and rollback, but its original formulation materializes the scheduler state as full-model checkpoints, making stage transitions costly to store, restore, and deploy. This paper introduces AuroSFT, a parameter-efficient framework that recasts the carried state of overfitting-aware multi-task SFT as a compact, mergeable adapter state. AuroSFT freezes the pretrained backbone, trains only injected adapters, rolls back adapter checkpoints at task-wise peaks, and continues on the remaining active mixture. At the layer level, each adapter applies an AuroRA-inspired adaptive nonlinear layer to a low-rank weight factor rather than to the sample representation. The resulting update remains linear in the input, rank-bounded, and exactly mergeable into the frozen projection. Under the retained-backbone comparison protocol, AuroSFT achieves 61.36% average accuracy, compared with 59.85% for the corresponding msft reference row, and obtains higher accuracy on all five backbones. Our code is available at the anonymous repository: https://anonymous.4open.science/r/AuroSFT-80D1.

## Metadata
- **Published**: 2026-08-05T15:57:43Z
- **Authors**: Yue Han, Ziniu Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05250v1)