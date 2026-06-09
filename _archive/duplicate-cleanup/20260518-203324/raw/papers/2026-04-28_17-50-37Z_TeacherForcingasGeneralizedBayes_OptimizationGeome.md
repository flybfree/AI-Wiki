---
title: Teacher Forcing as Generalized Bayes: Optimization Geometry Mismatch in Switching Surrogates for Chaotic Dynamics
published: 2026-04-28T17:50:37Z
authors: Andre Herz, Daniel Durstewitz, Georgia Koppe
url: http://arxiv.org/abs/2604.25904v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Teacher Forcing as Generalized Bayes: Optimization Geometry Mismatch in Switching Surrogates for Chaotic Dynamics

## Abstract
Identity teacher forcing (ITF) enables stable training of deterministic recurrent surrogates for chaotic dynamical systems and has been highly effective for dynamical systems reconstruction (DSR) with recurrent neural networks (RNNs), including interpretable almost-linear RNNs (AL-RNNs). However, as an intervention-based prediction loss (and thus a generalized Bayes update), teacher forcing need not match the free-running model's marginal likelihood geometry. We compare the objective-induced curvatures of ITF and marginal likelihood in a probabilistic switching augmentation of AL-RNNs, estimating ambiguity-aware observed information via Louis' identity. In the switching setting studied here, conditioning on a single forced regime path (as ITF does) inflates curvature, while marginal likelihood curvature is reduced by a missing-information correction when multiple switching explanations remain plausible. In Lorenz-63 experiments, windowed evidence fine-tuning improves held-out evidence but can degrade dynamical quantities of interest (QoIs) relative to ITF-pretrained models.

## Metadata
- **Published**: 2026-04-28T17:50:37Z
- **Authors**: Andre Herz, Daniel Durstewitz, Georgia Koppe
- **Source**: [ArXiv Link](http://arxiv.org/abs/2604.25904v1)