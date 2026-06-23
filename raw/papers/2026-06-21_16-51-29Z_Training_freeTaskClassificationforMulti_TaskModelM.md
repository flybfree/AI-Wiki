---
title: Training-free Task Classification for Multi-Task Model Merging
published: 2026-06-21T16:51:29Z
authors: Jungyong Son, Jinwook Jung, Sungyong Baik
url: http://arxiv.org/abs/2606.22589v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Training-free Task Classification for Multi-Task Model Merging

## Abstract
Ever since the advent of foundation models and the pre-training-finetuning paradigm, there have been numerous efforts to merge multiple task-specific experts into a single multi-task model. Prior work largely focuses on finding a single merged model, but it often underperforms individual experts due to parameter interference. To resolve this, dynamic model merging employs routing to activate task-relevant parameters per input. However, existing routers typically require either additional training with abundant labeled datasets or assume the access to task IDs of each input at inference time. In this work, we aim to close the gap to expert performance without additional training or task-ID-access assumption. To this end, we formulate routing as training-free task classification for each test input. Using singular value decomposition (SVD)-based low-rank manifold approximations for each task, SiM scores tasks by the projection residual of the test input feature onto each task manifold and routes accordingly. The task manifolds are pre-computable offline from a pretrained backbone using a small per-task support set (e.g., 32 examples per task) prior to merging process, requiring no router training and no data during the merging process. Moreover, SiM integrates seamlessly with subspace-/mask-based merging that represents task-expert via lightweight compressed task vectors, avoiding the need to store full expert parameters. Experiments across computer vision and natural language processing benchmarks under task-unknown inference demonstrate that SiM substantially improves merged-model performance and consistently narrows the gap to individual task experts.

## Metadata
- **Published**: 2026-06-21T16:51:29Z
- **Authors**: Jungyong Son, Jinwook Jung, Sungyong Baik
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.22589v1)