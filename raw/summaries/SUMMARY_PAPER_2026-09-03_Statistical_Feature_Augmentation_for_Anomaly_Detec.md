---
title: Statistical Feature Augmentation for Anomaly Detection in Dynamic Graphs
url: http://arxiv.org/abs/2609.02965v1
type: paper-summary
date: 2026-09-03
source_paper: 2026-09-02_07-20-54Z_StatisticalFeatureAugmentationforAnomalyDetectioni.md
generated_at: 2026-09-03 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a statistical feature augmentation method to embed behavioral interaction statistics into the input space of deep learning models for anomaly detection on dynamic graphs. Experiments on Reddit, Wikipedia and MOOC datasets show that augmenting raw event streams with engineered features consistently improves detection performance across seven model architectures. The enriched inputs also allow fine‑grained post‑hoc analysis because each statistic occupies a dedicated dimension.

## Key Takeaways
- The method explicitly encodes behavioral interaction statistics such as sender intensity and interaction inertia into the feature vector, providing a direct way to capture short‑term network dynamics.
- Augmentation consistently boosts anomaly detection accuracy compared with models trained on original embeddings alone across multiple datasets and model types.
- Each augmented statistic is represented by its own input dimension, enabling interpretable post‑hoc analysis of which behavioral factors drive anomalies.

## Context
Dynamic graph data are increasingly common in social media, logistics and education platforms where temporal changes affect network structure. Standard deep learning models often fail to capture rapid interaction patterns without explicit feature engineering, limiting their utility for real‑time anomaly detection tasks.

## Implications
This approach bridges classical network analysis with modern deep learning by turning raw event streams into interpretable statistical features. Practitioners can thus deploy robust anomaly detectors that are both accurate and explainable, supporting regulatory compliance and operational decision making in dynamic environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02965v1)
