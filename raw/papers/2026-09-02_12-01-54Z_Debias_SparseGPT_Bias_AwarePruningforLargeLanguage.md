---
title: Debias-SparseGPT: Bias-Aware Pruning for Large Language Models
published: 2026-09-02T12:01:54Z
authors: Irina Proskurina, Guillaume Metzler, Antoine Gourru, Julien Velcin
url: http://arxiv.org/abs/2609.02496v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Debias-SparseGPT: Bias-Aware Pruning for Large Language Models

## Abstract
Model compression techniques such as pruning and quantization facilitate the efficient deployment and acceleration of Large Language Models (LLMs). However, recent studies show that weight sparsification methods, such as SparseGPT, can amplify existing biases in models, with outputs varying significantly depending on persona cues in the prompt. In this paper, we introduce Debias-SparseGPT, a post-training pruning method incorporating representational debiasing using a second-order term defined over demographically contrasting inputs. We perform empirical validation of our method over a wide range of generative LLMs. Across models and sparsity regimes (25%, 50%, and structured 2:4 sparsity), Debias-SparseGPT consistently reduces pruning-induced bias compared to SparseGPT while preserving model perplexity and zero-shot accuracy. Under the most restrictive 2:4 structured sparsity pattern, which most aggressively degrades model quality, augmenting the calibration set with long-context, content-rich examples further improves both downstream performance and fairness. Overall, Debias-SparseGPT advances the bias-performance trade-off while preserving the computational efficiency of sparse models.

## Metadata
- **Published**: 2026-09-02T12:01:54Z
- **Authors**: Irina Proskurina, Guillaume Metzler, Antoine Gourru, Julien Velcin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02496v1)