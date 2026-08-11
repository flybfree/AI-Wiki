---
title: Addressable Memory for Video World Models
published: 2026-08-07T16:55:57Z
authors: Xindi Wu, Sven Elflein, James Lucas, Olga Russakovsky, Laura Leal-Taixé, Despoina Paschalidou, Jonathan Lorraine, Aljoša Ošep
url: http://arxiv.org/abs/2608.07408v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Addressable Memory for Video World Models

## Abstract
We study visual persistence in interactive video world models. These models rely on a Key-Value (KV) cache as a growing visual memory to carry forward previously generated frames. However, we find that models can no longer reliably address stored content once rollouts extend beyond the training horizon, because temporal Rotary Positional Embeddings (RoPE) offsets then fall outside the range seen during training and the model struggles to retrieve the relevant visual information through attention. Moreover, naively compressing the cache in the RoPE-rotated space corrupts memory by averaging together incompatible positional phases. To address this, we propose WorldTrace, a training-free memory framework for long-horizon visual persistence. WorldTrace keeps compressed memory addressable by assigning each summary slot a distinct, in-distribution virtual position. Within this addressable cache, we study two memory compression approaches: WorldTrace-Field compresses history for temporal coherence, while WorldTrace-Landmark stores verbatim scene traces at detected transitions for episodic recall. We further introduce LoopBench, a benchmark evaluating whether a compressed cache can reconstruct a previously visited scene after a long detour. WorldTrace-Field improves temporal consistency by +15.5%, and WorldTrace-Landmark improves episodic recall by +19.5% on LoopBench, extending visually persistent generation without retraining.

## Metadata
- **Published**: 2026-08-07T16:55:57Z
- **Authors**: Xindi Wu, Sven Elflein, James Lucas, Olga Russakovsky, Laura Leal-Taixé, Despoina Paschalidou, Jonathan Lorraine, Aljoša Ošep
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07408v1)