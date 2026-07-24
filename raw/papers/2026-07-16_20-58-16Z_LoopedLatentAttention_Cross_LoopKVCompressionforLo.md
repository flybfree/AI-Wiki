---
title: Looped Latent Attention: Cross-Loop KV Compression for Looped Transformers
published: 2026-07-16T20:58:16Z
authors: James O' Neill, Fergal Reid
url: http://arxiv.org/abs/2607.15456v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Looped Latent Attention: Cross-Loop KV Compression for Looped Transformers

## Abstract
Looped, weight-tied Transformers reduce parameters by reusing a block, but decoding still stores a separate K/V cache for every recurrence step. We show that this loop-indexed cache is highly structured. For a fixed token, layer and head, K/V vectors trace a short low-rank trajectory across loops, while the head and layer axes remain much flatter. We introduce Looped Latent Attention (LLA), a post-training cache codec that stores compact K and V latents and reconstructs loop-specific K/V vectors only when attention reads them. The default per-head codec compresses recurrence, while LLA-2D also folds heads into one latent for the extreme-compression regime. The codec is initialized from SVD of teacher activations and refined with KL and attention-output distillation. At matched cache budget, per-head LLA outperforms head-axis MLA, cross-layer sharing, KV quantization and final-loop reuse, showing that the recurrent cache is low-rank but not safely collapsible to a single state. The same axis advantage holds on Ouro-2.6B-Thinking and transfers to Huginn-3.5B, where an SVD codec remains near-lossless to 32x in decoder-independent evaluation. The cache reduction is exact. On one H200, the latent-store path increases measured Ouro-1.4B batch capacity at 4k context from 32 to 768 sequences at 21.3x compression. For long math rollouts, on-policy refinement on student-generated prefixes raises MATH-500 at 4x from 0.43 to 0.66 and reduces no-answer generations.

## Metadata
- **Published**: 2026-07-16T20:58:16Z
- **Authors**: James O' Neill, Fergal Reid
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.15456v1)