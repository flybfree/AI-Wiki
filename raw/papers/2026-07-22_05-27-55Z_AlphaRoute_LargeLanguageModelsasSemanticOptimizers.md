---
title: AlphaRoute: Large Language Models as Semantic Optimizers for Multi-Objective Routing
published: 2026-07-22T05:27:55Z
authors: Kabir Murjani, Mishri Bhavsar, Manish I. Patel, Jonti Talukdar
url: http://arxiv.org/abs/2607.19768v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AlphaRoute: Large Language Models as Semantic Optimizers for Multi-Objective Routing

## Abstract
Very Large Scale Integration (VLSI) global routing is an NP-hard combinatorial optimization problem requiring signal net assignment across capacity-constrained 3D grids while minimizing congestion, wirelength, and via transitions. Because traditional heuristics rely on static penalty schedules that fail on complex congestion topologies, we present AlphaRoute: a multi-objective adaptive search framework reformulating rip-up and reroute (R&R) into a dynamic optimization system. We introduce SHAP-based overflow decomposition to isolate per-net congestion, driving targeted subgraph extraction via 3D Dijkstra maze routing and an adaptive PathFinder policy. Crucially, AlphaRoute employs Large Language Models (LLMs) as semantic policy optimizers. Bounded by a deterministic knowledge graph, the LLMs interpret congestion metrics to dynamically adjust penalty parameters. Evaluated on ISPD 2025 benchmarks, AlphaRoute reduces overflow by 98.6% on MEMPOOL. On the constrained ARIANE design, we achieve an overflow of 146,109 (a 29.8x reduction in overflow over the state of the art), yielding a penalized score of S_orig = 0.0538 versus the State-of-the-art (SOTA) 1.780. These results demonstrate that superior algorithmic search geometry can overcome the latency of interpreted Python implementations.

## Metadata
- **Published**: 2026-07-22T05:27:55Z
- **Authors**: Kabir Murjani, Mishri Bhavsar, Manish I. Patel, Jonti Talukdar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.19768v1)