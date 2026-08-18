---
title: Bias-Corrected Ceilings of Emotion Predictability from Human Label Variation Based on Instance-Level Fano Bounds
url: http://arxiv.org/abs/2608.15619v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_08-34-46Z_Bias_CorrectedCeilingsofEmotionPredictabilityfromH.md
generated_at: 2026-08-17 21:32
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Bias-corrected Affective Ceiling Estimation (BACE) as a framework for quantifying the limits of emotion prediction accuracy on GoEmotions, emphasizing that saturation cannot be claimed without accounting for annotation bias and estimator variability. It shows that unconstrained point estimates range from 0.38 to 1.03, indicating that only certain claims survive rigorous analysis. The main finding is that about 33% of a classifier’s error on GoEmotions is irreducible across affective categories.

## Key Takeaways
- Unconstrained point estimates for reachability vary widely between 0.38 and 1.03, showing that saturation cannot be decided by any single estimator.
- The only assertion passing the claim gate is that roughly one-third of a representative classifier’s error on GoEmotions is irreducible, consistent across offensiveness and irony tasks.
- BACE separates reducible from irreducible error using an anchored Dirichlet-mixture empirical Bayes estimator, plug-in, NSB bracketing, annotator split, noise deconvolution, and a fixed claim gate to avoid circularity.

## Context
Current emotion recognition benchmarks report high accuracy but rarely discuss whether these results reflect true capability or are limited by finite annotation sets. This work addresses the need for principled ceiling estimation in affective computing, aligning with broader AI efforts to separate model performance from data artifacts.

## Implications
For practitioners, BACE provides a transparent method to evaluate how confidently saturation can be claimed, guiding resource allocation and model development. For industry, it encourages rigorous reporting of error sources rather than just accuracy scores, fostering trust in affective AI deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15619v1)
