---
title: Contrastive Concept Importance: Explaining Pairwise Class Decisions Through Automatically Extracted Concept Representations
url: http://arxiv.org/abs/2607.27904v1
type: paper-summary
date: 2026-07-30
source_paper: 2026-07-30_09-19-21Z_ContrastiveConceptImportance_ExplainingPairwiseCla.md
generated_at: 2026-07-30 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces contrastive concept importance (CCI), a method that evaluates how concepts influence the logit margin between a target class and its foil class rather than just the absolute contribution to a single class. By decomposing the signed scores into target‑logit and foil‑logit effects, CCI reveals whether concepts are globally important or specifically affect class‑pair distinctions. Experiments on ImageNet class pairs using CRAFT concept bases demonstrate that CCI uncovers class‑pair specific behavior not captured by ordinary concept importance.

## Key Takeaways
- CCI attributes the logit margin between a target and foil class to automatically extracted visual concepts, providing signed scores that indicate support for one class over the other.  
- The method decomposes these scores into separate target‑logit and foil‑logit components, allowing analysis of whether concept effects are shared or one‑sided.  
- Highly contrastive concepts can be compared to semantic superclass structure to determine if they drive fine‑grained distinctions rather than broad category evidence.

## Context
Explainability in deep learning often relies on feature attribution that focuses on a single class, limiting insight into model behavior during misclassifications or low‑margin predictions. Contrastive analysis is needed to understand why the model chooses one class over another, especially when class confusion occurs. This work advances explainability by shifting attention from absolute importance to relative, pairwise significance.

## Implications
Practitioners can use CCI to diagnose ambiguous predictions and improve model robustness in safety‑critical applications such as medical imaging or autonomous driving where correct class selection is crucial. The technique also offers a principled way to align model explanations with human semantic hierarchies, fostering trust and facilitating targeted retraining.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.27904v1)
