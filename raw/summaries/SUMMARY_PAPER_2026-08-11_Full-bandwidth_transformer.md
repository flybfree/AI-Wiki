---
title: Full-bandwidth transformer
url: http://arxiv.org/abs/2608.08888v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-09_19-59-45Z_Full_bandwidthtransformer.md
generated_at: 2026-08-11 12:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a full-bandwidth transformer that adds latent feedback to the standard autoregressive architecture, allowing non‑verbalized computation from earlier layers to re-enter the decoding stack without altering the KV cache. Experiments show that this modest change improves validation loss and several downstream tasks while keeping per‑token overhead negligible.

## Key Takeaways
- Latent feedback fuses the previous top‑layer hidden state with the sampled token embedding via a gated linear unit, feeding it back as the next input to preserve depth budget.
- The method uses a scheduled multi‑pass objective that introduces latent feedback late in pretraining and mixes a small fraction of deeper passes for stability during training.
- Full‑bandwidth transformers achieve comparable or better performance on 5‑shot language modeling, math generation, coding generation, and instruction tuning with roughly 1.5× more tokens.

## Context
Autoregressive transformers dominate modern language models but suffer from limited vertical communication between decoding steps, which restricts the model’s ability to reuse earlier computations. This work demonstrates that a simple architectural tweak can unlock additional capacity without sacrificing parallel training efficiency.

## Implications
For practitioners, full‑bandwidth transformers offer a low‑cost way to boost model performance on complex tasks such as reasoning and code generation. The approach could inspire future designs that balance depth reuse with computational cost in large language models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08888v1)
