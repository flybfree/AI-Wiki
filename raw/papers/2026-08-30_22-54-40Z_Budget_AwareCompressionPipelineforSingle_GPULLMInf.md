---
title: Budget-Aware Compression Pipeline for Single-GPU LLM Inference: Methods, Trade-offs, and Coupling Effects
published: 2026-08-30T22:54:40Z
authors: Hongyu Yu, Yifei Shen
url: http://arxiv.org/abs/2608.30076v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Budget-Aware Compression Pipeline for Single-GPU LLM Inference: Methods, Trade-offs, and Coupling Effects

## Abstract
Single-GPU deployment of 70B-parameter language models on an NVIDIA GPU is constrained by device memory, long-context throughput, and engineering integration cost. We cast single-GPU inference as a budget-aware design problem over these three axes and study how pruning, quantization, and KV-cache compression interact under realistic execution. Controlled ablations show that layer-wise pruning makes weight quantization more robust. KV-cache sparsification complements INT8 KV quantization by reducing memory without hurting decoding speed, while static vector quantizers often conflict with dynamic caching. Guided by these coupling results and explicit budget tracking, we assembled a practical pipeline and compressed a 70B model to about 33 GB, sustained about 57 tokens/s on 10k token prompts on a single A40, and kept absolute accuracy within 5% on common and reasoning benchmarks. We contribute design rules and a reproducible evaluation protocol that jointly report quality, memory, and end-to-end speed, and we provide a foundation for automated pipeline search under realistic single-GPU constraints.

## Metadata
- **Published**: 2026-08-30T22:54:40Z
- **Authors**: Hongyu Yu, Yifei Shen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30076v1)