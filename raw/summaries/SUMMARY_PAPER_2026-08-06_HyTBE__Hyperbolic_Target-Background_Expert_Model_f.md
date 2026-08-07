---
title: HyTBE: Hyperbolic Target-Background Expert Model for Cross-Domain Infrared Small Target Detection
url: http://arxiv.org/abs/2608.05771v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-06_09-02-09Z_HyTBE_HyperbolicTarget_BackgroundExpertModelforCro.md
generated_at: 2026-08-06 21:30
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces HyTBE, a Hyperbolic Target-Background Expert model designed to improve infrared small target detection across unseen domains. By addressing the shift in target‑background relations that causes cross‑domain degradation, HyTBE expands observable pattern space and yields stronger generalization than existing baselines on NUAA‑SIRST, NUDT‑SIRST, and IRSTD‑1K.

## Key Takeaways
- The Target-Background Relation Intervention perturbs either targets or backgrounds during training, thereby broadening the range of visible relation patterns while keeping supervision valid.  
- Hyperbolic Relation Modeling maps multi‑scale visual cues into a Poincaré ball, assigning each feature token a hyperbolic distance that encodes its relative proximity to target and background anchors.  
- A hyperbolic‑guided MoE Adapter uses these distances to calibrate features across scales and aggregates expert corrections tailored to the detected relation pattern.

## Context
Infrared small target detection often fails when moving from source to unseen infrared domains because detectors are trained on a narrow set of target‑background relations. Current methods enhance responses but do not model how those relations shift, limiting robust transfer. This work highlights that relational dynamics, rather than just response magnitude, drive cross‑domain performance.

## Implications
HyTBE provides a modular framework for modeling domain‑specific relational patterns in any multi‑modal AI system, offering a path to more reliable generalization without extensive retraining. Practitioners can integrate its hyperbolic MoE adapter into existing detectors to achieve stronger cross‑domain robustness with minimal overhead.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05771v1)
