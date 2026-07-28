---
title: Joint Flow Matching for Generator-Consistent Classification
published: 2026-07-27T02:45:39Z
authors: Hayden McAlister, Lech Szymanski
url: http://arxiv.org/abs/2607.23946v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Joint Flow Matching for Generator-Consistent Classification

## Abstract
We introduce Joint Flow Matching (JFM), a training framework for continuous normalising flows over multiple variables. Standard flow matching transports variables from noise to data simultaneously, offering no natural mechanism for forward and reverse conditional inference from a shared joint model. JFM resolves this by assigning opposite roles to each variable at the temporal endpoints. We prove that JFM produces a consistent joint distribution where that forward or reverse integration are conditionals of the same joint. We explore this consistency in the context of joint classification and generation as the basis for interpretability in discriminative-generative models. We validate JFM on conditional datasets producing competitive accuracy with inherently well-calibrated confidence scores without post-hoc calibration, and classifier-consistent image generation.

## Metadata
- **Published**: 2026-07-27T02:45:39Z
- **Authors**: Hayden McAlister, Lech Szymanski
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23946v1)