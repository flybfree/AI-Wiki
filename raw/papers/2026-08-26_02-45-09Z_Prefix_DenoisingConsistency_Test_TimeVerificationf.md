---
title: Prefix-Denoising Consistency: Test-Time Verification for Diffusion Language Models
published: 2026-08-26T02:45:09Z
authors: Yuki Ichihara, Naoto Iwase, Mohammad Atif Quamar, Junpei Komiyama
url: http://arxiv.org/abs/2608.25311v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Prefix-Denoising Consistency: Test-Time Verification for Diffusion Language Models

## Abstract
Diffusion Language Models (DLMs) have recently become increasingly competitive with autoregressive (AR) models, and even outperform them on certain tasks. Unlike AR models, DLMs produce output through iterative denoising without a left-to-right order. To further improve the performance of DLMs, we introduce PDC (\emph{Prefix-Denoising Consistency}), a test-time self-verification method for DLMs. PDC exploits a distinctive test-time signal in DLMs under prefix conditioned regeneration, correct trajectories are more stable and reproducible than incorrect ones. Concretely, given an initially generated sample, PDC splits the sentence at an intermediate position and regenerates the remaining tokens conditioned on the fixed prefix. Across mathematical reasoning and commonsense reasoning benchmarks, PDC consistently improves upon the initial sample, outperforms independent generations under a computational constrained comparison, and is robust to different unmasking strategies and parameter settings. These results highlight prefix-conditioned regeneration as an effective DLM-specific primitive for test-time verification.

## Metadata
- **Published**: 2026-08-26T02:45:09Z
- **Authors**: Yuki Ichihara, Naoto Iwase, Mohammad Atif Quamar, Junpei Komiyama
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25311v1)