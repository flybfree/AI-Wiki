---
title: Retrofitting Linear Attention into Diffusion Language Models
url: http://arxiv.org/abs/2608.06628v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-06_22-34-20Z_RetrofittingLinearAttentionintoDiffusionLanguageMo.md
generated_at: 2026-08-09 22:03
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces block‑hybrid attention to retrofit linear attention into diffusion language models, demonstrating that replacing a subset of the model’s attention layers with linear attention yields faster inference while preserving performance on standard benchmarks.

## Key Takeaways
- Block‑hybrid attention retains exact softmax within the active denoising block but applies linear attention over previous blocks.
- Retrofitting this hybrid attention can replace 6 of the 20 attention layers in LLaDA~2.1, requiring only about 60 hours of conversion and preserving benchmark scores such as HumanEval (72% vs 75.6%), MBPP+ (63% vs 57.7%) and CMATH (86.7% vs 88.3%).
- The Triton implementation achieves up to 1.7× higher decoding throughput and supports more concurrent requests before memory exhaustion.

## Context
Diffusion language models aim to accelerate generation by parallelizing denoising steps, yet they still incur quadratic prefix‑attention costs because each step must attend to all prior blocks. Linearizing this attention offers a scalable path to faster inference without retraining the model.

## Implications
This retrofit shows that large pretrained dLLMs can be made significantly faster with minimal effort, enabling real‑time applications and reducing latency for users of open‑source diffusion models, which could lower computational costs in industry deployment.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06628v1)
