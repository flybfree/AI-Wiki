---
title: What the Reranker Sees: Multi-Aspect Page Annotation for Long-Document Multimodal Question Answering
published: 2026-08-14T19:29:42Z
authors: Guanchen Wu, Jiayuan Ding, Subhabrata Mukherjee, Carl Yang
url: http://arxiv.org/abs/2608.14841v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What the Reranker Sees: Multi-Aspect Page Annotation for Long-Document Multimodal Question Answering

## Abstract
Long-document visual question answering (VQA) over documents of tens to hundreds of pages mixing text, tables, charts, and figures typically follows retrieve-then-read pipelines. In our setting, the bottleneck shifts from retrieval recall to reranker-side evidence selection: on MMLongBench-Doc, BGE-M3 reaches Recall@20 = 0.86 but only F1@5 = 0.254, and even the visual retriever ColPali reaches only F1@5 = 0.332; a text-only rerank LLM seeing only raw snippets misses table, chart, and layout evidence even when the upstream retriever encoded images. We propose Trident, with two complementary components: Trident-R, a retriever-agnostic LLM reranker that converts each candidate into an LLM-readable semantic record, including a visual caption, section path, entity tags, multi-axis concept hits, and a text snippet, then performs a single adaptive-K rerank call; and Trident-S, a generation-side module that prompts the VLM under topical, entity, and structural lenses before synthesis. On two long-document datasets, the annotation+rerank protocol substantially improves retrieval F1 across five heterogeneous pools, with every reranked pool exceeding the strongest adaptive-K baseline PageIndex. An LLM rerank without the annotation barely changes first-hit ranking, indicating the lift comes from the structured annotation. Trident-S targets open-ended synthesis questions by design, adding up to 6.6 points in generation accuracy on these questions. The best Trident configuration is the strongest downstream QA pipeline in our evaluation, with rankings consistent across two LLM judges (kappa = 0.913).

## Metadata
- **Published**: 2026-08-14T19:29:42Z
- **Authors**: Guanchen Wu, Jiayuan Ding, Subhabrata Mukherjee, Carl Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.14841v1)