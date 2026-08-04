---
title: Rewriting or Reweighting? A Geometric Account in Language Models
url: http://arxiv.org/abs/2608.01835v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_07-46-28Z_RewritingorReweighting_AGeometricAccountinLanguage.md
generated_at: 2026-08-03 23:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates how post‑training changes the geometric structure of language‑model behavior by analyzing two distinct failure modes—repetition and sycophancy. Using a behavioral manifold analysis that projects activation states and functional flow into low‑dimensional charts, the authors show that supervised fine‑tuning (SFT) reshapes this geometry while reward optimization mainly reweights it.

## Key Takeaways
- The behavior manifold reveals that SFT creates a new architectural pattern rather than merely adjusting probabilities.  
- Reward optimization preserves the core subspace but changes its weight distribution, indicating a reweighting effect.  
- The two charts—activation‑space and contribution‑space—differ in their sensitivity to model architecture, highlighting a shared yet family‑specific geometry.

## Context
Understanding whether post‑training modifies or refines existing mechanisms is crucial for reliable model deployment. Current methods often treat behavior changes as simple probability adjustments without probing the underlying representation space.

## Implications
Practitioners can leverage this geometric insight to design fine‑tuning pipelines that either rewrite or reweight behavior, reducing unintended side effects and improving alignment stability across different architectures.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01835v1)
