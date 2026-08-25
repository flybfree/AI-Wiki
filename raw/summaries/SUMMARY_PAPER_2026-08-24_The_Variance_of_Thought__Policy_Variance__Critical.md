---
title: The Variance of Thought: Policy Variance, Critical Forks, and Local Credit Assignment
url: http://arxiv.org/abs/2608.22467v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-23_15-46-56Z_TheVarianceofThought_PolicyVariance_CriticalForks_.md
generated_at: 2026-08-24 21:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a new measure of policy variance σπ^2(s) to explain credit assignment in long‑horizon language models. It shows that this variance appears only at critical forks and quantifies the cost of learning from each advantage signal.

## Key Takeaways
- Policy variance is a discovery budget: observing an action with advantage c requires Ω(c²/σπ^2(s)) draws, which matches the exact bound on a two‑point fork.
- The variance is bounded by the policy’s Gini dispersion σπ^2(s) ≤ 1 – ∥π(·|s)∥₂², allowing computation from logits without rollouts.
- Horizon determines estimation cost: at a fork with downstream success probability P, Monte Carlo advantage estimates have SNR ≈ √P, so sample cost scales as 1/P.

## Context
Credit assignment remains a bottleneck for multi‑step AI agents because returns are noisy and sparse. This work reframes the problem in terms of policy variance, offering a principled link between exploration effort, information content, and downstream success probability.

## Implications
Understanding σπ^2(s) can guide model design toward higher dispersion at critical points, reducing unnecessary exploration. Practitioners may adopt log‑value parameterizations to avoid product‑of‑survival bottlenecks in credit assignment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22467v1)
