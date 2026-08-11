---
title: Keep It Simple: Multi-Key Episodic Memory Retrieval for Ultra-Long Video Understanding
published: 2026-08-07T18:00:02Z
authors: Yeeun Choi, Youngbeom Yoo, Joon-Young Lee, Hyolim Kang, Seon Joo Kim
url: http://arxiv.org/abs/2608.07663v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Keep It Simple: Multi-Key Episodic Memory Retrieval for Ultra-Long Video Understanding

## Abstract
When videos extend from hours to days, directly processing them end-to-end becomes impractical for current Multi-modal Large Language Models (MLLMs). This ultra-long setting necessitates a two-stage paradigm: query-agnostic memory construction followed by retrieval-based inference. Prior work invests in complex memory construction to pre-model high-level relations in videos, despite not knowing the downstream query at build time. We instead prioritize high-recall retrievability during memory building, and defer query-specific, high-level relation composition to inference time. To this end, we propose MERIT(Multi-key Episodic Retrieval with Inference-time Temporal expansion), a simple yet effective agentic framework for ultra-long video understanding. First, we formulate an episodic multi-key representation that enables precise retrieval of fine-grained memories through a simple key-matching mechanism. Second, we introduce a neighbor filtering mechanism to capture broader semantic context without the massive computational overhead of global memory construction. This is achieved by expanding the temporal scope exclusively around the retrieved segments at inference time. By leveraging simple key-matching with this on-demand temporal expansion, MERIT achieves state-of-the-art performance across three long-video benchmarks: EgoLifeQA, LVBench, and Video-MME (Long).

## Metadata
- **Published**: 2026-08-07T18:00:02Z
- **Authors**: Yeeun Choi, Youngbeom Yoo, Joon-Young Lee, Hyolim Kang, Seon Joo Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.07663v1)