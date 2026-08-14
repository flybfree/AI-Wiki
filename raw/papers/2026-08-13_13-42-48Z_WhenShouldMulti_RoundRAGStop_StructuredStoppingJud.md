---
title: When Should Multi-Round RAG Stop? Structured Stopping Judgments and Retrieval Reduction in Search-R1
published: 2026-08-13T13:42:48Z
authors: Weimeng Luo
url: http://arxiv.org/abs/2608.13237v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Should Multi-Round RAG Stop? Structured Stopping Judgments and Retrieval Reduction in Search-R1

## Abstract
Multi-round retrieval-augmented generation (RAG) must decide when to stop searching as evidence accumulates. Because the deployed policy is determined by the first STOP on each trajectory, this is a sequential selection problem rather than an independent state-classification task. We adapt S2G-RAG's structured sufficiency-and-gap judgment to a frozen Search-R1 pipeline and train a Qwen3.5-2B judge on 3,009 states from 900 disjoint HotpotQA questions. Search-R1's reasoner, retriever, corpus, prompt, and search budget remain unchanged, while the judge checkpoint and stopping threshold are selected on grouped validation and frozen before confirmatory evaluation. On the confirmatory test set, the resulting policy reduces retrieval calls by 77 (3.70\%) relative to Native Search-R1, while Official Exact Match decreases by 0.625 percentage points. Thus, the trained S2G-style structured judge reduces retrieval while broadly preserving answer accuracy. The result does not imply unchanged or improved accuracy, safe stopping, or lower total inference cost.

## Metadata
- **Published**: 2026-08-13T13:42:48Z
- **Authors**: Weimeng Luo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.13237v1)