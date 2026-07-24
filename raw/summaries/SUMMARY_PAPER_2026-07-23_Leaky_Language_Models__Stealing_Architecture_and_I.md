---
title: Leaky Language Models: Stealing Architecture and Inference Optimizations via Per-Token Timing
url: http://arxiv.org/abs/2607.20723v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-22_20-51-28Z_LeakyLanguageModels_StealingArchitectureandInferen.md
generated_at: 2026-07-23 23:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
LeakyLMs is a set of attacks that infer proprietary model architecture and deployment details from token generation timing alone. The paper demonstrates two attacks: one detecting speculative decoding and context length, the other recovering layer count, hidden dimension, and attention heads. Experiments show near‑correct architectural guesses in top‑10 with 90% probability.

## Key Takeaways
- LeakyLMs can detect whether a provider uses speculative decoding and infer its draft context window of about 128K tokens.
- The timing model reveals hidden dimension size, number of transformer layers, and attention heads without accessing model weights.
- Searching the architecture space using this timing data yields near‑correct configurations in top‑10 guesses over 90% of the time.

## Context
Token generation latency is a common metric for inference optimization but has not been studied as a leakage vector. This work shows that such metrics can be exploited to reconstruct confidential model details, highlighting a gap between security and performance engineering.

## Implications
For cloud AI services, timing information could become a new attack surface, forcing providers to protect latency data as sensitive. Practitioners must consider that even without exposing weights, architectural leakage may impact competitive advantage.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.20723v1)
