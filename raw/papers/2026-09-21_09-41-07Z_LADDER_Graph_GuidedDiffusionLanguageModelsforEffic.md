---
title: LADDER: Graph-Guided Diffusion Language Models for Efficient Multi-Hop Reasoning
published: 2026-09-21T09:41:07Z
authors: Senlei Zhang, Linhao Luo, Qian-Wen Zhang, Siyu An, Junnan Dong, Shuhao Zhang, Xing Sun
url: http://arxiv.org/abs/2609.24346v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LADDER: Graph-Guided Diffusion Language Models for Efficient Multi-Hop Reasoning

## Abstract
Graph Retrieval-Augmented Generation (GraphRAG) has remarkably enhanced large language models on complex reasoning by leveraging structured entity topologies. However, existing frameworks heavily rely on standard autoregressive language models where the nature of inherent sequential generation severely hinders overall inference efficiency. Inspired by Diffusion Language Models (DLMs) that offer massive parallelism via continuous refine-in-parallel decoding, we aim to accelerate GraphRAG in the discrete space. However, it remains non-trivial for two challenges. First, partially denoised drafts are highly dynamic and uncertain, making dynamic graph grounding non-trivial. Second, raw denoising states are inherently noisy and unstable, making synchronous graph retrieval and multi-hop aggregation computationally prohibitive. To this end, we present LADDER, a novel framework that bridges diffusion language modeling with GraphRAG through graph-guided parallel decoding. Specifically, (i) we propose an event-driven self-clocking retrieval, inspired by our key insight that 88% of target entities emerge early in the partially denoised state, leading final commitment by an average of 5.7-9.6 steps. This mechanism dynamically triggers graph retrieval only when the set of graph-linkable entities expands, yielding an asynchronous self-clocking policy that bypasses learned gates or heuristic thresholds. (ii) An incomplete-query graph propagation module is designed to process the newly emerging entity queries using a specialized graph foundation model, continuously aggregating multi-hop evidence to sharpen parallel predictions and accelerate overall decoding convergence. Extensive experiments on three challenging multi-hop QA benchmarks show that LADDER raises average exact match from 39.6% to 45.2% while achieving a 4.1x latency reduction.

## Metadata
- **Published**: 2026-09-21T09:41:07Z
- **Authors**: Senlei Zhang, Linhao Luo, Qian-Wen Zhang, Siyu An, Junnan Dong, Shuhao Zhang, Xing Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.24346v1)