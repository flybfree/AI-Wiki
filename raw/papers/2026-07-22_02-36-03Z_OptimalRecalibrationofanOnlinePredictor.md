---
title: Optimal Recalibration of an Online Predictor
published: 2026-07-22T02:36:03Z
authors: Lunjia Hu, Kevin Tian, Chutong Yang
url: http://arxiv.org/abs/2607.19689v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Optimal Recalibration of an Online Predictor

## Abstract
We study the problem of recalibrating an online predictor [KE17, OKS24]: given an arbitrary "hint" sequence of forecasts, the learner must output new predictions that are calibrated while incurring small excess error relative to the original forecasts, under a proper loss. We give an online algorithm that achieves $(\varepsilon, \varepsilon^2)$-recalibration for Lipschitz proper losses in   $T \approx \varepsilon^{-3}$ rounds, using an imbalanced extension of the recent simultaneous Blackwell approachability reduction framework of [HTY26]. We show that this tradeoff is optimal by proving a matching lower bound for recalibrating against the squared loss. We also prove a companion $\mathcal{K}_2$-recalibration theorem that obtains the same tradeoffs up to a logarithmic factor.   As our main application, we show how our recalibration algorithms can be combined with the online refinement method of [FH23] to obtain simultaneous $\varepsilon$-calibration and $\varepsilon^2$-calibeating for smooth proper losses at the same asymptotic rate, improving upon prior works that achieved these properties separately or with a worse $\varepsilon$ dependence. In particular, the $\mathcal{K}_2$ variant answers a question of [CHJL26] on simultaneously achieving near-optimal calibeating and calibration rates. We also derive extensions to settings with multiple hint sequences. Finally, we empirically evaluate our algorithms on a classification dataset undergoing distribution shift.

## Metadata
- **Published**: 2026-07-22T02:36:03Z
- **Authors**: Lunjia Hu, Kevin Tian, Chutong Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19689v1)