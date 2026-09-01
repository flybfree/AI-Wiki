---
title: Tensor Methods for Language Models: From Token Representation to Training, Adaptation, Inference, Compression, and Interpretability
published: 2026-08-31T09:38:37Z
authors: Matvei Tarasov, Salman Ahmadi-Asl, Andre L. F. de Almeida, Andrzej Cichocki
url: http://arxiv.org/abs/2608.30505v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Tensor Methods for Language Models: From Token Representation to Training, Adaptation, Inference, Compression, and Interpretability

## Abstract
Large language models (LLMs) are built from structured high-dimensional objects such as token representations, weights, adaptation updates, caches, and activations, whose multilinear structure is underexploited by the conventional matrix-centric view. Tensor decompositions and tensor networks provide a principled algebraic language for this structure, yet the literature often treats them as isolated compression mechanisms. This survey organizes tensor methods for LLMs through two complementary views: a seven-stage lifecycle taxonomy covering tokenization, embeddings, pre-training, adaptation, compression, inference, and interpretability, and a component view covering embeddings, attention, and feed-forward networks. We provide unified notation and theoretical foundations, analyze tensorization strategies for individual Transformer components, and compare methods at each lifecycle stage while making differences in evaluation protocols and model scales explicit. We further connect tensor methods to neighboring efficiency techniques and probabilistic tensor networks. Finally, we synthesize open challenges and introduce $ρ_{\rm gap}$, a metric for the compression-realization gap between theoretical memory reduction and measured system-level speedup. By treating tensorization as a common structural principle, the survey provides a structured entry point to tensorized language models and clarifies when parameter savings can plausibly translate into memory efficiency, computational efficiency, or interpretability. The GitHub page dedicated to this paper is accessible at \href{https://github.com/ma-tt-a/awesome-tensor-methods-for-llms}{this https URL}.

## Metadata
- **Published**: 2026-08-31T09:38:37Z
- **Authors**: Matvei Tarasov, Salman Ahmadi-Asl, Andre L. F. de Almeida, Andrzej Cichocki
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30505v1)