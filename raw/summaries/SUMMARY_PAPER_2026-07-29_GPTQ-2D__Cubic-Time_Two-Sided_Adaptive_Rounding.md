---
title: GPTQ-2D: Cubic-Time Two-Sided Adaptive Rounding
url: http://arxiv.org/abs/2607.27042v1
type: paper-summary
date: 2026-07-29
source_paper: 2026-07-29_15-34-00Z_GPTQ_2D_Cubic_TimeTwo_SidedAdaptiveRounding.md
generated_at: 2026-07-29 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces GPTQ-2D, a cubic-time algorithm for adaptive rounding of real matrices when both left and right basis matrices are applied. It achieves the same rounded matrix as the original GPTQ method but reduces time complexity from quartic to cubic by processing anti-diagonal entries in parallel.

## Key Takeaways
- The two-sided rounding problem can be expressed as a quadratic metric with a Kronecker product Gram matrix, which would normally require quartic time when solved one-dimensionally.  
- GPTQ-2D processes each anti-diagonal independently, allowing parallel rounding and achieving cubic overall runtime.  
- The algorithm produces identical results to the original GPTQ method despite the different processing order.

## Context
Adaptive quantization techniques like GPTQ are crucial for compressing large language models without sacrificing performance. This work extends those ideas to matrix rounding in a two-sided basis, offering computational efficiency gains that could accelerate model compression pipelines.

## Implications
For practitioners, GPTQ-2D means faster preprocessing of model weights, enabling real-time deployment or on‑device inference where time is critical. The cubic complexity improvement may become a standard benchmark for adaptive quantization methods.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27042v1)
