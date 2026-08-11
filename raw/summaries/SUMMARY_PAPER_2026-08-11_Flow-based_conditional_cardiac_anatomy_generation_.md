---
title: Flow-based conditional cardiac anatomy generation for virtual cohorts
url: http://arxiv.org/abs/2608.09460v1
type: paper-summary
date: 2026-08-11
source_paper: 2026-08-10_11-30-02Z_Flow_basedconditionalcardiacanatomygenerationforvi.md
generated_at: 2026-08-11 12:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces CAN‑FLOW, a two‑step conditional normalizing flow framework for generating realistic biventricular cardiac anatomies conditioned on sex, age, and body‑mass‑index metadata. It is trained on 2,208 healthy UK Biobank subjects and outperforms existing cVAEs in reproducing phenotype distributions, subgroup variability, point‑cloud coverage, and high‑dimensional shape variability.

## Key Takeaways
- CAN‑FLOW learns geometry‑only latent representations of cardiac shape momenta using normalizing FLOWS before modeling their sex‑, age‑, and BMI‑dependent distribution with a conditional normalizing flow.
- The framework generates plausible stochastic biventricular anatomies that better reproduce clinical phenotype distributions compared to cVAEs across regularization strengths.
- Results show improved metadata‑dependent trends, subgroup variability, point‑cloud coverage, and high‑dimensional shape variability.

## Context
Cardiac digital twin research seeks virtual cohorts representing population subgroups while preserving realistic anatomical variability. Generative models are essential for creating such cohorts but must balance realism with computational efficiency. CAN‑FLOW advances this by combining geometry learning with conditional normalizing flows to handle multiple patient attributes simultaneously.

## Implications
The framework enables efficient generation of diverse, metadata‑conditioned cardiac anatomies for virtual cohort construction and in silico clinical trials without requiring large labeled datasets. Practitioners can leverage CAN‑FLOW to accelerate research, reduce data acquisition costs, and create more representative study populations.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09460v1)
