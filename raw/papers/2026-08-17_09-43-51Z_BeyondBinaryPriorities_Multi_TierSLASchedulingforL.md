---
title: Beyond Binary Priorities: Multi-Tier SLA Scheduling for Large Language Model Serving
published: 2026-08-17T09:43:51Z
authors: Anders Vestrum, Arya Raeesi, Hanna Roed
url: http://arxiv.org/abs/2608.16336v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Binary Priorities: Multi-Tier SLA Scheduling for Large Language Model Serving

## Abstract
Modern LLM serving deployments must simultaneously satisfy heterogeneous service-level objectives (SLOs) across a diverse population of user tiers, ranging from latency-critical API calls to background batch processing. Llumnix introduced a dynamic, migration-capable multi-instance scheduler for LLM inference that achieves load balancing, defragmentation, prioritization, and auto-scaling through a unified "freeness" metric. However, Llumnix's priority model is restricted to two levels (high and normal), an abstraction too coarse to express the richer SLA classes common in production deployments. In this work, we extend Llumnix's priority model to support an arbitrary number of tiers and evaluate the effects of this extension under three realistic priority distributions (uniform, Gaussian, enterprise) using Vidur, a high-fidelity LLM inference simulator. We implement per-tier headroom with exponential decay, tier-aware dispatch ordering, and the full Llumnix migration pipeline inside Vidur's hierarchical scheduling framework. We compare our extended scheduler against INFaaS (global routing baseline), vLLM, Orca, and Sarathi-Serve (per-replica baselines), sweeping priority levels from 1 to 10. Our experiments demonstrate that four priority tiers yields the best cost-effectiveness tradeoff, achieving prefill mean speedups of up to 8.3x and end-to-end P99 speedups of up to 3.1x over INFaaS with cost-per-latency improvements of 46 to 68%, while preserving strong SLO differentiation across tiers. We further show that the system sustains these gains at 10 priority levels without tail latency collapse, with overhead concentrated in the prefill phase.

## Metadata
- **Published**: 2026-08-17T09:43:51Z
- **Authors**: Anders Vestrum, Arya Raeesi, Hanna Roed
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16336v1)