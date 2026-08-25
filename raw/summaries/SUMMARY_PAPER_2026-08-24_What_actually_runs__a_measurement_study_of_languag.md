---
title: What actually runs: a measurement study of language model placement and decode speed on the Apple Neural Engine
url: http://arxiv.org/abs/2608.22110v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-22_21-22-24Z_Whatactuallyruns_ameasurementstudyoflanguagemodelp.md
generated_at: 2026-08-24 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper measures which language model components run on Apple’s Neural Engine and how fast they execute, using three measurement methods. It finds that placement depends on how a computation is expressed rather than what it computes; weight encoding determines whether the accelerator is used; and decode cost remains roughly constant across precision formats.

## Key Takeaways
- Placement is determined by how a computation is expressed, e.g., a fused RMSNorm runs on ANE while its decomposed version does not.  
- Weight encoding gates the accelerator: conv‑heavy fp16 models stay CPU‑only, int8/2‑bit versions run ~83% on ANE and are 1.8–2.2× faster; a smaller all‑attention fp16 model sits at 98.9% residency.  
- Decode cost is about 0.77 bytes per token across precisions, and ternary models achieve the smallest size (~10 MB) and fastest speed (~0.63 ms/token).

## Context
This study provides empirical evidence that Apple’s ANE can accelerate LLM inference beyond what compilers assume, highlighting the importance of model encoding choices in mobile AI.

## Implications
Practitioners should prioritize quantization and fused operations to maximize accelerator usage; designers must consider byte budget over parameter count; this research guides future hardware‑software co‑design for mobile AI.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22110v1)
