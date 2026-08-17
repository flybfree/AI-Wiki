---
title: On the Brittleness of Maximum Likelihood Estimation for Gaussian Process Hyperparameter Optimization
published: 2026-08-13T21:51:35Z
authors: Tyler R. Johnson, Kian Ben-Jacob, Christopher P. Muller, Ramin Bostanabad
url: http://arxiv.org/abs/2608.13793v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On the Brittleness of Maximum Likelihood Estimation for Gaussian Process Hyperparameter Optimization

## Abstract
Machine learning (ML) has become an indispensable part of modern engineering design workflows. A crucial step in training an ML model is the selection of the loss function which can be systematically formulated via various techniques such as maximum likelihood estimation (MLE) and cross-validation . While MLE is one of the most popular, effective, and intuitive mechanisms for training ML models, it is brittle: if the assumptions underpinning it are not met, the trained ML model may generalize poorly. This brittleness affects even Gaussian processes (GPs) which are widely used in engineering design and are often (incorrectly) presumed to be very robust to overfitting. In this paper, we fundamentally evaluate the brittleness of MLE in the context of training GPs for probabilistic regression or classification tasks. We compare theoretically grounded metrics against MLE and propose practical solutions. Our extensive studies demonstrate the effectiveness of our solutions in downstream design tasks such as Bayesian optimization and provide a blueprint for practitioners to build accurate and robust GPs that can even outperform tabular foundation models in terms of prediction accuracy, uncertainty quantification, and inference cost. Our contributions are publicly available via GitHub at https://github.com/Bostanabad-Research-Group/GP-vs-TabPFN-vs-GPyTorch.

## Metadata
- **Published**: 2026-08-13T21:51:35Z
- **Authors**: Tyler R. Johnson, Kian Ben-Jacob, Christopher P. Muller, Ramin Bostanabad
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13793v1)