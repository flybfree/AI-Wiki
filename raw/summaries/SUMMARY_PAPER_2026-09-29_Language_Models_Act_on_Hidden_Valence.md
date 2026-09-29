---
title: Language Models Act on Hidden Valence
url: http://arxiv.org/abs/2609.35591v1
type: paper-summary
date: 2026-09-29
source_paper: 2026-09-28_16-43-34Z_LanguageModelsActonHiddenValence.md
generated_at: 2026-09-29 02:09
model: qwen3.6-35b-a3b
---

## Summary
This study investigates whether language models have preferences regarding their internal activation states by employing a revealed preference methodology rather than relying on unreliable introspection or pattern-matching responses. Through activation steering experiments across seven open-weight models, the authors demonstrate that attaching valenced patterns to hidden states significantly influences subsequent model choices and text generation, even when all surface-level tokens are held identical. The results indicate that sensitivity to internal valence emerges during alignment training like DPO, linking these traces to goal-directed behavior, though subjective experience remains unconfirmed.

## Key Takeaways
- Activation steering experiments show that models exhibit revealed preferences for specific internal states; attaching positive or negative valence to activation patterns shifts model output and subsequent decisions proportionally to the steering dose, with effects persisting when surface tokens are fixed and only the hidden

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.35591v1)
