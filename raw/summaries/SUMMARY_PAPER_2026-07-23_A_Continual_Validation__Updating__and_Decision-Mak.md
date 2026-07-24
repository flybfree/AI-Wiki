---
title: A Continual Validation, Updating, and Decision-Making Framework for Self-Adaptive Digital Twins via Robust Model Predictive Control: A Case Study in Additive Manufacturing
url: http://arxiv.org/abs/2607.18164v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-20_17-07-41Z_AContinualValidation_Updating_andDecision_MakingFr.md
generated_at: 2026-07-23 23:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a continual validation, updating, and decision‑making framework for self‑adaptive digital twins that combats concept drift in neural‑network surrogate models. By combining a Fisher score drift detector, low‑rank adaptation (LoRA) updates, and an online Mann–Whitney U test, the system detects distributional shifts early, fine‑tunes fewer than 1 % of parameters, and statistically confirms improved predictive performance before deployment.

## Key Takeaways
- The framework monitors surrogate‑model confidence using Fisher score vectors to trigger timely model updates.  
- LoRA enables parameter‑efficient continual learning, limiting the number of updated weights to less than one percent.  
- Online statistical validation with a Mann–Whitney U test certifies that each update genuinely improves prediction accuracy and uncertainty quantification.

## Context
Digital twins rely on surrogate models that must remain accurate as operating conditions change, yet existing adaptive methods lack rigorous detection and certification mechanisms. This work addresses the gap by providing a statistically sound pipeline for continual learning in high‑uncertainty environments such as stochastic linear systems and additive manufacturing processes.

## Implications
For practitioners, this approach offers a reliable way to sustain trustworthy neural‑network digital twins throughout their operational lifespan without costly retraining cycles. In industry, it enables real‑time adaptation of manufacturing models, reducing downtime and improving product quality while maintaining uncertainty estimates.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.18164v1)
