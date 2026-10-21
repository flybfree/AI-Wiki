---
title: Memory as Code: Declarative Retrieval over Codified Long-Term Memory
published: 2026-10-20T06:17:51Z
authors: Aoting Zeng, Yuxin Du, Jianwei Wang, Yizhang He, Shan Jiang, Xuemin Lin, Kai Wang
url: http://arxiv.org/abs/2610.27700v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Memory as Code: Declarative Retrieval over Codified Long-Term Memory

## Abstract
In long-term memory systems, memories are constructed from interaction histories and retrieved in response to queries, enhancing the reasoning ability of LLM agents. In complex scenarios, facts are scattered across sessions and their relationships evolve over time, making it difficult for existing memory systems to compose them to adapt to diverse queries. Motivated by the modularity and composability of code, we propose Memory as Code (MaC), a unified memory framework that jointly designs memory construction and retrieval through a shared code abstraction. MaC couples codified construction, which establishes executable memory abstractions, with declarative retrieval, which translates queries into structured retrieval programs. Specifically, codified construction builds a three-layer executable memory structure that progresses from an atomic function layer, through a relational layer, to a modular composition layer. Declarative retrieval recasts retrieval from relevance-based fact selection into declarative query processing over memory. Experiments on LoCoMo and LongMemEval show relative gains of up to 15.91% in overall LLM-judge accuracy over the strongest baseline in each setting, while substantially reducing token consumption, highlighting the effectiveness of memory as code for long-horizon memory tasks.

## Metadata
- **Published**: 2026-10-20T06:17:51Z
- **Authors**: Aoting Zeng, Yuxin Du, Jianwei Wang, Yizhang He, Shan Jiang, Xuemin Lin, Kai Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.27700v1)