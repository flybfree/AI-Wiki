---
title: GEM: A Generative Embedding Model Bridging Reasoning and Retrieval
published: 2026-08-13T13:03:49Z
authors: Zhili Shen, Craig Macdonald
url: http://arxiv.org/abs/2608.13200v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GEM: A Generative Embedding Model Bridging Reasoning and Retrieval

## Abstract
Modern LLMs excel at reasoning and instruction following, enabling users to express complex and diverse information needs. However, conventional retrievers largely rely on surface-level matching between queries and documents, resulting in a growing gap between how users express their needs and how retrievers interpret them. In this paper, we present GEM, a generative embedding model that augments retrieval through its own knowledge by explicitly reasoning about user intent and relevance criteria. GEM unifies generation and embedding within a single model: it first reasons over the query, then appends an embedding token to encode the enriched context for retrieval. \zhili{Evaluated on reasoning-intensive and instruction-following retrieval tasks, GEM demonstrates the effectiveness of its reasoning-augmented retrieval, outperforming its non-reasoning variant and matching baselines using substantially larger models.} Furthermore, GEM's generative nature allows test-time compute scaling via prompting to further enhance retrieval performance. Our code is available at: https://anonymous.4open.science/r/GEM.

## Metadata
- **Published**: 2026-08-13T13:03:49Z
- **Authors**: Zhili Shen, Craig Macdonald
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13200v1)