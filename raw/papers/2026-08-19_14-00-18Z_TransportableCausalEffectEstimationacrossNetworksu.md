---
title: Transportable Causal Effect Estimation across Networks under Interference
published: 2026-08-19T14:00:18Z
authors: Xiaojing Du, Jiuyong Li, Lin Liu, Debo Cheng, Jixue Liu, Thuc Duy Le
url: http://arxiv.org/abs/2608.18932v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Transportable Causal Effect Estimation across Networks under Interference

## Abstract
Estimating causal effects under network interference typically assumes that the network used for training and the network used for deployment coincide. In practice, an intervention is run on one population while the question of interest concerns a different population, and the two generally differ in topology, node-covariate composition, and spillover pathways. Transporting a causal effect across networks is therefore a data-fusion problem that no existing algorithm solves. We employ a selection diagram, extended to the network setting so that covariate shift and structural network shift enter as separate selectors, and derive from it a transport formula for the direct, spillover, and total effects in the deployment population. Each formula makes explicit which interventional mechanism is assumed invariant and which observational distribution must be reweighted. We then turn the formulas into TranCE (Transported Causal Effects), a doubly-robust algorithm combining an interventional outcome model, a domain density-ratio correction, and cross-fitted inference. Extensive experiments on two semi-synthetic benchmarks derived from real-world social networks and on a fully real weather-insurance field experiment, where the transported effects are checked against held-out randomized estimates, confirm the effectiveness of our approach. Our findings have the potential to improve intervention strategies in networked systems, particularly in social networks and public health.

## Metadata
- **Published**: 2026-08-19T14:00:18Z
- **Authors**: Xiaojing Du, Jiuyong Li, Lin Liu, Debo Cheng, Jixue Liu, Thuc Duy Le
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.18932v1)