---
title: Keep It Simple: Multi-Key Episodic Memory Retrieval for Ultra-Long Video Understanding
url: http://arxiv.org/abs/2608.07663v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-07_18-00-02Z_KeepItSimple_Multi_KeyEpisodicMemoryRetrievalforUl.md
generated_at: 2026-08-10 22:17
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces MERIT, a simple agentic framework for ultra-long video understanding that separates memory construction from retrieval. By building an episodic multi‑key representation and using on-demand temporal expansion at inference time, MERIT achieves state-of-the-art performance on EgoLifeQA, LVBench, and Video-MME.

## Key Takeaways
- The episodic multi‑key representation enables precise retrieval of fine‑grained memories through a straightforward key‑matching mechanism.
- A neighbor filtering mechanism captures broader semantic context without the cost of global memory construction by expanding temporal scope only around retrieved segments at inference time.
- MERIT’s two‑stage approach—query‑agnostic memory building followed by query‑specific relation composition—delivers state‑of‑the‑art results across three long‑video benchmarks.

## Context
Current multi‑modal large language models struggle with videos longer than a few minutes because end‑to‑end processing is computationally infeasible. This work addresses the ultra‑long video understanding problem by decoupling memory construction from retrieval, allowing simpler yet effective architectures to scale to hours or days of footage.

## Implications
The separation of memory building and retrieval simplifies model design and reduces resource demands, making it feasible to deploy ultra‑long video analysis in real‑world applications such as surveillance monitoring and long‑form content summarization. Practitioners can adopt this two‑stage paradigm to improve recall and efficiency without sacrificing performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.07663v1)
