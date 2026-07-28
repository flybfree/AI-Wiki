---
title: On the Impossibility of Unbiased and Length-Invariant Policy Optimization with Outcome Rewards
url: http://arxiv.org/abs/2607.23364v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-25_21-12-51Z_OntheImpossibilityofUnbiasedandLength_InvariantPol.md
generated_at: 2026-07-27 20:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper establishes an impossibility theorem for outcome‑reward reinforcement learning under Group Relative Policy Optimization. It shows that no length‑based weighting can satisfy both gradient unbiasedness and length invariance simultaneously; GRPO fulfills the latter but not the former, while Dr. GRPO fulfills the former but violates the former.

## Key Takeaways
- The standard outcome reward + GRPO setting makes it impossible to have both gradient unbiasedness and length invariance simultaneously.
- GRPO approximately satisfies length invariance (P2) but violates gradient unbiasedness (P1).
- Dr. GRPO achieves gradient unbiasedness (P1) but breaks length invariance, causing longer trajectories to dominate updates by a factor proportional to the length ratio.

## Context
Group Relative Policy Optimization is widely used for training reasoning capabilities in large language models such as DeepSeek‑R1; recent efforts aim to correct response‑level length bias. This paper reveals that correcting one property inevitably harms the other, underscoring fundamental constraints on current normalization schemes.

## Implications
Practitioners cannot rely on a single algorithm as universally optimal; they must accept tradeoffs and design weighting functions accordingly. This influences model training pipelines and evaluation metrics for reasoning tasks, highlighting the need to balance bias and invariance in RL‑based LLM optimization.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.23364v1)
