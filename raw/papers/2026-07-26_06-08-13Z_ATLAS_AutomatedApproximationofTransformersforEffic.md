---
title: ATLAS: Automated Approximation of Transformers for Efficient Homomorphic Inference in One Hour
published: 2026-07-26T06:08:13Z
authors: Jianhang Xie, Sicheng Tan, Vishnu Naresh Boddeti, Zhichao Lu
url: http://arxiv.org/abs/2607.23478v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ATLAS: Automated Approximation of Transformers for Efficient Homomorphic Inference in One Hour

## Abstract
Fully homomorphic encryption (FHE) provides strong cryptographic guarantees for private inference, but deploying transformer models under FHE remains prohibitively expensive. A key bottleneck is that non-linear operations such as softmax, normalization, and activation must be replaced with polynomial approximations compatible with the CKKS scheme, and the multiplicative depth consumed by these approximations dominates inference cost. Recent frameworks have advanced approximation techniques, yet all rely on manually configured approximation hyperparameters (e.g., number of iterations, polynomial degree), applied uniformly across all layers. While convenient, this uniform-configuration approach is overly rigid: different layers can tolerate different levels of approximation error without degrading predictive accuracy, and uniform configurations cannot exploit this variability to reduce latency. Allowing each layer to adopt its own configuration, however, causes the search space to explode with model depth, reaching roughly $10^{84}$ configurations for BERT/ViT (12 layers) and $10^{225}$ for LLaMA3 (32 layers), rendering manual exploration practically impossible. We present ATLAS, an automated framework that configures per-layer approximation settings by formulating the problem as a multi-objective optimization over latency and predictive accuracy. The resulting problem is inherently difficult: 1) competing objectives over a large decision space (120 or 320 variables for BERT/ViT or LLaMA3); 2) expensive evaluation, as each configuration takes 70-1,000 seconds even in cleartext; and 3) sparse optimization signals, as 35-50% of candidate configurations yield numerically invalid solutions. ATLAS addresses these challenges through a two-stage optimization strategy that progressively relaxes layer-wise constraints, combined with surrogate models to accelerate evaluation.

## Metadata
- **Published**: 2026-07-26T06:08:13Z
- **Authors**: Jianhang Xie, Sicheng Tan, Vishnu Naresh Boddeti, Zhichao Lu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23478v1)