---
title: Learning-Based Stochastic Optimal Control with Infinite-Horizon Probabilistic Constraints
url: http://arxiv.org/abs/2608.01151v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_11-00-41Z_Learning_BasedStochasticOptimalControlwithInfinite.md
generated_at: 2026-08-03 23:39
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses stochastic optimal control with infinite‑horizon joint chance constraints by reformulating the problem as a constrained Markov decision process. It proves strong duality, allowing an unconstrained Lagrange dual formulation that can be solved with a dual‑ascent algorithm. The approach also introduces a learning component to approximate value functions offline, reducing online computational load.

## Key Takeaways
- The joint chance constraints are handled via state augmentation creating additive cost and constraint structures.
- Strong duality is proven enabling an equivalent unconstrained dual problem that converges to an optimal deterministic policy.
- An offline training phase learns a value function approximator that simplifies the online control loop.

## Context
The work extends classic stochastic control theory by integrating probabilistic constraints into infinite‑horizon settings, a challenge for real‑time systems. By leveraging duality and learning, it bridges theoretical guarantees with practical computational efficiency in AI‑driven decision making.

## Implications
For robotics and autonomous agents operating under uncertainty, this method offers scalable policies that maintain feasibility without heavy online optimization. Practitioners can deploy learned approximations to achieve near‑optimal performance while preserving safety constraints across long horizons.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01151v1)
