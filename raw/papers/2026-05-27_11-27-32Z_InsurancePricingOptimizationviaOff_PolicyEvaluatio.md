---
title: Insurance Pricing Optimization via Off-Policy Evaluation
published: 2026-05-27T11:27:32Z
authors: Sascha Günther, Dimitri Semenovich, Mario V. Wüthrich
url: http://arxiv.org/abs/2605.28327v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Insurance Pricing Optimization via Off-Policy Evaluation

## Abstract
Traditional insurance pricing relies on risk-based principles that ensure actuarial fairness and solvency but do not explicitly account for policyholders' price sensitivity. We formulate insurance pricing as a decision-making problem and study it using tools from off-policy evaluation and stochastic control. We propose a kernelized inverse propensity score estimator that exploits local structure in the action space and yields variance reduction compared to the classical inverse propensity score estimator. Building on these value estimates, we investigate policy optimization and present two practical approaches for computing optimal pricing rules: an interpretable data-shared Lasso formulation and a flexible policy parameterization based on neural networks. Using a controlled synthetic travel insurance environment, we empirically confirm the theoretical results and show that neural networks outperform existing techniques for policy optimization.

## Metadata
- **Published**: 2026-05-27T11:27:32Z
- **Authors**: Sascha Günther, Dimitri Semenovich, Mario V. Wüthrich
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.28327v1)