---
title: Weightless Fine-Tuning: Personalizing LLMs via Logit-Space Transport
published: 2026-08-11T18:49:03Z
authors: Bohan Zhang, Anqi Ni, Yixin Wang, Paramveer S. Dhillon
url: http://arxiv.org/abs/2608.11342v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Weightless Fine-Tuning: Personalizing LLMs via Logit-Space Transport

## Abstract
Supervised fine-tuning (SFT) is a standard approach for adapting LLMs to a target distribution, but in settings such as personalization, where each author requires separate weight access, optimization, storage, and retraining, its costs become prohibitive. We propose Weightless Fine-Tuning (WFT), a training-free decoding-time method that approximates the distributional effect of SFT without weight updates. WFT computes supervised residuals on an author's training sequence and transports them to the current prompt through a cross-prefix transport operator estimated from dropout-induced cross-covariance. The operator captures how a perturbation at one context propagates to predictions at another, replacing gradient-based parameter updates with logit-space corrections. On three LaMP personalization benchmarks, WFT achieves the best average performance across datasets, matches or exceeds SFT on individual tasks, and outperforms other lightweight baselines on average. In a budget-controlled comparison, WFT approaches SFT performance using less than 7% of the effective computation. Logit-level analysis shows a cosine similarity of 0.875 between the logit shifts induced by WFT and SFT over 95% of the next-token probability mass, suggesting that WFT captures the distributional effect of supervised adaptation without modifying model weights.

## Metadata
- **Published**: 2026-08-11T18:49:03Z
- **Authors**: Bohan Zhang, Anqi Ni, Yixin Wang, Paramveer S. Dhillon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11342v1)