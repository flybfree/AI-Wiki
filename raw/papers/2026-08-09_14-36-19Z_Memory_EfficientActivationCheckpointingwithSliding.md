---
title: Memory-Efficient Activation Checkpointing with Sliding Window and Hirschberg's Algorithm for 0/1 Knapsack Solving in PyTorch
published: 2026-08-09T14:36:19Z
authors: Jędrzej Maczan
url: http://arxiv.org/abs/2608.08740v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Memory-Efficient Activation Checkpointing with Sliding Window and Hirschberg's Algorithm for 0/1 Knapsack Solving in PyTorch

## Abstract
Activation checkpointing minimizes the runtime of neural networks under a given memory budget, by selecting which intermediate tensors to store and which to recompute. PyTorch solves this as a 0/1 knapsack problem, where operations from a joint forward-backward computation graph are items with a memory cost (weight) and a runtime saving (value). The default solver, dp_knapsack, allocates a full dynamic programming (DP) table of shape $(n+1) \times (W+1)$, where $n$ is the number of operations and $W$ is the quantized memory budget. This method is resource-hungry and crashes at $n = 100$ items on a machine with 64 GB RAM.   In this paper, we introduce dp_knapsack_sliding_hirschberg, which combines the sliding window trick and Hirschberg's algorithm to reduce peak memory from $O(nW)$ to $O(W)$ while preserving the exact optimal solution. Our experiments show successful knapsack execution at $n = 2000$, where dp_knapsack fails at $n = 100$, a 20$\times$ increase in computable problem size. In addition, our benchmarks show a consistent 25-28\% runtime speedup over dp_knapsack.   The implementation is merged into PyTorch and released in version 2.10.

## Metadata
- **Published**: 2026-08-09T14:36:19Z
- **Authors**: Jędrzej Maczan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08740v1)