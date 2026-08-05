---
title: Maglev: Sliding Recurrent Memory
url: http://arxiv.org/abs/2608.02870v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-03_20-40-49Z_Maglev_SlidingRecurrentMemory.md
generated_at: 2026-08-05 01:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a recurrent Transformer with fixed-size memory that generalizes sliding-window attention while remaining parallelizable during training. It achieves better validation loss and pretraining benchmarks compared to sliding-window and latent recurrent transformer baselines, thanks to a memory consistency loss aligning decoder memories with prefiller outputs. The design decouples full attention from local attention via shared parameters.

## Key Takeaways
- The architecture uses two coupled models Q (prefiller) that can use full attention to generate memory targets m'_t, while P (decoder) uses only sliding-window attention plus K/V injection.
- Memory consistency loss aligns m_t with m'_t enabling inference using just P.
- Parameter sharing between Q and P reduces parameter memory while preserving most of the gains.

## Context
This work addresses the trade-off between long-range context modeling in Transformers and computational efficiency, a persistent challenge as models scale. By decoupling full attention from sliding-window attention via recurrent memory injection, it offers a scalable alternative to pure autoregressive transformers.

## Implications
Practitioners can implement this architecture with reduced memory footprint, enabling larger models that still capture long dependencies without prohibitive compute cost. It may inspire future hybrid architectures combining global and local attention in sequence modeling tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02870v1)
