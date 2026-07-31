---
title: Hierarchical Multilevel Monte Carlo for Order-Optimal Neural Actor-Critic in Average-Reward CMDPs
url: http://arxiv.org/abs/2607.28390v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_15-46-22Z_HierarchicalMultilevelMonteCarloforOrder_OptimalNe.md
generated_at: 2026-07-30 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a hierarchical multilevel Monte Carlo neural critic to achieve order‑optimal convergence in average‑reward constrained Markov decision processes. It shows that the estimator can match the bias of a long critic optimization with only logarithmic sample cost, enabling primal‑dual natural actor‑critic methods to reach sub‑square‑root optimality gaps and constraint violations.

## Key Takeaways
- The hierarchical MLMC neural critic reduces bias while keeping optimizer cost low by debiasing both trajectory sampling and critic updates simultaneously.  
- This enables the primal‑dual natural actor‑critic algorithm to achieve an optimality gap of order T^{-1/2} without needing knowledge of the underlying mixing time.  
- The method works for infinite‑horizon average‑reward CMDPs with general policy parameterizations, providing order‑optimal guarantees even in unconstrained settings.

## Context
Constrained Markov Decision Processes are central to safety‑critical reinforcement learning where agents must balance reward maximization against long‑term constraints. Traditional primal‑dual methods rely on linear critics that guarantee order‑optimal convergence, but extending this to neural networks has been challenging due to bias‑cost tradeoffs. This work addresses the missing link by combining advanced Monte Carlo techniques with neural function approximation.

## Implications
Practitioners in autonomous systems and robotics can now design policies that satisfy hard constraints while converging faster than previous neural approaches. The theoretical foundation supports more reliable deployment of RL agents where safety is paramount, reducing risk of constraint violations over long horizons.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.28390v1)
