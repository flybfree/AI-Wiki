---
title: Can Language Models Imagine Without Seeing? Ekphrasis: Measuring Visual Creative Ideation in Text-Only LLMs
url: http://arxiv.org/abs/2608.06967v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_08-44-00Z_CanLanguageModelsImagineWithoutSeeing_Ekphrasis_Me.md
generated_at: 2026-08-09 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Visual Creative Ideation (VCI) and the Ekphrasis benchmark to evaluate whether text‑only language models can generate useful, expressive, and novel visual plans before image generation. Across 14 language models, VCI separates usefulness, expressiveness, and novelty rather than collapsing into fluency, showing that strong models can achieve similar overall scores through different profiles while still producing visually clichéd plans.

## Key Takeaways
- Strong models separate usefulness, expressiveness, and novelty rather than reducing to mere fluency.  
- Useful textual visual plans can remain visually clichéd despite high VCI scores.  
- The ordering of text‑level VCI survives faithful rendering and blind image‑level preference judgment.

## Context
Evaluating visual ideation in language models remains a challenge because current metrics focus on prose quality rather than the ability to conceive renderable scenes. This work provides a cross‑modal benchmark that isolates textual planning from downstream generation, aligning with broader AI research toward robust multimodal alignment and understanding of imagination.

## Implications
Providing a clear metric for visual creative ideation helps researchers design better prompts and training objectives for text‑only models. Practitioners can use VCI to assess the suitability of generated visual plans without relying solely on image fidelity or subjective fluency judgments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06967v1)
