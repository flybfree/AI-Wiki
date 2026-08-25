---
title: SelFusion: Self-distillation for Diffusion Language Models
url: http://arxiv.org/abs/2608.22898v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_07-26-35Z_SelFusion_Self_distillationforDiffusionLanguageMod.md
generated_at: 2026-08-24 21:33
model: nvidia/nemotron-3-nano-4b
---

## Summary
Diffusion language models suffer from latency but generate lower quality text, limiting use. This paper introduces SelFusion, a self-distillation method that avoids external teacher and improves generation quality. Experiments show SelFusion outperforms other KD methods and sometimes exceeds the LLM teacher.

## Key Takeaways
- SelFusion uses two forward passes with different masking probabilities to create hard and easy modes for distillation.
- The easy mode can be overconfident on incorrect tokens, requiring bidirectional knowledge transfer between modes.
- Self-distillation yields substantial gains in instruction-following tasks and can surpass the performance of external teacher models.

## Context
Autoregressive LLMs are constrained by latency while diffusion models trade quality for speed. Recent work seeks to boost diffusion generation without sacrificing accuracy. SelFusion addresses this gap by enabling internal teacher-student interaction, reducing reliance on costly external models.

## Implications
Self-distillation offers a scalable way to enhance diffusion model outputs, potentially replacing or supplementing large language model teachers in production pipelines. This could lower computational costs and improve real-time applications where latency is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22898v1)
