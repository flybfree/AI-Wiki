---
title: Finding the Needle in a Haystack: Test-Time Analog Circuit Representation Adaptation for Bayesian Optimization
published: 2026-08-13T01:09:58Z
authors: Fin Amin, Sounak Dutta, Paul D. Franzon
url: http://arxiv.org/abs/2608.12687v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Finding the Needle in a Haystack: Test-Time Analog Circuit Representation Adaptation for Bayesian Optimization

## Abstract
Bayesian optimization (BO) is a sample-efficient framework for analog circuit topology search, where evaluating each candidate topology can require costly simulation. However, representation-based BO methods typically treat circuit embeddings as fixed after encoder training. This creates a mismatch between representation learning and optimization: embeddings learned to encode or reconstruct circuit structure are not necessarily organized according to the figure of merit (FoM) being optimized. This paper introduces Test-Time Analog Representation Adaptation for Bayesian Optimization (TTARO), an online deep-kernel BO framework that adapts circuit representations throughout the search process. Starting from pretrained circuit embeddings, TTARO jointly learns a nonlinear feature transformation and a Gaussian-process surrogate using the FoM labels of the circuits evaluated so far. Following each new evaluation, TTARO updates the representation and surrogate before selecting the next candidate. We compare TTARO with conventional Gaussian Process-based BO over fixed embeddings and with Deep Kernel Learning (DKL), which learns the representation only from the initial evaluated designs and keeps it fixed throughout the remainder of the search. By continually incorporating newly observed FoM labels into representation learning, TTARO aligns the search space with the optimization objective as BO progresses. In our experiments, TTARO reduces regret AUC by 15.2% on average relative to BO and by 20.7% relative to DKL across 40 encoder/kernel/acquisition settings, outperforming prior art in most settings with reductions as large as 46.7%.

## Metadata
- **Published**: 2026-08-13T01:09:58Z
- **Authors**: Fin Amin, Sounak Dutta, Paul D. Franzon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12687v1)