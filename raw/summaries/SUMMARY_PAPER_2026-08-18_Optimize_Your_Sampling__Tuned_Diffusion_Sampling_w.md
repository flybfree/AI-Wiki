---
title: Optimize Your Sampling: Tuned Diffusion Sampling with Bayesian Optimization
url: http://arxiv.org/abs/2608.18040v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_17-33-00Z_OptimizeYourSampling_TunedDiffusionSamplingwithBay.md
generated_at: 2026-08-18 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Optimizing Your Sampling (OYS), a method that treats the selection of diffusion model timesteps as a black‑box optimization problem solved with Bayesian optimization. The authors demonstrate that OYS improves both quantitative and human evaluations compared to standard schedules such as default and Align Your Steps, while requiring no extra training or distillation.

## Key Takeaways
- OYS directly optimizes the sampling schedule using Bayesian optimization rather than optimizing a surrogate model for sample quality.
- A 5‑step OYS schedule retains roughly 89‑94% of the quality of a 50‑step schedule yet cuts inference cost by tenfold.
- The approach works on both simple samplers like Euler and advanced solvers such as DPM‑Solver++, including distilled models, without additional training.

## Context
Efficient generation from diffusion models remains limited by costly forward passes during sampling. While many efforts focus on faster solvers or better schedules, the paper highlights that the actual timestep sequence can be a hidden bottleneck. This work bridges that gap by applying advanced optimization to schedule design itself.

## Implications
For practitioners, OYS offers a practical way to reduce generation latency without sacrificing visual fidelity, making high‑quality diffusion outputs more accessible in real‑time applications. The method’s generality could inspire future research into adaptive model configurations and cost‑aware training pipelines.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.18040v1)
