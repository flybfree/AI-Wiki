---
title: DualAnchor: Preserving Language Priors and Improving Lexical Fidelity in Gloss-Free Sign Language Translation
url: http://arxiv.org/abs/2607.27614v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_03-02-13Z_DualAnchor_PreservingLanguagePriorsandImprovingLex.md
generated_at: 2026-07-30 21:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces DualAnchor, a framework for gloss‑free sign language translation that combats language‑prior degradation and lexical fidelity gaps. By coupling token‑level prior anchoring with optimal transport alignment, the model generates fluent and visually faithful translations on benchmark datasets PHOENIX‑2014T and CSL‑Daily.

## Key Takeaways
- Token‑Level Prior Anchoring (TPA) forces the decoder to follow the frozen LLM’s next‑token distribution at each step, preserving language fluency.
- Optimal Transport Alignment (OTA) uses entropy‑regularized partial optimal transport with Sinkhorn optimization to create a soft matching between visual tokens and text tokens, reducing lexical errors.
- The two anchors are complementary: TPA boosts overall fluency while OTA sharpens fine‑grained word accuracy.

## Context
Sign language translation remains limited by reliance on LLM backbones that ignore linguistic priors. Existing alignment strategies operate at sentence level, failing to capture subtle lexical details. This work bridges the gap between visual perception and textual generation in a unified manner.

## Implications
The approach can be applied to any multimodal translation task where fine‑grained fidelity matters. Practitioners may adopt DualAnchor’s anchor design to improve model outputs without retraining large language models, offering a practical boost for assistive technologies.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27614v1)
