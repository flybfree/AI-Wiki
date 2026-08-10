---
title: Stoicheia: Character-Level Masked Diffusion for Ancient Greek Textual Restoration, Parsing, and Metrical Scansion
url: http://arxiv.org/abs/2608.07249v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-07_14-07-43Z_Stoicheia_Character_LevelMaskedDiffusionforAncient.md
generated_at: 2026-08-09 22:14
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Stoicheia, a character-level masked diffusion model trained on Ancient Greek to restore unspaced texts, re-segment lines, accentuate diacritics, and punctuate. It achieves state-of-the-art results in reconstruction, parsing, and macronization with reduced error rates compared to previous methods.

## Key Takeaways
- Stoicheia uses a 405M‑parameter model that operates on five independent maskable planes: letters, word boundaries, sentence boundaries, diacritics, capitalization, and punctuation. - The pretraining corpus is 380 million words with revision‑pinned data and releases eleven checkpoints ensuring no overlap with any test passage. - Experiments show a 5.6 CER improvement on inscription reconstruction, 12.9 LAS gain on parsing, and 6.0 balanced accuracy boost on macronization.

## Context
Character‑level diffusion models are emerging as alternatives to token‑based transformers for low‑resource languages and historical texts where fine‑grained control over diacritics matters. This work demonstrates that such approaches can directly address ancient Greek’s unique orthographic constraints without task‑specific retokenization.

## Implications
For scholars of classical literature, Stoicheia offers a tool to recover damaged manuscripts with quantitative error metrics. Practitioners in AI research gain insight into how multi‑plane conditioning can improve model robustness and interpretability for domain‑specific tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07249v1)
