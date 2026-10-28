---
title: Batching the Reflective Optimization Loop: Parallel Proposals Make GEPA Faster and Better
published: 2026-10-27T07:41:40Z
authors: Jialin Zhang, Lakshya A Agrawal, Shangyin Tan, Donghyun Lee, Lutfi Eren Erdogan, Dan Klein, Koushik Sen, Alex Dimakis, Matei Zaharia
url: http://arxiv.org/abs/2610.36774v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Batching the Reflective Optimization Loop: Parallel Proposals Make GEPA Faster and Better

## Abstract
Reflective text optimization makes agentic systems better, but the optimization loop is itself a resource-hungry workload whose sequential structure leaves parallel evaluation capacity idle. We extend the open-source GEPA optimizer to propose and evaluate a batch of candidates on each optimization step instead of one candidate at a time. In our sweep on two tasks, most batched runs finished in half the wall-clock time or less, and the fastest in about a quarter to a third. Batched settings also achieved higher held-out test scores, from 68.9% to 72.1% on LiveBench-Math (with $2\times2$) and from 49.0% to 60.0% on HoVer (with $8\times1$). A simple runtime model explains the measured speedups under a finite worker pool, and batched settings also spend their metric-call and dollar budgets more efficiently. We frame the axes along which a reflective optimization step can scale in parallel, a first look at allocating a fixed optimization budget across them.

## Metadata
- **Published**: 2026-10-27T07:41:40Z
- **Authors**: Jialin Zhang, Lakshya A Agrawal, Shangyin Tan, Donghyun Lee, Lutfi Eren Erdogan, Dan Klein, Koushik Sen, Alex Dimakis, Matei Zaharia
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.36774v1)