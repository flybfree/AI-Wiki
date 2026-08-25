---
title: Two-level domain-decomposition AdaGrad method for scalable training of graph neural networks
published: 2026-08-23T19:54:30Z
authors: Laurynas Varnas, Julien Herrmann, Alexander Heinlein, Serge Gratton, Alena Kopaničáková
url: http://arxiv.org/abs/2608.22575v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Two-level domain-decomposition AdaGrad method for scalable training of graph neural networks

## Abstract
Graph neural networks (GNNs) have emerged as a powerful framework for learning from graph-structured data. However, their efficient training remains challenging, particularly in distributed computing environments. This challenge arises from the use of message passing, which couples all graph nodes, leading to expensive optimization steps, high memory requirements, and substantial communication overhead. To alleviate these limitations, we propose a novel domain-decomposition (DD) variant of AG2m, an AdaGrad method enhanced with second-order curvature information and momentum, denoted by DD-AG2m. The proposed DD-AG2m alternates between AG2m optimization on the original (global) graph and AG2m optimization on the partitioned graphs. To incorporate global information at reduced cost, we further introduce a two-level variant (2DD-AG2m) that performs global optimization steps on a coarse graph obtained by randomly subsampling nodes within each subdomain. Numerical experiments spanning graph classification, node-level regression, and spatiotemporal forecasting tasks demonstrate that the proposed DD methods reduce the computational cost required to achieve the same predictive performance by a factor of 4-8. Moreover, for the fixed computational cost, they improve the predictive performance of GNNs by up to 22% compared with the baseline AG2m.

## Metadata
- **Published**: 2026-08-23T19:54:30Z
- **Authors**: Laurynas Varnas, Julien Herrmann, Alexander Heinlein, Serge Gratton, Alena Kopaničáková
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22575v1)