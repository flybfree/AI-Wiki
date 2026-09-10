---
title: How Fragile Is Safety Alignment at Frontier Scale? A Single-Direction Attack on a 320B MoE
url: http://arxiv.org/abs/2609.09793v1
type: paper-summary
date: 2026-09-09
source_paper: 2026-09-09_06-48-08Z_HowFragileIsSafetyAlignmentatFrontierScale_ASingle.md
generated_at: 2026-09-09 20:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates the resilience of safety alignment in large mixture-of-experts models, showing that a simple directional ablation can still reduce refusal rates but not where expected. It demonstrates that removing specific modules reduces refusal by up to 78% while leaving overall capability unchanged, revealing hidden fragility.

## Key Takeaways
- The attack works on GLM‑5.3‑Flash, a 320B MoE with quantized weights and residual streams split across experts, yet it still lowers refusal rates.
- Editing only the attention writer reduces refusal by 0.039, while dense expert writers reduce it by 0.016, showing that many of the effect is in the routed‑expert path.
- The full reduction (0.776) requires simultaneous edits to all three components, indicating that most safety impact resides only under joint intervention.

## Context
Frontier MoE models compress weights and split residual streams across experts, making traditional white‑box attacks harder to apply. This study shows that even with such complexity, simple directional manipulations can still degrade alignment without retraining.

## Implications
For practitioners, the results warn that safety guarantees may be fragile in large compressed architectures. Designing robust defenses must consider joint module edits rather than single‑component fixes.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.09793v1)
