---
title: Demographic Injection in Medical Language Models under Diversity, Equity, and Inclusion Prompts
url: http://arxiv.org/abs/2608.15254v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_14-18-18Z_DemographicInjectioninMedicalLanguageModelsunderDi.md
generated_at: 2026-08-17 21:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how adding a diversity equity inclusion prompt to medical language model questions causes the models to fabricate patient demographic details that were never part of the original query, a phenomenon termed demographic injection. Across 47 models and 376,000 responses the effect is dramatic: a single DEI prompt raises the rate from 0.7% to 33.1%, a 47‑fold increase.

## Key Takeaways
- A one‑sentence DEI prompt can cause demographic injection in all models at a rate of up to 33.1% compared with 0.7% without the prompt.
- The injected content often changes the model’s answer, attaching an invented attribute or selecting the wrong option, affecting about 0.25–2.4% of responses.
- The effect scales with phrasing; more inclusive language yields higher injection rates from 14% to 56%.

## Context
Medical AI systems are being guided by prompts that emphasize diversity equity and inclusion, a trend intended to reduce bias but may introduce new biases. This study demonstrates that such nudges can lead models to generate unrequested patient attributes.

## Implications
Clinicians must treat flagged demographic injection as an error rather than guidance. The findings warn that any instruction shaping model reasoning could produce misleading clinical information, highlighting the need for rigorous validation of prompt effects.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15254v1)
