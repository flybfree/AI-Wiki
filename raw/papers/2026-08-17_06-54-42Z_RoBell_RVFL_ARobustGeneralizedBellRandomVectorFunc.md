---
title: RoBell-RVFL: A Robust Generalized Bell Random Vector Functional Link Network
published: 2026-08-17T06:54:42Z
authors: A. Rahaman, A. Quadir, M. Tanveer
url: http://arxiv.org/abs/2608.16965v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RoBell-RVFL: A Robust Generalized Bell Random Vector Functional Link Network

## Abstract
The dominance of majority classes in real-world datasets poses a fundamental challenge to randomized neural networks, often biasing decision boundaries and overlooking critical minority samples. Existing remedies, such as synthetic minority over-sampling (SMOTE) and class-weighted loss functions, primarily address class proportions while neglecting intra-class distribution, making them vulnerable to label noise and outliers. In this paper, we propose \textbf{RoBell-RVFL}, a robust and lightweight \emph{quality-aware} generalized bell random vector functional link network that redefines how randomized models handle class imbalance and noisy data. RoBell-RVFL employs a dual-strategy, sample-level weighting mechanism that strictly preserves minority class information using unit weights, while adaptively regulating the influence of majority class samples through a probability-weighted generalized bell (gbell) membership function in a kernel-induced feature space. This design effectively suppresses noisy, boundary, and outlier samples within the majority class, enabling the network to learn from informative samples rather than merely abundant ones. By explicitly incorporating local class probability and class distribution information into the learning process, RoBell-RVFL achieves adaptive control over sample contributions without sacrificing the closed-form learning efficiency of RVFL networks. Extensive evaluations on UCI and KEEL benchmark datasets, along with robustness tests under up to 40\% label noise, demonstrate that RoBell-RVFL consistently and significantly outperforms recent state-of-the-art RVFL variants. The results indicate that adaptive, quality-aware sample weighting is essential for robust RVFL learning, rendering conventional global weighting schemes ineffective in noisy and imbalanced environments.

## Metadata
- **Published**: 2026-08-17T06:54:42Z
- **Authors**: A. Rahaman, A. Quadir, M. Tanveer
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16965v1)