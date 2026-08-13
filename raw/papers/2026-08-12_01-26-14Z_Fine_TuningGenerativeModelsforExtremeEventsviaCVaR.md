---
title: Fine-Tuning Generative Models for Extreme Events via CVaR-Penalized Wasserstein Gradient Flows
published: 2026-08-12T01:26:14Z
authors: Thejani Gamage, Hyemin Gu, Zhizhen Zhang, Ziyu Chen, Markos Katsoulakis, Luc Rey-Bellet
url: http://arxiv.org/abs/2608.11544v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Fine-Tuning Generative Models for Extreme Events via CVaR-Penalized Wasserstein Gradient Flows

## Abstract
We propose CVaR-penalized Generative Particle Algorithm (CVaR-GPA), a robust, tail-agnostic algorithm for fine-tuning generative models to learn heavy-tailed distributions and capture extreme events, requiring no prior knowledge or estimation of the target's tail characteristics. The method is the Wasserstein gradient flow of the Lipschitz-regularized Kullback-Leibler (KL) divergence penalized by a Conditional Value-at-Risk (CVaR) discrepancy term: the Lipschitz-regularized KL divergence enables robust learning under minimal assumptions on the target distribution, while the CVaR penalty restores the velocity that otherwise vanishes prematurely in the under-sampled tails. The penalized flow admits a bounded but non-Lipschitz velocity field. This departs from the Lipschitz transport maps of standard generators, which preserve the tail behavior of a light-tailed source, and enables transport toward heavier-tailed targets. To define this flow on empirical measures, we derive the first-variation subgradients of CVaR from its Rockafellar-Uryasev representation, valid precisely where the classical density-based formula fails. The particle algorithm CVaR-GPA fine-tunes the output samples of any pre-trained model, without access to its architecture, and runs on an adaptive time horizon set by a kinetic-energy stopping criterion rather than a preset depth. On synthetic isotropic and anisotropic Student-$t$ target distributions, Neal's funnel distribution, and the real-world high-dimensional Fama-French 25 portfolio dataset, CVaR-GPA dramatically improves global and tail accuracy on heavy-tailed targets over the pre-trained baseline.

## Metadata
- **Published**: 2026-08-12T01:26:14Z
- **Authors**: Thejani Gamage, Hyemin Gu, Zhizhen Zhang, Ziyu Chen, Markos Katsoulakis, Luc Rey-Bellet
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11544v1)