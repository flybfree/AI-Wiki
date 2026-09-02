---
title: LEAP: Likelihood Elicitation and Aggregation for LLM-based Probabilistic Forecasting
url: http://arxiv.org/abs/2609.01337v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_14-49-19Z_LEAP_LikelihoodElicitationandAggregationforLLM_bas.md
generated_at: 2026-09-01 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces LEAP, a framework that reorganizes evidence usage in LLM‑based probabilistic forecasting to improve transparency and uncertainty handling. Experiments on a benchmark of forecasting, information‑seeking, and browsing tasks show that LEAP outperforms monolithic prediction designs across multiple models while maintaining reproducibility.

## Key Takeaways
- LEAP examines each evidence item separately, generating likelihood parameters that quantify its impact on the target outcome.  
- A deterministic probabilistic model combines these individual likelihoods with an explicit prior to produce a posterior distribution for continuous or single‑choice forecasts.  
- The approach supports multi‑choice predictions and preserves clear contributions from each piece of evidence.

## Context
Current LLM forecasting systems often treat all collected evidence as a single input, leading to opaque decision processes and collapsed uncertainty. This monolithic design hampers interpretability and limits the ability to calibrate forecasts under varying inference budgets or prior access.

## Implications
LEAP offers practitioners a more interpretable pipeline that can be integrated into agent loops without sacrificing performance. By decoupling evidence processing from final aggregation, it enables better calibration in real‑world applications such as finance and sports analytics, encouraging adoption of transparent probabilistic forecasting tools.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01337v1)
