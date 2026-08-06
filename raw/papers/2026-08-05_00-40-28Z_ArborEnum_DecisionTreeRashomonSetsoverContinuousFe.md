---
title: ArborEnum: Decision Tree Rashomon Sets over Continuous Features
published: 2026-08-05T00:40:28Z
authors: Zakk Heile, Hayden McTavish, Margo Seltzer, Cynthia Rudin
url: http://arxiv.org/abs/2608.04310v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ArborEnum: Decision Tree Rashomon Sets over Continuous Features

## Abstract
The Rashomon effect describes the phenomenon that many models can achieve nearly equivalent performance on the same learning task, with significant ramifications for robustness, feature importance, and customizability. These use cases motivate the computation of Rashomon sets: the set of all models whose regularized loss is near-optimal. Decision trees are one of the few model classes for which Rashomon sets can be fully enumerated, but this computation has always been conditional on a binarization of the original data, either restricting which splits each tree is allowed to make or substantially increasing the complexity of an already difficult combinatorial problem. We introduce the first algorithm that exactly enumerates decision-tree Rashomon sets while exploiting the ordered structure of continuous features. We further develop a relaxation for approximate enumeration and an anytime algorithm that progressively refines the set of candidate thresholds, producing increasingly detailed approximations that converge to the continuous-feature Rashomon set. Experiments show that coarse binarization can miss many trees, important features, and predictive multiplicity; our algorithms achieve orders-of-magnitude speedups over existing enumeration methods, with approximations providing further speedups while maintaining near-perfect recall.

## Metadata
- **Published**: 2026-08-05T00:40:28Z
- **Authors**: Zakk Heile, Hayden McTavish, Margo Seltzer, Cynthia Rudin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04310v1)