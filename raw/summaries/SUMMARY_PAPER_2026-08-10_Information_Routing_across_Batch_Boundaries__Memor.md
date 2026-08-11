---
title: Information Routing across Batch Boundaries: Memory--Batch Tradeoffs in Lipschitz Bandits
url: http://arxiv.org/abs/2608.07922v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_04-57-24Z_InformationRoutingacrossBatchBoundaries_Memory__Ba.md
generated_at: 2026-08-10 22:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how adaptive learning in stochastic Lipschitz bandits balances the amount of live reward information stored (width W) with the number of committed batches (B). It shows that the optimal trade‑off yields a pseudo‑regret bound involving both parameters and proves that state width and update depth cannot be swapped. The analysis also reveals an information‑routing constraint linking regional decisions to memory capacity.

## Key Takeaways
- For widths W at least on the order of log(eT), the minimax expected pseudo‑regret is bounded up to logarithmic factors, while lower bounds hold for any W.
- A new penalty term T^{(d+2)/(d+3)} (1+(B−1)W)^{-1/(d(d+3))} appears, showing that increasing memory width reduces the cost of committing actions across batches.
- The interaction is an information‑routing constraint: regional decisions must encode Θ_d(s^{-d}) bits, while boundary states carry at most (B−1)W bits of entropy.

## Context
Adaptive algorithms in bandits must retain enough reward history to make informed choices while limiting computational overhead. This work formalizes the width–depth tradeoff as a memory‑batch bottleneck that affects regret performance across different algorithmic regimes.

## Implications
For practitioners, the result clarifies when expanding state capacity is worthwhile versus committing actions earlier into batches. It guides design of batching strategies in online learning systems where both latency and accuracy matter.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07922v1)
