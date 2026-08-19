---
title: Recirculation
url: http://arxiv.org/abs/2608.17981v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_16-30-21Z_Recirculation.md
generated_at: 2026-08-18 21:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces recirculation, an inference‑time architectural enhancement that reduces perplexity and improves accuracy on generation and reasoning tasks with essentially no added latency during generation. It adds a form of recurrence to feedforward transformers, allowing the model to act as a dynamical system and track belief states without retraining.

## Key Takeaways
- Recurrence is introduced for state tracking while keeping generation latency unchanged.
- The technique differs from chain‑of‑thought and depth‑recurrence methods, requiring only light hyperparameter tuning with original weights frozen.
- Adaptive recirculation achieves a 23 % reduction in perplexity on Gemma3 datasets, a 21 % increase in GSM8k accuracy, and reliable gains elsewhere.

## Context
This work tackles the limitation that feedforward transformers cannot maintain unbounded state updates, a bottleneck for reasoning tasks. By embedding recurrence within inference, it offers a lightweight upgrade to existing models without full retraining.

## Implications
The approach shows architectural improvements can be guided by model behavior rather than arbitrary design choices, opening pathways for automated model evolution. Practitioners can apply recirculation to off‑the‑shelf foundation models to boost performance with minimal cost.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17981v1)
