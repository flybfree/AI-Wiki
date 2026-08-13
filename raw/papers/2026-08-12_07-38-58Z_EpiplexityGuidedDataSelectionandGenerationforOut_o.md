---
title: Epiplexity Guided Data Selection and Generation for Out-of-Distribution Generalization
published: 2026-08-12T07:38:58Z
authors: Ellen Su, Andres Potapczynski, Shikai Qiu, Edward Hughes, Andrew Gordon Wilson
url: http://arxiv.org/abs/2608.11746v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Epiplexity Guided Data Selection and Generation for Out-of-Distribution Generalization

## Abstract
Modern systems are increasingly expected to transfer across tasks not specified during training. What data facilitates generalization in these new, unanticipated settings? One hypothesis is that data with more structural information could contain shared circuits and subprograms that could be recycled in a wider array of downstream settings. Epiplexity, a recently proposed measure of the structural information a compute-bounded learner can extract from data, provides a mechanism to reason about this relationship. In this paper, we show how to operationalize epiplexity as an online training signal for data selection and synthetic data generation. For selection, we fit scaling laws to the training loss curves of natural data domains to predict the expected epiplexity gain as a function of training tokens, and use this signal to adaptively determine the sampling weights over domains during training. For synthetic data generation, we define a generator's reward as the change in learner epiplexity over a buffer of previously generated data and use REINFORCE policy gradients to guide the generator toward an epiplexity-maximizing distribution. In both cases, higher epiplexity predicts improved downstream performance on zero-shot and fine-tuning based tasks, supporting the hypothesis that data rich in structural information yield representations that transfer across domains.

## Metadata
- **Published**: 2026-08-12T07:38:58Z
- **Authors**: Ellen Su, Andres Potapczynski, Shikai Qiu, Edward Hughes, Andrew Gordon Wilson
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11746v1)