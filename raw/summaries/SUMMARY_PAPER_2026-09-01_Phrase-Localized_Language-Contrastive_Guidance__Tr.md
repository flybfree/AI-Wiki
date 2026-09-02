---
title: Phrase-Localized Language-Contrastive Guidance: Training-Free Localized Accent Control for Code-Switching Text-to-Speech
url: http://arxiv.org/abs/2609.01016v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_10-07-00Z_Phrase_LocalizedLanguage_ContrastiveGuidance_Train.md
generated_at: 2026-09-01 22:23
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Phrase-Localized Language-Contrastive Guidance (LCG), a training-free method that restores native accents to code-switched phrases in cross-lingual text-to-speech. By applying separate language guidance per region and using self‑attention probing to locate phrase boundaries, LCG eliminates accent leakage while preserving speaker identity.

## Key Takeaways
- LCG replaces global language guidance with region‑specific guidance, allowing each segment to be voiced with its own native accent.
- The self‑attention probing technique automatically detects phrase boundaries without requiring external alignment data.
- Experiments across multiple language pairs show that the code‑switched phrase gains higher nativeness and accent leakage is suppressed while overall speaker identity remains intact.

## Context
Current text‑to-speech systems often apply a single language model to an entire utterance, leading to mismatched accents when foreign words appear. This limitation hampers naturalness in multilingual applications where code‑switching is common.

## Implications
LCG provides a practical solution that can be integrated into existing TTS pipelines without retraining models or building auxiliary components. Practitioners can achieve more authentic cross‑lingual speech, improving user experience and expanding the reach of AI‑generated audio in multilingual contexts.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01016v1)
