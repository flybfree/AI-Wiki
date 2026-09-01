---
title: Event-Driven Language Models with Sparse Neural Activity for Neuromorphic Hardware
published: 2026-08-31T08:28:01Z
authors: Simon Richter, Ruhai Lin, Jason Yik, Taylor Kergan, Rui-Jie Zhu, Farshad Moradi, Jason Eshraghian
url: http://arxiv.org/abs/2608.30439v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Event-Driven Language Models with Sparse Neural Activity for Neuromorphic Hardware

## Abstract
Inference with transformer-based large language models (LLMs) is often limited by the memory-bound KV cache and quadratic attention cost. State-space models (SSMs) mitigate this through linear attention and fixed-size recurrent states, but their large dense linear projections remain computationally expensive even after quantization. We introduce a method that induces sparse neural activity in heavily quantized linear-attention models with minimal performance loss. Activations below a per-projection trainable threshold ($\pm Δ$) are nullified while preserving crucial outliers, achieving comparable performance to dense models with up to 4$\times$ fewer effective arithmetic operations. Targeting a multi-core, multi-chip neuromorphic platform, where event-driven execution converts unstructured sparsity into throughput at both the compute and communication levels, a capability GPU architectures fundamentally lack, we project up to 37$\times$ higher throughput and 16$\times$ lower power versus edge GPU inference of a comparable transformer-based model, and up to 5.4$\times$ improvements over the non-sparsified baseline. These results position sparse, quantized linear-attention models as a natural fit for deploying LLMs on event-driven multi-core platforms.

## Metadata
- **Published**: 2026-08-31T08:28:01Z
- **Authors**: Simon Richter, Ruhai Lin, Jason Yik, Taylor Kergan, Rui-Jie Zhu, Farshad Moradi, Jason Eshraghian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30439v1)