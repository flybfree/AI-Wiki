---
title: GARLIC: Graph Attention-based Relational Learning of Multivariate Time Series in Intensive Care
url: http://arxiv.org/abs/2608.10969v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_14-29-48Z_GARLIC_GraphAttention_basedRelationalLearningofMul.md
generated_at: 2026-08-11 22:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces GARLIC, a graph attention based relational learning model for multivariate time series in intensive care. It learns to impute missing data and predict outcomes while providing interpretable explanations. On PhysioNet 2012/2019 and MIMIC-III benchmarks it achieves state‑of‑the‑art AUROC and AUPRC.

## Key Takeaways
- GARLIC uses a learnable exponential‑decay encoder to impute missing values in irregularly sampled ICU series, enabling reliable downstream prediction. - The model builds time‑lagged summary graphs that capture inter‑sensor dependencies, allowing the network to fuse global patterns with cross‑dimensional sequential attention. - An alternating decoupled optimization scheme aligns reconstruction and classification objectives, stabilizing training while keeping all attention weights and graph edges interpretable.

## Context
Explainable deep learning for irregularly sampled medical time series remains a challenge because standard models cannot handle missing data or provide transparent explanations. GARLIC addresses this by integrating imputation and attribution within a single end‑to‑end framework, offering a practical alternative to separate preprocessing pipelines.

## Implications
Clinicians can rely on GARLIC’s risk warnings that are grounded in learned attention scores, fostering trust in automated ICU alerts. The architecture’s modular design also suggests transferability to other time‑series domains, expanding its impact beyond intensive care.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10969v1)
