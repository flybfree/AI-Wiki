---
title: Algorithm for Contextual Queueing Bandits with Rate-Optimal Queue Length Regret
url: http://arxiv.org/abs/2606.09668v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-06-08_15-51-25Z_AlgorithmforContextualQueueingBanditswithRate_Opti.md
generated_at: 2026-06-11 10:54
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces CQB‑η‑2, a three‑phase algorithm for contextual queueing bandits that reduces the expected queue length regret to \(\widetilde{\mathcal{O}}(T^{-1/2})\) instead of the previous \(\widetilde{\mathcal{O}}(T^{-1/4})\). The authors prove this improvement by limiting random exploration to an early cutoff and using η‑random exploration with a UCB rule thereafter. They also establish a matching lower bound, showing the bound is tight up to logarithmic factors.

## Key Takeaways
- Random exploration is only needed up to a carefully chosen cutoff round, after which pure UCB decisions are used, drastically cutting regret.
- The algorithm achieves \(\widetilde{\mathcal{O}}(T^{-1/2})\) queue length regret by combining negative drift from early phases with sufficient random samples for UCB stability.
- A minimax lower bound of Ω(T⁻¹²) is proven using two hard instances and a coupling argument that converts testing error into queue length regret.

## Context
Contextual queueing bandits model scheduling jobs whose service rates depend on unknown context features, a common problem in resource allocation. Achieving low regret in such stochastic settings is crucial for real‑time systems where timely service impacts performance.

## Implications
The O(T⁻¹²) bound translates to faster convergence in practice, allowing operators to schedule jobs with near‑optimal latency sooner. Practitioners can rely on this algorithm to design robust scheduling policies without excessive computational overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2606.09668v1)
