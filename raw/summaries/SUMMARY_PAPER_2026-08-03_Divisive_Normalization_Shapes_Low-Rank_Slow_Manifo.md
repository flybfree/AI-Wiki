---
title: Divisive Normalization Shapes Low-Rank Slow Manifolds for Continuous Working Memory
url: http://arxiv.org/abs/2608.01947v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_09-20-05Z_DivisiveNormalizationShapesLow_RankSlowManifoldsfo.md
generated_at: 2026-08-03 23:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how divisive normalization can enable recurrent networks to learn stable continuous manifolds, addressing the fragility of classical attractor models. The authors show that their Recurrent Divisive Normalization Network (RDNN) converges to high‑fidelity slow manifolds and that BPTT gradients are scaled by activity, limiting updates in active regimes.

## Key Takeaways
- Divisiive normalization provides a biological constraint that yields robust, low‑dimensional slow manifolds instead of point attractors.  
- The activity‑dependent local gradient scaling introduced during BPTT reduces effective rank and prevents manifold shattering under time‑varying inputs.  
- Ablations reveal that subtractive inhibition alone cannot prevent shattering; divisive normalization is mathematically essential for continuous memory.

## Context
Continuous working memory remains a challenge for standard RNNs such as GRUs and LSTMs, which often discretize state space into isolated points. This work bridges the gap by leveraging a biologically observed mechanism to stabilize dynamics without explicit low‑rank factorization.

## Implications
The findings suggest that incorporating activity‑dependent normalization can improve continuous representation learning in AI systems. Practitioners may benefit from designing networks that mimic this scaling to achieve more stable and efficient memory operations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01947v1)
