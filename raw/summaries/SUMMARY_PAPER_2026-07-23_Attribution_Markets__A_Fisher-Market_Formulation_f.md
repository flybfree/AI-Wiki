---
title: Attribution Markets: A Fisher-Market Formulation for Fractional Credit Assignment Between Planned Tasks and Performed Actions
url: http://arxiv.org/abs/2607.20694v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_19-49-38Z_AttributionMarkets_AFisher_MarketFormulationforFra.md
generated_at: 2026-07-23 23:19
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a Fisher‑market model that links planned task budgets with performed actions, treating tasks as budget‑constrained buyers and actions as divisible goods. It derives theoretical results such as conservation, hard caps, and junk filtering, and shows convergence via a satiation‑threshold fixed point. Empirical tests reveal sensitivity to affinity noise, resolved by an entropy‑regularized generalization.

## Key Takeaways
- The quasi‑linear Fisher market ensures that the sum of effort budgets equals total logged duration while preserving individual task caps.
- A seller reserve price and buyer cash option guarantee a provable junk filter that discards actions unrelated to any plan.
- Entropy‑regularization links the market’s zero‑entropy equilibrium to optimal transport, improving robustness to affinity noise.

## Context
In AI attribution systems, separating planned effort from actual work is essential for accurate performance measurement. This formulation bridges planning and execution with a mathematically grounded mechanism that can be adapted to various task graphs.

## Implications
Practitioners can use this model to design fair credit assignment pipelines that respect budget constraints and reduce false stalls. The entropy‑regularized variant offers a stable, noise‑resilient alternative for real‑world deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20694v1)
