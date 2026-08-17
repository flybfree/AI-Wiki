---
title: Boosting Data Augmentation with Stochastic Weight Averaging
published: 2026-08-14T15:15:23Z
authors: Longde Huang, Axel Flinth, Jan E. Gerken
url: http://arxiv.org/abs/2608.14373v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Boosting Data Augmentation with Stochastic Weight Averaging

## Abstract
The symmetries of a learning task have become an important factor in designing modern deep learning solutions. Data augmentation is a straightforward and effective way of incorporating symmetries into a generic neural network. Recent results show that infinitely large deep ensembles show perfect symmetry when trained on augmented data. However, since training ensembles requires repeating the training process many times, this method is costly. In this work, we study stochastic weight averaging (SWA) as an alternative ensembling technique that does not require repeated training runs. We analyze SWA by approximating the stochastic training trajectory at the end of training with an Ornstein--Uhlenbeck process. We show that in the infinite-width limit, SWA on augmented data provides an equiviariance boost that goes beyond what could be expected from the performance increase due to SWA alone. We verify our results with extensive numerical experiments on numerous models spanning computer vision and graph classification with both discrete and continuous symmetries.

## Metadata
- **Published**: 2026-08-14T15:15:23Z
- **Authors**: Longde Huang, Axel Flinth, Jan E. Gerken
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14373v1)