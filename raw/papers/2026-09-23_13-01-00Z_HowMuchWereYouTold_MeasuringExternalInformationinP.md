---
title: How Much Were You Told? Measuring External Information in Peer Reviews
published: 2026-09-23T13:01:00Z
authors: Matthieu Dubois, Pablo Piantanida, François Yvon
url: http://arxiv.org/abs/2609.28041v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# How Much Were You Told? Measuring External Information in Peer Reviews

## Abstract
Conference policies distinguish using Large Language Models (LLMs) to polish one's own review from delegating the critique, but current Artificial Text Detection (ATD) methods largely measure surface form rather than the origin of its content. We instead measure the external information carried by a review: information not explained by the reviewed paper and a generic reviewing instruction. We propose Self-Conditioning, an unsupervised information-theoretic estimator that compares the likelihood of a review under its production context with its likelihood when that context is augmented with hints extracted from the review itself. On the IntelLabs peer-review benchmark, Self-Conditioning separates fully-delegated from machine-polished reviews with AUC up to $1.0$ while remaining largely insensitive to surface rewriting. Moreover, as generators receive increasing amounts of externally-provided information, their scores move monotonically towards the human regime, unlike standard ATD baselines. High-temperature sampling can evade the estimator, but at the cost of output quality.

## Metadata
- **Published**: 2026-09-23T13:01:00Z
- **Authors**: Matthieu Dubois, Pablo Piantanida, François Yvon
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.28041v1)