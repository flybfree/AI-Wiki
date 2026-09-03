---
title: Unfolding the Leech Lattice: Fused Multi-Shell Decoding and VRAM Layouts for 2-Bit LLM Weights
url: http://arxiv.org/abs/2609.02652v1
type: paper-summary
date: 2026-09-02
source_paper: 2026-09-02_14-26-06Z_UnfoldingtheLeechLattice_FusedMulti_ShellDecodinga.md
generated_at: 2026-09-02 23:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a fused multi‑shell decoder for leech‑lattice vector quantization and compares its serving cost with existing 2‑bit codebooks. It shows that a full 301‑class codebook can be decoded efficiently on GPU, achieving higher throughput than one‑hot masks while keeping bandwidth constant.

## Key Takeaways
- The fused kernel reads the entire 301‑class leech lattice in a single GPU layout, eliminating warp divergence and matching f64 reference results.  
- Bit‑exact layouts up to 4.8 bits per weight outperform one‑hot masks on both size and speed at constant bandwidth of 4.80 bits per weight.  
- The trellis kernel consumes fewer bytes and runs faster than the served layout, illustrating the tradeoff between codebook size and lookup‑table overhead.

## Context
Leech lattice vector quantization is a promising technique for compressing large language model weights into ultra‑low bit depths while preserving quality. Efficient GPU kernels are essential to realize these savings in real‑time inference pipelines.

## Implications
This work demonstrates that multi‑shell decoding can be integrated with standard GEMV kernels, reducing memory traffic and increasing token generation speed. Practitioners can adopt the layout strategy to push 2‑bit quantization further without sacrificing performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.02652v1)
