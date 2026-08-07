---
title: EdgeXpert: An Edge Device for Memory-Efficient LLM Inference with Mixture-of-Experts and Speculative Decoding
url: http://arxiv.org/abs/2608.05303v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-05_18-03-47Z_EdgeXpert_AnEdgeDeviceforMemory_EfficientLLMInfere.md
generated_at: 2026-08-06 21:35
model: nvidia/nemotron-3-nano-4b
---

## Summary
EdgeXpert proposes a co-designed accelerator that integrates mixture-of-experts routing with speculative decoding to reduce external memory access in LLM inference on edge devices. The paper demonstrates that by reformulating expert reuse at the prompt level and using depth-aware coalescing during decode, the system cuts latency by up to 56% and energy use by 44% while keeping accuracy near baseline.

## Key Takeaways
- EdgeXpert resolves incompatibility between MoE and speculative decoding by applying prompt-wise expert reuse in prefill, which reduces per-token routing cost.
- The depth-aware expert coalescing loads only salient channels during decode, avoiding full channel union and lowering memory traffic.
- Synthesized at 28nm with 800 MHz clock, EdgeXpert achieves significant latency and energy savings compared to prior LLM accelerators.

## Context
Edge device deployment of LLMs faces severe constraints from external memory access in feed-forward layers. Prior solutions either sacrifice accuracy or increase compute. This work shows that hardware-software co-design can overcome these trade-offs.

## Implications
For practitioners, EdgeXpert offers a practical path to run large models locally with minimal power and latency. For industry, it enables scalable edge AI services without cloud dependency.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05303v1)
