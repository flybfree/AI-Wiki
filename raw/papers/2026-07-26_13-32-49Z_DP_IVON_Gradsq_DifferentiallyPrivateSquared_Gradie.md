---
title: DP-IVON-Gradsq: Differentially Private Squared-Gradient Improved Variational Online Newton
published: 2026-07-26T13:32:49Z
authors: Nour Jamoussi, Ikram Dridi, Giuseppe Serra, Marios Kountouris
url: http://arxiv.org/abs/2607.23649v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DP-IVON-Gradsq: Differentially Private Squared-Gradient Improved Variational Online Newton

## Abstract
Differential privacy provides formal privacy guarantees for training neural networks on sensitive data, while Bayesian deep learning offers a principled framework for uncertainty-aware prediction. Combining these two objectives remains challenging, as privacy noise can interact with the stochasticity introduced by Bayesian posterior sampling. In this work, we investigate differentially private variational Bayesian learning through the Improved Variational Online Newton (IVON) optimizer. We introduce DP-IVON-Gradsq, a private variant of IVON. The proposed method constructs its curvature estimate from the privatized gradient using a noise-corrected squared-gradient estimator, reducing the direct interaction between posterior-sampling noise and privacy noise while preserving the Adam-like computational efficiency of IVON. We evaluate DP-IVON-Gradsq on CIFAR-10 against the standard private optimizers DP-SGD and DP-Adam over a range of privacy budgets. The results show that DP-IVON-Gradsq is competitive under weak-to-moderate privacy constraints, i.e., large-to-moderate values of $\varepsilon$, while degrading under strong privacy. Code is available at https://github.com/NourJamoussi/DP-IVON-Gradsq.git.

## Metadata
- **Published**: 2026-07-26T13:32:49Z
- **Authors**: Nour Jamoussi, Ikram Dridi, Giuseppe Serra, Marios Kountouris
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23649v1)