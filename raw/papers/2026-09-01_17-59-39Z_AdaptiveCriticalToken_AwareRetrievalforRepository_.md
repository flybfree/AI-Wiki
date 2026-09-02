---
title: Adaptive Critical Token-Aware Retrieval for Repository-Level Code Generation
published: 2026-09-01T17:59:39Z
authors: Kefeng Duan, Dewu Zheng, Yanlin Wang, Terry Yue Zhuo, Mingwei Liu, Jianxing Yu, Jiachi Chen, Ensheng Shi, Xilin Liu, Yuchi Ma, Zibin Zheng
url: http://arxiv.org/abs/2609.01601v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Adaptive Critical Token-Aware Retrieval for Repository-Level Code Generation

## Abstract
The repository-level code generation task requires synthesizing code that satisfies task requirements while remaining consistent with the target repository context. Since real-world repositories often exceed the input length limits of LLMs, existing approaches commonly adopt retrieval-augmented generation (RAG) to provide repository-specific context. Despite improving repository-context retrieval, existing methods typically provide context as task-level support, without explicitly identifying the critical tokens that require fine-grained repository context during generation. During the autoregressive generation process of LLMs, errors often concentrate at a small number of decisive positions: once such tokens are generated incorrectly, subsequent code may follow an incorrect semantic path and eventually lead to functional failure. We refer to these positions as "critical tokens". In this paper, we propose ACToR, an adaptive critical token-aware retrieval framework for repository-level code generation. ACToR identifies critical tokens during generation and triggers targeted retrieval on demand to provide repository context at these decisive positions. In addition, we design a position-aware weighting method for dense retrievers to prioritize context that is more informative for generation. We evaluate ACToR on two representative repository-level benchmarks, RepoExec and CoderEval. Experimental results show that ACToR consistently outperforms state-of-the-art methods, achieving relative improvements of 8.4% on RepoExec and 15.4% on CoderEval. Beyond performance gains, we systematically quantify the impact of critical tokens, revealing their central role in major generation failures and highlighting the necessity of targeted retrieval strategies. We provide the code and data at https://github.com/DeepSoftwareAnalytics/ACToR.

## Metadata
- **Published**: 2026-09-01T17:59:39Z
- **Authors**: Kefeng Duan, Dewu Zheng, Yanlin Wang, Terry Yue Zhuo, Mingwei Liu, Jianxing Yu, Jiachi Chen, Ensheng Shi, Xilin Liu, Yuchi Ma, Zibin Zheng
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.01601v1)