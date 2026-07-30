---
title: Equilibrium Training of Energy-Based Models with Parallel Trajectory Tempering
published: 2026-07-29T16:00:59Z
authors: Nicolas Béreux, Aurélien Decelle, Cyril Furtlehner, Beatriz Seoane
url: http://arxiv.org/abs/2607.27077v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Equilibrium Training of Energy-Based Models with Parallel Trajectory Tempering

## Abstract
Energy-Based Models (EBMs) provide an interpretable framework for generative modeling of scientific data, but poor Markov Chain Monte Carlo mixing often limits their reliability. We introduce a training algorithm based on Parallel Trajectory Tempering (PTT), which exploits the continuity of the optimization path to maintain equilibrium sampling throughout learning. This enables stable and fast training on highly multimodal and data-scarce scientific datasets. Combined with reservoir sampling and adaptive optimization, PTT has a computational cost comparable to Persistent Contrastive Divergence, making it a practical replacement for standard training methods. It also provides direct estimates of thermalization times, equilibrium samples from trained models, and accurate log-likelihoods at essentially no additional cost. Experiments on Restricted Boltzmann Machines show that PTT consistently outperforms existing EBM training approaches. On discrete tabular data, it also surpasses state-of-the-art deep generative models, yielding higher-quality samples and greater robustness to overfitting and limited data. Our results make equilibrium maximum-likelihood training of EBMs practical and computationally efficient.

## Metadata
- **Published**: 2026-07-29T16:00:59Z
- **Authors**: Nicolas Béreux, Aurélien Decelle, Cyril Furtlehner, Beatriz Seoane
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27077v1)