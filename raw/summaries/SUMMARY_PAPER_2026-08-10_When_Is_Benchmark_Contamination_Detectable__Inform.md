---
title: When Is Benchmark Contamination Detectable? Information Limits and Power-Calibrated Audits
url: http://arxiv.org/abs/2608.07914v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_04-41-36Z_WhenIsBenchmarkContaminationDetectable_Information.md
generated_at: 2026-08-10 22:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper formalizes the distinction between a benchmark being clean versus contaminated by an unknown fraction alpha of items seen during training, and between a detector lacking power due to insufficient sample size. It derives that detectability scales with alpha times behavioral separability rho times sqrt(m), and shows that any scalar detector’s efficacy is bounded by rho and can be estimated from controls before the audit. Empirically, calibrated efficacy predicts held‑out power curves well, but the inversion of a Gaussian budget fails at small sample sizes, leading to vacuous non‑rejections.

## Key Takeaways
- Detectability is governed by alpha * rho * sqrt(m), where rho^2 = chi^2(P_1 || P_0) measures how different the seen and clean distributions are.  
- The efficacy of any scalar detector satisfies |E_1 f - E_0 f| / sqrt(Var_0(f)) ≤ rho, which can be estimated from matched controls without needing an orientation assumption.  
- A two‑stage planner that simulates the deployed test repairs budgets and abstains when its probe does not transport provides a valid but vacuous certificate at audit scale.

## Context
Benchmark contamination detection is crucial for ensuring AI models are evaluated on truly unseen data, preserving fairness and reliability. Current methods often rely on orientation assumptions or calibrated efficacy that break down in small audits, leading to misleading non‑rejection signals.

## Implications
For practitioners, audits must incorporate both efficacy budgets and validity gates to avoid vacuous certificates; otherwise a “no evidence” result may be uninterpretable. A calibrated two‑stage planner offers a practical solution but remains conservative at audit scale.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07914v1)
