---
title: Generalization and Trade-off in Adversarial Training: An RKHS Perspective via Kernel Integral Operators
published: 2026-07-30T10:43:29Z
authors: Yiling Xie, Xiaoming Huo
url: http://arxiv.org/abs/2607.27995v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Generalization and Trade-off in Adversarial Training: An RKHS Perspective via Kernel Integral Operators

## Abstract
Adversarial training has emerged as a powerful approach for protecting models against adversarial attacks in a broad range of real-world applications. In this paper, we study adversarial training in the reproducing kernel Hilbert space (RKHS) framework through the associated kernel integral operator. We first derive source-uniform generalization error bounds for the RKHS adversarial training estimator in terms of the robustness level, sample size, source smoothness, and kernel spectrum. On a fixed polynomial-spectrum model, we further establish a matching lower bound showing that the optimally balanced generalization rate can be slower than the minimax prediction benchmark. This result reveals a loss of statistical accuracy in adversarial training. Our analysis shows that this loss arises from the interaction between adversarial robustness and observation noise: the noise contribution in the mixed robustness term slows the approximation rate, although the same term reduces the estimation complexity. To address this limitation, we propose a two-stage noise-debiased procedure that estimates and removes the noise contribution from the mixed term. The resulting estimator improves the generalization rate and attains the minimax polynomial rate, up to a logarithmic factor, when the robustness level is selected at the stated sample-dependent order. Our results characterize the generalization behavior of adversarial training in a nonparametric framework and provide a new interpretation and a principled solution for the trade-off between adversarial robustness and generalization. Numerical experiments support the theoretical findings and demonstrate the effectiveness of the proposed method.

## Metadata
- **Published**: 2026-07-30T10:43:29Z
- **Authors**: Yiling Xie, Xiaoming Huo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27995v1)