---
title: CODS: Iterative Bellman-Residual Data Selection for Reusable Offline Reinforcement Learning
url: http://arxiv.org/abs/2608.07719v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-07_19-11-54Z_CODS_IterativeBellman_ResidualDataSelectionforReus.md
generated_at: 2026-08-10 22:33
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CODS, a critic‑guided selector that alternates between fitting an algorithm‑matched critic and acquiring high‑residual transitions before freezing a reusable offline reinforcement learning subset. Evaluated on 20 D4RL task–algorithm cells, CODS retains 96.6 % of the eligible‑pool performance at a 10 % budget, outperforming ReDOR and OPER on 19/20 cells while all six subset advantages remain significant. The method is reusable rather than a formal coreset guarantee.

## Key Takeaways
- CODS retains 96.6 % of eligible‑pool performance at a 10 % budget, demonstrating strong reuse efficiency across multiple tasks.
- It outperforms ReDOR and OPER on 19 out of 20 cells, showing superior selection compared to prior baselines.
- The five acquisition rounds improve four representative cells by 11.23 points over one round before saturating.

## Context
Offline reinforcement learning suffers from redundant data across seeds and hyperparameters, making efficient reuse a critical challenge. Prior methods either discard rare transitions needed for long‑horizon credit assignment or produce non‑reusable artifacts that limit scalability. CODS addresses these issues with a dynamic selection mechanism that balances fit and sparsity.

## Implications
For practitioners, CODS offers a practical way to reduce compute costs while preserving performance in large offline RL experiments. Its ability to maintain high scores across many seeds makes it valuable for hyperparameter sweeps and multi‑task settings where data reuse is essential. The findings suggest that reusable selection procedures can be integrated into standard offline RL pipelines without sacrificing accuracy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07719v1)
