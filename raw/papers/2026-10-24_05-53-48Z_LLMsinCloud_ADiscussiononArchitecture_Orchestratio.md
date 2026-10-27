---
title: LLMs in Cloud: A Discussion on Architecture, Orchestration, and Inference
published: 2026-10-24T05:53:48Z
authors: Jannatun Noor, Athar Noor Mohammad Rafee, Md. Sadman Haque, Sreezon Das Gupta, Atiar Osman, Md. Abu Obaida Zishan
url: http://arxiv.org/abs/2610.33475v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLMs in Cloud: A Discussion on Architecture, Orchestration, and Inference

## Abstract
The widespread deployment of foundational Large Language Models (LLM) across cloud datacenters marks a fundamental paradigm shift from stateless deep learning toward distributed, memory-intensive generative workloads. However, serving massive foundation models under stringent Service Level Objectives (SLO) exposes critical physical and system bottlenecks. These challenges include the persistent High Bandwidth Memory (HBM) wall, operational asymmetry between compute-bound prefilling and memory-bandwidth-bound decoding, explosive Key-Value (KV) cache expansion, prohibitive serverless cold starts, and hardware reliability vulnerabilities. Existing literature reviews remain layer-siloed, decoupling low-level accelerator virtualization from cluster orchestration and runtime inference, while largely overlooking defining advancements from 2024 to 2026. To address these limitations, this study presents a comprehensive, cross-layer systematic review guided by the Preferred Reporting Items for Systematic Reviews and Meta-Analyses (PRISMA) 2020 framework. We synthesize a holistic taxonomy unifying hardware virtualization, cluster-level scheduling, and runtime inference optimizations, including iteration-level continuous batching, prefill-decoding disaggregation, and hierarchical KV cache offloading. Furthermore, we evaluate resilient cloud-native service architectures, examining scale-to-zero serverless paradigms, fault-tolerant checkpointing against silent data corruption, and hardware-enforced Trusted Execution Environments (TEEs) for multi-tenant isolation. Finally, we formalize the multi-dimensional Pareto trade-offs governing throughput, latency, monetary cost, and confidentiality, outlining a forward-looking research roadmap spanning Compute Express Link (CXL) memory pooling, in-memory computing, and autonomous multi-agent control planes to guide future cloud LLM infrastructure.

## Metadata
- **Published**: 2026-10-24T05:53:48Z
- **Authors**: Jannatun Noor, Athar Noor Mohammad Rafee, Md. Sadman Haque, Sreezon Das Gupta, Atiar Osman, Md. Abu Obaida Zishan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.33475v1)