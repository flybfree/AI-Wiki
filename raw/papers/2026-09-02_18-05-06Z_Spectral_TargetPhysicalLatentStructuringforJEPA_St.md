---
title: Spectral-Target Physical Latent Structuring for JEPA-Style World Models
published: 2026-09-02T18:05:06Z
authors: Penghao Zhu, Salvatore Penachio, Kaustav Mukherjee, Aneesh Jonelagadda
url: http://arxiv.org/abs/2609.04264v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Spectral-Target Physical Latent Structuring for JEPA-Style World Models

## Abstract
Latent world models have become increasingly popular as a method to predict and plan in latent space rather than pixel space. Recent architectures, such as LeWorldModel (LeWM), jointly train the encoder and predictor using regularization techniques like SIGReg to prevent representation collapse. Even with such regularization preventing representation collapse, we identify a new world model failure mode of \textit{physical representation laziness}, particularly noted in highly dynamic environments. For these lazy cases, the learned latent states do not collapse but nonetheless fail to represent key physical properties, causing ubiquitous downstream planning failure. To resolve this issue, we propose training-time auxiliary supervision with a lightweight "Fourier auxiliary head", which enforces physically-informed structuring of the latent space with no additional inference-time cost and can be generalized to any environment. Experimentally, we show that the auxiliary head substantially improves planning success rates in dynamic environments where the baseline LeWM exhibits physical representation laziness. It also leads to modest improvements in other environments, even when the baseline does not exhibit physical representation laziness. We further observe superior planning performance being accompanied by higher latent space correlations with key physical properties, indicating both the ability of our method to physically structure latent states and the potential planning-side benefit to the learned representation being physically structured. We also see in low-data regimes, auxiliary supervision is particularly impactful in increasing success rate. These findings support the use of our Fourier auxiliary head method to improve both overall success rate and data efficiency, while avoiding representation laziness in latent world models.

## Metadata
- **Published**: 2026-09-02T18:05:06Z
- **Authors**: Penghao Zhu, Salvatore Penachio, Kaustav Mukherjee, Aneesh Jonelagadda
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04264v1)