---
title: Music Restoration via Latent Operator Optimization and Diffusion Model Priors
published: 2026-08-03T09:36:40Z
authors: Michal Švento, Eloi Moliner, Valtteri Kallinen, Lauri Juvela, Vesa Välimäki, Pavel Rajmic
url: http://arxiv.org/abs/2608.01972v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Music Restoration via Latent Operator Optimization and Diffusion Model Priors

## Abstract
Music restoration seeks to recover a clean signal from an observed recording degraded by an unknown effect, distortion, or corruption. Existing systems often rely on paired training data and distortion-specific supervision, which limits their use when the forward process is not known in advance. We propose LOUDAR (Latent-space Optimization of Unknown Distortion for Audio Restoration) a general-purpose restoration method that operates in the latent space of a pretrained audio autoencoder and models the unknown distortion as a learnable latent operator. At inference time, LOUDAR alternates between estimating the clean latent variable and updating the latent operator parameters. An unconditional latent diffusion model provides a prior over clean audio and regularizes this inference by steering the latent estimate toward the manifold of clean recordings. Because the degradation model is adapted per input, the approach is broadly applicable across diverse restoration problems. We evaluate LOUDAR on singing voice effect removal and restoration, as well as guitar distortion removal, and show that it consistently improves over degraded inputs and is competitive with supervised and unsupervised baselines in waveform and latent domains.

## Metadata
- **Published**: 2026-08-03T09:36:40Z
- **Authors**: Michal Švento, Eloi Moliner, Valtteri Kallinen, Lauri Juvela, Vesa Välimäki, Pavel Rajmic
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01972v1)