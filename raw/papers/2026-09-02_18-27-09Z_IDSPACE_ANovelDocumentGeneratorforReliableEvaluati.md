---
title: IDSPACE: A Novel Document Generator for Reliable Evaluation of Digital Identity Verification Systems [Extended Technical Report]
published: 2026-09-02T18:27:09Z
authors: Lulu Xie, Yancheng Wang, Kanchan Chowdhury, Rolando Garcia, Yingzhen Yang, Jia Zou
url: http://arxiv.org/abs/2609.03052v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# IDSPACE: A Novel Document Generator for Reliable Evaluation of Digital Identity Verification Systems [Extended Technical Report]

## Abstract
As services move online, trust institutions such as banks, lenders, and governments must verify the identity of remote users. Fraud detection tools are widely available, but evaluating and fine-tuning them remains difficult because identity documents are sensitive and therefore scarce. Synthetic data generation offers a path forward, and demand is clear: our prior work in this area has been downloaded over $11{,}000$ times (aggregated from eight parts). We introduce IDSpace, extending this line of research in three directions. First, we propose model-guided Bayesian optimization, which tunes generation parameters to maximize both visual similarity and prediction consistency with target-domain models given only a few samples from a target domain. Second, we decouple user-specified metadata (demographics, fraud patterns, capture device) from automatically tuned control parameters (font styles, noise levels, image quality), allowing users to configure evaluations without low-level expertise. Third, we expand beyond template images to support scanned and mobile-captured documents. Experiments show IDSpace improves evaluation consistency by $15-45\%$ over baselines including CycleGAN, diffusion inpainting, and non-guided optimization, using only a few real samples, while improving training accuracy by up to $9\%$ and SSIM similarity with the target domain by $10\%$. We also released a new dataset consisting of $359{,}240$ high-quality synthetic documents across ten European ID types.

## Metadata
- **Published**: 2026-09-02T18:27:09Z
- **Authors**: Lulu Xie, Yancheng Wang, Kanchan Chowdhury, Rolando Garcia, Yingzhen Yang, Jia Zou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.03052v1)