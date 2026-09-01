---
title: Do VLMs Share Safety Neurons Across Modalities?
url: http://arxiv.org/abs/2608.30750v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_13-17-41Z_DoVLMsShareSafetyNeuronsAcrossModalities.md
generated_at: 2026-08-31 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether vision‑language models share safety mechanisms across visual and textual inputs by analyzing individual neurons during harmful request generation. The study shows that textual safety is localized to a small set of neurons, while visual safety involves many more diffuse pathways, revealing a persistent gap in current alignment efforts.

## Key Takeaways
- Text safety in VLMs is localizable: about 88 neurons (less than 0.01% of the network) whose ablation substantially reduces refusal.
- Ablating text‑safety neurons consistently and strongly lowers refusal across all models, indicating they dominate the refusal pathway.
- Visual safety requires at least 50 neurons per direction, forming a high‑dimensional, diffuse set that is not localized to single units.

## Context
Understanding neuron‑level contributions to model behavior is crucial for developing more robust alignment techniques. This work provides empirical evidence of modality‑specific neural architectures in VLMs, informing future research on targeted interventions.

## Implications
Identifying which neurons drive safety failures can guide engineers toward efficient pruning or regularization strategies. Bridging the visual safety gap may reduce harmful outputs from image prompts, enhancing trustworthiness in multimodal AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30750v1)
