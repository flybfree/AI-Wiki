---
title: Automated Data Engineering and Feature Selection for the Case Study of Warpage Detection in Fused Deposition Modeling
url: http://arxiv.org/abs/2607.18515v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-20_21-15-12Z_AutomatedDataEngineeringandFeatureSelectionfortheC.md
generated_at: 2026-07-23 23:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces an Automated Data Processing framework that uses reinforcement learning and SHAP XAI to select optimal machine learning models and feature subsets for warpage detection in fused deposition modeling datasets. Across 217 datasets, the method converges to configurations with higher AUC and reward scores than a baseline using all features.

## Key Takeaways
- The framework evaluates model‑feature pairs each episode and updates Q values based on predictive accuracy and F1‑score.
- SHAP XAI generates reduced feature subsets that guide exploration of dimensionality while preserving importance.
- Test‑set AUC improves from 0.9248 to 0.9731 and mean reward rises by over fifty percent compared with full‑feature baseline.

## Context
In additive manufacturing, accurate warpage detection is critical for product quality and process optimization. Current approaches often rely on manual feature selection or fixed models, limiting adaptability to new datasets.

## Implications
The ADP framework offers a scalable method for automated model tuning that can be applied beyond FDM to other manufacturing processes. It reduces development time and improves reliability by aligning features with predictive performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18515v1)
