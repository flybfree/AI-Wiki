---
title: Measuring Structured Predictability in Neural Training Dynamics: A Cross-Regime Study
published: 2026-08-16T02:17:51Z
authors: Fanqi Wang, Weisheng Tang, Hairong Qi
url: http://arxiv.org/abs/2608.15483v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Measuring Structured Predictability in Neural Training Dynamics: A Cross-Regime Study

## Abstract
Modern deep networks are trained through long update trajectories, yet their temporal organization remains less systematically characterized than architectures, losses, or optimizers. We study short-horizon predictability as a measure of temporal redundancy: where, when, and under which training conditions recent updates contain information about near-future parameter motion. We combine three complementary probe families, displacement-direction, subspace-residual, and predictor-based probes, with convention-aware, null-calibrated group-level readouts, and apply them to multi-pass vision training on CIFAR and public Pythia pretraining checkpoints. Across both regimes, vector-like tensors such as normalization parameters and biases (auxiliary parameters) exhibit simpler short-horizon dynamics than matrix-like feature-transforming weights (bulk parameters), whose predictable behavior concentrates in localized, time-varying pockets. Agreement within and across probe families, and with independent trajectory diagnostics, indicates that these measurements capture intrinsic trajectory structure, while probe differences distinguish complementary forms of temporal organization. Controlled CIFAR comparisons further show that architecture and training recipe systematically modulate the measured structure. A Pythia-70M case study further exposes a sequence of role-, depth-, and scale-dependent events, including bulk ESA falling below the random sign-agreement level and the emergence and redistribution of predictable qkv pockets across layers. These results position short-horizon predictability as a retrospective, parameter-resolved diagnostic of training dynamics.

## Metadata
- **Published**: 2026-08-16T02:17:51Z
- **Authors**: Fanqi Wang, Weisheng Tang, Hairong Qi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15483v1)