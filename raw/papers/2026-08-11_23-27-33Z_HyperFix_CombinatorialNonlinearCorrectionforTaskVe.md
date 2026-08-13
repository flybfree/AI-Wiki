---
title: HyperFix: Combinatorial Nonlinear Correction for Task Vector Merging
published: 2026-08-11T23:27:33Z
authors: Hyo Seo Kim, Ren Wang
url: http://arxiv.org/abs/2608.11499v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HyperFix: Combinatorial Nonlinear Correction for Task Vector Merging

## Abstract
Task vectors enable model merging without joint retraining. In practice, the subset of task vectors to be merged may vary, but many existing methods use scalar tuning for a particular subset, requiring repeated tuning across subsets and restricting task vector merging to linear rescaling. We therefore formulate merging across varying task subsets as a combinatorial correction problem and introduce HyperFix, a lightweight hypernetwork that predicts subset-conditioned nonlinear corrections in weight space. Trained once on singleton, pair, and triple subsets from a task bank, HyperFix generalizes to larger subsets without per-subset optimization. Our local perturbation analysis bounds the residual correction beyond linear merging and motivates learning it from small task updates. Experiments across diverse benchmarks show that HyperFix outperforms existing task vector merging methods while reducing tuning cost.

## Metadata
- **Published**: 2026-08-11T23:27:33Z
- **Authors**: Hyo Seo Kim, Ren Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11499v1)