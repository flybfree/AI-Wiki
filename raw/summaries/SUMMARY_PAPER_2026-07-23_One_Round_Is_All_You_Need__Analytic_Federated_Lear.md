---
title: One Round Is All You Need: Analytic Federated Learning for Task-Heterogeneous Multi-Label Medical Image Classification
url: http://arxiv.org/abs/2607.20641v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_18-11-37Z_OneRoundIsAllYouNeed_AnalyticFederatedLearningforT.md
generated_at: 2026-07-23 23:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces an analytic federated learning framework for multi‑label medical image classification that handles task heterogeneity where each clinical site only annotates a subset of disease categories. By replacing iterative gradient updates with three closed‑form operations, the method achieves convergence in at most two communication rounds and eliminates systematic false‑negative bias caused by missing labels.

## Key Takeaways
- The balanced label projection normalizes positive and negative contributions across all classes, ensuring each class contributes equally to the model’s total mass regardless of how many sites observe it.  
- A per‑class absolute aggregation law computes an optimal ridge‑regression classifier for each disease category using only the sufficient statistics uploaded by annotating clients, thus isolating class‑specific learning without interference from other labels.  
- An optional analytic pseudo‑label refinement round uses a confidence‑filtered teacher model to provide missing‑class information to non‑annotating sites, improving performance without additional communication.

## Context
Federated learning is increasingly vital for collaborative health data research because it preserves patient privacy while enabling large‑scale model improvement. However, real‑world medical datasets often exhibit task heterogeneity, a challenge that most existing FL algorithms struggle to address analytically and computationally.

## Implications
The proposed approach offers clinicians and researchers a practical solution that reduces communication overhead dramatically, accelerating deployment of multi‑label diagnostic models across diverse institutions. This efficiency can lower costs, shorten training timelines, and improve model accuracy, making federated learning more accessible in resource‑constrained healthcare settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20641v1)
