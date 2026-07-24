---
title: Pipelined Gradient Coding
published: 2026-07-22T21:36:57Z
authors: Xian Su, Jun Li
url: http://arxiv.org/abs/2607.20739v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Pipelined Gradient Coding

## Abstract
In large-scale machine learning, distributed training commonly involves multiple workers evaluating the gradients of the model on different dataset partitions. A common challenge is the presence of straggling workers, which may significantly slow down training. Traditional gradient coding (GC) addresses this by duplicating dataset partitions across workers, allowing for the replacement of missing gradients from stragglers. However, GC requires workers to evaluate gradients on multiple dataset partitions in each step, potentially increasing overall training time. In this paper, we propose to pipeline GC, such that gradient evaluation is segmented across multiple steps and each worker evaluates gradients on just a single dataset partition per step. We develop the pipelined version for fractional repetition (FR) and cyclic repetition (CR), two representative dataset placement schemes in GC, and prove convergence guarantees for both. Through extensive simulations and experiments on cloud infrastructure, our schemes not only significantly reduce training time but also accelerate convergence compared to GC and other baselines.

## Metadata
- **Published**: 2026-07-22T21:36:57Z
- **Authors**: Xian Su, Jun Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20739v1)