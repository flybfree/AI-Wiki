---
title: NANQ: Noise-Floor-Aware Mixed-Precision Non-Uniform Quantization for Analog Compute-in-Memory
url: http://arxiv.org/abs/2608.02700v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-03_14-21-21Z_NANQ_Noise_Floor_AwareMixed_PrecisionNon_UniformQu.md
generated_at: 2026-08-05 01:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces NANQ, a noise‑aware mixed‑precision non‑uniform quantization scheme for analog compute‑in‑memory (CIM). Experiments on an eFlash CIM SoC show that NANQ boosts vision‑model accuracy by 8.05 percentage points and cuts language‑model perplexity by 54.7 % compared with PowerQuant while using only 3.2–3.8 equivalent bits.

## Key Takeaways
- Magnitude‑dependent weight noise is modeled from measured eFlash CIM responses, turning the hardware’s noise profile into an adaptive quantization density.  
- Finer resolution is assigned to low‑noise regions and coarser resolution to noise‑dominated areas, avoiding ineffective precision allocation.  
- Layer‑wise bit widths are determined by a unified threshold that identifies each layer’s precision saturation point under the hardware noise.

## Context
Analog compute‑in‑memory promises energy‑efficient inference but suffers from device variation and read noise that degrade low‑bit models. Existing quantization approaches focus solely on ideal error minimization, ignoring these practical constraints and leading to inefficient precision usage.

## Implications
NANQ demonstrates that mixed‑precision quantization can unlock substantial accuracy gains in analog hardware with minimal additional bits, encouraging both researchers and industry practitioners to adopt noise‑aware strategies for deploying quantized neural networks on CIM platforms.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.02700v1)
