---
title: RoRA: Role-Oriented Regional Allocation for Visual Token Pruning in MLLMs
published: 2026-08-07T10:39:47Z
authors: Qiyanhui Lu, Han Wu, Rongjian Xu, Tingzhang Luo, Cheng Fan, Xinghao Chen, Minjing Dong, Jufeng Yang, Jianyuan Guo
url: http://arxiv.org/abs/2608.07088v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RoRA: Role-Oriented Regional Allocation for Visual Token Pruning in MLLMs

## Abstract
Multimodal large language models (MLLMs) encode images as long visual token sequences, making prefilling and KV-cache storage expensive. Existing training-free pruning methods select tokens by importance, diversity, or spatial coverage, but treat retained tokens as interchangeable and do not explicitly track which object-related regions are already covered. We present RoRA, a training-free framework that casts visual token pruning as role-oriented regional evidence allocation. Given a fixed budget, RoRA partitions tokens into a protected semantic core, complementary context, and fine-grained detail. It first calibrates text-conditioned attention with a positional prior and a prompt-calibrated object prior, then builds Attention-Anchored Regions (AARs) from high-confidence anchors as lightweight proxies for covered object support. Context is explored mainly outside AARs, while a small AAR-guided budget restores local detail; pairwise similarity is used only for context-stage redundancy filtering. Under matched budgets, RoRA consistently outperforms strong training-free baselines across LLaVA and Qwen-VL families, retaining most of the unpruned accuracy even at aggressive pruning ratios, e.g., 96.5% of full performance at 88.9% pruning on LLaVA-1.5, and improving over D2Pruner by about 5% on Qwen3-VL at 75-90% pruning. At a 66.7% pruning ratio, RoRA requires only 0.7 ms for token selection and reduces end-to-end inference time by 24.6%, corresponding to a 1.33x speedup over unpruned inference on an NVIDIA H800.

## Metadata
- **Published**: 2026-08-07T10:39:47Z
- **Authors**: Qiyanhui Lu, Han Wu, Rongjian Xu, Tingzhang Luo, Cheng Fan, Xinghao Chen, Minjing Dong, Jufeng Yang, Jianyuan Guo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07088v1)