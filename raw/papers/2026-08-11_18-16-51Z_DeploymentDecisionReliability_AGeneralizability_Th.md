---
title: Deployment Decision Reliability: A Generalizability-Theory Framework for Sizing Long-Horizon Agent Evaluations
published: 2026-08-11T18:16:51Z
authors: Vasundra Srinivasan
url: http://arxiv.org/abs/2608.11323v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Deployment Decision Reliability: A Generalizability-Theory Framework for Sizing Long-Horizon Agent Evaluations

## Abstract
Enterprise practitioners read agent leaderboards as if they ranked agent capability. We show, across three open agent-trace benchmarks (TheAgentCompany, $τ^2$-bench, and AppWorld), that the agent main effect accounts for less than 3% of total variance in every dataset and check type, while the agent-by-task interaction accounts for 7-23%. Leaderboards rank specialization, not capability. We arrive at this through a four-facet Generalizability Theory variance decomposition, fit with three estimators (Henderson Method-I, REML via lme4, and a Bayesian binomial GLMM) that agree to three decimal places. Four further findings sharpen what the leaderboard is hiding. First, aggregate reliability collapses on the hardest task quartile: $Eρ^2$ on $τ^2$ action_checks falls from 0.752 to 0.000. Second, training-cell reliability negatively correlates with held-out reliability ($r = -0.90$ on $τ^2$), meaning the designs that look most reliable replicate worst. Third, population-level diagnostics transfer across enterprise benchmarks (capability-gap ratio stable at 0.35-0.40) but per-family agent rankings invert. Fourth, on the MAST failure taxonomy, trace-level mode profiles are idiosyncratic (MAE = 0.261) while cell-level profiles generalise (MAE = 0.056, $r = 0.83$). We package these into Deployment Decision Reliability (DDR), a one-page reporting discipline that turns the variance-component table into five decisions an enterprise buyer can defend. All code, data loaders, and fit artifacts are released under an open-source license.

## Metadata
- **Published**: 2026-08-11T18:16:51Z
- **Authors**: Vasundra Srinivasan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11323v1)