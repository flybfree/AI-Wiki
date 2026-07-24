---
title: Adaptive Bayesian Online Learning via Expert Aggregation
published: 2026-07-22T14:59:09Z
authors: Jungbin Jun, Ilsang Ohn
url: http://arxiv.org/abs/2607.20239v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adaptive Bayesian Online Learning via Expert Aggregation

## Abstract
Bayesian online learning promises uncertainty-aware prediction on data streams, but its performance hinges on inferential choices, including learning rates, prior distributions and variational families, which are usually fixed before seeing the stream. We address this by treating Bayesian update rules as experts and aggregating the Bayesian experts according to sequential predictive losses. We prove that the resulting aggregate competes with the best expert in hindsight at an aggregation cost determined by how each expert's per-round performance is evaluated. We instantiate the framework in online conformal inference and Gaussian process regression. The conformal inference application yields a smoothed Bayesian counterpart of adaptive conformal inference with long-run randomized coverage, while the Gaussian process application gives an oracle inequality in cumulative predictive Kullback-Leibler risk and adaptation to unknown Hölder smoothness up to logarithmic factors. Experiments show that the aggregate tracks strong experts without oracle expert selection.

## Metadata
- **Published**: 2026-07-22T14:59:09Z
- **Authors**: Jungbin Jun, Ilsang Ohn
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20239v1)