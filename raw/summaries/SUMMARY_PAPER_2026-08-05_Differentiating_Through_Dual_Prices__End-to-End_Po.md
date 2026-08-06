---
title: Differentiating Through Dual Prices: End-to-End Policy Learning Under Capacity Constraints
url: http://arxiv.org/abs/2608.04669v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_10-28-21Z_DifferentiatingThroughDualPrices_End_to_EndPolicyL.md
generated_at: 2026-08-05 22:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes an end‑to‑end learning framework for allocating scarce social resources when arrivals are sequential and capacities must be respected. Instead of fitting outcome models blindly, it differentiates dual prices to estimate the value of the deployed policy while training the models jointly. The authors evaluate both exact nonconvex formulations and a convex relaxation that guarantees expected compliance with capacity constraints.

## Key Takeaways
- Dual price differentiation enables an off‑policy estimate of the policy’s value without separate outcome models, improving alignment with resource limits.
- A convex relaxation ensures capacity constraints are satisfied in expectation, with suboptimality bounded by temperature and logarithmic terms in arms.
- In simulation across six datasets, including a hospital cohort of seventy thousand patients, end‑to‑end methods outperform decision‑blind baselines, especially when capacities are binding.

## Context
This work addresses the challenge of learning allocation policies from observational data where real‑time decisions affect long‑term resource usage. By integrating value estimation with capacity constraints, it moves beyond traditional regression pipelines that ignore feasibility, reflecting broader AI concerns about responsible and efficient decision making in constrained environments.

## Implications
For practitioners managing limited medical or housing interventions, the approach offers a more accurate estimate of policy impact while guaranteeing operational limits are respected. The method can be deployed to reduce queueing delays and improve equity, highlighting a practical pathway for scalable, constraint‑aware AI in healthcare and social services.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04669v1)
