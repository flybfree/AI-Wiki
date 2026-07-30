---
title: From Unsupervised Subgroups to Hypothetical State-Intervention Policies: An Evaluation of Selected Subgrouping Methods in Observational Health Data
published: 2026-07-29T06:41:56Z
authors: Vasundhara Acharya, Bulent Yener
url: http://arxiv.org/abs/2607.26521v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Unsupervised Subgroups to Hypothetical State-Intervention Policies: An Evaluation of Selected Subgrouping Methods in Observational Health Data

## Abstract
Conventional subgroup analyses can yield unstable and difficult-to-interpret conclusions, especially in observational biomedical data where each individual is observed under only one exposure state, true individual treatment effects are unavailable, and causal structure is uncertain. We investigate whether subgroups constructed from pretreatment characteristics, without using exposure, outcome, or estimated treatment-effect information, can serve as interpretable units for budget-constrained policy prioritization. We propose a framework combining causal-discovery-informed covariate selection, discovery-evaluation sample splitting, inductive unsupervised clustering, uncertainty-aware subgroup selection, and held-out doubly robust policy evaluation. We compare K-means, hard, membership-weighted, and stochastic Fuzzy C-means, Bayesian Gaussian mixture models, and a supervised causal-forest-derived CATE-tree comparator. Policies are evaluated under a 70% budget for hypothetical obesity-to-non-obesity and elevated-to-lower-glucose state shifts in the PIMA Indians Diabetes dataset and for a lifetime-smoking-history contrast in NHANES. The highest estimated ungated utilities were 0.799 for the BMI policy using Bayesian GMM, 0.735 for the glucose policy using hard or membership-weighted FCM, and 0.775 for the smoking-history policy using K-means. All paired 95% confidence intervals for policy-risk differences included zero, and no comparison remained statistically significant after Holm adjustment. Bayesian pooling generally preserved ungated allocations, whereas Empirical Bernstein gating was more conservative. Policies with similar estimated utility could nevertheless prioritize different individuals. The findings should be interpreted as assumption-dependent decision-support evidence for hypothetical state contrasts rather than proof of intervention benefit.

## Metadata
- **Published**: 2026-07-29T06:41:56Z
- **Authors**: Vasundhara Acharya, Bulent Yener
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26521v1)