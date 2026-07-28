---
title: Discrepancy-Rounded Fair Bandits with Static and Time-Varying Exposure Floors
published: 2026-07-24T22:20:44Z
authors: Ibne Farabi Shihab, Joyanta Jyoti Mondal, Anuj Sharma
url: http://arxiv.org/abs/2607.22935v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Discrepancy-Rounded Fair Bandits with Static and Time-Varying Exposure Floors

## Abstract
Minimum-exposure constraints arise in recommendation, content curation, and regulated allocation when each provider, arm, or group must receive guaranteed exposure inside a period rather than only in aggregate. We study stochastic bandits with exact exposure floors and show that the right object is a rounding problem: a fractional fair schedule is realized as integral pulls, and the exposure error is exactly a discrepancy vector. The main contribution is a blockwise model with time-varying floors. BDQ-UCB satisfies every block floor deterministically and has fair regret governed by the nonmandatory budget $R$, not the horizon $T$, with high-probability regret $O(\sqrt{KR\log(KT)})$. A MOSS residual variant attains $O(\sqrt{KR})$, and a matching lower bound gives the minimax rate $Θ(\sqrt{KR})$, even with positive mandatory exposure; a kl-UCB$^{++}$ residual rule adds instance-dependent optimality. The formulation becomes essential for overlapping group floors: per-arm rounding can violate a group constraint by $Ω(s)$ in the group size, whereas Beck--Fiala null-space rounding meets every group floor within the block budget with violation below the arm degree $t$, and composes with UCB at the same $R$-parametrized regret. For learned group plans, we close disjoint systems at $\widetildeΘ(\sqrt{KT})$, give a dual-ledger decomposition explaining why naive index rules fail under overlap, and prove a plan-sampling rule that is pathwise feasible under an initial cover-slack condition and attains a conditional $\widetilde O(\sqrt{KT})$ guarantee, leaving the condition-free overlap rate open. Experiments on synthetic floors, MovieLens-100k genre exposure, and deployment stress tests show exact feasibility without penalty tuning and regret competitive with tuned Lagrangian baselines.

## Metadata
- **Published**: 2026-07-24T22:20:44Z
- **Authors**: Ibne Farabi Shihab, Joyanta Jyoti Mondal, Anuj Sharma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.22935v1)