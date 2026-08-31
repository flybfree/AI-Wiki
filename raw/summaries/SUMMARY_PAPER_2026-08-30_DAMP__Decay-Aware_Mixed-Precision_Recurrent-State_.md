---
title: DAMP: Decay-Aware Mixed-Precision Recurrent-State Quantization
url: http://arxiv.org/abs/2608.27513v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-27_09-11-48Z_DAMP_Decay_AwareMixed_PrecisionRecurrent_StateQuan.md
generated_at: 2026-08-30 20:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces DAMP, a quantization method for recurrent states in Gated DeltaNet and Kimi Delta Attention models. It shows that uniform INT8 or FP8 quantization harms reasoning accuracy on complex tasks while INT4 and NVFP4 reduce degradation to near zero. By using decay‑aware channel analysis, DAMP stores high‑risk channels at higher precision and reduces storage by 69 % with speedups up to 2×.

## Key Takeaways
- Uniform INT8 or FP8 quantization degrades reasoning accuracy on complex tasks while INT4 and NVFP4 reduce degradation to near zero. - The energy of quantization errors is concentrated in a small subset of channels, allowing selective higher‑precision storage. - Recurrent‑state update kernels speed up by up to 2.01× and full‑model throughput improves by 10.9%.

## Context
Language models increasingly rely on recurrent state mechanisms to avoid growing KV caches during inference, yet these states are often stored in high‑precision formats that limit model size and speed. This work addresses the trade‑off between memory efficiency and accuracy for such states.

## Implications
DAMP enables larger language models to run efficiently with minimal loss of performance, supporting deployment on resource‑constrained devices. Practitioners can adopt channel‑aware quantization strategies to balance storage, latency, and reasoning quality in real‑time applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.27513v1)
