---
title: Language models suffer from a curse of ambiguity
published: 2026-08-15T23:22:01Z
authors: Nicolas Zucchet, Hyun Dong Lee, Scott Linderman
url: http://arxiv.org/abs/2608.15448v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Language models suffer from a curse of ambiguity

## Abstract
Large language models increasingly rely on sampling as a driver of their own improvement, making the fidelity of their learned distributions more critical than ever. Yet, not all distributions are equally easy to learn. In this work, we identify a curse of ambiguity: in large language models, and more broadly in all neural networks that produce discrete probability distributions, the more ambiguous a next-token distribution is, the harder it is to learn accurately. Through an extensive theoretical analysis, we trace this curse to architectural and learning roots. More ambiguous distributions require more capacity to be stored, larger embeddings to be represented, more steps to be fitted, and amplify token-sampling noise. We validate these findings on synthetic tasks with controlled ground truth and observe the same signatures in language models trained on real data. Our results provide a new perspective on the statistical capabilities of large language models and a practical framework for when to trust their output distribution.

## Metadata
- **Published**: 2026-08-15T23:22:01Z
- **Authors**: Nicolas Zucchet, Hyun Dong Lee, Scott Linderman
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15448v1)