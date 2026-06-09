---
title: Conflict-Aware Harmonized Rotational Gradient for Multiscale Kinetic Regimes
published: 2026-04-27T17:47:42Z
authors: Zhangyong Liang
url: http://arxiv.org/abs/2604.24745v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Conflict-Aware Harmonized Rotational Gradient for Multiscale Kinetic Regimes

## Abstract
In this paper, we propose a harmonized rotational gradient method, termed HRGrad, for simultaneously tackling multiscale time-dependent kinetic problems with varying small parameters.   These parameters exhibit asymptotic transitions from microscopic to macroscopic physics, making it a challenging multi-task problem to solve over all ranges simultaneously.   Solving tasks in different asymptotic regions often encounter gradient conflicts, which can lead to the failure of multi-task learning.   To address this challenge, we explicitly encode a hidden representation of these parameters, ensuring that the corresponding solving tasks are serialized for simultaneous training.   Furthermore, to mitigate gradient conflicts, we segment the prediction results to construct task losses and introduce a novel gradient alignment metric to ensure a positive dot product between the final update and each loss-specific gradient.   This metric maintains consistent optimization rates for all task losses and dynamically adjusts gradient magnitudes based on conflict levels.   Moreover, we provide a mathematical proof demonstrating the convergence of the HRGrad method, which is evaluated across a range of challenging asymptotic-preserving neural networks (APNNs) scenarios.   We conduct an extensive set of experiments encompassing the Bhatnagar-Gross-Krook (BGK) equation and the linear transport equation in all ranges of Knudsen number.   Our results indicate that HRGrad effectively overcomes the `failure modes' of APNNs in these problems.

## Metadata
- **Published**: 2026-04-27T17:47:42Z
- **Authors**: Zhangyong Liang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2604.24745v1)