---
title: Approaching I/O-optimality for Approximate Attention
published: 2026-05-22T15:23:26Z
authors: Pál András Papp, Aleksandros Sobczyk, Anastasios Zouzias
url: http://arxiv.org/abs/2605.23751v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Approaching I/O-optimality for Approximate Attention

## Abstract
We revisit the I/O complexity of attention in large language models. Given query-key-value matrices $Q,K,V\in\mathbb{R}^{n\times d}$, and a machine with fast memory size $M$, the goal is to compute the "attention matrix" $A=\text{softmax}(Q K ^{\top}/\sqrt{d}) V$ with the minimal number of data transfers between fast and slow memory. Existing methods in the literature, most notably FlashAttention and its variants, incur an I/O cost that depends quadratically on $n$, while a trivial lower bound only requires $Ω(nd)$ I/O's to read the inputs and write the output. In this work, we present a technique for computing attention where the I/O cost only depends almost-linearly on $n$ in most parameter regimes. This is achieved by developing I/O-efficient algorithms inspired by the recent approximate attention framework of Alman and Song. We also prove corresponding lower bounds in each parameter regime to show that our algorithms are indeed close to I/O-optimal.

## Metadata
- **Published**: 2026-05-22T15:23:26Z
- **Authors**: Pál András Papp, Aleksandros Sobczyk, Anastasios Zouzias
- **Source**: [ArXiv Link](http://arxiv.org/abs/2605.23751v1)