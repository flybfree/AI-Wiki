---
title: SAGA: Structure-Attended Generative Action Embedding Model that encodes Multi-Surface User Action Sequences
published: 2026-08-15T22:11:34Z
authors: Tsz Fung Pang, Po Jen Chen, Nimish Ronghe, Farhad Farahani, Bo Zhang
url: http://arxiv.org/abs/2608.15429v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SAGA: Structure-Attended Generative Action Embedding Model that encodes Multi-Surface User Action Sequences

## Abstract
Prior embedding models for sequential recommendation typically operate within a homogeneous action space, limiting their ability to capture cross-surface behavioral signals spanning distinct behavioral domains. We present SAGA, a generative action embedding model that encodes multi-surface user interaction sequences across a Financial Service organization's ecosystems, from checkout, peer-to-peer (P2P) transactions, in-app engagement, email to account actions, into a unified user representation for downstream recommendation tasks. Central to SAGA is a per-field tokenization schema that decomposes each action event into multiple field-level tokens (e.g. product, interaction, surface), enabling field-level attention and per-field training objectives that fused single-token approaches cannot support. Through an offline ablation study on loss formulation, tokenization granularity and training data scope, we isolate the contribution of each design choice. A downstream model integrated with SAGA-generated user embeddings delivers the strongest overall click and conversion lift across diverse downstream touchpoints, compared to all ablated and alternative architectures.

## Metadata
- **Published**: 2026-08-15T22:11:34Z
- **Authors**: Tsz Fung Pang, Po Jen Chen, Nimish Ronghe, Farhad Farahani, Bo Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15429v1)