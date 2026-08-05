---
title: Training Documents Reranker with Search Rubrics for Deep Research Agent
published: 2026-08-04T12:11:14Z
authors: Wenhan Liu, Yu Lu, Qiaolin Xia, Hui Xu, Tong Zhao, Jian Xi, Yutao Zhu, Haijin Liang, Haibo Shi, Hao Wang, Zhicheng Dou
url: http://arxiv.org/abs/2608.03527v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Training Documents Reranker with Search Rubrics for Deep Research Agent

## Abstract
Retrieval systems help deep research agents generate high-quality answers by providing relevant documents. However, existing retrievers typically select documents through relevance matching, while individually well-matched top-$k$ documents may not form a \textit{set} that satisfies the complex information needs of an agent query (\eg, diverse, concise and authoritative documents). In this paper, we propose search-oriented rubrics that \textit{explicitly} define the requirements that high-quality document sets should satisfy for each agent query. Our search rubrics are organized into a hierarchical structure and synthesized using a powerful LLM. Based on these search rubrics, we further train a document reranker \textbf{RubricRanker} to select a high-quality subset from retrieved documents. We design a two-stage training framework that consists of rubrics-guided supervised fine-tuning and rubric-based reinforcement learning. Extensive experiments demonstrate that RubricRanker outperforms the strongest baseline by 2.6 points on four deep research benchmarks and generalizes well to five RAG benchmarks.

## Metadata
- **Published**: 2026-08-04T12:11:14Z
- **Authors**: Wenhan Liu, Yu Lu, Qiaolin Xia, Hui Xu, Tong Zhao, Jian Xi, Yutao Zhu, Haijin Liang, Haibo Shi, Hao Wang, Zhicheng Dou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.03527v1)