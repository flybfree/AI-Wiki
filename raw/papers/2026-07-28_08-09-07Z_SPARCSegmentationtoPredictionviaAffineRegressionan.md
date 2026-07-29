---
title: SPARC Segmentation to Prediction via Affine Regression and Counterfactuals
published: 2026-07-28T08:09:07Z
authors:  Shivani, Subhayan Roy
url: http://arxiv.org/abs/2607.25413v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SPARC Segmentation to Prediction via Affine Regression and Counterfactuals

## Abstract
Transaction propensity prediction in B2B e commerce presents unique challenges distinct from B2C contexts, primarily due to the heterogeneous procurement behaviors of organizational entities, which violate SMOTE's implicit assumption of within class feature homogeneity. Specifically, B2B buyers exhibit multi modal procurement cycles that render linear interpolation between minority class samples structurally invalid, producing synthetic data that does not represent real purchasing behavior. This paper introduces a production deployed propensity modeling framework designed to address these complexities through two primary contributions. First, we replace conventional SMOTE based augmentation with a synthetic data generation approach leveraging Diverse Counterfactual Explanations (DiCE). This method produces minority class samples with superior distributional fidelity compared to SMOTE, as validated through quantitative proximity analysis and UMAP cluster visualization. Second, we adapt the PyPARC piecewise affine classification framework to generate calibrated propensity probabilities, facilitating the interpretable segmentation of customers into actionable risk tiers. Evaluated on two years of longitudinal data from a large scale B2B e commerce platform with a 1 to 9 class imbalance ratio, the proposed architecture achieves 93.1% precision at a decision threshold of 0.8, a 9.2 percentage point improvement over SMOTE based baselines at the same threshold (83.9%), and a 26.1 point improvement over SMOTE at threshold 0.7 (66.04%), demonstrating consistent superiority across operating points. These results demonstrate the framework's efficacy in enabling high precision marketing campaigns with significant improvements in customer activation and return on investment.

## Metadata
- **Published**: 2026-07-28T08:09:07Z
- **Authors**:  Shivani, Subhayan Roy
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25413v1)