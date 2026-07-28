---
title: Soft-Constrained Optimization of Latent Space in Variational Autoencoders
published: 2026-07-26T16:52:35Z
authors: Ye Shi
url: http://arxiv.org/abs/2607.23751v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Soft-Constrained Optimization of Latent Space in Variational Autoencoders

## Abstract
The usefulness of a variational autoencoder (VAE) depends on two properties of its latent space that are hard to obtain together: high encoding capacity in the individual latent variables, and a low-dimensional, disentangled organization of those variables. Weakening the Kullback-Leibler regularization raises capacity but degrades disentanglement, while strengthening it prunes latent variables away entirely. We formulate VAE training as a soft-constrained optimization problem that addresses both. First, we impose an entropy-based constraint (EC) on individual latent variables, showing that the entropy of a latent code upper-bounds the mutual information it carries about the generative factors of the data. Second, we propose a weight-filter method that exploits the slack of the soft constraint to prune low-entropy dimensions during downstream training. On dSprites, the EC raises the aggregate latent-variable activation score by 43-62% over a vanilla VAE, attains the highest FactorVAE score among the \b{eta} \b{eta}-VAE variants (0.891 vs 0.847), and lowers reconstruction error by up to 38%. On MNIST, the weight filter reduces the latent dimensionality supplied to a downstream classifier from ten to two while holding accuracy above 90%, converging in 37% fewer epochs than the same procedure without the EC. We also find that low-entropy discrete factors tend to merge into a single latent variable, whereas high-entropy continuous factors are distributed across several.

## Metadata
- **Published**: 2026-07-26T16:52:35Z
- **Authors**: Ye Shi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23751v1)