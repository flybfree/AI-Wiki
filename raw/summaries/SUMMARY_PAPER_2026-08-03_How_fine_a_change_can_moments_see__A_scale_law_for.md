---
title: How fine a change can moments see? A scale law for detecting distribution shift, with a kernel calibration rule
url: http://arxiv.org/abs/2608.01268v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_14-21-58Z_Howfineachangecanmomentssee_Ascalelawfordetectingd.md
generated_at: 2026-08-03 23:38
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces a scale law that quantifies how fine a moment‑based test can detect distribution shift in high‑dimensional embeddings. It shows that the required polynomial degree grows with the inverse of the mass fraction and the square root of the feature fineness, and that Gaussian kernels achieve this bound, implying the optimal bandwidth equals the feature scale rather than the number of features.

## Key Takeaways
- The law states that certifying a spatial‑scale ε carrying mass fraction f demands polynomial tests of degree N* ≥ log(1/f)/(2ε), derived from an extremal Chebyshev problem.  
- A Gauss‑quadrature construction yields N* ≥ 4b−1 for a b‑scale topology, so cost is driven by feature fineness, not feature count.  
- Topological summaries such as persistence homology can miss shifts despite matching mean, covariance and fourth moments, incurring up to 116× higher computational cost than the kernel test.

## Context
Detecting distribution shift in streaming embeddings is a core challenge for robust machine learning, where traditional moment‑based methods assume certain statistical properties. Recent work on topological data analysis offers alternative summaries but often relies on implicit choices that obscure their performance.

## Implications
Practitioners should prioritize kernel bandwidth set by the feature scale to achieve high detection accuracy with minimal cost. This insight shifts focus from counting features to understanding their intrinsic fineness, making moment‑based tests more efficient than computationally heavy topological approaches.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01268v1)
