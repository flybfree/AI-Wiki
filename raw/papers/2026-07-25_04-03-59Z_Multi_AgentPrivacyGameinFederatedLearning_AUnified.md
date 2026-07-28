---
title: Multi-Agent Privacy Game in Federated Learning: A Unified Mean-Field View
published: 2026-07-25T04:03:59Z
authors: Kun Zhao, Xu Chen
url: http://arxiv.org/abs/2607.23029v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Multi-Agent Privacy Game in Federated Learning: A Unified Mean-Field View

## Abstract
Federated learning enables collaborative model training across distributed clients without centralising their data, yet privacy remains a persistent concern because the shared model updates can leak information about local datasets. Existing privacy-preserving methods either inject calibrated noise into client updates, limiting their composition guarantees, or formulate client privacy choices as a multi-agent game whose Nash equilibrium becomes intractable as the number of clients grows. We bridge these two lines of work by formulating privacy-preserving federated learning as a mean-field privacy game: each client strategically chooses its own privacy budget while interacting with the population only through a single mean-field statistic. The mean-field limit yields a tractable equilibrium for arbitrarily many clients, accommodates heterogeneous client preferences, and inherits an exponentially decaying privacy guarantee through a log-Sobolev contraction. The framework recovers the entropic privacy baseline as the homogeneous special case and the multi-agent privacy game as the finite-population case. Experiments on quadratic regression, logistic regression, and MNIST demonstrate that the proposed framework attains the privacy-utility trade-off of the entropic baseline while delivering a personalized privacy guarantee that the homogeneous baseline cannot express.

## Metadata
- **Published**: 2026-07-25T04:03:59Z
- **Authors**: Kun Zhao, Xu Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23029v1)