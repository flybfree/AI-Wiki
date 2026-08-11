---
title: Spatial Heterogeneity-Aware Multi-Hazard Susceptibility and Risk Mapping at Regional Scale
url: http://arxiv.org/abs/2608.08321v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-08_20-16-43Z_SpatialHeterogeneity_AwareMulti_HazardSusceptibili.md
generated_at: 2026-08-11 13:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a spatial heterogeneity‑aware framework to map flood and landslide susceptibility at the regional scale for Kerala and Nepal. It compares two training strategies—proximity‑gated cross‑zone learning (S1) and ecology‑gated zone‑constrained learning (S2)—and finds S1 generally yields higher predictive performance.

## Key Takeaways
- S1’s cross‑zone approach improves flood susceptibility AUC‑ROC from 0.728 to 0.886 in Nepal, raising PR‑AUC from 0.512 to 0.823 while maintaining zone‑specific predictor selection and SHAP rankings.
- Brier scores are lower under S2 for both hazards, preserving ecological differences but limiting overall accuracy gains.
- Bivariate risk‑map agreement is modest (0.521 in Kerala, 0.711 in Nepal), indicating significant disagreement between susceptibility and risk classes.

## Context
This work advances AI‑driven hazard mapping by integrating spatial heterogeneity into model training, a step beyond traditional homogeneous datasets that assume uniform environmental controls across regions.

## Implications
Practitioners can adopt cross‑zone learning to boost regional discrimination when data overlap is high, while zone‑constrained methods remain valuable for preserving local ecological nuances. The findings guide the design of hybrid AI systems that balance accuracy with environmental fidelity in disaster risk assessment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08321v1)
