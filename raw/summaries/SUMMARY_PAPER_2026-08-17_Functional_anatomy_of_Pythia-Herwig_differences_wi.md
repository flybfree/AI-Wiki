---
title: Functional anatomy of Pythia-Herwig differences with Kolmogorov-Arnold networks
url: http://arxiv.org/abs/2608.15952v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-16_22-53-06Z_FunctionalanatomyofPythia_HerwigdifferenceswithKol.md
generated_at: 2026-08-17 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates the functional differences between two event generators Pythia and Herwig by analyzing how their log density ratios vary across shower, hadronization, and full‑generator stages. Using an additive Kolmogorov–Arnold network on eight observable jet responses it decomposes these differences into explicit one‑dimensional components that can be isolated and transported between stages.

## Key Takeaways
- The Pythia‑Herwig discrepancy is primarily driven by multiplicity at the shower level, indicating a strong reweighting effect there. 
- After hadronization the difference shifts toward jet mass and shape, showing that later observable structures become important but may lack sufficient statistical support. 
- Transporting individual shower‑level functional components downstream shows that multiplicity information retains its reweighting power while shape responses do not.

## Context
This work contributes to AI research by applying a KAN framework to decompose high‑dimensional classifier outputs into interpretable, stage‑specific features. It demonstrates how deep learning can be used to uncover hidden dependencies in complex simulation pipelines, offering a method for functional model comparison beyond simple global scores.

## Implications
For particle physics and machine‑learning practitioners this approach provides a systematic way to diagnose generator mismatches, guiding improvements in event generation or classifier design. The methodology could also inform other domains where high‑dimensional data are decomposed into interpretable stages, enhancing transparency and trust in AI models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15952v1)
