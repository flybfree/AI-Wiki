---
title: Expert-Guided Forecast Editing for Time-Series Foundation Models
url: http://arxiv.org/abs/2607.19659v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_01-49-23Z_Expert_GuidedForecastEditingforTime_SeriesFoundati.md
generated_at: 2026-07-23 23:24
model: nvidia/nemotron-3-nano-4b
---

## Summary  
The paper proposes DEFT, an expert-guided forecast editing framework that balances exploitation of a frozen foundation model with structured exploration guided by expensive expert feedback. It demonstrates that DEFT outperforms baseline methods like best‑of‑N and optimization algorithms across multiple datasets and query budgets. The results show improved forecasting accuracy when limited test‑time guidance is applied.  

## Key Takeaways  
- DEFT queries the expert only on complete trajectories, allowing reuse of component‑level scores for trend and seasonal parts, which reduces redundant expert calls while preserving structured feedback.  
- The framework decomposes forecasts into trend and seasonal components before refinement, enabling efficient exploration around predicted samples without reshuffling the whole horizon.  
- Compared to best‑of‑N and other search methods, DEFT consistently yields higher forecast quality under tight query budgets across diverse datasets.  

## Context  
Time‑series foundation models aim to provide universal forecasting capabilities with minimal task‑specific adaptation. However, their static outputs limit integration of expert feedback, which is costly and often sparse in real‑world applications. This paper addresses the gap by introducing a principled editing process that leverages component‑wise scores.  

## Implications  
For practitioners, DEFT offers a scalable way to incorporate expert insight without retraining models, saving computational resources. The approach can be applied across industries where domain experts provide high‑stakes feedback, such as molecular dynamics simulations, and may inspire future work on test‑time adaptation in foundation models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19659v1)
