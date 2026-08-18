---
title: Information Geometry of Message Passing
published: 2026-08-16T20:36:58Z
authors: Mykola Lukashchuk, Kyrylo Yemets, Alex Ledbetter, İsmail Şenöz
url: http://arxiv.org/abs/2608.15922v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Information Geometry of Message Passing

## Abstract
We show that the natural-gradient stationary condition of variational inference has an edge-local form on a Forney-style factor graph. We start from the Bethe free energy and constrain a selected edge marginal to an exponential family. At a stationary point, the natural parameter of that edge equals the sum of two projected messages, one from each incident factor. Each projected message is the natural-gradient projection of the exact belief-propagation log-message at the current receiving marginal, or equivalently, the gradient of its expectation in the so-called mean coordinates. We call the resulting scheme natural-gradient message passing (NGMP). The rule is local; each edge may carry its own exponential family, and the message a factor sends depends on the marginal that receives it. Compared with variational message passing, NGMP keeps the part of the exact message that the receiving family can represent instead of averaging the factor under the neighboring beliefs. The two coincide when the uncertainty on the edges entering a non-conjugate factor vanishes, and NGMP is more accurate when that uncertainty persists, for example, along a partially observed latent chain or when parameters are filtered through successive data batches. Experiments on Poisson smoothing, heteroskedastic regression, and hourly ETTh forecasting confirm this and show that the gain appears mainly in uncertainty calibration.

## Metadata
- **Published**: 2026-08-16T20:36:58Z
- **Authors**: Mykola Lukashchuk, Kyrylo Yemets, Alex Ledbetter, İsmail Şenöz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15922v1)