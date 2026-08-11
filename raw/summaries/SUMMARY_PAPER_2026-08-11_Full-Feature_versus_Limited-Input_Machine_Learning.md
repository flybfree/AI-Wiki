---
title: Full-Feature versus Limited-Input Machine Learning for Residential Energy Estimation: A Comparative Analysis of RECS and ResStock Under Realistic Input Constraints
url: http://arxiv.org/abs/2608.09255v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_08-14-26Z_Full_FeatureversusLimited_InputMachineLearningforR.md
generated_at: 2026-08-11 12:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper compares full‑feature and limited‑input machine learning models for estimating residential energy use across two U.S. datasets: the survey‑based RECS and the simulation‑based ResStock. It finds that CatBoost achieves the highest R2 scores with all features (0.90 for ResStock, 0.73 for RECS) but drops to around 0.61–0.62 when only ten homeowner‑accessible inputs are used, indicating a strong trade‑off between data availability and predictive power.

## Key Takeaways
- The full‑feature CatBoost model reaches R2 = 0.90 on ResStock and R2 = 0.73 on RECS, showing that tree ensembles can capture complex energy patterns when all available variables are used.  
- When restricted to ten low‑burden inputs, performance collapses to R2 ≈ 0.61–0.62, demonstrating that algorithmic complexity cannot fully offset missing physical or behavioral information.  
- A homogeneous ResStock subset benefits from reduced‑input modeling, achieving R2 = 0.85, suggesting targeted approaches can be effective when the population shares similar characteristics.

## Context
The study highlights a persistent challenge in AI for energy estimation: balancing model fidelity with real‑world data constraints. By using tree‑based ensembles on both empirical and synthetic datasets, it provides insights into how feature availability limits predictive accuracy, a concern relevant to scalable deployment of smart‑home and grid‑integration solutions.

## Implications
For practitioners, the results underscore that high‑accuracy models require comprehensive data; otherwise, simplified models may suffice for specific use cases. The findings guide resource allocation in AI research toward robust, low‑input estimators that can operate under realistic constraints without sacrificing essential performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09255v1)
