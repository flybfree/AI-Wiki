---
title: WorldDynCache: Risk-Controlled Latent Dynamics Approximation for Diffusion World Model
published: 2026-08-03T07:52:55Z
authors: Leyang Chen, Junyi Wu, Shaoqiu Zhang, Yulun Zhang
url: http://arxiv.org/abs/2608.01845v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WorldDynCache: Risk-Controlled Latent Dynamics Approximation for Diffusion World Model

## Abstract
Diffusion world models generate high-quality futures, but re- peated transformer evaluations make inference prohibitively slow. Existing caches reuse intermediate features, selectively update tokens, or reuse and extrapolate denoising outputs ac- cording to local drift or short native-space histories. These criteria can miss both approximation-induced latent transition defects that accumulate across skipped steps and phase- or condition-dependent changes in the direction of latent evo- lution. We propose WorldDynCache, a risk-controlled latent dynamics approximation framework with two core compo- nents. First, a lightweight latent-transition risk estimator tracks the accumulated future impact of approximation defects and calibrates its predictions against counterfactual defects ob- served at exact anchors. Second, a condition- and phase- aware lifted latent surrogate approximates latent evolution without extra transformer evaluations. On HunyuanVoyager- 13B and Aether-5B, WorldDynCache achieves 4.92 times and 2.15 times speedups, respectively, while attaining the best gen- eration quality among the compared caching methods across WorldScore, PSNR, SSIM, and LPIPS.

## Metadata
- **Published**: 2026-08-03T07:52:55Z
- **Authors**: Leyang Chen, Junyi Wu, Shaoqiu Zhang, Yulun Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01845v1)