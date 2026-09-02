---
title: Vision Is Not Overhead: One-Pass Block Drafting for Lossless Speculative Decoding in Vision-Language Models
url: http://arxiv.org/abs/2609.00355v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-31_20-50-35Z_VisionIsNotOverhead_One_PassBlockDraftingforLossle.md
generated_at: 2026-09-01 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces GLANCE, a one-pass block drafter that enables lossless speculative decoding for vision-language models by reading the fused vision‑language state and filling an entire block in a single forward pass. It eliminates the need to store or compress images at each step, breaking the self‑defeating cycle of autoregressive drafters and achieving up to 2.93× faster generation with only one draft pass per round.

## Key Takeaways
- GLANCE reads the target's already fused vision‑language state, so vision costs the drafter nothing and fills a block in one forward pass.
- The candidate tree is verified in one target pass, guaranteeing that every audited prompt reproduces greedy decoding exactly.
- Under one engine and round budget, GLANCE decodes up to 2.93× faster than autoregressive methods, accepting longer blocks while maintaining lossless fidelity.

## Context
Vision‑language models face a fundamental bottleneck: speculative decoding requires the drafter to be small enough to stay within token limits, yet this forces image compression that degrades reliability where visual cues are strongest. GLANCE’s block‑diffusion head addresses this by decoupling vision cost from draft length, offering a scalable alternative.

## Implications
GLANCE demonstrates that lossless speculative decoding can outperform autoregressive approaches in real‑world workloads, suggesting a path to faster generation without sacrificing quality. Practitioners may adopt it to reduce latency and computational overhead in multimodal systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00355v1)
