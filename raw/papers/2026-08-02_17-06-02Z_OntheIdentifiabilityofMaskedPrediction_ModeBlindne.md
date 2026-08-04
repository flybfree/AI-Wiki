---
title: On the Identifiability of Masked Prediction: Mode Blindness and Mask Schedules
published: 2026-08-02T17:06:02Z
authors: Yichao Cai, Javen Qinfeng Shi
url: http://arxiv.org/abs/2608.01383v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# On the Identifiability of Masked Prediction: Mode Blindness and Mask Schedules

## Abstract
Masked prediction learns representations by fitting a schedule-weighted family of conditional laws, but it remains unclear when near-optimal conditional prediction pins down the underlying joint law. We study this question for data with two well-separated global modes, outside the reach of rapid-mixing recovery guarantees, and show that the answer is decided by the mask schedule alone. Under large-context mode pinning, reweighting the two modes can move the joint law by a constant in total variation while perturbing the masked objective exponentially little in the visible-context size: mask schedules dominated by large contexts are provably blind to the global mode weights. To quantify this, we introduce an $\varepsilon$-identifiability modulus, the largest distributional error consistent with a given excess risk, and prove that it remains macroscopic at an excess risk that is exponentially small. An exact information decomposition pinpoints what restores identifiability: mode-weight sensitivity is governed by the residual mode uncertainty given the visible context. Consequently, low-visibility masks recover this sensitivity, and positive full-mask mass anchors the joint law over all admissible models with no assumption on the data law. Empirically, we test our theory at three levels: enumeration on computable laws verifies the predicted rates, gradient training reproduces both the mode blindness and the recovery, and measurements on real corpora place natural text between the two certified regimes.

## Metadata
- **Published**: 2026-08-02T17:06:02Z
- **Authors**: Yichao Cai, Javen Qinfeng Shi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01383v1)