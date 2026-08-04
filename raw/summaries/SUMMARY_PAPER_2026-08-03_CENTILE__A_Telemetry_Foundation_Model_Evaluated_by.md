---
title: CENTILE: A Telemetry Foundation Model Evaluated by the Decisions It Drives
url: http://arxiv.org/abs/2608.01725v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_05-45-19Z_CENTILE_ATelemetryFoundationModelEvaluatedbytheDec.md
generated_at: 2026-08-03 23:31
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CENTILE, a telemetry foundation model that replaces per‑task predictors with a single pretrained generative model. Experiments on HPC job logs and network traffic show it reduces the mean bounded slowdown of backfilling by up to 77 % and halves rule violation rates compared with deployed user estimates.

## Key Takeaways
- CENTILE treats telemetry as event‑driven streams, allowing flexible forecast horizons without future timestamps.  
- The model’s runtime estimator transfers zero‑shot across months and pretrained weights across domains within hours of target data.  
- It improves both HPC scheduling decisions and network provisioning under replay, lowering error that previously saturated simple baselines.

## Context
Telemetry systems generate massive irregular event streams but rely on separate models for each decision task, limiting scalability and performance. Recent advances in foundation models aim to unify these tasks into a single system, yet few have demonstrated real‑world impact beyond controlled benchmarks.

## Implications
For operators, CENTILE offers a practical path to lower operational costs and higher reliability by aligning forecasts with actual decisions. Practitioners can adopt the model across domains without extensive retraining, accelerating deployment of smarter telemetry pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01725v1)
