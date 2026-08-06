---
title: When Shared Rollouts Fail in Defensive Driving Evaluation: A NAVSIM Score Basis Audit
url: http://arxiv.org/abs/2608.04896v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_14-22-23Z_WhenSharedRolloutsFailinDefensiveDrivingEvaluation.md
generated_at: 2026-08-05 20:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how reference‑conditioned forgiveness in defensive driving scores can mask shared rollout failures, leading to inflated compliance credits. It audits NAVSIM v2.2 on a 32‑token diagnostic set and shows that numerical instability from solver refit causes blind probes to outperform human replay. The study identifies that fixing the solver restores proper ordering while keeping forgiveness enabled.

## Key Takeaways
- Reference‑conditioned forgiveness can credit agents for compliance even when both agent and reference share an unstable rollout transformation, causing widespread false credit.
- Numerical instability in the NAVSIM numerical backend, triggered by a solver refit, propagates shared reference failures into compliance scores across blind and route‑aware probes.
- Replacing only the solver eliminates rollout divergence and restores blind‑last ordering while keeping forgiveness enabled.

## Context
Defensive driving evaluation relies on scoring agents based on how well they follow human reference behavior. Traditional benchmarks assume stable rollouts, but real‑world simulations often generate divergent trajectories that break this assumption.

## Implications
If scores are used to claim safety compliance, the audit protocol described here can prevent misleading results by requiring score basis disclosure and rollout stability checks. Practitioners must therefore validate numerical backends before trusting defensive driving metrics.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04896v1)
