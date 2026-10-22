---
title: MAPS: Macro-Adaptive Parallel Reasoning for Regulating Search Momentum in Retrieval-Augmented Generation
published: 2026-10-21T14:19:17Z
authors: Xinze Li, Dingwen Zhang, Zhenghao Liu, Yukun Yan, Shuo Wang, Yu Gu, Ge Yu, Maosong Sun
url: http://arxiv.org/abs/2610.29792v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MAPS: Macro-Adaptive Parallel Reasoning for Regulating Search Momentum in Retrieval-Augmented Generation

## Abstract
Retrieval-Augmented Generation (RAG) improves the performance of Large Language Models (LLMs) by retrieving external knowledge. Recently, some RAG methods interleave reasoning and retrieval, enabling LLMs to progressively generate sub-queries and retrieve external knowledge. However, these methods may suffer from redundant or ineffective sub-queries and insufficiently diverse query exploration. Moreover, due to the tightly interleaved nature of reasoning and retrieval, it remains unclear how the evolving reasoning process influences query intent. To characterize the evolution of query intent during reasoning, we introduce search momentum, which captures the accumulated retrieval tendency induced by historical changes in generated sub-queries along the reasoning trajectory. Through momentum-based analysis, we find that the query generation process tends to continuously evolve along existing retrieval trajectories. Based on this observation, we propose MAPS, a Macro-Adaptive Parallel Reasoning framework for regulating search momentum and mitigating query-intent drift. MAPS first retains the retrieved knowledge and a refined reasoning state, thereby reducing the influence of historical reasoning trajectories on subsequent sub-query generation. Subsequently, MAPS extends the conventional sequential reasoning process into a parallel reasoning paradigm. At each iteration, MAPS identifies complementary retrieval directions, generates corresponding sub-queries for parallel retrieval, and consolidates the retrieved evidence to update the knowledge and reasoning states. Experiments on six question-answering benchmarks demonstrate that MAPS consistently outperforms representative RAG methods across different backbone models. All code and resources are available at https://github.com/NEUIR/MAPS.

## Metadata
- **Published**: 2026-10-21T14:19:17Z
- **Authors**: Xinze Li, Dingwen Zhang, Zhenghao Liu, Yukun Yan, Shuo Wang, Yu Gu, Ge Yu, Maosong Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.29792v1)