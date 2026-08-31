---
title: HARTS: Efficient Agentic Reinforcement Learning for Hybrid-Attention Models over Arbitrary Rollout Trees
published: 2026-08-28T10:18:54Z
authors: Boyuan Meng, Peihua Bao, Hong Liu, Xiaowei Zhu, Chao Wang, Gen Li, Zhenxuan Pan
url: http://arxiv.org/abs/2608.28158v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HARTS: Efficient Agentic Reinforcement Learning for Hybrid-Attention Models over Arbitrary Rollout Trees

## Abstract
Agentic reinforcement learning (RL) often produces irregular rollout trees with shared histories. Training root-to-leaf trajectories independently recomputes these shared prefixes. Existing systems primarily target full-attention models and lack dense, differentiable hybrid-attention execution compatible with activation recomputation. We present HARTS (Hybrid-Attention RL over Tree Structures). HARTS jointly plans microbatches, data-parallel (DP) replica assignments, and microbatch-slot schedules using non-replay compact-token work after prefix compression. For chunkwise linear attention, a linear-time algorithm coordinates chunk-boundary state recovery and replay and produces the minimum number of sequential linear-attention calls under our packed execution model. HARTS preserves the chunkwise state partitioning of trajectory-wise training: it does not repeat projections, MLP/MoE computation, or final outputs, and performs only bounded state replay for numerical alignment. Per round, HARTS batches all branches into one packed call, propagates gradients through differentiable state handoffs, supports activation recomputation, and restores per-token log-probabilities. For deterministic, no-token-drop top-$k$ MoE routing, semantic multiplicities restore MoE-objective token weights and load statistics. Existing RL objectives retain their interface. To our knowledge, HARTS is the first system to demonstrate arbitrary-rollout-tree prefix-sharing speedups on a real hybrid-attention model. On an Agentic RL workload generated from SWE-bench tasks, HARTS achieves $4.81$--$4.87\times$ forward/backward/gradient speedup with activation recomputation across multiple parallel configurations. Its numerical differences are comparable to baseline self-rerun variation, and its reward trend is similar to the baseline over the first 120 steps of $τ^3$-Bench training.

## Metadata
- **Published**: 2026-08-28T10:18:54Z
- **Authors**: Boyuan Meng, Peihua Bao, Hong Liu, Xiaowei Zhu, Chao Wang, Gen Li, Zhenxuan Pan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28158v1)