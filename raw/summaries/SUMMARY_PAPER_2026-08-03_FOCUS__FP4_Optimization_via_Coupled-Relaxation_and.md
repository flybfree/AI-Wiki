---
title: FOCUS: FP4 Optimization via Coupled-Relaxation and Dual-Granularity Scaling
url: http://arxiv.org/abs/2608.01847v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_07-54-56Z_FOCUS_FP4OptimizationviaCoupled_RelaxationandDual_.md
generated_at: 2026-08-03 23:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FOCUS, a post‑training quantization framework that optimizes FP4 precision for large language models. It uses Coupled‑Relaxation Scaling and Dual‑Granularity Scaling to improve accuracy without extra inference cost.

## Key Takeaways
- The framework decouples the quantization and dequantization scales with a learnable coefficient, allowing independent optimization while still respecting hardware constraints such as E8M0.  
- A finer sub‑block granularity in Dual‑Granularity Scaling enables local adaptation to weight distributions, improving accuracy beyond coarse scaling.  
- Experiments show state‑of‑the‑art FP4 results on MXFP4 and NVFP4 formats with no added latency.

## Context
Large language models benefit from low‑precision quantization but hardware support is limited by strict scale formats. Existing methods suffer because they force both scales into a single discrete value, wasting optimization potential.

## Implications
This work opens a path to higher accuracy in FP4 deployment without sacrificing performance or speed, encouraging more aggressive precision tuning in AI hardware and software pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01847v1)
