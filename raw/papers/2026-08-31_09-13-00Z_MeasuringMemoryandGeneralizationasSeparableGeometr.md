---
title: Measuring Memory and Generalization as Separable Geometric Channels: The Topo^2 Framework
published: 2026-08-31T09:13:00Z
authors: Zhanbo Zhang, Ming Liu, Qing Wang
url: http://arxiv.org/abs/2608.30487v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Measuring Memory and Generalization as Separable Geometric Channels: The Topo^2 Framework

## Abstract
Deep networks trained on noisy labels simultaneously generalize on clean data and memorize flipped labels. These are usually conflated as pressures on one capacity. We present Topo^2, a measurement framework that makes them causally separable, measurable, and law-governed. Persistent-homology H1 structure of the representation space separates into a within-class manifold channel (a function of the training stopping point) and a cross-class channel (a monotone readout of memorized flipped samples). An intervention, the FM0 prescription (zero loss on flipped samples from epoch 0), reaches each setting's generalization ceiling while memorizing essentially nothing. Within the framework we establish a law set with graded evidence: (L2) FM0 separation prescription (9/9); (L1) the within-channel as a training-position function (mid-rise 6/6; convergence-back CIFAR 3/3, SVHN 2/3); (L3) a ring-construction identity (definitional, not a law); and TLS (memory-generalization topological layering): memory is causally additive, anchored (silencing clean collapses the representation), invertible (stripping memory restores near-ceiling generalization), and quantitatively billable (the memorization cost law, effective slope coefficient C ~ 0.38 at the reference capacity: CIFAR-10 0.3801 / SVHN 0.3806 / CIFAR-100 0.384 / VGG 0.3715, capacity-dependent in general and traced to clean-sample feature displacement). We also publish the framework's boundaries: a falsification ledger of nine dead ends, and an instrument-vindication section that excludes six families of global statistics as explanations of the within-channel. The framework turns "memorization" from an ill-defined capacity into a measurable, separable, invertible topological layer.

## Metadata
- **Published**: 2026-08-31T09:13:00Z
- **Authors**: Zhanbo Zhang, Ming Liu, Qing Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30487v1)