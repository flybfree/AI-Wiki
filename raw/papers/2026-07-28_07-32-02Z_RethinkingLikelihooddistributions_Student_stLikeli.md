---
title: Rethinking Likelihood distributions: Student's t Likelihood Boosts Bayesian Neural Network Performance
published: 2026-07-28T07:32:02Z
authors: Pei-Hsuan Hsia, Lars H. Heyen, Arvid Weyrauch, Markus Goetz, Achim Streit, Sebastian Krumscheid, Charlotte Debus
url: http://arxiv.org/abs/2607.25376v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Rethinking Likelihood distributions: Student's t Likelihood Boosts Bayesian Neural Network Performance

## Abstract
In Bayesian neural networks (BNNs), variational inference is a widely adopted framework for modeling uncertainty in a distributional way, with the evidence lower bound (ELBO) serving as the standard objective function. Several distributions contribute to the ELBO loss, such as the prior, approximated posterior, and likelihood distribution. Typically, these distributions are all approximated by a Gaussian distribution, since it is easy to compute, allows for reparameterized gradients, and provides a closed-form loss for training. However, several works have highlighted that this assumption may not generally hold, posing the risk of model misspecification. Alternative distributions have been proposed for the prior specifically, while the effect of distribution choice on the likelihood distribution remains unexplored. In this work, our aim is to close this gap by investigating whether alternative assumptions for the likelihood distribution can outperform the commonly used Gaussian. We compare several likelihood distribution assumptions, such as skewed or heavy-tailed, across regression tasks on both artificial and real-world datasets using standard multilayer perceptrons (MLPs). Our findings demonstrate that Student's t yields better predictive performance than a Gaussian likelihood distribution, independent of the data distribution and MLP architecture (depth and width). In some cases, Student's t can also lead to shorter training times, while still being easy to implement.

## Metadata
- **Published**: 2026-07-28T07:32:02Z
- **Authors**: Pei-Hsuan Hsia, Lars H. Heyen, Arvid Weyrauch, Markus Goetz, Achim Streit, Sebastian Krumscheid, Charlotte Debus
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25376v1)