---
title: Discovering Cross-Language Reasoning Invariance in LLMs with Geometry-Invariant Sparse Autoencoders
published: 2026-08-24T20:17:55Z
authors: Igor Bogdanov, Changcheng Huang
url: http://arxiv.org/abs/2608.23809v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Discovering Cross-Language Reasoning Invariance in LLMs with Geometry-Invariant Sparse Autoencoders

## Abstract
Multilingual language models can solve the same mathematical problem in different languages, but it remains unclear whether they rely on shared features or on language-specific computations that only produce similar outputs. We study this question in five models from four families using the Multilingual Grade School Math (MGSM) dataset, with problems solved in English, German, French, Spanish, Russian, and Chinese, retaining problems with valid reasoning traces in all six languages and replaying those traces through the model to record representations at multiple layers. For each model, we first use Centered Kernel Alignment (CKA) to identify layers with cross-language alignment. At each selected layer, we train two sparse autoencoders (SAE): a baseline reconstruction-only model and a contrastive variant introduced in this work, the Geometry-Invariant SAE (GI-SAE). GI-SAE supplements the reconstruction loss with an Information Noise-Contrastive Estimation (InfoNCE) loss that trains the encoder to produce similar activations for traces of the same problem, regardless of language or token position. We then test whether the resulting shared features are functionally interchangeable by swapping their values between languages during the model's forward pass and measuring the resulting change in output, quantified by Kullback-Leibler (KL) divergence per feature. Although GI-SAE yields higher CKA and Jaccard similarity at nearly every layer, higher geometric similarity does not consistently imply greater functional interchangeability. We find that cross-language feature sharing is model- and architecture-dependent in this sample and appears at different depths in different models. GI-SAE primarily amplifies cross-language structure already present: the pattern is model-specific, with strengthening in Qwen, no functional benefit in Gemma, and mixed layer-dependent effects in Llama and Phi.

## Metadata
- **Published**: 2026-08-24T20:17:55Z
- **Authors**: Igor Bogdanov, Changcheng Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.23809v1)