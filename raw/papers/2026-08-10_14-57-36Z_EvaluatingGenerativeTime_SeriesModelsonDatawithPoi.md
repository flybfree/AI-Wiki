---
title: Evaluating Generative Time-Series Models on Data with Point Masses
published: 2026-08-10T14:57:36Z
authors: Jian Xu
url: http://arxiv.org/abs/2608.09692v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evaluating Generative Time-Series Models on Data with Point Masses

## Abstract
Many of the series that generative time-series models are benchmarked on place a large probability mass on a single value --- it does not rain, no ride is requested, no part is ordered. We report what happens when such data is evaluated carefully. First, the standard rolling-origin protocol can score a model on a window whose atom structure bears no resemblance to the dataset: on one benchmark the dataset is $42\%$ zeros and the evaluation windows are $13\%$, on another $47\%$ against $5\%$. This is not a cosmetic problem --- it reversed one of our own conclusions, turning the strongest occurrence model in our study into what looked like a cautionary tale. Second, we give a control in which CRPS is invariant \emph{by construction} while the temporal coupling is destroyed, which measures exactly how much that coupling contributes to a chosen statistic. Third, benchmarking seven models on a matched protocol over five seeds, an autoregressive hurdle beats a conditional flow on five of six datasets, by up to a factor of $153$, while the flow's own occurrence statistics vary by up to $62\%$ across training seeds and every baseline is deterministic. Finally, the model ordering is not the same under five different occurrence statistics, and the two that do not share a construction agree with each other least.

## Metadata
- **Published**: 2026-08-10T14:57:36Z
- **Authors**: Jian Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.09692v1)