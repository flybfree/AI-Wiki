---
title: RecurrentGPT: Expressive Depth through Recurrent Modulation in Transformers
published: 2026-08-15T06:22:00Z
authors: Amr Hegazy, Amr Alanwar, Mostafa Elhoushi
url: http://arxiv.org/abs/2608.15062v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RecurrentGPT: Expressive Depth through Recurrent Modulation in Transformers

## Abstract
Scaling transformer language models creates an inherent tension between expressivity and memory efficiency. While unique weights across layers preserve functional specialization---from input-grounding to abstract refinement---they incur a substantial memory footprint. Conversely, standard depth-sharing enforces uniform transformations that collapse representational diversity and degrade modeling quality. We introduce RecurrentGPT, a recurrent depth transformer where fixed-depth prelude and coda blocks bracket a single shared core iterated R times. Inspired by gated recurrent neural networks, we employ a lightweight projection and an elementwise update gate---conditioned on the hidden state, the fixed prelude output, and noise resampled at every step---to modulate the recurrent update. This allows the model to specialize the input to the same few layers across recurrences, rather than requiring many unique layers to achieve functional diversity. Under an isoFLOPS constraint, a 3-layer RecurrentGPT matches the accuracy of a 12-layer GPT-2 Small baseline with similar training and inference FLOPs, and leads MoR and heavy-tail depth sampling in all nine scale-by-budget cells; at medium and large scale it approaches dense quality at the standard token budget and overtakes it at medium scale once that budget is doubled. Under an isoPARAMS constraint, deeper recurrence achieves a 2.76 validation loss versus 2.84 for a non-recurrent counterpart at matched parameter and data budget. Our results demonstrate that adaptive depth reuse is a principled strategy for trading parameters for quality: at large scale, 63% fewer parameters and 59% less peak decoding memory for a 10% increase in compiled generation latency.

## Metadata
- **Published**: 2026-08-15T06:22:00Z
- **Authors**: Amr Hegazy, Amr Alanwar, Mostafa Elhoushi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15062v1)