---
title: AdROD: HyperNetwork-based Adversarially Robust Object Detection for Autonomous Driving
published: 2026-08-17T02:52:01Z
authors: Yuting Wu, Dongfang Guo, Xiangzhong Luo, Qun Song, Rui Tan
url: http://arxiv.org/abs/2608.16031v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AdROD: HyperNetwork-based Adversarially Robust Object Detection for Autonomous Driving

## Abstract
Camera-based object detectors are vulnerable to physical adversarial attacks designed to suppress detections. While adversarial training and input purification offer some protection, they often overfit to specific attack distributions and fail on adaptive adversaries. This paper presents AdROD, an embedded, stochastic ensemble defense software designed for autonomous driving. AdROD employs {\em low-rank HyperNetworks}, which require only 1.6\% of the parameter footprint of standard HyperNetworks, to generate diverse detectors at a per-frame rate, making it impractical for attackers to obtain the deployed detectors in time. To further improve adversarial robustness, AdROD incorporates a novel \emph{functional diversity} mechanism, which couples stochastic weight updates with unique input-space transformations. We design two serving modes of AdROD that strike different trade-offs between robustness and runtime overhead: AdROD-I, a continuous protection mode for maximum resilience that leverages inter-detector disagreement to recover compromised detections, and AdROD-II, an on-demand mode triggered by kinematic discontinuities in object tracking. Through comprehensive evaluation with synthetic benchmarks, physically deployed adversarial patches, and end-to-end safety tests in the OpenCDA co-simulator, AdROD outperforms five baseline defenses and exhibits superior generalizability compared with the evaluated adversarial-training baselines, while maintaining real-time performance for safely stopping the vehicle at a stop sign instrumented with adversarial patches.

## Metadata
- **Published**: 2026-08-17T02:52:01Z
- **Authors**: Yuting Wu, Dongfang Guo, Xiangzhong Luo, Qun Song, Rui Tan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16031v1)