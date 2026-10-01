---
title: Low-Discrepancy Dither for Quantized Recurrent State Caches
url: http://arxiv.org/abs/2609.39185v1
type: paper-summary
date: 2026-09-30
source_paper: 2026-09-30_07-41-07Z_Low_DiscrepancyDitherforQuantizedRecurrentStateCac.md
generated_at: 2026-09-30 22:10
model: qwen3.6-35b-a3b
---

## Summary
This paper investigates optimal rounding strategies for quantized recurrent state caches in Mamba-style and hybrid language models, addressing the accumulation of rounding errors during long-generation decoding. The authors demonstrate that a deterministic golden-ratio Weyl dither consistently outperforms stochastic rounding and round-to-nearest methods across various model architectures and storage formats, bringing quantized models closer to full-precision performance without additional computational overhead.

## Key Takeaways
- A deterministic golden-ratio Weyl dither rounding scheme provides superior accuracy compared to stochastic rounding used in production systems, maintaining alignment with full-precision models over extended decoding horizons without requiring random number generation or incurring extra costs.
- Round-to-nearest rounding exhibits deceptive short-term performance by discarding small updates, which causes error accumulation to grow steadily over time; while it may appear favorable in brief evaluations, it significantly degrades model quality during long-generation tasks compared to dithering approaches.
- A discrepancy analysis elucidates the mathematical ordering of rounding behaviors, revealing why Weyl dither minimizes error propagation in recurrent state updates, while the authors also document specific implementation pitfalls that can inadvertently nullify the benefits of these advanced rounding techniques if not carefully managed.

## Context
Efficient inference in large language models increasingly relies on quantization to reduce memory bandwidth and accelerate generation, particularly for stateful architectures like Mamba that maintain recurrent states across tokens. As deployment demands push for lower precision storage, understanding how rounding errors propagate through these fixed-size caches becomes critical for maintaining model fidelity without sacrificing efficiency gains.

## Implications
Practitioners deploying quantized recurrent models should adopt Weyl dithering to ensure robust performance in long-context scenarios, avoiding the silent degradation associated with standard rounding methods. This work provides actionable guidance for optimizing inference engines and cache management strategies, enabling higher-quality generation at lower precision levels while highlighting implementation nuances necessary to realize theoretical benefits.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.39185v1)
