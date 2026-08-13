---
title: Small-Scale Experiments: Are We There Yet?
published: 2026-08-12T09:47:01Z
authors: Nicholas Lourie, Kyunghyun Cho, Karen Ullrich, Sanae Lotfi
url: http://arxiv.org/abs/2608.11859v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Small-Scale Experiments: Are We There Yet?

## Abstract
Scaling laws promised cost-effective experiments; six years later, they have yet to fully deliver. Instead, researchers have found them unreliable at small scales (starting at 4M parameters) and concluded that sizable models cannot be avoided. We show this is not the case: the confounding factor is hyperparameters. Small models are highly sensitive, but hyperparameter sensitivity fades with scale. This small-scale sensitivity makes scaling laws easy to miss because they only emerge on the fully tuned frontier, and reaching that frontier requires an extensive search far beyond what most ever run. By ablating the basic scaling law recipe, we show well-tuned hyperparameters matter more than any other ingredient. Further, we reveal why those hyperparameters become easier to find: as scale increases, the hyperparameter loss surface becomes lower dimensional. Nevertheless while scaling laws exist in small models, extrapolation hits statistical limitations. A holistic approach is required. Synthesizing our insights with the recent literature, we develop a new methodology for model-centric research and demonstrate it on a question that once took the field years to settle: where to place normalization layers in the transformer architecture. From small-scale experiments, we recover the large scale result: pre-normalization works better as models grow in size. With the right tools and a better understanding, small-scale experiments can deliver on scaling laws' long-awaited promise.

## Metadata
- **Published**: 2026-08-12T09:47:01Z
- **Authors**: Nicholas Lourie, Kyunghyun Cho, Karen Ullrich, Sanae Lotfi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11859v1)