---
title: Compute-Optimal Is Not Cluster-Optimal: Systems-Aware Scaling for Sparse Mixture-of-Experts
url: http://arxiv.org/abs/2608.10605v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_07-49-00Z_Compute_OptimalIsNotCluster_Optimal_Systems_AwareS.md
generated_at: 2026-08-11 22:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MOSAIC, a framework that jointly optimizes model architecture and systems implementation for sparse Mixture-of-Experts language models. It shows that within a fixed compute budget the loss improves with sparser models but the optimal sparsity is not achieved when only compute is considered; instead system constraints drive the best trade‑off.

## Key Takeaways
- Within a calibrated sparsity range an efficiency‑agnostic FLOPs budget yields no interior optimum, meaning the model can be made sparser without loss. 
- The fitted scaling law indicates that loss decreases monotonically with increasing sparsity across active parameters from 104 million to 2.7 billion and total model size up to 79 billion. 
- Optimal sparsity emerges when system constraints such as communication cost, memory footprint, and parallel layout are included in the co‑design.

## Context
Large‑scale pretraining typically separates architecture design from hardware optimization, leading to suboptimal implementations that ignore real‑world compute and memory limits. This paper bridges that gap by treating both as a single optimization problem for MoE models.

## Implications
Practitioners must adopt unified co‑design pipelines rather than stage‑wise tuning to achieve truly efficient frontier models. The approach can be extended beyond language modeling to any sparse architecture where hardware constraints dominate performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10605v1)
