---
title: Order Matters: Improving Domain Adaptation by Reordering Data
published: 2026-05-06T16:20:24Z
authors: Andrea Napoli, Paul White
url: http://arxiv.org/abs/2605.05084v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Order Matters: Improving Domain Adaptation by Reordering Data

## Abstract
Domain shift remains a key challenge in deploying machine learning models to the real world. Unsupervised domain adaptation (UDA) aims to address this by minimising domain discrepancy during training, but the discrepancy estimates suffer from high variance in stochastic settings, which can stifle the theoretical benefits of the method. This paper proposes Optimal Reordering of Data for Error-Reduced Estimation of Discrepancy (ORDERED), a novel unbiased stochastic variance reduction technique which reduces the discrepancy estimation error by optimising the order in which the training data are sampled. We consider two specific domain discrepancy losses (correlation alignment and the maximum mean discrepancy), formulate their stochastic estimation error as a function of the data sampling order, and propose a practical optimisation algorithm. Our simulations demonstrate reduced variance compared to related methods, and experiments on two domain shift image classification benchmarks show improved target domain accuracy.

## Metadata
- **Published**: 2026-05-06T16:20:24Z
- **Authors**: Andrea Napoli, Paul White
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.05084v1)