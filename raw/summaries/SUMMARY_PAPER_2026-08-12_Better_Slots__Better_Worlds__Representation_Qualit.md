---
title: Better Slots, Better Worlds: Representation Quality & Robustness in Object-Centric World Models
url: http://arxiv.org/abs/2608.12078v1
type: paper-summary
date: 2026-08-12
source_paper: 2026-08-12_14-02-36Z_BetterSlots_BetterWorlds_RepresentationQuality_Rob.md
generated_at: 2026-08-12 21:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates object-centric world models (OCWMs) for visual model-predictive control, comparing them to scene-centric approaches across representation quality and distribution shift. It finds that higher slot-quality metrics improve planning but plateau, that auxiliary proprioception becomes unnecessary when slots are well-bound, and that OCWM with good slots outperforms end-to-end scene models under unseen shifts while DINO‑based WM remains competitive due to pretrained features.

## Key Takeaways
- Planning success improves with unsupervised slot-quality metrics such as FG‑ARI and mBO, but gains level off once slot quality is already high.
- When object slots are well-bound, the need for auxiliary proprioception inputs and masking inductive bias drops, simplifying the model.
- Under unseen distribution shifts, the OCWM with well‑bound slots shows greater robustness than end‑to‑end scene models, though DINO‑based WM remains a strong competitor.

## Context
Object-centric representations aim to reduce sample complexity by focusing on salient objects rather than full scene pixels. This study contributes empirical evidence that such inductive bias can be effective without relying on costly auxiliary signals or fine‑tuned pretrained encoders.

## Implications
Practitioners can adopt object-centric world models as a more efficient alternative for real‑time control tasks, especially when combined with robust pretrained features. The findings suggest that careful slot binding and leveraging existing feature representations are key to achieving generalization in dynamic environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12078v1)
