---
title: CAI-DLLM: Convergence Aware Inference for Diffusion Language Models
published: 2026-08-23T23:03:59Z
authors: Farhana Amin, Sabiha Afroz, Dimitrios S. Nikolopoulos
url: http://arxiv.org/abs/2608.22646v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CAI-DLLM: Convergence Aware Inference for Diffusion Language Models

## Abstract
Diffusion language models can generate many tokens in parallel, but they still require repeated denoising steps during inference. This makes generation costly, especially when the model continues to recompute tokens that are already stable. To address these limitations, we propose CAI-DLLM, a training-free inference method that uses first-step confidence to guide denoising and reduce inference time. Specifically, CAI-DLLM commits easy tokens earlier, allocates more denoising steps to harder tokens, and adjusts decoding schedules across output blocks. As it relies only on first-step confidence signals, it does not require retraining, extra predictors, or weight updates. We evaluate CAI-DLLM on LLaDA-8B-Instruct and Dream-7B-Instruct across math, code, reasoning, commonsense, and long-context tasks. CAI-DLLM achieves up to 18.2x wall clock inference speedup on LLaDA GSM8K while improving accuracy from 76.27% to 77.41%, and up to 13.1x speedup on Dream HumanEval while achieving higher pass@1 than no-cache inference, 48.17% compared with 46.95%. On harder reasoning tasks, speedups reach 44.8x, with a largest accuracy drop of 4.4 points, while energy consumption is reduced by up to 95.3%.

## Metadata
- **Published**: 2026-08-23T23:03:59Z
- **Authors**: Farhana Amin, Sabiha Afroz, Dimitrios S. Nikolopoulos
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22646v1)