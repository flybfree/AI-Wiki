---
title: Deriving Scaling Laws for OpenEuroLLM Models: Learning Rate, Batch Size and Loss
published: 2026-08-28T13:16:56Z
authors: Niccolò Ajroldi, Diana Alexandra Onutu, Haider Al-Tahan, Jörg Franke, Sampo Pyysalo, Jenia Jitsev, Aaron Klein
url: http://arxiv.org/abs/2608.28308v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Deriving Scaling Laws for OpenEuroLLM Models: Learning Rate, Batch Size and Loss

## Abstract
We study the scaling behavior of learning rate and batch size in pretraining dense large language models on English-prevalent corpora. Beyond scaling \textit{jointly optimal} learning rates and batch sizes, we investigate their \textit{marginal} evolution with model capacity and data scale and develop a model that captures these relationships. As we employ a Warmup-Stable-Decay learning rate schedule, we further investigate the gains from learning rate annealing over a broad range of hyperparameters settings, models and data budgets, and whether the optimal learning rate and batch size \textit{transfer} between the stable and decay phases. Finally, we characterize the dependence of loss on model capacity and dataset size, evaluating recently proposed scaling forms that explicitly model their interaction. We find these approaches particularly effective at capturing both undertraining and overtraining regimes across our experiments. This study establishes a first baseline and scaling procedure for the development of future OpenEuroLLM models. We open-source the complete collection of pretraining runs used in this study.

## Metadata
- **Published**: 2026-08-28T13:16:56Z
- **Authors**: Niccolò Ajroldi, Diana Alexandra Onutu, Haider Al-Tahan, Jörg Franke, Sampo Pyysalo, Jenia Jitsev, Aaron Klein
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.28308v1)