---
title: Uncertainty-guided active learning for surrogate prediction of stream-finishing wear fields
published: 2026-08-01T11:12:39Z
authors: Anand Kumar, Puli Saikiran, Vineet Dawara, Koushik Viswanathan
url: http://arxiv.org/abs/2608.00593v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Uncertainty-guided active learning for surrogate prediction of stream-finishing wear fields

## Abstract
In stream finishing, the wear experienced by a workpiece depends strongly on its orientation within the rotating abrasive media. Determining suitable orientations to achieve uniform wear requires evaluating the wear-rate field over all feasible orientations. Although the discrete element method (DEM) accurately resolves particle interactions, simulating hundreds of feasible orientations for a new geometry is computationally expensive. We present an uncertainty-guided surrogate framework that predicts, directly from geometry, the three fields governing erosion: per-triangle normal impact velocity, tangential impact velocity, and particle impact flux. These fields are combined through the Finnie wear model to reconstruct the wear-rate distribution. The surrogate employs a deep ensemble whose disagreement estimates epistemic uncertainty, enabling an active-learning strategy that selectively performs DEM simulations for the most uncertain orientations. Trained using only $13\%$ of the $696$ feasible orientations, the surrogate achieves Spearman rank correlations of $0.93$, $0.89$, and $0.93$ for the normal impact velocity, tangential impact velocity, and particle impact flux, respectively. Moreover, the predicted uncertainty is well calibrated, reliably anticipating prediction error and the fidelity of the reconstructed wear field, which matches DEM with a Spearman rank correlation of up to $0.97$ for low-uncertainty orientations and degrades in a controlled manner as uncertainty increases.

## Metadata
- **Published**: 2026-08-01T11:12:39Z
- **Authors**: Anand Kumar, Puli Saikiran, Vineet Dawara, Koushik Viswanathan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00593v1)