---
title: 'AnchorMoE: Interpretable Time Series Classification via Anchor-Routed MoE'
published: 2026-06-02T13:30:54Z
authors: Tao Xie, Zexi Tan, Haoyi Xiao, Mengke Li, Yiqun Zhang, Yang Lu, Cuie Yang, Yiu-ming Cheung
url: http://arxiv.org/abs/2606.03631v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AnchorMoE: Interpretable Time Series Classification via Anchor-Routed MoE

## Abstract
Multivariate time series classification (MTSC) is pivotal in high-stakes domains, such as clinical diagnosis and industrial fault detection, where safe deployment necessitates transparent decision-making. However, isolating the temporal segments that drive model predictions is challenging because discriminative signals in real-world time series are typically sparse, heterogeneous, and heavily obscured by background noise. This paper, therefore, proposes AnchorMoE, an interpretable-by-construction classification framework. Built upon a Mixture-of-Experts (MoE) architecture, AnchorMoE encodes multi-view representations of local patches and routes them to specialized experts, ensuring that the final prediction is formulated as an exact additive decomposition over the input segments, facilitating ante-hoc transparency rather than relying on post-hoc estimations. To maintain the reliability of this decomposition under sparse signal distributions, we introduce a geometric orthogonality constraint that penalizes representational redundancy, compelling distinct experts to specialize in heterogeneous predictive patterns. Furthermore, an uncertainty-aware reliability gate is designed to dynamically calibrate the contribution of each segment, effectively suppressing residual background noise. Extensive experiments on real-world and synthetic benchmarks demonstrate that AnchorMoE achieves highly competitive classification performance while faithfully grounding its decisions in the raw time series.

## Metadata
- **Published**: 2026-06-02T13:30:54Z
- **Authors**: Tao Xie, Zexi Tan, Haoyi Xiao, Mengke Li, Yiqun Zhang, Yang Lu, Cuie Yang, Yiu-ming Cheung
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.03631v1)