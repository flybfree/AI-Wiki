---
title: FairDiffuseVQVAE: Sampling-Time Fairness in Tabular Diffusion via Conditional Refinement of Vector-Quantized Latents
published: 2026-07-31T01:57:07Z
authors: Nitish Nagesh, Mahdi Bagheri, Amir M. Rahmani
url: http://arxiv.org/abs/2607.28945v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FairDiffuseVQVAE: Sampling-Time Fairness in Tabular Diffusion via Conditional Refinement of Vector-Quantized Latents

## Abstract
Synthetic tabular data is increasingly used in privacy-preserving data sharing, data augmentation, and to mitigate downstream classifier bias. State-of-the-art tabular diffusion models such as TabDDPM and TabSyn achieve excellent distributional fidelity but offer no mechanism for fairness; conversely, fairness-aware tabular generators (DECAF, FairTGAN, FairTabDDPM) impose explicit fairness penalties at training time, yielding modest fairness gains at substantial cost to either sample quality or downstream utility. We introduce FairDiffuseVQVAE, a two-stage architecture that decouples fidelity from fairness: a vector-quantized autoencoder with a row-level discriminator (Stage~1, no fairness terms) is followed by a DiffuseVAE-style continuous diffusion refiner that conditions on both the Stage-1 reconstruction and the protected attribute via classifier-free guidance (Stage~2). Fairness emerges as a property of the sampling distribution -- uniform sampling of the protected attribute at inference time enforces demographic parity by construction, rather than from competing loss terms. On the Adult, Bank and COMPAS datasets, FairDiffuseVQVAE achieves the highest mean Demographic Parity Ratio ($0.702$, $+47\%$ over FairTabDDPM) and Equalized Odds Ratio ($0.686$, $+100\%$). It also attains the lowest mean pair-wise correlation error ($0.034$) of any published method, while explicitly trading $\sim$$15$ AUC points for these fairness gains.

## Metadata
- **Published**: 2026-07-31T01:57:07Z
- **Authors**: Nitish Nagesh, Mahdi Bagheri, Amir M. Rahmani
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28945v1)