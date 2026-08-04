---
title: SAFE-Merge: Data-Free Continual Model Merging with General Knowledge Preservation
published: 2026-08-02T12:09:37Z
authors: Zihuan Qiu, Zhiyang Liao, Chiyuan He, Yi Xu, Fanman Meng, Linfeng Xu, Qingbo Wu, Hongliang Li
url: http://arxiv.org/abs/2608.01184v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SAFE-Merge: Data-Free Continual Model Merging with General Knowledge Preservation

## Abstract
Data-free continual model merging must incorporate a stream of specialized models while retaining both pretrained general knowledge and previously acquired tasks, without access to task data. Existing methods mainly merge task updates by suppressing interference among downstream tasks; while this protects previously acquired tasks, it overlooks the safety of the pretrained knowledge itself, whose erosion degrades generalization to held-out distributions and weakens the foundation for future task acquisition. We propose SAFE-Merge, a simple data-free continual-merging framework that first decides which parameter updates are safe to retain, and then recovers the task information lost through masking. Specifically, to ensure safety, risk-aware sparse masking selects parameter updates that carry task-specific information while posing low risk to general knowledge. Masked low-rank recovery then compensates for the lost task information using only the same retained parameter updates, while leaving all masked-out parameters strictly unchanged. Finally, the combined update is fused into the backbone, incurring no additional inference cost. Across vision and language benchmarks, SAFE-Merge consistently achieves the best H-score. On longer CLIP task sequences, it substantially improves H-score over NUFILT while also achieving the highest accuracy.

## Metadata
- **Published**: 2026-08-02T12:09:37Z
- **Authors**: Zihuan Qiu, Zhiyang Liao, Chiyuan He, Yi Xu, Fanman Meng, Linfeng Xu, Qingbo Wu, Hongliang Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01184v1)