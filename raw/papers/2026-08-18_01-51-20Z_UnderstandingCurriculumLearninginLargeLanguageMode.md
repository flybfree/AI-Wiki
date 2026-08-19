---
title: Understanding Curriculum Learning in Large Language Models via Cross-Difficulty Optimization Dynamics
published: 2026-08-18T01:51:20Z
authors: Zhikai Ding, Ziyi Ye
url: http://arxiv.org/abs/2608.17268v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Understanding Curriculum Learning in Large Language Models via Cross-Difficulty Optimization Dynamics

## Abstract
Curriculum learning has been widely adopted in the post-training of large language models by organizing training data from easy to hard. However, its effectiveness varies substantially across reasoning tasks, suggesting that no single curriculum is universally optimal and raising a fundamental question: what determines when curriculum learning works? In this paper, we answer this question by analyzing the optimization dynamics induced by different curriculum schedules. We show that the transfer relationship between different difficulty levels characterizes the optimization dynamics induced by curriculum learning, which in turn explains the effectiveness of different curriculum schedules, and formalize this relationship as Relative Transfer, a principled measure of cross-difficulty knowledge transfer. Based on this measurement, we derive Transfer-aware Dynamic Curriculum Sampling (TDCS), which dynamically adjusts the sampling distribution according to the estimated transfer relationship throughout training. Extensive experiments on multiple reasoning benchmarks demonstrate that TDCS consistently outperforms representative scheduling strategies across different tasks, model scales, and training paradigms. More importantly, our work provides a unified optimization-based explanation of curriculum learning through cross-difficulty transfer.

## Metadata
- **Published**: 2026-08-18T01:51:20Z
- **Authors**: Zhikai Ding, Ziyi Ye
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.17268v1)