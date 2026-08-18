---
title: MAPLE: MoE Adaptive Plug-and-play Layer-wise Expert allocation
published: 2026-08-15T16:10:28Z
authors: Lie Li, Wen Li, Junxiao Shen, Gusheng Hu
url: http://arxiv.org/abs/2608.15299v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MAPLE: MoE Adaptive Plug-and-play Layer-wise Expert allocation

## Abstract
Sparsely-activated Mixture-of-Experts (MoE) Transformers universally fix the same number of routed experts across all layers, a convention that ignores the well-documented heterogeneity in layer-wise redundancy. We demonstrate that this uniformity is systematically suboptimal and propose MAPLE, a plug-and-play framework that reallocates the routed-expert budget heterogeneously across layers of any pretrained MoE LLM, without modifying weights or requiring retraining. Our core contribution is a closed-form sensitivity-guided allocation: we probe each layer's response to variation in expert count, quantify sensitivity using three measures, and derive an analytically optimal budget assignment that directs capacity towards sensitive layers and absorbs reductions in redundant layers. This closed-form solution is further refined by a sensitivity-constrained genetic search that uses layer-wise sensitivity as a prior to guide exploration, yielding faster convergence and superior allocation quality. On four MoE models spanning different scales and architectures, MAPLE outperforms uniform and pruning-based baselines under a 75% routed-expert budget. Notably, on DeepSeek-MoE-16B, MAPLE uses only 75% of the experts yet surpasses the original 100% expert-uniform baseline on ARC-E, ARC-C, and BoolQ, improving accuracy from 65.09 to 71.40, 48.49 to 51.50, and 80.03 to 82.38, respectively. These accuracy gains translate into measured deployment efficiency: implementing MAPLE in SGLang reduces single-GPU end-to-end serving latency by 32.2% and improves throughput by 47.4%. These results show that well-designed heterogeneous allocation can be more effective than simply activating more experts, establishing it as a principled and practical axis for improving MoE efficiency.

## Metadata
- **Published**: 2026-08-15T16:10:28Z
- **Authors**: Lie Li, Wen Li, Junxiao Shen, Gusheng Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15299v1)