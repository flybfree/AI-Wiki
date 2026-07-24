---
title: Weak-to-Strong Learning in Decision Making
published: 2026-07-20T19:37:35Z
authors: Jingwei Ji, Renyuan Xu
url: http://arxiv.org/abs/2607.18467v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Weak-to-Strong Learning in Decision Making

## Abstract
Many operational decisions rely on predictive models that estimate uncertain outcomes conditional on observable contexts. Training such models, however, often faces a fundamental data asymmetry: labeled outcomes are scarce or costly to obtain, while contextual covariates are abundant. Motivated by this data asymmetry, we develop a decision-aware weak-to-strong (W2S) framework that leverages both labeled and unlabeled data to improve contextual stochastic optimization. Specifically, we first train a weak model using limited labeled data and then use it to generate predicted outcome distributions on unlabeled contexts. These distributions provide soft supervision for training a strong model. We establish a non-asymptotic upper bound on the excess decision risk of W2S and a complementary lower bound for a strong-only benchmark. Their comparison yields explicit sufficient conditions under which W2S improves downstream decision performance. The key quantity is the correlation dimension between the weak and strong feature representations: when it is small, abundant unlabeled data reduce the effect of teacher errors along non-overlapping directions. A synthetic newsvendor experiment and a comment moderation experiment based on real-world data provide empirical evidence consistent with the theory.

## Metadata
- **Published**: 2026-07-20T19:37:35Z
- **Authors**: Jingwei Ji, Renyuan Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.18467v1)