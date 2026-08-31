---
title: Coverage, Not Credit: Failure-Credit Routing of Zeroth-Order Perturbation Budgets Does Not Improve On-Pool Sample Efficiency for LLM Agents
published: 2026-08-28T07:27:02Z
authors: Yuxu Ge
url: http://arxiv.org/abs/2608.28011v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Coverage, Not Credit: Failure-Credit Routing of Zeroth-Order Perturbation Budgets Does Not Improve On-Pool Sample Efficiency for LLM Agents

## Abstract
Trajectory-level credit assignment can localize which module of a tool-using LLM agent causes failures using only verifiable signals. We ask whether such failure credit should route a fixed zeroth-order/evolution-strategies (ZO/ES) perturbation budget. Across a synthetic environment and frozen Qwen2.5-1.5B/3B and SmolLM2-1.7B agents, three task families, six allocation schemes, a credit-noise sweep, paired seeds, and exact sign-flip tests, we find no statistically detectable improvement over uniform allocation in any on-pool comparison (no gain of at least 2 percentage points). The joint soft-plus-sigma scheme is equivalent to uniform within a +/- 0.02 AUC margin on 1.5B and 3B; concentrating the full budget on the credit argmax is marginally equivalent on 1.5B, where that module is the verified bottleneck, and significantly worse on 3B. Inverse-propensity debiasing does not rescue routing, and misrouting costs up to -0.074 AUC in-house and -0.118 end-to-end on the BFCL-derived family. Across six fixed-step schedules, loss is linear in bottleneck starvation rate (R^2 = 0.94, descriptive), and a preregistered credit-free coverage floor removes detected harm. Matched-budget burst and step-compensating catch-up schedules are consistent with harm arising from insufficient cumulative parameter movement rather than update frequency. Our primary estimand is optimization efficiency on a fixed task pool. On unseen BFCL functions, the study's one exception is that soft routing exceeds uniform on held-out endpoints (+0.047, p = 0.031, n = 6). A plausible but untested reading is that routing-favored caller improvements transfer while uniform's on-pool gains reflect a synthesizer behavior specific to our harness. We report this exception explicitly and document three failure modes that can silently invalidate ZO/ES experiments on frozen LLMs.

## Metadata
- **Published**: 2026-08-28T07:27:02Z
- **Authors**: Yuxu Ge
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28011v1)