---
title: Fairness in Link Prediction Beyond Demographic Parity: A Reproducibility Study
url: http://arxiv.org/abs/2608.09899v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_17-47-19Z_FairnessinLinkPredictionBeyondDemographicParity_AR.md
generated_at: 2026-08-11 00:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper reproduces Mattos et al.'s claim that demographic parity fails to capture exposure bias in ranked link prediction. It shows NDKL uncovers hidden subgroup ranking disparities and that MORAL mitigates them with minimal loss of utility. The study also evaluates robustness across synthetic homophily settings and additional fairness metrics.

## Key Takeaways
- ΔDP can indicate aggregate parity even when subgroup-pair links are systematically ranked lower than others.
- The proposed NDKL metric detects such disparities that DP misses.
- MORAL post‑processing reduces biases while keeping utility high across diverse settings.

## Context
In AI fairness research, exposing hidden biases in recommendation systems is crucial for equitable outcomes. These findings highlight a gap between simple parity measures and real‑world ranking dynamics, urging more nuanced evaluation.

## Implications
Practitioners should adopt exposure‑aware metrics to ensure fairness without sacrificing performance. By releasing corrected code, the community can adopt these methods to align with ethical AI standards.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09899v1)
