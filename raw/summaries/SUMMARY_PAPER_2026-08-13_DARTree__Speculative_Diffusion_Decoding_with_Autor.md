---
title: DARTree: Speculative Diffusion Decoding with Autoregressive Draft Trees
url: http://arxiv.org/abs/2608.13524v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_17-43-44Z_DARTree_SpeculativeDiffusionDecodingwithAutoregres.md
generated_at: 2026-08-13 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DARTree, a training-free speculative decoding method that extends an autoregressive correction head to tree structures instead of linear chains. It demonstrates higher acceptance lengths and speedups across multiple benchmarks compared with existing approaches like DFlash and Domino.

## Key Takeaways
- DARTree builds a fixed-width candidate tree by expanding and scoring all nodes at each depth in one batch, which decouples AR‑head inference from sequential heap operations.
- The method achieves up to 12.97 tokens per verification round, representing 98.6% more acceptance than DFlash and 27.9% more than Domino under the same model temperature settings.
- It reaches a lossless speedup of up to 9.73× over locally measured autoregressive decoding, highlighting its efficiency gains.

## Context
Speculative decoding aims to accelerate language generation by generating multiple draft tokens in parallel and verifying them later. Recent diffusion‑based drafters predict token blocks simultaneously but suffer from marginal position distributions that are not conditioned on selected paths. DARTree addresses these limitations by leveraging tree structures for broader candidate coverage.

## Implications
This work shows that tree‑structured speculative decoding can outperform chain‑based methods, offering a scalable path to faster generation in large language models. Practitioners may adopt DARTree’s batch construction and pruning strategy to improve real‑time performance without retraining the model.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.13524v1)
