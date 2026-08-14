---
title: Excess Separability: Nuisance-Controlled Residual-Stream Probing for Benchmark Contamination Detection
url: http://arxiv.org/abs/2608.12652v1
type: paper-summary
date: 2026-08-13
source_paper: 2026-08-12_23-27-20Z_ExcessSeparability_Nuisance_ControlledResidual_Str.md
generated_at: 2026-08-13 21:28
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a new method for detecting benchmark contamination in AI models by measuring the excess separability of internal activations with a linear probe, rather than relying on external artifacts like n‑grams or canary strings. Experiments show that this approach can reliably identify contamination across four Pile arms while rejecting false positives even under strong null hypotheses.

## Key Takeaways
- The natural way to diagnose contamination—using n‑gram overlap or likelihood‑based membership inference—requires unavailable resources such as the training corpus or foresight at release, whereas probing internal activations needs only a test set.  
- A zero‑sum contrast on probe accuracy, centered on a level‑matched placebo baseline and tested against a label‑permutation null, yields false positive rates that range from 0.03 to 0.99 under true nulls, highlighting the sensitivity of the method to analyst control set size.  
- Item bootstrapping can reject up to 0.09 when a permutation null that refits the probe holds only 0.02, demonstrating that fixed‑probe comparisons are prone to inflated errors.

## Context
Benchmark contamination detection is crucial for ensuring fairness and reproducibility in large language models, yet current methods often depend on external artifacts or require knowledge of the training data that may never be released. This work shifts focus inward, using only model internals, which aligns with privacy‑preserving auditing practices and reduces reliance on dataset provenance.

## Implications
For practitioners, this protocol offers a transparent, reproducible way to flag suspicious test splits without exposing proprietary data, supporting more trustworthy model evaluation pipelines. The field can adopt such internal probing as a standard safeguard against hidden contamination, fostering confidence in AI system integrity.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.12652v1)
