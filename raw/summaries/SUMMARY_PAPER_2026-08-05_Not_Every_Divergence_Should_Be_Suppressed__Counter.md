---
title: Not Every Divergence Should Be Suppressed: Counterfactual Recoverability in On-Policy Distillation
url: http://arxiv.org/abs/2608.04408v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_03-32-08Z_NotEveryDivergenceShouldBeSuppressed_Counterfactua.md
generated_at: 2026-08-05 22:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a counterfactual recoverability framework for on-policy distillation that decides whether an erroneous prefix can be corrected by replaying the error state through teacher-continuation and rollback branches. It demonstrates that states classified as recoverable improve performance, while irreversible ones degrade it, achieving perfect AUC with the proxy compared to 0.392 using divergence alone.

## Key Takeaways
- Recoverable states yield a mean continuation-minus-rollback effect of 0.185, indicating they benefit from retaining teacher-correctable prefixes.  
- Irreversible-but-avoidable states produce an effect of -1.000, showing that continuing training harms performance and rollback is preferred.  
- A branch-derived recoverability proxy reaches AUC 1.000, outperforming divergence alone at 0.392.

## Context
On-policy distillation aims to transfer knowledge from a teacher model to a student model using only trajectories visited by the student. Traditional methods rely on simple divergence metrics that cannot distinguish between correctable and irreversible errors.

## Implications
This outcome-grounded decision variable enables more effective supervision, leading to stronger performance gains across benchmark suites such as AIME2025, AIME2024-2025 average@32, and GPQA-Diamond. Practitioners can adopt recoverability-aware control to improve model training efficiency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04408v1)
