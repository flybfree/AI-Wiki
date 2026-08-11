---
title: Failure-Mechanism Transferability of Cumulative-Damage Features for Health State Estimation of SiC Power Modules
published: 2026-08-08T23:28:57Z
authors: Mattia Scarpa, Evgeny Kusmenko, Francesco Toso, Mattia Bruschetta, Ruggero Carli, Simon Achatz
url: http://arxiv.org/abs/2608.08365v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Failure-Mechanism Transferability of Cumulative-Damage Features for Health State Estimation of SiC Power Modules

## Abstract
Data-driven health-state estimators for SiC (Silica-Carbide) power modules typically report their performance on a single accelerated-aging campaign, and how that performance transfers to a different failure mechanism is rarely tested. We benchmark five reference methods from the prognostics and condition-monitoring literature against a physics-informed NODE (Neural Ordinary Differential Equation) on two SiC power-cycling campaigns driven by structurally different failure mechanisms, solder-layer fatigue and wire-bond lift-off, under a per-module $k$-fold protocol. The NODE is evaluated under two input regimes that share the rest of the pipeline: the baseline electrical precursors and a set of cumulative thermoelectric features. Every reference method degrades on the wire-bond campaign, with average errors growing and precision decreasing with respect to their performance on the soldered campaign. The NODE fed with the cumulative features keeps its soldered-campaign metrics on both mechanisms, with differences inside the fold-to-fold variance, while the same architecture fed with the baseline precursors falls back to the reference-method cluster. The input representation contributes at least as much as the architecture to failure-mechanism transferability of a health-state estimator.

## Metadata
- **Published**: 2026-08-08T23:28:57Z
- **Authors**: Mattia Scarpa, Evgeny Kusmenko, Francesco Toso, Mattia Bruschetta, Ruggero Carli, Simon Achatz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08365v1)