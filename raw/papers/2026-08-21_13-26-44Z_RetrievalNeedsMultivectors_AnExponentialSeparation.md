---
title: Retrieval Needs Multivectors: An Exponential Separation
published: 2026-08-21T13:26:44Z
authors: Mihir Agarwal, Viraj Agrawal, Sabyasachi Basu, Ankit Garg, Kirankumar Shiragur
url: http://arxiv.org/abs/2608.21494v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Retrieval Needs Multivectors: An Exponential Separation

## Abstract
Recent works have highlighted the expressive limitations of embedding based retrieval models through both theoretical analyses and challenging benchmarks such as LIMIT. While multi-vector embeddings consistently outperform single-vector embeddings, the precise representational gap between them remains poorly understood. In this work, following Jayaram's work, we provide the first explicit family of query and document sets, together with their relevance matrices, for which single-vector embeddings that rank all relevant documents above irrelevant ones require exponential size, whereas polynomial-size multi-vector embeddings suffice. Our result establishes an exponential separation between the expressive power of single-vector and multi-vector embeddings for the task of ranking of documents as opposed to approximating numerical scores as in the work of Jayaram.   Motivated by our theoretical construction, we introduce ANDOR, a new retrieval benchmark that naturally instantiates these hard examples. We show that state-of-the-art single-vector embedding models perform poorly on ANDOR in the zero-shot setting and exhibit only marginal improvements after fine-tuning, highlighting the inherent difficulty of the benchmark compared to prior work. In contrast, multi-vector models consistently outperform their single-vector counterparts and improve substantially with fine-tuning, closely aligning with our theoretical predictions.

## Metadata
- **Published**: 2026-08-21T13:26:44Z
- **Authors**: Mihir Agarwal, Viraj Agrawal, Sabyasachi Basu, Ankit Garg, Kirankumar Shiragur
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.21494v1)