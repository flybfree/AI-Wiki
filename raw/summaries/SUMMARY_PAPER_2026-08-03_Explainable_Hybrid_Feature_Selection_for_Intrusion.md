---
title: Explainable Hybrid Feature Selection for Intrusion Detection in Internet of Medical Things Environments
url: http://arxiv.org/abs/2608.00869v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_21-10-24Z_ExplainableHybridFeatureSelectionforIntrusionDetec.md
generated_at: 2026-08-03 23:41
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes an intrusion detection system for IoMT networks that uses a two‑stage feature selection process to reduce dimensionality while preserving performance. By applying a Pearson correlation filter followed by a hybrid model‑based and SHAP attribution method, the authors achieve up to 88% reduction in features without sacrificing accuracy or F1-score on benchmark datasets.

## Key Takeaways
- The Pearson correlation filter removes redundant attributes, which is essential for handling heterogeneous medical devices with limited resources. - The hybrid strategy combines model‑based feature importance from Random Forest and LightGBM with SHAP attribution to select a compact subset of features that remains interpretable. - Experiments on CIC‑IoMT 2024 and CIC‑IDS 2017 show the method cuts the feature space by up to 88%, retaining only five features while accuracy and F1-score remain within a few points of full‑feature models.

## Context
Feature selection is a core challenge in AI for edge devices where computational power is scarce. This work demonstrates that explainable methods such as SHAP can be integrated with traditional filters to produce compact, interpretable classifiers suitable for real‑time monitoring in resource‑constrained IoMT environments.

## Implications
Practitioners can deploy these detectors on low‑power medical sensors without sacrificing detection quality, supporting safer and more efficient health‑care networks. The approach also sets a benchmark for explainable feature selection in constrained AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00869v1)
