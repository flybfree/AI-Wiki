---
title: 'From Scores to Gibbs Correctors: Accelerating Uniform-Rate Discrete Diffusion Models'
published: 2026-05-26T17:52:28Z
authors: Yuchen Liang, Ness Shroff, Yingbin Liang
url: http://arxiv.org/abs/2605.27352v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# From Scores to Gibbs Correctors: Accelerating Uniform-Rate Discrete Diffusion Models

## Abstract
Discrete diffusion models have achieved strong empirical performance in text and other symbolic domains, but, especially for uniform-rate models, they often require many steps to generate a single sample. Existing acceleration methods either rely on training additional quantities or suffer from slow mixing. In this work, we propose a novel Gibbs-based corrector for discrete diffusion models, termed Gibbs-Accelerated Discrete Diffusion (GADD). GADD leverages the structure of the concrete score function to construct Gibbs posterior likelihoods directly, without requiring any additional training beyond standard score estimation. We show that GADD achieves an overall sampling complexity of $\mathcal{O}(\mathrm{polylog} (\varepsilon^{-1}))$, yielding the first such rate for diffusion-based samplers for uniform-rate discrete diffusion models. We also conduct numerical experiments demonstrating the practical advantages of GADD across synthetic data, zero-shot text sampling, and zero-shot conditional music generation. These results corroborate the theory and show that GADD consistently improves sample quality and wall-clock efficiency over standard baselines, including vanilla Euler methods and CTMC correctors. Beyond this, our theoretical analysis introduces a novel framework for analyzing predictor-corrector methods in discrete diffusion models, which may be of independent interest. Unlike existing approaches that rely on the Girsanov change-of-measure technique, our method is based on an induction argument that tracks error propagation across predictor iterations while accounting for inaccuracies in the corrector updates.

## Metadata
- **Published**: 2026-05-26T17:52:28Z
- **Authors**: Yuchen Liang, Ness Shroff, Yingbin Liang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.27352v1)