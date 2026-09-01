---
title: Explainable Machine Learning for Broadband Adoption Disparities: Tract-Level Prediction and SHAP-Based Factor Profiling
published: 2026-08-29T07:39:08Z
authors: Xiao Han
url: http://arxiv.org/abs/2608.29110v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Explainable Machine Learning for Broadband Adoption Disparities: Tract-Level Prediction and SHAP-Based Factor Profiling

## Abstract
The United States has allocated approximately $65 billion through the Infrastructure Investment and Jobs Act for broadband expansion, yet evidence-based methods for targeting these investments remain underdeveloped. This paper presents an explainable machine learning framework for profiling broadband adoption disparities at census-tract granularity across 83,359 tracts nationwide. Using 65 socioeconomic, demographic, and infrastructure features derived from the American Community Survey 2022, we train a LightGBM model under spatial five-fold cross-validation, achieving R^2 = 0.533 and Spearman rho = 0.763; state-held-out cross-validation (51 folds) confirms generalization (R^2 = 0.525). TreeSHAP analysis identifies income and education as the dominant factor group (with the engineered interaction term absorbing attribution from its constituent features), and SHAP-based clustering reveals three exploratory factor profiles: Well-Connected Moderate (~49K tracts), Affordability-Limited Severe (~21K tracts), and Rural-Elderly (~13K tracts). As a screening tool, ML-based tract selection captures 38.0% of the total adoption gap within the top 10% of tracts versus 35.2% for income-only heuristics (+2.8 pp, p < 0.002, county-block bootstrap); in regret-reduction terms, the model closes 19% of the remaining gap between income-only and oracle selection. The primary contribution is the per-tract factor decomposition: SHAP identifies which feature groups (income/education, rurality, age) are most strongly associated with each tract's predicted gap, and informs differentiated investigation. A temporal stability check, training on ACS 2017 and predicting ACS 2022 with zero survey-year overlap, confirms ranking stability (rho = 0.784, noting hyperparameters tuned on 2022 data).

## Metadata
- **Published**: 2026-08-29T07:39:08Z
- **Authors**: Xiao Han
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29110v1)