---
title: Loss-Based Active Learning for Neural Abstractive Summarization
published: 2026-08-26T14:52:47Z
authors: Michail Ioannou, Tatiana Passali, George Michalopoulos, Grigorios Tsoumakas
url: http://arxiv.org/abs/2608.25881v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Loss-Based Active Learning for Neural Abstractive Summarization

## Abstract
Fine-tuning abstractive summarization models requires high-quality annotated data. However, obtaining such corpora is expensive and time-consuming, as it requires human annotators to read and comprehend long documents to create accurate summaries. Active learning mitigates this issue by selecting only the most informative instances for annotation, allowing models to achieve competitive results with significantly fewer labels. However, the application of active learning to summarization remains under-explored, and existing studies often suffer from instability and significant computational bottlenecks. To overcome these challenges, we propose LOBSTER (LOss-BaSed acTivE leaRning), a novel active learning framework designed specifically for abstractive summarization. LOBSTER improves performance by prioritizing unlabeled instances semantically similar to the model's current high-loss training examples, enabling the model to explicitly correct its specific weaknesses. Our empirical evaluation across three benchmark datasets and two summarization backbone models demonstrates that LOBSTER consistently matches or outperforms current state-of-the-art approaches while achieving a query selection speedup of up to 665x.

## Metadata
- **Published**: 2026-08-26T14:52:47Z
- **Authors**: Michail Ioannou, Tatiana Passali, George Michalopoulos, Grigorios Tsoumakas
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.25881v1)