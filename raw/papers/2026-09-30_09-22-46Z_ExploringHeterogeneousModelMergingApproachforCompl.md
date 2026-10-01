---
title: Exploring Heterogeneous Model Merging Approach for Complex Knowledge Transfer
published: 2026-09-30T09:22:46Z
authors: Jiahe Fan, Si Chen, Yinghao Hou, Wenbo Xia, Ke Xu, Hong Xie, Enhong Chen
url: http://arxiv.org/abs/2609.39369v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Exploring Heterogeneous Model Merging Approach for Complex Knowledge Transfer

## Abstract
Specialized models encode task-oriented behavior, but transferring that behavior to a general language model usually requires training, distillation, or representation alignment. We study whether such ability can instead be transferred directly at the parameter level. We apply two existing training-free heterogeneous merging methods, previously shown to transfer knowledge between general language models, to specialist-to-general transfer, projecting a specialist donor into the recipient's shape and interpolating backbone parameters without gradient updates or semantic alignment. Intersection-Merge (IM) injects a prefix-aligned donor slice matching the recipient shape, while Activate-Prune-Merge (APM) uses forward-pass activation statistics to select which donor dimensions to retain before injection. Across embedding, reranking, reward modeling, and MoE code-specialist transfer, both methods improve the general recipient, showing that simple heterogeneous merging can move capabilities across diverse specialist roles.

## Metadata
- **Published**: 2026-09-30T09:22:46Z
- **Authors**: Jiahe Fan, Si Chen, Yinghao Hou, Wenbo Xia, Ke Xu, Hong Xie, Enhong Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.39369v1)