---
title: Asymptotically Optimal Regret for Reinforcement Learning without Horizon Dependence
url: http://arxiv.org/abs/2607.19854v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_07-42-19Z_AsymptoticallyOptimalRegretforReinforcementLearnin.md
generated_at: 2026-07-23 23:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents an algorithm for minimizing regret in horizon‑free tabular MDP with bounded rewards and proves a bound of tilde O(sqrt(SAK)+S^8A^3) up to poly log factors. The result is tight up to logarithmic factors, matching the contextual bandit lower bound.

## Key Takeaways
- The regret bound is H‑free, eliminating the sqrt(log H) factor that appears in prior results.
- It matches the contextual bandit lower bound up to logarithmic factors, showing asymptotically optimal performance.
- The algorithm avoids a min{log H,S} factor by using monotonicity of value functions and grid projection, improving over earlier guarantees.

## Context
Horizon‑free RL is crucial for applications where planning horizons are unbounded or unknown. Prior works suffered from extra log H dependencies that hinder scalability as horizon grows.

## Implications
For practitioners, this means more efficient policy learning without needing to estimate long‑term value functions, leading to faster deployment and lower computational cost in large state spaces.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19854v1)
