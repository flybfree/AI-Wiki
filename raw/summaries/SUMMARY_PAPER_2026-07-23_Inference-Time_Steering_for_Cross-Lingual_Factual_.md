---
title: Inference-Time Steering for Cross-Lingual Factual Consistency in LLMs
url: http://arxiv.org/abs/2607.19243v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_16-15-05Z_Inference_TimeSteeringforCross_LingualFactualConsi.md
generated_at: 2026-07-23 23:26
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates whether cross‑lingual factual inconsistency in large language models can be reduced at inference time. It tests four steering methods on the Gemma 3 12B Instruct model and finds that persona prompting delivers the best balance of accuracy, safety, and generalization.

## Key Takeaways
- Persona prompting is the strongest overall intervention because it forces English‑prompted queries to behave as if asked in German, Spanish or Bulgarian while preserving safety and out‑of‑domain transfer. - Contrastive Activation Addition produces sharp shifts on consistency benchmarks but is sensitive to hyperparameters and can degrade model knowledge. - Direct Preference Optimization yields permanent but limited improvements that are not easily transferred across languages.

## Context
Cross‑lingual performance gaps in LLMs stem from uneven training data distribution, leading to language‑specific answer drift. Mitigating this at inference offers a practical way to align outputs without retraining massive models.

## Implications
Practitioners can adopt lightweight persona prompts to improve factual consistency across languages with minimal resource cost. This approach supports scalable deployment where model updates are costly and safety remains paramount.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19243v1)
