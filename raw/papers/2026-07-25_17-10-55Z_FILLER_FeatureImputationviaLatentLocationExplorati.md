---
title: FILLER: Feature Imputation via Latent Location Exploration and Retrieval
published: 2026-07-25T17:10:55Z
authors: Santu Mondal, Chayan Maitra, Rajat K. De
url: http://arxiv.org/abs/2607.23295v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# FILLER: Feature Imputation via Latent Location Exploration and Retrieval

## Abstract
In real-world machine learning applications, incomplete observations create a fundamental challenge. Researchers have come up with several ideas to address this crucial problem. However, current models still face challenges in balancing scalability and structural consistency. This study proposes a feature imputation method, called FILLER, that deliberately searches the two-dimensional latent space produced by a generative model and fills the missing values with appropriate entries. The generative model is trained on fully observed data to generate samples from the latent space, and FILLER uses this trained model to impute the values missing in the corrupted test samples. In this study, G-NeuroDAVIS serves the purpose of the generative model. This work also presents a mathematical proof on the convergence of the iterative search. Finally, FILLER has been evaluated on several image datasets under random and structured missingness patterns with varying levels of imputation complexities. In order to justify the efficacy of FILLER, it has been compared against existing state-of-the-art solution strategies in terms of RMSE, PSNR, and SSIM. In addition, Wilcoxon signed-rank test has been carried out to validate statistical significance. Moreover, downstream analyses (classification and clustering) have also established the quality of imputation in terms of standard metrics.

## Metadata
- **Published**: 2026-07-25T17:10:55Z
- **Authors**: Santu Mondal, Chayan Maitra, Rajat K. De
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23295v1)