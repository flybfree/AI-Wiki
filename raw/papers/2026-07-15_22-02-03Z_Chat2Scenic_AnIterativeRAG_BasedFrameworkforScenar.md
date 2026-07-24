---
title: Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving
published: 2026-07-15T22:02:03Z
authors: Yuan Gao, Wenting Miao, Mattia Piccinini, Haoyu Wang, Qunying Song, Johannes Betz
url: http://arxiv.org/abs/2607.14387v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Chat2Scenic: An Iterative RAG-Based Framework for Scenario Generation in Autonomous Driving

## Abstract
Validating autonomous driving systems requires diverse, regulation-compliant test scenarios. In simulation-based testing, scenarios are defined as executable scripts. Yet automatically generating such scripts from regulatory descriptions remains an open challenge, and existing approaches face fundamental trade-offs. Retrieval-assemble methods achieve reasonable compilation rates but lack scalability, whereas retrieval-based full-script generation suffers from low compilation success rates. We present Chat2Scenic, the first iterative retrieval-augmented framework to generate scenario scripts in Domain Specific Language (DSL). Specifically, Chat2Scenic provides a chatbot interface that supports interactive scenario refinement and integrates Retrieval-augmented Generation (RAG) to ground scenario generation in regulatory knowledge and DSL syntax. Furthermore, we propose an open benchmark for scenario generation comprising 123 scenarios from various regulations, including NHTSA and United Nations Vehicle Regulations, as well as other sources. Extensive evaluation with State-of-the-Art (SOTA) Large Language Models (LLMs) demonstrates that Chat2Scenic achieves 76.42% Compilation Success Rate (CSR) and 58.17% Framework Accuracy (FA), outperforming existing methods (Retrieval Assemble with 30.08% CSR, 11.03% FA and Retrieval full script generation with 16.26% CSR, 10.86% FA). To facilitate future research, we release our code as open source at https://github.com/TUM-AVS/chat2scenic.

## Metadata
- **Published**: 2026-07-15T22:02:03Z
- **Authors**: Yuan Gao, Wenting Miao, Mattia Piccinini, Haoyu Wang, Qunying Song, Johannes Betz
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.14387v1)