---
title: Do Time-Series Forecasters Use the Right History: Recoverability, Recovery, and Functional Use of Temporal Delays
url: http://arxiv.org/abs/2608.10433v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_03-30-36Z_DoTime_SeriesForecastersUsetheRightHistory_Recover.md
generated_at: 2026-08-11 22:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether time‑series forecasters can correctly identify the lag used to generate a prediction. It introduces recoverability measures that separate genuine ambiguity from model error, shows that a predictor can report the right delay while still using an incorrect history, and demonstrates that among high‑quality forecasts with correct delay reports only a minority actually use the reported past.

## Key Takeaways
- The study derives input‑conditioned recoverability metrics that distinguish intrinsic uncertainty from model mistakes. 
- A model may produce arbitrarily reliable delay reports yet still generate forecasts close to the oracle while ignoring the true history, as shown in finite‑sample point‑delay tasks where 55.4% of N‑HiTS and 92.7% of TCN cases use a reported history that is functionally unused under masking tests. 
- Routing predictions through the reported history eliminates off‑report bypass paths; a one‑hot control achieves exact fixed‑report alignment.

## Context
Time‑series forecasting often relies on explicit delay structures, yet current models may misalign their internal computation with the declared lag. This disconnect can lead to misleading diagnostics and suboptimal routing of information in downstream systems.

## Implications
For practitioners, relying solely on reported delays is insufficient; they must verify that forecasts actually incorporate the intended history. Aligning model behavior with delay reports improves trustworthiness and enables correct data‑driven routing in AI pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10433v1)
