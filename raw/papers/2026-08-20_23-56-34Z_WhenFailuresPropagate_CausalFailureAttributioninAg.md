---
title: When Failures Propagate: Causal Failure Attribution in Agentic Retrieval-Augmented Generation
published: 2026-08-20T23:56:34Z
authors: Lauren Pothuru
url: http://arxiv.org/abs/2608.20627v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Failures Propagate: Causal Failure Attribution in Agentic Retrieval-Augmented Generation

## Abstract
Agentic retrieval-augmented generation (RAG) interleaves retrieval, reasoning, and answer generation across multiple hops. A retrieval error at hop 1 can surface only as a wrong answer at hop 3, while later retrieval can also repair the trajectory. This paper introduces AgenticRAG-FP, an interventional benchmark for causal failure attribution in agentic RAG. The benchmark injects a certified fault at a specified hop, re-executes the downstream trajectory, and evaluates diagnosers against the known intervention. Its central question is whether a post-hoc trace still identifies the injected hop after the suffix changes. In the completed strict dense Claude Haiku 4.5 sweep on 80 three-hop MuSiQue questions, coverage-based diagnosis is 0.91 at hop 1 and 0.00 at hops 2 and 3 (n=43,36,21 failed trajectories). A smaller content-corruption study changes an answer-bearing or bridge fact in topically intact evidence. At depth 2, where 18 failed cases remain after filtering, coverage-based diagnosis is 0.00 and a frozen-hop counterfactual probe is 0.67 in an exploratory pooled comparison. Depth-3 content estimates are descriptive only because they contain three failed cases. These results make propagation depth an explicit evaluation axis for diagnosing agentic RAG failures while distinguishing broad evidence of post-hoc signal loss from small-sample method comparisons.

## Metadata
- **Published**: 2026-08-20T23:56:34Z
- **Authors**: Lauren Pothuru
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20627v1)