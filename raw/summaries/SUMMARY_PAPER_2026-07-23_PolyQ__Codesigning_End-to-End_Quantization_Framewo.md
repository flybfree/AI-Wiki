---
title: PolyQ: Codesigning End-to-End Quantization Framework for Scalable Edge CPU LLM Inference
url: http://arxiv.org/abs/2607.14618v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-16_06-31-39Z_PolyQ_CodesigningEnd_to_EndQuantizationFrameworkfo.md
generated_at: 2026-07-23 23:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
PolyQ is a CPU‑oriented compiler/quantization co‑design that allocates per‑channel bit widths from {2,3,4,8,16} while respecting a user‑specified average‑bit budget. It produces SIMD‑ and LUT‑compatible kernels with regular channel layouts, achieving fractional‑bit deployment on edge CPUs.

## Key Takeaways
- PolyQ assigns per‑channel bit widths from {2,3,4,8,16} and uses a compile‑time model to permute channels into homogeneous blocks.  
- The compiler merges compatible permutations across operators, keeping layout regularization off the runtime path.  
- Across three models on WikiText‑2, PolyQ improves perplexity by up to 32.1% at a 3‑bit budget while keeping energy overhead below 2%.

## Context
Edge deployment of large language models faces challenges from limited compute and power budgets. Existing quantization methods either use coarse bit depths or fine‑grained mixed precision that is hard to implement efficiently on CPUs.

## Implications
PolyQ demonstrates that fractional‑bit quantization can be practical for edge devices, offering predictable performance and low energy cost. This could enable more compact and efficient LLM inference in smartphones, wearables, and embedded systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.14618v1)
