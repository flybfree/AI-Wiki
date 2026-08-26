---
title: Mixture of Channel Experts: Static Sparse Supports with Input-Adaptive Mixing for Pointwise Projections
url: http://arxiv.org/abs/2608.23794v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-24_19-55-39Z_MixtureofChannelExperts_StaticSparseSupportswithIn.md
generated_at: 2026-08-25 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Mixture of Channel Experts (MoCE), a sparse channel‑mixing layer that replaces dense pointwise projections in convolutional networks. By routing each input through a small set of experts, MoCE reduces the computational cost while maintaining performance on ImageNet and CIFAR‑100 benchmarks.

## Key Takeaways
- MoCE replaces a dense 1×1 projection with an expert that selects k << C input channels per output channel, cutting MACs by roughly 16.7% compared to the quadratic cost of dense projections.
- The softmax temperature is predicted per input, allowing experts to switch between mean‑like and max‑like aggregation and improving coverage across the channel space.
- A residual expert summarizes unselected channels and a load‑balancing loss ensures complete channel coverage, preserving accuracy while achieving significant latency savings.

## Context
Modern deep networks face scalability challenges as channel dimensions grow. Dense projection layers become computationally prohibitive for large C, limiting model size and inference speed. Prior sparse methods focus on operator sparsity or feature selection, but few integrate channel‑level mixing with residual pathways to maintain full coverage.

## Implications
MoCE demonstrates that structured sparsity can be applied at the channel level without sacrificing representational power, offering a path toward larger, faster models for vision tasks. Practitioners can adopt MoCE to reduce training and inference costs while preserving accuracy, aligning with industry goals of efficient AI deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.23794v1)
