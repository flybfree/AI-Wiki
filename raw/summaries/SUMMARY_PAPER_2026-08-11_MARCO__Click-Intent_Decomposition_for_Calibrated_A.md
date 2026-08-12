---
title: MARCO: Click-Intent Decomposition for Calibrated Ads Conversion Prediction
url: http://arxiv.org/abs/2608.10562v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-11_06-49-59Z_MARCO_Click_IntentDecompositionforCalibratedAdsCon.md
generated_at: 2026-08-11 22:22
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MARCO, a framework that decomposes each user click into intent types to improve ad conversion prediction calibration. By training separate CVR heads per intent and composing them at serving time, MARCO corrects the bias of standard CVR models, achieving near‑perfect population calibration, a +2.80% lift in conversions per click, and a cumulative +0.98% improvement in topline metrics.

## Key Takeaways
- Users generate free intent signals through UI interactions that differ by up to fourfold conversion rates across click types.  
- Decomposition yields exact headroom under squared loss and maintains non‑negativity under the deployed loss, never raising population risk.  
- The framework’s gains are finite‑capacity estimation and calibration effects validated both offline and online.

## Context
In AI‑driven ad ranking, calibrated conversion prediction is essential because uncalibrated models can misallocate budget to low‑intent clicks while ignoring high‑potential ones. This paper addresses the gap between aggregate model performance and per‑click utility by leveraging behavioral intent labels as a free signal for more precise risk estimation.

## Implications
For practitioners, MARCO offers a scalable method to refine ad ranking without sacrificing population safety, enabling higher conversion rates at lower cost. The approach also provides a principled credit assignment framework that can be extended to multi‑impression attribution under production constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.10562v1)
