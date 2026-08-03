---
title: MerchantBench: Benchmarking LLM Agents for Long-Term Coherence in E-Commerce Operations
published: 2026-07-31T02:20:24Z
authors: Qiming Shi, Yulong Tao, Linbo Jin, Zhaolu Kang, Yibo Dou, Jiawen Zhu, Tianjun Pan, Shaokang Fu, Chengyu Wang, Siyue Li, Yaping Cheng, Di Weng, Chengfu Huo
url: http://arxiv.org/abs/2607.28956v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MerchantBench: Benchmarking LLM Agents for Long-Term Coherence in E-Commerce Operations

## Abstract
Large language model agents are increasingly evaluated as autonomous tool users, yet most benchmarks focus on bounded tasks with immediate success criteria. Real-world deployments often require Long-Term Coherence, the capacity to preserve purposeful behavior across extended horizons while adapting decisions to accumulated evidence. Evaluating this capacity requires a persistent environment in which actions constrain future choices, feedback arrives at heterogeneous delays, and incoherent behavior produces measurable cumulative effects. Seller-side e-commerce provides a suitable setting for this evaluation through recurrent and interdependent decisions over Product Sourcing, Listing and Pricing Control, Cash-Flow Management, and Mixed-Latency Feedback Adaptation. We introduce MerchantBench, a 365-day order-level simulation grounded in 98,843 real e-commerce product records and equipped with 26 tools for agent interaction. MerchantBench couples promptly observable Upstream Supplier Events with delayed Downstream Order Outcomes, requiring agents to follow individual order lifecycles and revisit earlier decisions. We evaluate eight LLMs under two agent frameworks in 48 runs, each spanning 365 simulated days. Our results reveal a substantial gap between even the latest LLMs and human participants, with the best LLM configuration attaining only 27.3\% of the mean final net assets achieved by human participants.

## Metadata
- **Published**: 2026-07-31T02:20:24Z
- **Authors**: Qiming Shi, Yulong Tao, Linbo Jin, Zhaolu Kang, Yibo Dou, Jiawen Zhu, Tianjun Pan, Shaokang Fu, Chengyu Wang, Siyue Li, Yaping Cheng, Di Weng, Chengfu Huo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28956v1)