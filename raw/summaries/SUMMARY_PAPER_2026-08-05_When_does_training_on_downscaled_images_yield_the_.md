---
title: When does training on downscaled images yield the same gradients?
url: http://arxiv.org/abs/2608.04448v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-05_04-53-46Z_Whendoestrainingondownscaledimagesyieldthesamegrad.md
generated_at: 2026-08-05 23:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether training diffusion transformers on downscaled images preserves the native gradient signal, which is crucial for efficient fine‑tuning. It introduces a decomposition of the gradient change into a noise‑dependent term and an absolute token count floor, showing that certain resolution and noise combinations keep gradients close to those computed at full resolution.

## Key Takeaways
- The gradient preservation depends on two factors: a ratio‑based decay at high noise levels and a constant floor set by the target grid’s token count.  
- A specific window (0.65 < σ< 0.95) for the 1024→768 downscale route yields gradients within a small margin of the native ones, despite no spectral criterion predicting this.  
- Training LoRA adapters restricted to these routes and noise windows cut training time by about 14.6% while keeping weight space close to native.

## Context
Training diffusion models at full resolution is computationally expensive, prompting interest in lower‑resolution training strategies. Understanding how gradients behave under downsampling could unlock faster fine‑tuning pipelines without sacrificing model quality.

## Implications
Practitioners can selectively apply downscaled steps where they are safe, reducing GPU usage and time while maintaining performance. This insight streamlines large‑scale diffusion model deployment and personalizes training resources per workload.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.04448v1)
