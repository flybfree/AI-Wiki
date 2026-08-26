---
title: XP-JEPA: Cross-Predictive Physics Grounding for Forecastable Latent Dynamics
url: http://arxiv.org/abs/2608.24044v1
type: paper-summary
date: 2026-08-25
source_paper: 2026-08-25_04-07-07Z_XP_JEPA_Cross_PredictivePhysicsGroundingforForecas.md
generated_at: 2026-08-25 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
XP-JEPA introduces a method that aligns visual latent dynamics with privileged physical trajectories by jointly encoding observations and states through an action‑conditioned predictor. The unified objective reduces rollout drift from 0.361 to 0.104 and lifts mean control success from 53.6 % to 78.2 %, showing that cross‑predictive grounding improves forecastability without requiring privileged inputs at test time.

## Key Takeaways
- The shared action‑conditioned predictor produces predictions for both visual representations and physical states, forcing them to evolve together.
- After training the physical branch is discarded, leaving a purely visual model that can be deployed in rollout‑based control.
- Direct physical‑state regression improves position decodability but does not enhance forecastability or control beyond the baseline.

## Context
This work addresses a longstanding challenge in self‑predictive models where latent dynamics are weakly constrained by physics. By grounding these dynamics in explicit physical trajectories, XP-JEPA demonstrates how shared modeling can bridge perception and actuation without costly privileged inputs.

## Implications
For practitioners, XP-JEPA offers a path to more reliable rollout policies that rely solely on visual data, reducing reliance on external state information. In industry, this could lead to simpler deployment pipelines and lower latency in autonomous control systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.24044v1)
