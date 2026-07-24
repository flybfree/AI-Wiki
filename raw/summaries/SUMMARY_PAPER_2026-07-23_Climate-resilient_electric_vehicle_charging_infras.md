---
title: Climate-resilient electric vehicle charging infrastructure for sustainable cities: An interpretable causal-ensemble framework for preventive maintenance and low-carbon mobility
url: http://arxiv.org/abs/2607.21444v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-23_15-51-08Z_Climate_resilientelectricvehiclecharginginfrastruc.md
generated_at: 2026-07-23 23:20
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FGDSE, a feature‑governed dynamic stacking ensemble that predicts EV charging fault risk up to 30 days ahead and supports preventive maintenance. On 25 months of data from 13 stations it outperforms twelve baselines beyond ten days, maintains high macro‑recall at the thirty‑day horizon, and shows climate stress, especially extreme heat, as a key driver of increasing fault probability.

## Key Takeaways
- FGDSE achieves superior performance across short and long horizons by combining domain‑expert models with deep temporal experts for short‑term pulses and long‑term degradation.  
- The model’s SHAP attribution reveals that extreme heat is the sole exposure whose causal effect grows over time, flagging about 30 % of posts as heat‑sensitive.  
- Quantitative thresholds derived from the X‑learner enable climate‑adaptive maintenance strategies that preserve low‑carbon mobility.

## Context
This work advances AI for infrastructure resilience by integrating heterogeneous signals across physical, behavioral, contextual and historical domains into an interpretable ensemble framework. It demonstrates how causal‑ensemble methods can translate probabilistic forecasts into actionable treatment effects for real‑world asset management.

## Implications
Practitioners can use FGDSE’s thresholds to schedule maintenance before failures occur, reducing downtime and carbon emissions. The approach offers a scalable template for other climate‑resilient services that rely on long‑term prediction and causal insight.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.21444v1)
