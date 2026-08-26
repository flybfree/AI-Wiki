---
title: Diverse by Reasoning: Harnessing the Wisdom of LLM Crowds for Future Prediction
published: 2026-08-25T02:46:28Z
authors: Nirupam Chetlapalli, Yiming Liao, Min-Chun Chen, Keke Chen
url: http://arxiv.org/abs/2608.24001v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Diverse by Reasoning: Harnessing the Wisdom of LLM Crowds for Future Prediction

## Abstract
Large language models (LLMs) are increasingly used for future prediction, motivating the use of multiple models as a wisdom-of-the-crowd mechanism. However, simply increasing crowd size does not guarantee effective diversity, as different LLMs may exhibit redundant behaviors. We propose a behavior-aware framework for constructing diverse LLM crowds. The framework characterizes models using their reasoning traces on independent development tasks, clusters models by behavioral similarity, and selects representatives for collective prediction. We evaluate 25 LLMs using seven development benchmarks for behavioral diversity modeling and two future-prediction benchmarks for evaluating diverse crowds' performance. Our results show that crowd composition can matter more than crowd size: a three-model medoid crowd based on K-means++ behavioral clustering outperforms conventional voting over all 25 models on both prediction benchmarks, while reducing model calls by 88% and inference cost by approximately 80%. The results further suggest that representative behavioral diversity, rather than simply maximizing diversity, is important for constructing effective LLM crowds

## Metadata
- **Published**: 2026-08-25T02:46:28Z
- **Authors**: Nirupam Chetlapalli, Yiming Liao, Min-Chun Chen, Keke Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24001v1)