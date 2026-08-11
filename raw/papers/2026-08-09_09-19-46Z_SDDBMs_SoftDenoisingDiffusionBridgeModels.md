---
title: SDDBMs: Soft Denoising Diffusion Bridge Models
published: 2026-08-09T09:19:46Z
authors: Shiyi Qi, Kun He, Mingmou Liu
url: http://arxiv.org/abs/2608.08594v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SDDBMs: Soft Denoising Diffusion Bridge Models

## Abstract
Diffusion bridge models leverage Doob's \(h\)-transform to construct stochastic transports between arbitrary endpoint distributions, and have shown strong potential in image-to-image translation and restoration. However, most existing bridge models rely on hard endpoint conditioning, which forces the terminal state to match a prescribed target exactly. This hard constraint induces terminal-boundary singularities: the terminal law collapses to a Dirac measure, and the resulting drift coefficients become ill-conditioned near the endpoint. In this paper, we propose Soft Denoising Diffusion Bridge Models (SDDBMs), a generalized framework that regularizes diffusion bridges directly at the level of their terminal constraints. Instead of imposing an exact endpoint, SDDBMs prescribe a non-degenerate Gaussian terminal marginal under the transformed path measure, with a flexible terminal center and variance. Starting from this prescribed marginal, we develop a complete closed-form construction of the soft bridge, including the Gaussian terminal reweighting and soft \(h\)-function, the induced Gaussian forward marginals and \(\mathbf{x}_0\)-free dynamics. Theoretically, SDDBMs provide a unified probabilistic perspective that encompasses existing diffusion bridge models, including DDBMs, GOUB, and UniDB, as special cases under specific parameter choices. Extensive experiments on image restoration tasks demonstrate that SDDBMs achieve improved numerical stability and superior generation quality over existing bridge-based methods.

## Metadata
- **Published**: 2026-08-09T09:19:46Z
- **Authors**: Shiyi Qi, Kun He, Mingmou Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08594v1)