---
title: Neural Network-Assisted CLEAN for Channel Modeling in Low-SNR Regimes
published: 2026-07-29T20:32:42Z
authors: Chaofan Deng, Linyu Sun, Jaeho Lee, Arijit Raychowdhury
url: http://arxiv.org/abs/2607.27450v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Neural Network-Assisted CLEAN for Channel Modeling in Low-SNR Regimes

## Abstract
Accurate multipath parameter estimation is critical for modern wireless communication systems, particularly in challenging low-SNR environments. Traditional Maximum Likelihood Estimation algorithms, such as CLEAN, provide high-resolution parameter extraction but suffer from prohibitive computational complexity due to exhaustive grid search. Conversely, purely data-driven deep learning approaches lack physical grounding and struggle to generalize across variable multipath densities and off-grid parameters. To address these limitations, this paper proposes Neural Network-Assisted CLEAN (NN-CLEAN), a hybrid framework that embeds a multi-head residual network directly into the iterative CLEAN extraction loop. By replacing the exhaustive grid search with rapid, parallelizable forward passes while delegating residual subtraction to exact mathematical models, NN-CLEAN isolates physical multipath parameters without accumulating non- physical errors. Extensive Monte Carlo simulations demonstrate that NN-CLEAN achieves estimation accuracy exceeding 96% at 5 dB SNR, matching the traditional Grid-Search CLEAN (GS- CLEAN) baseline, while providing a massive reduction in computational complexity and substantially outperforming subspace methods and standalone one-shot neural networks. Crucially, NN-CLEAN exhibits a near-flat scaling in execution runtime and memory consumption as batch sizes increase. This highly efficient parallelization establishes NN-CLEAN as a robust, real- time solution for channel estimation in MIMO systems.

## Metadata
- **Published**: 2026-07-29T20:32:42Z
- **Authors**: Chaofan Deng, Linyu Sun, Jaeho Lee, Arijit Raychowdhury
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27450v1)