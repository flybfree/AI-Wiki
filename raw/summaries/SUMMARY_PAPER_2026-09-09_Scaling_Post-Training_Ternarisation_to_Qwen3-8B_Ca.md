---
title: Scaling Post-Training Ternarisation to Qwen3-8B Capability Retention, Reproduction, Lossless Packing, and Packed Execution
url: http://arxiv.org/abs/2609.09240v1
type: paper-summary
date: 2026-09-09
source_paper: 2026-09-08_06-21-44Z_ScalingPost_TrainingTernarisationtoQwen3_8BCapabil.md
generated_at: 2026-09-09 20:16
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper scales an aggressive post‑training ternarisation pipeline from a 4B to an 8B model while preserving capability. It shows the 8B version retains performance comparable to FP16 but uses far less memory.

## Key Takeaways
- The 8B model reaches a three‑corpus perplexity ratio of 1.361x across WikiText‑2, C4 and PTB.
- Zero‑shot accuracy drops from 72.4% (FP16) to 64.6%, yielding an 8.9‑point advantage over the retained 4B run.
- The packed checkpoint is only 8.24 GiB and matches recorded perplexity precisely.

## Context
Ultra‑low‑bit models aim to cut storage and compute, yet their real‑world deployment depends on how bits are represented and executed.

## Implications
This work validates that aggressive quantization can be safely applied to large language models without sacrificing utility. It opens the door for cost‑effective inference in resource‑constrained settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.09240v1)
