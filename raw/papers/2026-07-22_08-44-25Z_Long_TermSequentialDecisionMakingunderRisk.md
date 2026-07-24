---
title: Long-Term Sequential Decision Making under Risk
published: 2026-07-22T08:44:25Z
authors:  Irmaan,  Mirzanejad, Nadjet Bourdache, Abdel-Illah Mouaddib
url: http://arxiv.org/abs/2607.19914v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Long-Term Sequential Decision Making under Risk

## Abstract
We study finite-horizon MDP planning under \emph{root-based} (resolute) risk objectives that apply a rank-dependent functional to the distribution of total returns. Such objectives are non-linear in the return distribution and generally break Bellman optimality, so direct optimization by scenario-tree enumeration is intractable. We propose \textbf{ERQDP}, an enumeration-free and sampling-free method that solves a rank--quantile surrogate via exact DP (Dynamic Programming), evaluates candidate policies exactly by DP over return Probability Mass Functions (PMFs) on a discretized return grid (with an explicit rounding bound), and refines the surrogate in an anytime loop that reports an explicit upper--lower gap (certificate) for the target objective up to discretization budgets. Across tested benchmarks, ERQDP returns certified solutions or explicit residual gaps, enables fast risk-parameter sweeps with substantial runtime gains, and supports both risk-averse and risk-seeking behaviors.

## Metadata
- **Published**: 2026-07-22T08:44:25Z
- **Authors**:  Irmaan,  Mirzanejad, Nadjet Bourdache, Abdel-Illah Mouaddib
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19914v1)