---
title: Conformalized Rate-Adaptive Sensing
published: 2026-07-29T13:16:27Z
authors: Jiawei Yang, Yao Zhang
url: http://arxiv.org/abs/2607.26887v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Conformalized Rate-Adaptive Sensing

## Abstract
Many high-resolution imaging systems face the same fundamental question: when have enough measurements been collected to reconstruct an image accurately? We develop Conformalized Rate-Adaptive Sensing (CoRAS), a method that adaptively chooses an acquisition or compression rate for each image while keeping the reconstruction error below a target level with high probability. As measurements are collected, an image reconstruction model gradually recovers the true image, producing a reconstruction path over acquisition rates. CoRAS uses this path up to an early decision time to estimate the target stopping time, defined as the first time at which the reconstruction error falls below the target level. It then calibrates this estimate using images with similar early reconstruction behavior, producing an upper bound on the stopping time with marginal and approximate conditional coverage guarantees. Experiments on image datasets show that CoRAS attains the target stopping-time coverage, uses fewer measurements on average than fixed-rate stopping rules, and assigns more measurements to images that are harder to reconstruct.

## Metadata
- **Published**: 2026-07-29T13:16:27Z
- **Authors**: Jiawei Yang, Yao Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26887v1)