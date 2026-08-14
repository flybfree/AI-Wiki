---
title: Dual-Stream Cross-Anchor Correction Grounding Long-Form Captions and the Domain Limits of Object-Level Anchors
url: http://arxiv.org/abs/2608.12746v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-13_02-52-58Z_Dual_StreamCross_AnchorCorrectionGroundingLong_For.md
generated_at: 2026-08-13 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Dual-Stream Cross-Anchor Correction (DSCC) to reduce object hallucination in multimodal language models by embedding visual anchors directly into the model's training pipeline. Experiments show that DSCC achieves higher precision on long captions than vanilla supervised fine‑tuning, reaching 88.19 % precision per object mention at a modest increase in caption length.

## Key Takeaways
- The perception stream aligns object‑level hidden states with frozen text anchors using contrastive learning, but alone it degrades precision because the model over‑fits to visual cues without grounding them in language.
- Stacking the cognition stream’s cross‑attention on top of the perception stream reverses this degradation and restores high precision, demonstrating a synergistic effect between streams.
- The two‑stage curriculum gate ensures that evidence retrieval is a structural constraint at each autoregressive step, enabling long‑form captions with low hallucination rates.

## Context
Object hallucination remains a persistent challenge for multimodal large language models where visual evidence does not reliably guide text generation. Prior solutions are either post‑hoc or limited to short captions, highlighting the need for training‑time interventions that integrate perception and cognition streams.

## Implications
For practitioners, DSCC offers a framework to embed domain‑specific anchors during fine‑tuning, improving reliability in long‑form captioning tasks. However, its performance is sensitive to the semantic domain of the anchors, limiting generalisation across unrelated visual concepts such as charts or optical illusions.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12746v1)
