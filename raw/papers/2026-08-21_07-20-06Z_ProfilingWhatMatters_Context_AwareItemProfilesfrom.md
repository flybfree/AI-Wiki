---
title: Profiling What Matters: Context-Aware Item Profiles from Large-Scale Metadata for LLM Recommenders
published: 2026-08-21T07:20:06Z
authors: Dojun Hwang, Seunghan Lee, Cheonyoung Park, Sara Yu, SeongKu Kang
url: http://arxiv.org/abs/2608.20801v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Profiling What Matters: Context-Aware Item Profiles from Large-Scale Metadata for LLM Recommenders

## Abstract
While Large Language Models (LLMs) have significantly advanced reranking in recommendation, effectively leveraging item-side information remains challenging. Real-world items are described by vast, heterogeneous, and unstructured metadata, where decision-relevant signals are often implicit, noisy, or buried in long descriptions. Moreover, feature salience is highly context-dependent, varying not only across items but also across users. Existing methods often rely on item titles, fixed attributes, or static item summaries, which limit personalized and fine-grained item understanding. To bridge this gap, we propose CAIRO, a user context-aware item profiling framework for LLM-based reranking. CAIRO first structures raw metadata and reviews into objective features and subjective traits, and employs a lightweight profiler to select the most relevant information for each user-item pair with limited serving-time overhead. The resulting profiles are concise and context-specific, providing relevant item-side evidence for the LLM's ranking decision. Experiments show that CAIRO consistently improves LLM-based reranking, highlighting the importance of item profiling that effectively exploits vast item-side information.

## Metadata
- **Published**: 2026-08-21T07:20:06Z
- **Authors**: Dojun Hwang, Seunghan Lee, Cheonyoung Park, Sara Yu, SeongKu Kang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20801v1)