---
title: When Should Graph Attention Be Sparse? Learning a Per-Edge Tsallis Index
url: http://arxiv.org/abs/2608.02938v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-03_22-51-49Z_WhenShouldGraphAttentionBeSparse_LearningaPer_Edge.md
generated_at: 2026-08-05 01:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces LTGA, a graph attention layer that learns a Tsallis entropic index q to adaptively switch between heavy‑tailed, softmax and compact‑support attention shapes. Experiments on eight benchmarks show the learned index improves average rank by 2.75 points compared with fixed GAT or grid‑search baselines while requiring only one model run. However, a validation‑tuned frozen grid still outperforms LTGA-Edge in some cases.

## Key Takeaways
- The model learns a per‑edge Tsallis index q that interpolates between q<1 (heavy‑tailed) and q>1 (compact‑support), allowing the attention mechanism to prune 42 % of coefficients when q leaves 1.  
- Those pruned edges are identified as “wrong” ones, and restoring them costs only 7.1 points versus 13.0 points for random pruning at the same rate, demonstrating a selective improvement over uniform removal.  
- Despite these gains, an omnibus test does not reject the benefit (p=0.199) and learning q does not consistently beat exhaustive grid search, which reaches 62.2 % accuracy.

## Context
Graph attention mechanisms have become standard in neural graph networks, but their fixed softmax normalization limits adaptability to heterogeneous graph structures. Recent work on Tsallis entropies explores alternative intensity parameters that can produce sparse or dense attention patterns, yet most implementations treat q as a global scalar rather than per‑edge. This paper bridges that gap by integrating q into the network’s reparameterization.

## Implications
For practitioners, LTGA offers a single‑run solution that balances interpretability and performance without exhaustive hyperparameter tuning. In industry applications where edge pruning can reduce computational cost, the selective zeroing of attention coefficients may lead to faster inference with minimal accuracy loss. The paper thus advances both theory and practice by providing an interpretable mechanism for dynamic graph attention scaling.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02938v1)
