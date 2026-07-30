---
title: Which RAG Paradigm Wins at Scale? A Scaling Study of Retrieval-Augmented Generation Paradigms
published: 2026-07-29T05:46:11Z
authors: Pengyu Wang, Benfeng Xu, Shaohan Wang, Xin Zeng, Huarui Wu, Lei Zhang, Licheng Zhang
url: http://arxiv.org/abs/2607.26497v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Which RAG Paradigm Wins at Scale? A Scaling Study of Retrieval-Augmented Generation Paradigms

## Abstract
Retrieval-augmented generation (RAG) methods range from lexical and dense retrieval to graph-based indexing and agentic search. They are usually evaluated on different benchmarks at one corpus size, leaving their accuracy-cost scaling unclear. To bridge this gap, we present a controlled corpus-scaling study of these four paradigms. A ladder of 28 strictly nested tiers grows from roughly 1,000 to 512,000 documents while questions and a fixed bedrock of relevant and adversarial documents remain unchanged. Under one reader and judging protocol, we measure official accuracy, construction and query tokens, and latency. Our experimental results show that BM25 scales best in this controlled setting: it defines the low-cost end of the Pareto frontier at every measured tier and leads accuracy from mid-scale onward, without LLM-based construction. The File-System Agent matches or slightly exceeds BM25 at the smallest tiers but uses 39 times more query tokens per answer at the bedrock and falls nearly 20 points behind at full scale. A matched retrieval swap reverses this failure: Agent+BM25 scores 69.4 at full scale, versus 36.9 for raw-file agency and 54.8 for native BM25 on the same 150 questions. Graph-based RAG hits a construction wall: its heaviest builders use up to 24.6 generative LLM tokens per indexed corpus token yet stop within the first 2% of the full corpus, while scalable variants remain less accurate than BM25 at shared tiers.

## Metadata
- **Published**: 2026-07-29T05:46:11Z
- **Authors**: Pengyu Wang, Benfeng Xu, Shaohan Wang, Xin Zeng, Huarui Wu, Lei Zhang, Licheng Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26497v1)