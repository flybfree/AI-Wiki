---
title: MiSS: A Logic-Driven Explanation of Minimal Sufficient Coalitions for Point Cloud Classifiers
url: http://arxiv.org/abs/2607.24074v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_07-17-04Z_MiSS_ALogic_DrivenExplanationofMinimalSufficientCo.md
generated_at: 2026-07-27 23:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
MiSS is a black‑box query based framework that explains point cloud classifiers by identifying minimal sufficient coalitions through perturbation‑relative sufficiency reasoning. The system returns a binary attribution and guarantees the minimum cardinality when its certified search completes.  

## Key Takeaways
- MiSS separates proposal from verification using a weighted MaxSAT procedure with an adaptive heuristic, exact‑size fallback, tightened upper bound, blocking clauses, and a surrogate acquisition learned from oracle evaluations.  
- It employs a blackbox statistical oracle to decide sufficiency solely from prediction queries, avoiding the need for white‑box logical encodings or Boolean feature spaces.  
- Experiments on ModelNet40 and ShapeNet with PointNet and PointMLP classifiers achieve higher precision and coverage than rule‑based baselines while providing explanations faster than exhaustive search.  

## Context
The paper tackles a critical challenge in AI interpretability: explaining complex 3D point cloud classifiers that are often black‑box models without accessible feature spaces. Traditional explainers rely on white‑box encodings or exhaustive searches, which are impractical for real‑time deployment. MiSS offers a data driven alternative that works directly with geometric regions and statistical queries.  

## Implications
For practitioners, MiSS delivers faster, more reliable attributions than exhaustive search, enabling trustworthy AI in applications such as autonomous vehicles and augmented reality. In industry, the method supports regulatory compliance by providing statistically verified explanations, fostering adoption of point cloud vision technologies where safety and transparency are paramount.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24074v1)
