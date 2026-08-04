---
title: Cross-Fitted Residual Utility for Primary-Preserving Cognitive Decision Correction in Automatic Modulation Classification
published: 2026-08-03T11:07:37Z
authors: Linzhuo Han, Zongyong Cui, Houbiao Li
url: http://arxiv.org/abs/2608.02063v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Cross-Fitted Residual Utility for Primary-Preserving Cognitive Decision Correction in Automatic Modulation Classification

## Abstract
Automatic modulation classification research has largely emphasized representation accuracy, but a cognitive receiver must also decide when heterogeneous evidence justifies overriding a trusted default prediction. We study this post-inference problem through cross-fitted residual utility and a primary-preserving cognitive decision policy. A structured KAN-Fourier classifier supplies the default probability, while neural and non-neural candidates provide observable evidence. Candidate-specific residual utility is learned from train-split out-of-fold predictions, and a disjoint validation split freezes action thresholds, approved transitions, conditional routes, and a unified risk mask before held-out evaluation. On RMLA, RMLB, and HISAR, the complete system improves overall accuracy from 63.632% to 66.332%, 65.161% to 66.168%, and 77.769% to 79.867%, respectively. Controlled comparisons show that the isolated utility target does not uniformly dominate alternative out-of-fold meta-learners; the consistent gain comes from the complete evidence-and-action policy. Paired bootstrap and Holm-corrected McNemar analyses support the controlled gains. A frozen-policy stress test under carrier-frequency offset, I/Q imbalance, and synthetic Rayleigh/Rician fading yields positive gains in all 11 conditions, with every paired 95\% confidence interval above zero.

## Metadata
- **Published**: 2026-08-03T11:07:37Z
- **Authors**: Linzhuo Han, Zongyong Cui, Houbiao Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02063v1)