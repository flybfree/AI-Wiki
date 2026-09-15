---
title: CompCQR: Compositional Query Generation for Training-Free Conversational Search
published: 2026-09-13T16:31:22Z
authors: Yunah Jang, Kang-il Lee, Joongbo Shin, Kyomin Jung
url: http://arxiv.org/abs/2609.14646v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CompCQR: Compositional Query Generation for Training-Free Conversational Search

## Abstract
Multi-turn interactions with LLMs are becoming increasingly common in information-seeking scenarios. However, user queries are often ambiguous and context-dependent, making them ill-suited for direct use as retriever queries. Conversational query reformulation (CQR) addresses this issue by rewriting the current utterance into a stand-alone query grounded in the dialogue history. Recent LLM-based CQR approaches achieve strong performance; however, their repeated LLM invocations and misalignment with downstream retrievers remain challenges. In this work, we begin from the observation that retrievers are highly sensitive to content ordering: simply reordering the same content can lead to changes in retrieval coverage and performance. Based on this, we propose a novel training-free method that generates a very large number of queries with minimal LLM usage by compositionally combining a small set of atomic components. We further apply LLM reasoning to construct a high-quality document set that balances precision and recall while capturing the user's core intent. Our framework generalizes across both open- and closed-source LLMs as well as dense and sparse retrievers. It achieves strong performance on four widely used conversational benchmarks, with up to 22.5% relative MRR improvement over the previous state-of-the-art baseline with far fewer LLM calls.

## Metadata
- **Published**: 2026-09-13T16:31:22Z
- **Authors**: Yunah Jang, Kang-il Lee, Joongbo Shin, Kyomin Jung
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.14646v1)