---
title: DiffusionGemma Technical Report
url: http://arxiv.org/abs/2608.00146v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-07-31_16-11-46Z_DiffusionGemmaTechnicalReport.md
generated_at: 2026-08-03 20:09
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents DiffusionGemma, an open-weight language model that leverages discrete diffusion to generate text far faster than traditional autoregressive models. By refining 256‑token blocks in parallel and using a two‑stage fine‑tuning pipeline on the Gemma 4 base, it achieves roughly 1,500 output tokens per second on a single NVIDIA H100 GPU while maintaining most of the original model’s capabilities.

## Key Takeaways
- DiffusionGemma generates about 20 tokens per forward pass and reaches around 1,500 output tokens per second on one H100 GPU, which is significantly faster than AR models even with state‑of‑the‑art speculative decoding.  
- The two‑stage training pipeline uses less than 10% of the starting AR model’s total token budget: supervised fine‑tuning teaches bidirectional denoising, and a second stage combines reinforcement learning with sampler distillation to boost both quality and efficiency.  
- Despite diffusion fine‑tuning, DiffusionGemma retains support for thinking mode, multimodal inputs, and long contexts, showing only minor performance degradation compared to pure AR generation.

## Context
The rapid growth of large language models has highlighted a bottleneck: their autoregressive decoding is slow because it processes tokens sequentially. This paper addresses that limitation by introducing diffusion‑based inference, which can produce multiple tokens in parallel and thus dramatically increase throughput without sacrificing quality.

## Implications
For researchers, DiffusionGemma demonstrates a viable path toward hybrid decoding strategies that balance speed and capability, encouraging further exploration of non‑autoregressive generation techniques. For industry practitioners, the model’s high inference speed makes it attractive for real‑time applications such as chatbots, content creation, and interactive AI assistants where latency is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00146v1)
