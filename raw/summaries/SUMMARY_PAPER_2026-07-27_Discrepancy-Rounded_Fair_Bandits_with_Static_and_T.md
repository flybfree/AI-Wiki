---
title: Discrepancy-Rounded Fair Bandits with Static and Time-Varying Exposure Floors
url: http://arxiv.org/abs/2607.22935v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-24_22-20-44Z_Discrepancy_RoundedFairBanditswithStaticandTime_Va.md
generated_at: 2026-07-27 23:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the challenge of satisfying minimum‑exposure constraints in stochastic bandits by reformulating the problem as a rounding task. It introduces blockwise models with time‑varying floors and shows that optimal regret scales with the nonmandatory budget rather than the horizon, achieving provable high‑probability bounds.

## Key Takeaways
- The exposure error for each arm is modeled as a discrepancy vector, allowing exact feasibility of fractional fair schedules through integral pulls.  
- A blockwise rule (BDQ‑UCB) guarantees deterministic satisfaction of every floor and yields regret O(√K·R·log(KT)), while a MOSS residual variant improves to O(√KR), matching the Θ(√KR) minimax lower bound even with mandatory exposure.  
- For overlapping group floors, Beck‑Fiala null‑space rounding keeps violations below arm degree t and composes with UCB, preserving R‑parameterized regret.

## Context
The work builds on classic bandit literature where only aggregate constraints are considered, but many real‑world systems require per‑provider or per‑group exposure guarantees. By treating these guarantees as rounding problems, the paper bridges combinatorial fairness theory with online learning algorithms, offering a principled way to handle both static and time‑varying floor structures.

## Implications
For industry practitioners, this framework enables automated recommendation engines that respect user caps without costly tuning of penalty parameters. Practitioners can rely on provable regret guarantees while ensuring compliance with regulatory exposure limits, reducing risk in regulated allocation scenarios.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.22935v1)
