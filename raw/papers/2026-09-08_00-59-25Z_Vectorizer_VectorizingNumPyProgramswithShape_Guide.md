---
title: Vectorizer: Vectorizing NumPy Programs with Shape-Guided Rewrite
published: 2026-09-08T00:59:25Z
authors: Jingqian Liu, Xiaoyu Liu, Yuepeng Wang
url: http://arxiv.org/abs/2609.08088v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Vectorizer: Vectorizing NumPy Programs with Shape-Guided Rewrite

## Abstract
NumPy is a widely used Python library for numerical scientific computing, known for its declarative APIs and its optimized implementations. However, writing efficient NumPy programs, which often entails using vectorized array operations instead of explicit Python loops, may not be straightforward. This can be difficult for programmers who are accustomed to imperative array traversal, especially when vectorized API invocations require careful reasoning about shapes, broadcasting, and advanced indexing. This paper presents a rewrite-based approach for vectorizing Numpy programs with explicit loops over array data. Our approach vectorizes loops from the inside out, using array shapes and dataflow analysis to guide a source-to-source transformation that replaces loop bodies with vectorized statements. Following a set of rewrite rules that are correct by construction, our approach is consistently fast. We have implemented the approach as a tool called Vectorizer and evaluated it on 150 benchmarks collected from prior work and Stack Overflow. The evaluation shows that Vectorizer vectorizes 142 of the 150 benchmarks directly and 2 more after minor changes to the original benchmarks, with only 0.53 seconds on average to rewrite each one. The resulting programs are, on average, 74.83x faster than the original loop-based implementations.

## Metadata
- **Published**: 2026-09-08T00:59:25Z
- **Authors**: Jingqian Liu, Xiaoyu Liu, Yuepeng Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.08088v1)