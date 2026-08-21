---
title: ReCache: Efficient KV Cache Reuse and Compression for Tool-Augmented LLM Agents
published: 2026-08-20T05:57:24Z
authors: Yichu Fang, Sitong Wei, Haozhe Hu, Xiaoyu Shen
url: http://arxiv.org/abs/2608.19662v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ReCache: Efficient KV Cache Reuse and Compression for Tool-Augmented LLM Agents

## Abstract
Agentic language models repeatedly encode tool and skill schemas that recur across requests in different combinations and orders, preventing standard prefix caching from reusing their key--value (KV) states. We introduce \textbf{ReCache}, a framework for independently caching resource representations while reducing their inference-time computational and memory overhead. Resource-wise attention removes cross-resource interactions and assigns resource-local positions, producing composition-invariant KV blocks. ReCache then restricts resource visibility to contribution-selected layer--KV-head-group routes and retains only invocation-critical fields through structural and semantic pruning. We evaluate ReCache on a benchmark assembled from seven public tool- and skill-use datasets, including resource-disjoint tests. Resource-wise attention matches dense invocation performance (82.3\% versus 82.4\% Inv-F1) while providing a 3.655$\times$ time-to-first-token speedup. The complete framework reduces allocated KV-tensor memory by 92.43\% and accelerates attention by 1.423$\times$. These results show that separating reusable schema encoding from selective resource access substantially reduces agentic inference costs with limited effectiveness loss. The code is available at https://github.com/EIT-NLP/ReCache.

## Metadata
- **Published**: 2026-08-20T05:57:24Z
- **Authors**: Yichu Fang, Sitong Wei, Haozhe Hu, Xiaoyu Shen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19662v1)