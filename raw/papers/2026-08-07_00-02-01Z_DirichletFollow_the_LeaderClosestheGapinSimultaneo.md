---
title: Dirichlet Follow-the-Leader Closes the Gap in Simultaneous Multiclass U-Calibration
published: 2026-08-07T00:02:01Z
authors: Pahan Dewasurendra
url: http://arxiv.org/abs/2608.06656v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dirichlet Follow-the-Leader Closes the Gap in Simultaneous Multiclass U-Calibration

## Abstract
Can one forecaster attain the optimal regret rate for every bounded proper loss and also adapt to every smooth proper loss? Recent work answered this up to a dimension gap. Its self-concordant perturbation gives roughly $K^{5/4}\sqrt{T}$ worst-case regret and incurs an additional $β\sqrt{K}\log K$ for $β$-smooth losses. We close both gaps with a one-line forecaster. After observing class counts $c_{t-1}$, draw the next prediction from $\operatorname{Dir}(c_{t-1})$, on the face of classes seen so far. This is a fresh Bayesian bootstrap of the outcomes. The analysis rests on an exact identity: averaging any bounded proper loss under $\operatorname{Dir}(α)$ equals a discrete derivative of its Dirichlet-averaged Bayes risk. The identity makes the be-the-perturbed-leader term telescope to a nonpositive Jensen gap. A one-count likelihood ratio then bounds stability by the inverse square root of that class's count. The resulting single, horizon-free algorithm satisfies $\sup_{\ell}\mathbb{E}\operatorname{Reg}_{\ell}\leq 4\sqrt{S_T T}\leq 4\sqrt{K T}$ and $\mathbb{E}\operatorname{Reg}_{\ell}\leq \frac{5}{2}β(1+\log T)$ for every $β$-smooth proper loss. Here $S_T$ is the number of observed classes. Known lower bounds show that both rates are optimal in their nontrivial regimes. The proof covers nondifferentiable losses and changes of the active simplex face.

## Metadata
- **Published**: 2026-08-07T00:02:01Z
- **Authors**: Pahan Dewasurendra
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.06656v1)