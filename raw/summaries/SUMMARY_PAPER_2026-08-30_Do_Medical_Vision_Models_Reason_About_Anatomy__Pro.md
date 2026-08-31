---
title: Do Medical Vision Models Reason About Anatomy? Probing the Spatial Inductive Biases of Learned Visual Representations
url: http://arxiv.org/abs/2608.28092v1
type: paper-summary
date: 2026-08-30
source_paper: 2026-08-28_08-59-27Z_DoMedicalVisionModelsReasonAboutAnatomy_Probingthe.md
generated_at: 2026-08-30 20:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper investigates whether medical vision encoders can perform genuine spatial reasoning about anatomy in abdominal CT scans. By constructing SPAR-Bench, a suite of probes that test coordinate localization, relational inference, and spatial queries across multiple organ configurations, the authors find that most tasks remain at chance even with fine‑tuning or architectural changes.

## Key Takeaways
- Probes that ask for comparisons within a single slice achieve no improvement over random guessing, suggesting encoders lack true intra‑slice reasoning.  
- Zero‑shot transfer of domain‑specific accuracy collapses to chance, indicating that performance relies on memorized anatomical maps rather than computation from the image.  
- Using only pooled features instead of full token sets boosts relational recovery dramatically, revealing that pooling underestimates what the representation actually holds.

## Context
Medical vision models are increasingly integrated into diagnostic pipelines, yet their interpretability remains opaque. Understanding whether these encoders capture spatial relationships or merely memorized structures is crucial for trustworthy AI deployment in healthcare.

## Implications
If spatial reasoning is limited to recall of canonical anatomy, clinicians may rely on models that cannot adapt to individual patient variations, undermining personalized medicine. The findings push the field toward architectures and evaluation methods that explicitly test relational computation rather than static mapping.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28092v1)
