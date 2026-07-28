---
title: Structure over Depth: A Single-Block Spatio-Temporal Transformer for Multi-Entity Reasoning
published: 2026-07-25T07:02:07Z
authors: Narthana Sivalingam, Santhirarajah Sivasthigan, Buddhi Wijenayake, Roshan Godaliyadda, Vijitha Herath, Parakrama Ekanayake
url: http://arxiv.org/abs/2607.23077v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Structure over Depth: A Single-Block Spatio-Temporal Transformer for Multi-Entity Reasoning

## Abstract
Modeling multi-entity temporal data requires capturing dependencies across entities, time, and their interactions. Transformer-based approaches perform well but often rely on deep stacks of layers to learn these heterogeneous dependencies implicitly, increasing computational cost. We revisit this problem from a structural perspective and decompose multi-entity temporal dynamics into three interaction types: spatial interactions among entities, temporal interactions across time, and cross interactions coupling the two domains. We propose a structured spatio-temporal transformer block that explicitly models all three within a single stage. It uses parallel spatial and temporal self-attention, followed by bidirectional cross-attention, and combines the outputs through learnable gated fusion. By directly encoding these complementary views, the model reduces the need for deep stacking. We evaluate the approach on video-based group activity recognition, skeleton-based human interaction analysis, and wearable sensor-based activity recognition. Despite its simplicity, the single structured Transformer block matches or outperforms deeper architectures with only 1.76M parameters. The results suggest that depth in prior models partly compensates for implicit and entangled interaction modeling, whereas explicit factorization offers a more efficient and transparent alternative. More broadly, this work supports a structure-first design principle: expressive multi-entity temporal reasoning can emerge by exposing interaction structure rather than relying on depth.

## Metadata
- **Published**: 2026-07-25T07:02:07Z
- **Authors**: Narthana Sivalingam, Santhirarajah Sivasthigan, Buddhi Wijenayake, Roshan Godaliyadda, Vijitha Herath, Parakrama Ekanayake
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23077v1)