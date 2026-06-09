# Summary: 2026-05-06_16-30-48Z_Driver_WM_ADriver_CentricTraffic_ConditionedLatent.md
Saved: 2026-05-07 22:08
Source: 2026-05-06_16-30-48Z_Driver_WM_ADriver_CentricTraffic_ConditionedLatent.md
Model: None

---

## Summary
Driver-WM is a driver-centric latent world model for forecasting in-cabin dynamics during shared-control driving transitions. It conditions internal driver-state rollout on external traffic context while also supporting recognition of behavioral and emotional states.

## Key Takeaways
- Separates external traffic encoding from internal driver-state encoding.
- Uses a gated causal injection mechanism to couple the two streams.
- Works in a compact latent space built from frozen vision-language features.
- Improves long-horizon forecasting and semantic alignment on a multi-task driving benchmark.

## Context
The paper addresses a gap in driving world models, which usually forecast the road environment but not the human-in-the-loop response inside the cabin. That limitation matters for L2/L3 automation and transition safety.

## Implications
The model may support safer shared-control systems by making driver response forecasting more explicit. Its causal conditioning setup also enables controlled interventions for mechanism analysis.

## Original Reference
- Title: Driver-WM: A Driver-Centric Traffic-Conditioned Latent World Model for In-Cabin Dynamics Rollout
- Authors: Haozhuang Chi, Daosheng Qiu, Hao Su, Haochen Liu, Zirui Li, Haoruo Zhang, Chen Lv
- URL: http://arxiv.org/abs/2605.05092v1
- Published: 2026-05-06T16:30:48Z