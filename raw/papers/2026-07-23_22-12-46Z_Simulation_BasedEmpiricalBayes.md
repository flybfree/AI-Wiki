---
title: Simulation-Based Empirical Bayes
published: 2026-07-23T22:12:46Z
authors: Xinwei Shen, Diana Cai, Cheng Zhang, David M. Blei
url: http://arxiv.org/abs/2607.21843v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Simulation-Based Empirical Bayes

## Abstract
Empirical Bayes (EB) performs simultaneous inference across many related latent variables. Classical EB assumes that the likelihood p(x | z) is tractable. In many scientific applications, however, the likelihood is available only through a simulator. This paper develops EB for such implicit likelihoods. We introduce simulation-based empirical Bayes (SBEB), which connects nonparametric EB to simulation-based inference (SBI). SBEB computes EB estimates without an explicit density by using the observed data, simulator samples, and an amortized inference network. SBEB iteratively refines the fitted EB prior toward the population prior. With several scientific simulators and real-world data, we demonstrate that SBEB improves accuracy over SBI with a fixed prior.

## Metadata
- **Published**: 2026-07-23T22:12:46Z
- **Authors**: Xinwei Shen, Diana Cai, Cheng Zhang, David M. Blei
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.21843v1)