---
title: Modular TTT: Rethinking Test-Time Training as Composable Modules
published: 2026-08-07T11:11:43Z
authors: Bohao Tang, Zhen Qin, Yuqi Pan, Zheng Li, Pengfei Liu, Ya Zhang
url: http://arxiv.org/abs/2608.07110v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Modular TTT: Rethinking Test-Time Training as Composable Modules

## Abstract
Test-time training (TTT) views sequence modeling as an online learning problem in which fast weights are updated by an internal learning rule. Despite the growing number of TTT variants, existing approaches typically hard-code each variant separately, which makes it difficult to design new TTT methods and to isolate the role of each component. To address this, we propose Modular TTT, a framework that represents the inner learner as a directed acyclic graph and exposes the fast-weight network, loss function, learning rate, weight decay, and normalization as explicit design dimensions. Modular TTT automatically composes primitive-level train-view forward, train-view backward, and causal query-view rules into the full graph-level TTT computation, including the fast-weight state transition. Using Modular TTT, we systematically ablate the components of TTT and find that small learning-rate initialization, weight decay, and a single-layer nonlinearity improve performance, while MSE and inner-product losses perform similarly. Deeper fast-weight networks and normalization tend to hurt performance because they induce excessively large activations, while residual connections and gating provide little measurable benefit. Guided by these findings, we train the best resulting variant as 410M- and 1.45B-parameter models on 100B tokens, and observe training loss and benchmark performance comparable to Gated DeltaNet.

## Metadata
- **Published**: 2026-08-07T11:11:43Z
- **Authors**: Bohao Tang, Zhen Qin, Yuqi Pan, Zheng Li, Pengfei Liu, Ya Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07110v1)