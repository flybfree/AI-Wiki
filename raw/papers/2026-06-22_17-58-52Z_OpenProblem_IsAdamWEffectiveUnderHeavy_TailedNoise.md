---
title: Open Problem: Is AdamW Effective Under Heavy-Tailed Noise?
published: 2026-06-22T17:58:52Z
authors: Dingzhi Yu, Hongyi Tao, Yuanyu Wan, Luo Luo, Lijun Zhang
url: http://arxiv.org/abs/2606.23676v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Open Problem: Is AdamW Effective Under Heavy-Tailed Noise?

## Abstract
AdamW is the de facto optimizer for training large language models (LLMs), yet the theory behind it still lives mostly in finite-variance regimes. This is increasingly unsatisfying, as empirical evidence indicates that stochastic gradient noise in LLM pretraining is typically heavy-tailed. Recent work shows that sign-based optimizers such as Lion and Muon achieve sharp heavy-tailed rates, and that AdaGrad can also converge under heavy-tailed noise. However, no rigorous convergence theory for AdamW has yet been established in this regime. Can AdamW converge under the same heavy-tailed assumptions, or does its second-moment accumulator create a genuine obstruction? We formulate this as an open problem, prove a positive weighted-metric benchmark, and give a corridor lower-bound mechanism showing how denominator memory can hide large gradients.

## Metadata
- **Published**: 2026-06-22T17:58:52Z
- **Authors**: Dingzhi Yu, Hongyi Tao, Yuanyu Wan, Luo Luo, Lijun Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.23676v1)