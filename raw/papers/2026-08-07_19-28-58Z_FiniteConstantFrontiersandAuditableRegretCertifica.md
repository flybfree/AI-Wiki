---
title: Finite Constant Frontiers and Auditable Regret Certificates for Average-Reward Reinforcement Learning
published: 2026-08-07T19:28:58Z
authors: Ibne Farabi Shihab, Abu Sa-Adat Mohamed Moon-Im Al Ahsan, Md Najmus Swaqeeb
url: http://arxiv.org/abs/2608.07725v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Finite Constant Frontiers and Auditable Regret Certificates for Average-Reward Reinforcement Learning

## Abstract
Average-reward reinforcement-learning regret is known up to logarithmic factors, but the numerical content of published guarantees is difficult to compare because probability mode, structural parameter, logarithmic normalization, prior information, and planning assumptions differ. We introduce a constant-aware comparison protocol and derive an explicit finite lower certificate for communicating MDPs. The construction is a binary tree of two-state blocks; its proof uses exact trajectory-level Bernoulli KL divergence and keeps action budget, diameter, occupancy, navigation cost, and terminal bias explicit. A common closed-form envelope improves the published coefficient $0.015$ across a finite frontier: $0.0200$ in a moderate regime and up to $0.0291$ under stronger action, diameter, and horizon conditions, a $94\%$ increase. The limiting coefficient is $\frac1{32}\sqrt{(A-3)/A}$. For upper bounds, we give an auditable composition rule for a span-constrained optimistic learner, but do not claim a coefficient while adaptive directional-variance and planning certificates remain open. We also formalize valid expectation conversion and constant comparability. Controlled diagnostics test diameter dependence, bonus-by-width interactions, span misspecification, and the finite lower certificate on its exact family.

## Metadata
- **Published**: 2026-08-07T19:28:58Z
- **Authors**: Ibne Farabi Shihab, Abu Sa-Adat Mohamed Moon-Im Al Ahsan, Md Najmus Swaqeeb
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07725v1)