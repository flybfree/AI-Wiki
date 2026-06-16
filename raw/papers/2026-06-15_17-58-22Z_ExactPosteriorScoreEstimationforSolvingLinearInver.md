---
title: Exact Posterior Score Estimation for Solving Linear Inverse Problems
published: 2026-06-15T17:58:22Z
authors: Abbas Mammadov, Ozgur Kara, Kaan Oktay, Iskander Azangulov, Adil Kaan Akan, Hyungjin Chung, James Matthew Rehg, Yee Whye Teh
url: http://arxiv.org/abs/2606.17048v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Exact Posterior Score Estimation for Solving Linear Inverse Problems

## Abstract
Diffusion and flow-based models learn powerful data priors by training a denoiser to reverse Gaussian corruption. To use this prior to solve a linear inverse problem, one needs to sample from the posterior, but the score that the prior provides is the unconditional score, not the posterior score. Existing methods either steer a fixed pretrained denoiser with approximate measurement-matching corrections, or train a conditional restoration model that abandons the denoising structure of the prior. We derive the exact posterior score in closed form for linear Gaussian inverse problems under general Gaussian interpolants, and show that posterior sampling reduces to a denoising problem at an operator-dependent shifted pivot under an anisotropic noise covariance. We turn this identity into Exact Posterior Score (EPS), a denoising training objective that preserves the input/output structure of standard pretraining and can therefore be trained from scratch or fine-tuned from a pretrained denoiser. At inference, EPS uses the same sampler as the underlying backbone, with no likelihood gradients or projections. We evaluate EPS on five linear inverse problems across FFHQ and ImageNet, where it outperforms training-free and training-based baselines on fidelity, perceptual, and distributional metrics, while using roughly an order of magnitude fewer denoiser evaluations than gradient-based posterior samplers.

## Metadata
- **Published**: 2026-06-15T17:58:22Z
- **Authors**: Abbas Mammadov, Ozgur Kara, Kaan Oktay, Iskander Azangulov, Adil Kaan Akan, Hyungjin Chung, James Matthew Rehg, Yee Whye Teh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.17048v1)