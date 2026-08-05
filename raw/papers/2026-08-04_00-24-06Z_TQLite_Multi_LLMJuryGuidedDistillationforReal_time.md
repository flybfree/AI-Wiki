---
title: TQLite: Multi-LLM Jury Guided Distillation for Real-time MQM Translation Quality Evaluation
published: 2026-08-04T00:24:06Z
authors: Bhavin Jawade, Cameron R. Wolfe
url: http://arxiv.org/abs/2608.02975v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TQLite: Multi-LLM Jury Guided Distillation for Real-time MQM Translation Quality Evaluation

## Abstract
Large language models (LLMs) have demonstrated impressive performance in MQM-based translation quality (TQ) evaluation, and recent advances in large reasoning models (LRMs) promise even greater improvements. However, both LLMs and LRMs are computationally expensive to deploy at scale, while small language models (SLMs)---though much more efficient---struggle with the complex reasoning required for evaluation tasks. In this work, we present an extensive empirical study benchmarking SLMs, LLMs, and LRMs across a wide range of TQ evaluation setups, providing a comprehensive view of the current landscape and establishing best practices. To address the scalability challenge, we introduce TQLite, a novel distillation framework that enables SLMs to approach the MQM evaluation performance of the best LRM-based evaluators. Our approach leverages a multi-LRM jury to generate high-quality synthetic training data via practical data curation techniques and aggregation of evaluation responses across a diverse panel of models. Our results demonstrate that SLMs trained via TQLite achieve strong MQM evaluation performance that far exceeds off-the-shelf evaluation capabilities of standard SLMs, offering a scalable and cost-effective alternative to LLM- and LRM-based evaluators.

## Metadata
- **Published**: 2026-08-04T00:24:06Z
- **Authors**: Bhavin Jawade, Cameron R. Wolfe
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02975v1)