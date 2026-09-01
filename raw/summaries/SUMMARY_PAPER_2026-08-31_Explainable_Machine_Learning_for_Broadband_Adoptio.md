---
title: Explainable Machine Learning for Broadband Adoption Disparities: Tract-Level Prediction and SHAP-Based Factor Profiling
url: http://arxiv.org/abs/2608.29110v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-29_07-39-08Z_ExplainableMachineLearningforBroadbandAdoptionDisp.md
generated_at: 2026-08-31 21:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes an explainable machine learning framework that predicts broadband adoption gaps at the census‑tract level using LightGBM and interprets results with SHAP analysis across 83,359 tracts in the United States. The model achieves strong predictive performance (R² = 0.533) and identifies income and education as primary driver groups while revealing three distinct factor profiles of adoption disparity.

## Key Takeaways
- Income and education emerge as the dominant socioeconomic factors shaping broadband gaps, with their interaction term absorbing attribute contributions.  
- SHAP‑based clustering uncovers three tract‑level profiles: Well‑Connected Moderate (~49K tracts), Affordability‑Limited Severe (~21K tracts), and Rural‑Elderly (~13K tracts).  
- The ML‑driven selection captures 38.0 % of the adoption gap in the top 10 % of tracts, outperforming income‑only heuristics by 2.8 percentage points (p < 0.002).

## Context
Explainable AI methods are increasingly used to translate complex predictive models into actionable insights for policy and practice. This work demonstrates how SHAP can decompose feature groups at a granular administrative level, offering a bridge between statistical prediction and targeted intervention.

## Implications
Policymakers can leverage the tract‑level factor profiles to allocate infrastructure investments more efficiently than broad income heuristics. Practitioners gain a transparent tool that highlights which demographic or geographic clusters need prioritized attention, supporting equitable broadband expansion.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29110v1)
