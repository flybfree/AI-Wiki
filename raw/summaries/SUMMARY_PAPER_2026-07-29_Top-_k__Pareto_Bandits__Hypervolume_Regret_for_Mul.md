---
title: Top-$k$ Pareto Bandits: Hypervolume Regret for Multi-Objective Slate Selection
url: http://arxiv.org/abs/2607.26273v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-28_21-10-39Z_Top__k_ParetoBandits_HypervolumeRegretforMulti_Obj.md
generated_at: 2026-07-29 21:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper tackles a stochastic multi‑objective bandit problem where an agent chooses k arms each round and receives d‑dimensional rewards with semi‑bandit feedback. The goal is to keep a small set of actions that collectively approximate the Pareto frontier, measured by dominated hypervolume. The authors propose THV‑UCB, an optimistic arm‑selection algorithm, and prove a gap‑free regret bound O(d√(nkT)) plus a gap‑dependent polylogarithmic bound once arms are well separated.

## Key Takeaways
- The objective is defined via dominated hypervolume, and the paper introduces an α‑approximate hypervolume regret where α = 1 – 1/e reflects greedy submodular maximization guarantees.  
- THV‑UCB selects arms greedily using optimistic estimates of marginal hypervolume contributions to achieve a gap‑free bound O(d√(nkT)).  
- When the arms are sufficiently well separated, the regret becomes polylogarithmic in T via a second bound O(nk^{2.5}/Δ_min).

## Context
In multi‑objective decision making, selecting only a subset of actions that approximate the Pareto frontier is often more practical than tracking a single optimal arm. This work extends bandit theory to handle d‑dimensional rewards and semi‑bandit feedback, providing theoretical guarantees for small‑k selection problems.

## Implications
Practitioners can use THV‑UCB to efficiently maintain Pareto‑optimal sets in applications such as multi‑criterion resource allocation or personalized recommendation systems where computational cost is limited. The poly‑logarithmic regret under good separation suggests scalable performance, encouraging adoption in real‑world AI pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.26273v1)
