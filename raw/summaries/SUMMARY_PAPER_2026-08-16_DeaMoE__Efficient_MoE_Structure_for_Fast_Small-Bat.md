---
title: DeaMoE: Efficient MoE Structure for Fast Small-Batch Decoding
url: http://arxiv.org/abs/2608.14385v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_15-25-32Z_DeaMoE_EfficientMoEStructureforFastSmall_BatchDeco.md
generated_at: 2026-08-16 20:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
Mixture-of-Experts models face a memory bottleneck during small‑batch decoding because expert weights must be loaded each step. DeaMoE solves this by grouping experts into departments that share most parameters, adding private parameters for uniqueness, and using a two‑stage routing strategy that avoids redundant loading, achieving up to 50.9% fewer loaded weights and speedups of 1.33–2.0 on A40/H100.

## Key Takeaways
- Grouping experts into departments reduces per‑step loaded weights by ~50.9%, cutting the memory bottleneck.
- The custom two‑stage routing eliminates redundant loading, improving throughput without sacrificing accuracy.
- DeaMoE delivers up to 2.0x speedup on H100 and 1.33x on A40 for a pre‑trained 7B model.

## Context
Real‑time interactive AI systems demand ultra‑low latency, yet MoE inference is often limited by the time spent loading expert weights rather than computation. This paper addresses that bottleneck with an architectural redesign tailored to decoding efficiency.

## Implications
The approach can be applied broadly across any MoE deployment, offering a scalable method to accelerate decoding on edge devices and cloud services. It encourages further research into parameter‑sharing strategies for low‑latency AI inference.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14385v1)
