---
title: A Multi-stage Constrained Optimization Framework for Data-driven Problems
published: 2026-07-26T06:11:06Z
authors: Ye Shi
url: http://arxiv.org/abs/2607.23480v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Multi-stage Constrained Optimization Framework for Data-driven Problems

## Abstract
Variational autoencoders (VAEs) transform high-dimensional, often noisy data into a compact latent representation, making downstream optimization more tractable. Three challenges persist in VAE-based constrained optimization: (i) sampling effectively within the latent space, (ii) identifying the active decision variables that actually influence the objective and constraints, and (iii) enforcing constraints without destabilizing training. We propose a Multi-stage Constrained Optimization Framework (MCOF). First, an entropy-constrained VAE (EC-VAE) coupled with a feature selector embeds objective and constraint information into a designated subset of latent variables, so that optimization proceeds over a low-dimensional subspace while the remaining coordinates supply solution diversity. Second, a Uniform Transformation (UT) module applies a per-dimension probability integral transform, replacing the irregular aggregate posterior with a uniform distribution over a bounded box and mitigating posterior collapse and Gaussian mixture bias. Third, a constraint-priority filter method (CPFM) solves the resulting surrogate problem by alternating violation-reduction and objective-reduction steps under a filter acceptance test, returning solutions that are feasible for the learned surrogate to a specified tolerance without requiring multiplier estimation. Finally, unselected latent coordinates are resampled to generate diverse decodings of a single optimized solution. We validate MCOF on a synthetic problem, where we ablate each stage and recover the analytic optimum, and on a ZINC250k drug design task, where the generated molecules satisfy the imposed constraints and are entirely novel relative to the training set.

## Metadata
- **Published**: 2026-07-26T06:11:06Z
- **Authors**: Ye Shi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23480v1)