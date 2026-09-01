---
title: Normalized Low-Rank Adaptation
published: 2026-08-31T16:15:36Z
authors: Jiale Kang, Ziyin Yue, Zheng Zhan, Yangyi Huang, Weiyang Liu
url: http://arxiv.org/abs/2608.31036v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Normalized Low-Rank Adaptation

## Abstract
While low-rank adaptation (LoRA) is widely used for parameter-efficient model adaptation, how to regularize its training dynamics for stable and effective optimization remains underexplored. Because LoRA initializes the up-projection to zero, its early optimization dynamics are largely governed by the down-projection. Building on this observation, we introduce Normalized Low-Rank Adaptation (NoRA), a simple yet effective method that normalizes the down-projection matrices during training. We further show that the same normalization can be applied only at initialization, improving standard LoRA without requiring repeated normalization throughout training. Across pretraining, supervised finetuning, and reinforcement learning, NoRA consistently accelerates convergence, improves performance and training stability, and mitigates catastrophic forgetting. These benefits require neither additional trainable parameters nor inference-time computation, making NoRA a simple and broadly applicable enhancement to LoRA.

## Metadata
- **Published**: 2026-08-31T16:15:36Z
- **Authors**: Jiale Kang, Ziyin Yue, Zheng Zhan, Yangyi Huang, Weiyang Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.31036v1)