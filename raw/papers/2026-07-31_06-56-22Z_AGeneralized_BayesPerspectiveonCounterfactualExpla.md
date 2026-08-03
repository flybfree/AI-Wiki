---
title: A Generalized-Bayes Perspective on Counterfactual Explanations: Posterior-Based Decision-Making and Evaluation
published: 2026-07-31T06:56:22Z
authors: Keita Kinjo
url: http://arxiv.org/abs/2607.29077v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Generalized-Bayes Perspective on Counterfactual Explanations: Posterior-Based Decision-Making and Evaluation

## Abstract
Counterfactual explanations (CEs) enhance the interpretability of machine learning models by identifying the smallest change to an input required to obtain a desired output. Although CEs are conventionally formulated as a distance-minimization problem, the theoretical basis of this formulation has received limited attention. We show that a distance-minimization-based CE is mathematically equivalent to the maximum a posteriori (MAP) estimate of a Gibbs posterior within the generalized Bayes framework, specifically when a distance-based prior is used. We call this formulation the Distance-Prior Generalized Bayes CE (DP-GBCE). Building on this posterior perspective, we introduce two decision rules beyond MAP within a unified framework: a Bayes decision that minimizes expected decision loss and CVaR-CE, a risk-averse decision rule. We also propose an extension that uses Bayesian model weights to mix the posterior distributions of multiple models, thereby accounting for model multiplicity, where several models have comparable predictive performance. Finally, we define metrics for evaluating both individual CEs and the posterior distribution as a whole, and use experiments on simulated data and Google Trends data to quantify the trade-offs among the decision rules.

## Metadata
- **Published**: 2026-07-31T06:56:22Z
- **Authors**: Keita Kinjo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29077v1)