---
title: Recall What Is Missing: Composing Evidence from Long-Term Agent Memory
published: 2026-10-11T14:18:11Z
authors: Qi Feng, Jicong Fan
url: http://arxiv.org/abs/2610.15642v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Recall What Is Missing: Composing Evidence from Long-Term Agent Memory

## Abstract
Under a limited context budget, a long-term agent must recall not merely memories that are individually relevant, but evidence that is collectively sufficient for the current query. Conventional memory access retrieves, scores, and truncates memories, often spending multiple context slots on redundant facts while leaving complementary evidence behind. We cast the read phase of long-term memory as query-conditioned evidence composition: each memory is valued by what it adds beyond the evidence already selected. We instantiate this operation with MemPursuit, a training-free mechanism that uses the residual of a sparse convex query reconstruction as a representation-space proxy for what the current memory set is missing. By reusing the query and candidate embeddings already available from retrieval, MemPursuit progressively composes nested evidence contexts without invoking a language model or cross-encoder to score each query--memory pair. The effectiveness of our method is verified on 3 popular benchmarks in comparison to strong baselines. In fixed-budget LoCoMo experiments, MemPursuit improves end-to-end accuracy by 7.2 percentage points at Top-10 and 5.5 percentage points at Top-20, with consistent gains across multiple memory frameworks, while achieving a 32.9$\times$ speedup in median reranking latency over fully batched BGE-v2-m3. Our implementation is available at https://github.com/FengQi-HITSZ/MemPursuit.

## Metadata
- **Published**: 2026-10-11T14:18:11Z
- **Authors**: Qi Feng, Jicong Fan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.15642v1)