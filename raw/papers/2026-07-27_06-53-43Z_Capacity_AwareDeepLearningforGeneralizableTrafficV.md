---
title: Capacity-Aware Deep Learning for Generalizable Traffic Volume Estimation Across Links and Cities
published: 2026-07-27T06:53:43Z
authors: Léo Hein, Giovanni De Nunzio, Aurélie Pirayre, Laurent Najman
url: http://arxiv.org/abs/2607.24056v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Capacity-Aware Deep Learning for Generalizable Traffic Volume Estimation Across Links and Cities

## Abstract
Network-wide traffic volume estimation typically relies on propagating measurements from fixed sensors, making performance highly dependent on sensor density and limiting deployment in sparsely instrumented networks. We propose a link-level learning framework that estimates hourly traffic volumes from widely available territorial data only, including probe speed profiles, road and topological descriptors, along with weather observations. A supervised local mapping is learned from sparse sensor measurements and evaluated under two generalization settings: intra-network (unseen links within the training network) and inter-network (unseen city). This formulation frames traffic volume estimation as a spatial out-of-distribution generalization problem under sparse supervision. To enhance spatial robustness, we introduce a capacity-aware formulation that models volume as the product of a link-specific structural capacity and an hourly regime-aware utilization ratio, embedding traffic-theoretic constraints directly into the learning process. Extensive experiments in both generalization settings demonstrate that the proposed structural constraints consistently outperform a state-of-the-art baseline under spatial distribution shift.

## Metadata
- **Published**: 2026-07-27T06:53:43Z
- **Authors**: Léo Hein, Giovanni De Nunzio, Aurélie Pirayre, Laurent Najman
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24056v1)