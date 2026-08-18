---
title: The Distributional View of Knowledge Distillation
published: 2026-08-15T13:03:31Z
authors: Gordei Verbii, Juho Lee
url: http://arxiv.org/abs/2608.15215v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Distributional View of Knowledge Distillation

## Abstract
Token-level knowledge distillation (KD) matches two conditional distributions per position, yet the standard objectives compare them pointwise: a Kullback-Leibler gradient is blind to which wrong token receives probability mass. We develop a distributional view in which the teacher is represented not by a single softened output but by a family of multi-temperature views - marginals of the annealing path of its logits - and the student is trained against a geometry-aware aggregate of these views under an embedding-based ground cost. We formalize the resulting design space (mixtures, log-linear pooling, entropic Wasserstein barycenters, and a debiased Sinkhorn-divergence flagship in hub and path forms), prove an exact collapse result showing log-linear pooling of tempered views is equivalent to a single temperature, and give a multi-marginal Schrodinger-bridge reading that yields falsifiable predictions. On instruction-tuned Pythia pairs, experiments yield three empirical laws: (i) dispersion law - the benefit of multi-temperature aggregation grows monotonically with the effective temperature dispersion of the views, not with their number; (ii) dispersed views unlock the aggregation operator - the barycenter separates from the arithmetic mixture exactly when transport-based aggregation starts to beat averaging; and (iii) two-regime picture governed by the ceiling gap $Γ=\mathrm{PPL}_{\mathrm{SFT}}-\mathrm{PPL}_{T}$: when the fine-tuned teacher barely beats a supervised student the gentle transport objective is the best KD loss but no KD beats supervised fine-tuning, whereas at a real ceiling the ranking inverts - and the sign of the fidelity-generalization correlation flips. We argue that "which distillation loss is the best" is not a fixed property of the loss but a function of $Γ$.

## Metadata
- **Published**: 2026-08-15T13:03:31Z
- **Authors**: Gordei Verbii, Juho Lee
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15215v1)