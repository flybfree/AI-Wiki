---
title: Accelerating Cross-Model LLM Inference via Attention Map Reuse
published: 2026-10-10T08:02:52Z
authors: Zhan Jin, Yuze Luo, Bin Cui, Xupeng Miao
url: http://arxiv.org/abs/2610.14688v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Accelerating Cross-Model LLM Inference via Attention Map Reuse

## Abstract
LLM-augmented data workflows often involve multiple heterogeneous models operating over substantial shared context, such as schemas, tool specifications, interaction history, and intermediate results. Although prefix caching can reduce prefilling overhead, existing approaches are largely limited to reuse within the same model because KV states are tightly coupled to model-specific architectures. We present MapFlow, a system for efficient heterogeneous LLM serving via cross-model attention map reuse. Instead of reusing KV states, MapFlow reuses attention maps, which capture token dependency patterns and are more transferable across models. To enable efficient and accurate reuse, we combine partial recomputation with lightweight linear translation across layers and heads. To make attention reuse practical for long contexts, we further introduce block-level sparse compression and a fused retrieval kernel. Experiments show that MapFlow reduces prefilling latency and improves end-to-end serving efficiency while preserving generation quality across heterogeneous model pairs and multi-turn routing workloads. These results suggest that attention maps provide an effective reusable state for heterogeneous LLM serving, especially in prefix-heavy data workflows. Our code is available: https://github.com/PKU-DAIR/MapFlow.

## Metadata
- **Published**: 2026-10-10T08:02:52Z
- **Authors**: Zhan Jin, Yuze Luo, Bin Cui, Xupeng Miao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.14688v1)