---
title: The Label Defines the Timescale: Trait-State Limits of Temporal-Aggregate Learning
published: 2026-08-03T01:44:01Z
authors: Xizhe Zhang
url: http://arxiv.org/abs/2608.01587v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Label Defines the Timescale: Trait-State Limits of Temporal-Aggregate Learning

## Abstract
Machine-learning benchmarks often pair a label that aggregates a long temporal horizon with input observed through one or a few short windows. Their apparent performance ceiling may therefore be an acquisition-protocol ceiling rather than a model-capacity ceiling. We study labels of the form $Θ_{g,T}=T^{-1}\int_0^T g\{Z(t)\}\,\mathrm{d}t$ when the latent Gaussian process contains both a stable individual trait and a correlated within-individual state. An exact protocol-conditioned Bayes-risk identity provides a common tool. First, we decompose label variance into an $O(1)$ trait component and an $O(T^{-1})$ state component, explaining why a snapshot can retain cross-sectional predictability while poorly tracking within-person change. Second, we derive task-dependent effective temporal spans: mean labels depend on the ordinary correlation time, whereas occupation-time labels depend on an entire spectrum of higher-order correlation times. Third, state-driven occupation-label variance is maximal when the stable trait lies at the threshold; window efficiency decays much more slowly away from that boundary. Under an equal segment budget, exact risks and Monte Carlo experiments show that repeated segments at one time rapidly saturate, whereas temporally dispersed observations continue to increase state explainability. The trait ceiling uses quantities available from ordinary test-retest data; only the state ceiling requires short-lag temporal calibration. The results distinguish architectural limits from protocol limits and show that the label, rather than duration or segment count alone, defines the relevant timescale.

## Metadata
- **Published**: 2026-08-03T01:44:01Z
- **Authors**: Xizhe Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01587v1)