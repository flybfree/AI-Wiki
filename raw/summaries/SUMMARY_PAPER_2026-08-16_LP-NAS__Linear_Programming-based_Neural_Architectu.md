---
title: LP-NAS: Linear Programming-based Neural Architecture Search
url: http://arxiv.org/abs/2608.14472v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_16-53-11Z_LP_NAS_LinearProgramming_basedNeuralArchitectureSe.md
generated_at: 2026-08-16 20:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces LP‑NAS, a linear programming framework that guides differentiable NAS by using validation‑loss gradients and training‑loss Hessians to compute efficient architecture updates. The authors demonstrate two variants—S‑LP‑NAS and R‑LP‑NAS—on the DARTS search space, showing faster convergence and higher early‑stage validation performance compared with standard DARTS. Experiments on CIFAR‑10 and CIFAR‑100 confirm that LP‑DARTS outperforms several existing DARTS variants.

## Key Takeaways
- The method formulates an architecture update direction using the validation‑loss gradient and training‑loss Hessian, enabling a linear program to steer search.  
- Both S‑LP‑NAS and R‑LP‑NAS achieve faster convergence and significantly higher early‑stage validation scores than baseline DARTS.  
- LP‑DARTS outperforms P‑DARTS, PC‑DARTS, and STO‑DARTS on CIFAR‑10 and delivers comparable or better results on ImageNet.

## Context
NAS methods aim to automate deep network design while preserving performance; differentiable NAS relaxes the search into a continuous space for optimization. This work extends that idea by replacing gradient‑based heuristics with a principled linear program, offering a more systematic approach to architecture updates.

## Implications
LP‑NAS provides practitioners with a scalable algorithmic tool that can be integrated into existing differentiable NAS pipelines without sacrificing speed. Its ability to improve early search performance may accelerate model deployment and reduce computational costs in large‑scale AI projects.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14472v1)
