---
title: End-to-End Fairness Optimization with Fair Decision-Focused Learning
published: 2026-07-31T14:07:43Z
authors: Yu Wang,  Violet,  Chen
url: http://arxiv.org/abs/2607.29441v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# End-to-End Fairness Optimization with Fair Decision-Focused Learning

## Abstract
Many real-world systems rely on predictive models to inform decisions, and fairness concerns arise in both the prediction and decision stages. We introduce end-to-end fairness optimization (E2EFO) as a unifying framework that integrates fairness across the prediction-to-decision pipeline. We focus on resource allocation with group-based fairness: the prediction task estimates allocation impacts while limiting accuracy disparity across groups, and the decision task distributes those impacts equitably by optimizing a group-based alpha-fairness measure. Within this framework, we propose fair decision-focused learning (FDFL), a training paradigm that jointly accounts for prediction accuracy, prediction fairness, and decision regret -- the loss in decision fairness due to imperfect predictions. FDFL trains the predictor by gradient descent, combining the objective gradients through multi-task learning techniques. The core computational challenge is the decision Jacobian with respect to the predictor parameters: we derive exact closed-form formulas for a tractable class of fair allocation and apply a differentiable optimization layer in the general case. We further establish a finite-sample generalization bound for the scalarized FDFL objective. Numerical experiments on a healthcare-based single resource allocation and a synthetic multiple resource allocation illustrate the value of jointly accounting for prediction fairness and decision fairness in prediction-informed decision-making.

## Metadata
- **Published**: 2026-07-31T14:07:43Z
- **Authors**: Yu Wang,  Violet,  Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29441v1)