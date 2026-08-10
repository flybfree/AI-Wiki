---
title: MiCoPro: End-to-End Mixed Precision HW/SW Co-design with HW-aware Proxy Model
url: http://arxiv.org/abs/2608.06916v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_07-50-42Z_MiCoPro_End_to_EndMixedPrecisionHW_SWCo_designwith.md
generated_at: 2026-08-09 22:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces MiCoPro, an end‑to‑end framework that jointly optimizes mixed‑precision quantization and hardware deployment for edge AI. By integrating a hardware‑aware proxy model, the method achieves up to 40 % latency reduction with less than 3 % accuracy loss on both BitFusion accelerators and SIMD‑extended RISC‑V processors.

## Key Takeaways
- MiCoPro combines mixed‑precision quantization exploration with a hardware‑aware proxy that models target latency, enabling rapid optimization from PyTorch to bare‑metal C.  
- The framework’s novel algorithm respects strict latency constraints while maximizing accuracy, demonstrating strong trade‑off performance on two heterogeneous edge platforms.  
- Results show up to 40 % latency reduction with less than 3 % accuracy drop, highlighting the effectiveness of hardware‑aware modeling in quantization.

## Context
Quantized neural networks are increasingly vital for deploying AI on resource‑constrained devices where storage and compute efficiency matter. Mixed‑precision quantization offers a way to balance speed and fidelity but lacks systematic tools for end‑to‑end deployment across different hardware. This work fills that gap by providing a unified approach.

## Implications
The framework lowers the barrier for developers to create latency‑optimized, low‑bitwidth models without sacrificing performance. For industry practitioners, it enables faster prototyping of edge AI solutions and reduces time spent on manual quantization tuning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06916v1)
