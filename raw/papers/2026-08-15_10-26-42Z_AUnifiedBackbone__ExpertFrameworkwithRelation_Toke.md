---
title: A Unified Backbone--Expert Framework with Relation-Token and Residual--Classifier Interfaces for Automatic Modulation Recognition
published: 2026-08-15T10:26:42Z
authors: Zhixiang Deng, Houbiao Li, Zongyong Cui
url: http://arxiv.org/abs/2608.15160v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Unified Backbone--Expert Framework with Relation-Token and Residual--Classifier Interfaces for Automatic Modulation Recognition

## Abstract
Automatic modulation recognition (AMR) faces distinct representation bottlenecks under varying observation lengths, where a single model architecture often fails to excel. To address this, we propose a unified backbone-expert framework with a common convolutional state-space backbone and two specialized interfaces. For short sequences, we inject explicit lag-aware complex-plane descriptors as relation tokens before encoding to compensate for information loss. For long sequences, we design a gated multi-scale residual refinement module to correct the feature map, combined with a fixed-averaging classifier collaboration to harness complementary evidence. Our framework achieves overall average accuracies of 67.28 \pm 0.14% on RML2016.10b and 87.19 \pm 0.77% on HisarMod2019 (mean \pm sample standard deviation over three runs), respectively. The framework's efficacy is further validated through three-seed ablations, native-length cross-configuration tests, and controlled window studies, confirming the benefit of expert-interface decoupling over one-size-fits-all architectures.

## Metadata
- **Published**: 2026-08-15T10:26:42Z
- **Authors**: Zhixiang Deng, Houbiao Li, Zongyong Cui
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15160v1)