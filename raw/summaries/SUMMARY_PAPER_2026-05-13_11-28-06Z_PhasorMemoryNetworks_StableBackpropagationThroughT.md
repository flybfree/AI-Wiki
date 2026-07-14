---

title: "Summary: Phasor Memory Networks: Stable Backpropagation Through Time for Scalable Explicit Memory"
url: http://arxiv.org/abs/2605.13370v1
type: paper-summary
date: 2026-06-11
source_paper: 2026-05-13_11-28-06Z_PhasorMemoryNetworks_StableBackpropagationThroughT.md
generated_at: "2026-06-11 10:39"
model: nvidia/nemotron-3-nano-4b

---
# Summary: 2026-05-13 11-28-06Z Phasormemorynetworks Stablebackpropagationthrought


## Summary
This paper introduces Phasor Memory Network (PMNet), a new architecture that tackles gradient instability in explicit memory models by using unitary phasor dynamics and hierarchical learnable anchors. The authors show that PMNet can retrieve data across long temporal distances with high accuracy, matching the performance of larger models like Mamba while being far smaller.

## Key Takeaways
- PMNet resolves memory volatility through phase rotations on a complex unit circle, preserving gradient norms without special initialization.
- An 85-slot hierarchical memory tree enables exact retrieval over distances beyond local attention windows in a byte‑level copy‑paste task.
- Despite only 119M parameters and training on 18.8B tokens, PMNet achieves zero‑shot long‑context robustness comparable to a three‑times larger Mamba model.

## Context
Explicit memory architectures such as Neural Turing Machines have struggled with backpropagation through time due to gradient blow‑up. This work provides a principled solution that could enable scalable sequence modeling without sacrificing performance or requiring massive compute.

## Implications
Practitioners can adopt PMNet’s design to build compact yet powerful models for long‑range tasks, reducing hardware costs and inference latency while maintaining state‑of‑the‑art accuracy in memory‑centric applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2605.13370v1)
