---
title: HERO: Human-profile Enhanced Retrieval Optimization Framework for Long-term Agent Memory
published: 2026-08-23T09:19:34Z
authors: Yuanhua Lin, Yile Li, Zhiyuan Zhao, Jing Shang, Jian Sun
url: http://arxiv.org/abs/2608.22310v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HERO: Human-profile Enhanced Retrieval Optimization Framework for Long-term Agent Memory

## Abstract
Long-term memory is crucial for personalized responses and long-horizon agent interactions. Existing methods often rely on LLMs to compress or rewrite dialogue histories and use the transformed memories as retrieval evidence. Despite the progress in organizing fragmented contexts, two major drawbacks persist: (1) information loss from compression, which discards fine-grained but later useful details, and (2) semantic drift from rewriting, which erodes the original tone and situated context. In this work, we propose a novel Human-profile Enhanced Retrieval Optimization framework for long-term agent memory (HERO). Specifically, HERO converts the dialogue history into a traceable heterogeneous memory graph that preserves raw dialogue text as evidence for reasoning, thereby mitigating information loss. For retrieval, HERO extracts initial anchors from the current query and incorporates human profiles via an iterative graph traversal; these anchors and profiles provide guidance signals that adaptively activate the most informative regions of the graph. Experiments on two benchmark datasets show that HERO outperforms strong baselines on both factual and personalized reasoning, while providing more faithful access to raw dialogue evidence.

## Metadata
- **Published**: 2026-08-23T09:19:34Z
- **Authors**: Yuanhua Lin, Yile Li, Zhiyuan Zhao, Jing Shang, Jian Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22310v1)