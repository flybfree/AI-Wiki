---
title: RotaryQuant: Fitting 120B MoE Models on Consumer Hardware via Fused Compressed-Space Attention
url: http://arxiv.org/abs/2608.08081v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_11-58-56Z_RotaryQuant_Fitting120BMoEModelsonConsumerHardware.md
generated_at: 2026-08-10 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces RotaryQuant, a three‑axis compression system that reduces the memory footprint of large MoE models by quantizing dense weights to 4 bits, routing experts to 2 bits, and applying IsoQuant to compress key‑value caches to 3 bits while preserving performance. The fused GPU pipeline executes attention directly on packed tensors without materializing full‑precision KV state, enabling models up to 120 B to run within consumer hardware budgets.

## Key Takeaways
- Mixed‑precision weight quantization uses 4‑bit for dense layers, 2‑bit for routed experts and 8‑bit for the shared expert with high activation kurtosis.  
- LRU expert offloading pages non‑resident experts to disk only when memory pressure occurs.  
- IsoQuant compresses KV caches using a Walsh–Hadamard transform followed by block‑diagonal SO(4) rotations, achieving 3‑bit scalar quantization and O(d log d) cost versus O(d²).

## Context
Large MoE models such as Gemma or Qwen exceed typical consumer GPU memory, limiting deployment. Traditional compression methods either sacrifice performance or require large temporary buffers, making real‑time interaction difficult.

## Implications
This work demonstrates that state‑of‑the‑art language models can be served on a 16 GB device with near‑zero perplexity loss, encouraging developers to adopt compressed MoE architectures for edge AI applications. The fused execution model also reduces hardware complexity and power consumption.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08081v1)
