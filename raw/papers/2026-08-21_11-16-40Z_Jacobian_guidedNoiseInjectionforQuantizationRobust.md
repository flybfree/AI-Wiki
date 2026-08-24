---
title: Jacobian-guided Noise Injection for Quantization Robustness in Large Language Models
published: 2026-08-21T11:16:40Z
authors: Deepanshu Pandey, Arnav Chavan, Nahush Lele, Sankalp Dayal, Deepak Gupta
url: http://arxiv.org/abs/2608.20988v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Jacobian-guided Noise Injection for Quantization Robustness in Large Language Models

## Abstract
Quantization of Large Language Models (LLMs) is often hindered by the sensitivity of the self-attention mechanism to discretization errors. We identify the softmax operator as a bottleneck for quantization stability due to its sensitivity to outliers and state-dependent Jacobian. We theoretically establish that suppressing the norm of this Jacobian helps in bounding quantization-induced performance degradation. Based on this, we propose Jacobian-Guided Noise Injection, a training strategy that injects zero-mean Gaussian noise into pre-attention logits, with variance derived directly from the Jacobian Frobenius norm. Unlike prior approaches that rely on heuristic or penalise jacobian directly, our method provides a way to identify the optimal noise variance based on the local attention sensitivity. We evaluate the method on SOTA LLM architectures, where it demonstrates improved robustness over popular PTQ methods. Empirical analysis reveals that the proposed method gives up to +37% relative gains on Top-1 accuracy on ImageNet-1K for SigLIP and improves relative perplexity by upto 40% on WikiText for language models in low bit quantisation settings, proving the efficacy of the approach.

## Metadata
- **Published**: 2026-08-21T11:16:40Z
- **Authors**: Deepanshu Pandey, Arnav Chavan, Nahush Lele, Sankalp Dayal, Deepak Gupta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20988v1)