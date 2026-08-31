---
title: Coverage, Not Credit: Failure-Credit Routing of Zeroth-Order Perturbation Budgets Does Not Improve On-Pool Sample Efficiency for LLM Agents
url: http://arxiv.org/abs/2608.28011v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_07-27-02Z_Coverage_NotCredit_Failure_CreditRoutingofZeroth_O.md
generated_at: 2026-08-30 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether failure‑credit routing of a fixed zeroth‑order perturbation budget improves sample efficiency for LLM agents compared to uniform allocation, using synthetic tasks and frozen models. The study evaluates six allocation schemes across three task families, using paired seeds and exact sign‑flip tests.

## Key Takeaways
- Uniform allocation yields no statistically detectable gain; the joint soft-plus-sigma scheme is within ±0.02 AUC of uniform on 1.5B/3B.
- Concentrating the full budget on the credit argmax matches uniform only when that module is the verified bottleneck, otherwise it worsens performance.
- Inverse‑propensity debiasing and misrouting incur up to -0.118 end‑to‑end AUC loss; loss is linear in bottleneck starvation rate (R^2 = 0.94).
- Loss is linear in bottleneck starvation rate (R^2 = 0.94).  

## Context
This work addresses a longstanding challenge in LLM agent training where on‑pool sample efficiency is measured under fixed perturbation budgets; prior methods often assume uniform exploration but lack empirical evidence of benefit from targeted routing. The synthetic environment mimics real‑world tool use, allowing verification of credit signals without relying on external benchmarks.

## Implications
The findings suggest that allocating resources based on failure credit may not boost overall optimization and could even harm it, urging practitioners to consider simpler allocation schemes and monitor cumulative parameter movement rather than update frequency. For practitioners, this suggests that sophisticated routing may be unnecessary and could lead to wasted compute.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28011v1)
