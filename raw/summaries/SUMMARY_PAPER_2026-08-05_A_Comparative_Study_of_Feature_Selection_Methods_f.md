---
title: A Comparative Study of Feature Selection Methods for EHR Diagnosis Codes in Opioid Use Disorder Prediction
url: http://arxiv.org/abs/2608.04180v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_19-37-29Z_AComparativeStudyofFeatureSelectionMethodsforEHRDi.md
generated_at: 2026-08-05 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper evaluates five feature selection methods for predicting opioid use disorder from electronic health record diagnosis codes, focusing on recurrence enrichment, NTK-motivated early gradient sensitivity, LightGBM‑SHAP, Elastic Net, and LLM‑guided semantic selection. The study finds that NTK sensitivity offers the best balance of predictive accuracy and stability across resampling, while LLM guidance adds clinically relevant signals despite lower standalone performance.

## Key Takeaways
- NTK‑motivated early gradient sensitivity delivers the highest overall performance with consistent results across multiple resampling runs, indicating strong model robustness.  
- Recurrence enrichment improves prediction when larger feature budgets are used but shows diminishing returns beyond a moderate size, highlighting the trade‑off between complexity and utility.  
- LLM‑guided semantic selection captures rare diagnosis codes that other methods miss, providing clinically meaningful insights even though its predictive score is lower.

## Context
Feature selection remains a bottleneck in EHR‑driven AI because raw records contain thousands of sparse, overlapping codes. Recent advances in gradient‑based and language models offer new ways to prune this noise, yet few studies compare them under the same clinical prediction framework.

## Implications
Clinicians can rely on NTK methods for reliable, high‑accuracy OUD predictions without overfitting, while LLM guidance should be used as an auxiliary tool to surface rare but important diagnoses. This dual approach could enhance both model performance and interpretability in real‑world healthcare settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04180v1)
