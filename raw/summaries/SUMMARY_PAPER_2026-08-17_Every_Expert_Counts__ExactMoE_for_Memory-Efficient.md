---
title: Every Expert Counts: ExactMoE for Memory-Efficient W4A16 Inference
url: http://arxiv.org/abs/2608.15383v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_19-26-07Z_EveryExpertCounts_ExactMoEforMemory_EfficientW4A16.md
generated_at: 2026-08-17 21:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces ExactMoE, a memory‑efficient inference design for mixture‑of‑experts language models that keeps all experts available while reducing GPU memory usage. By applying symmetric group‑128 four‑bit quantization to routed experts and storing them in kernel‑native MARLIN form, the approach cuts peak reserved GPU memory dramatically without altering routing or numerical results.

## Key Takeaways
- ExactMoE stores only the selected experts in a GPU slot cache using 4‑bit weight quantization, reducing peak reserved GPU memory from 14.168 GiB to 1.836 GiB for a 16‑slot configuration.
- The fused grouped MoE kernels execute all routed experts simultaneously, achieving 1.97× speedup over sequential W4 reference while maintaining high decode throughput.
- Accuracy loss is minimal: ExactMoE reaches 70.35% normalized accuracy on zero‑shot multiple‑choice tasks versus 70.90% for the BF16 baseline.

## Context
Mixture‑of‑experts models scale to billions of parameters by routing tokens to a subset of experts, yet full deployment still requires loading all experts into GPU memory, limiting practical size. This work addresses that bottleneck with exact expert availability and efficient storage techniques.

## Implications
Practitioners can deploy larger MoE models on limited hardware without sacrificing performance or accuracy. The approach enables cost‑effective inference for real‑time applications where both memory and compute are constrained.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15383v1)
