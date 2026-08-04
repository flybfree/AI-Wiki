---
title: Verifier-Induced Support Reshaping in On-Policy Optimization
url: http://arxiv.org/abs/2608.00220v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-07-31_19-05-43Z_Verifier_InducedSupportReshapinginOn_PolicyOptimiz.md
generated_at: 2026-08-03 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how on‑policy reinforcement learning with verifiable rewards reshapes the support that a policy can learn, showing that successful trajectories become scarce after verification. Experiments on mathematical reasoning and constrained instruction following reveal that Math‑RLVR improves pass@1 but reduces best@32, indicating a trade‑off between early success and later diversity.

## Key Takeaways
- Verifier‑induced support reshaping makes high‑scoring trajectories rare, limiting the pool of rewards available for later objectives. - The effective rewardable support is defined as successful trajectories that can be sampled within a fixed rollout budget, which shrinks after verification. - RLVR reranks only existing openings in the base policy and those openings causally affect subsequent math searchability.

## Context
On‑policy RL with verifiable rewards aims to align training with human feedback while preserving sample efficiency. This work demonstrates that verification can unintentionally degrade diversity of successful behaviors, a concern for continual learning where past successes must not block future progress.

## Implications
For practitioners, the findings warn against assuming endpoint improvements guarantee trainability on later tasks under on‑policy optimization. Industry systems relying on such verifiers may need to monitor support distribution to avoid hidden bottlenecks in model evolution.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00220v1)
