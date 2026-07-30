---
title: Denoising growth complexity: Data geometry and certified schedules for diffusion sampling
published: 2026-07-28T21:26:16Z
authors: Martin J. Wainwright
url: http://arxiv.org/abs/2607.26285v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Denoising growth complexity: Data geometry and certified schedules for diffusion sampling

## Abstract
Two central challenges in diffusion-based sampling are the theoretical one of understanding their remarkable effectiveness even in high-dimensional settings, and the practical one of designing algorithms with certified performance guarantees. We show that these questions are intimately connected via the \emph{denoising growth complexity} ($\mathsf{DGC}$). It is a geometric measure defined by a log-time weighted integral of the derivative of the denoising mean-squared error along the Gaussian heat flow. We show how the $\mathsf{DGC}$ increments lead to a simple and explicit bound on the KL error of an Euler scheme applied to the stochastic innovations representation. The bound is local along the path: each step is controlled by the corresponding $\mathsf{DGC}$ increment and its relative stepsize. This structure allows us to derive KL sampling guarantees for optimized stepsize schedules, both in a simpler single-block setting and in a more refined $K$-block setting. The $\mathsf{DGC}$ function has a natural martingale structure, which we exploit to develop fully data-certified versions of these algorithms. It also admits information-theoretic upper bounds in terms of covariance, rate distortion, metric entropy, and the Poincar'e constant, thereby recovering and sharpening a range of existing diffusion-sampling guarantees, as well as giving new results. In log heat-time, the fine partition limit is governed by an integral involving the square root of the $\mathsf{DGC}$ density, whereas a single-block schedule depends on its ordinary integral. This comparison precisely characterizes when adaptation to data geometry yields substantial computational gains, including logarithmic-to-constant separations for simple Gaussian mixture models.

## Metadata
- **Published**: 2026-07-28T21:26:16Z
- **Authors**: Martin J. Wainwright
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26285v1)