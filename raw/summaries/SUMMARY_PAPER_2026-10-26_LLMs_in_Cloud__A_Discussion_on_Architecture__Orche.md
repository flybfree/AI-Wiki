---
title: LLMs in Cloud: A Discussion on Architecture, Orchestration, and Inference
url: http://arxiv.org/abs/2610.33475v1
type: paper-summary
date: 2026-10-26
source_paper: 2026-10-24_05-53-48Z_LLMsinCloud_ADiscussiononArchitecture_Orchestratio.md
generated_at: 2026-10-26 21:29
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper presents a comprehensive cross-layer systematic review, guided by the PRISMA 2020 framework, that unifies hardware virtualization, cluster-level scheduling, and runtime inference optimizations for serving Large Language Models in cloud datacenters. The authors synthesize a holistic taxonomy addressing the physical and system bottlenecks introduced by memory-intensive generative workloads, while evaluating resilient cloud-native service architectures and formalizing multi-dimensional trade-offs between throughput, latency, cost, and confidentiality.

## Key Takeaways
- The paper identifies critical physical and system bottlenecks in serving foundation models under stringent Service Level Objectives, including the persistent High Bandwidth Memory wall, the operational asymmetry between compute-bound prefilling and memory-bandwidth-bound decoding, explosive Key-Value cache expansion, prohibitive serverless cold starts, and hardware reliability vulnerabilities. These bottlenecks represent fundamental constraints that existing layer-siloed literature reviews have failed to address in an integrated manner.
- The authors propose a unified taxonomy spanning iteration-level continuous batching, prefill-decoding disaggregation, and hierarchical KV cache offloading as runtime inference optimizations, alongside scale-to-zero serverless paradigms, fault-tolerant checkpointing against silent data corruption, and hardware-enforced Trusted Execution Environments for multi-tenant isolation. This cross-layer approach bridges the gap between low-level accelerator virtualization and cluster orchestration that prior reviews have left unaddressed.
- The paper formalizes Pareto trade-offs governing throughput, latency, monetary cost, and confidentiality, and outlines a forward-looking research roadmap encompassing Compute Express Link memory pooling, in-memory computing, and autonomous multi-agent control planes, explicitly incorporating defining advancements from 2024 to 2026 that earlier surveys overlooked.

## Context
The deployment of foundational LLMs across cloud datacenters represents a paradigm shift from stateless deep learning toward distributed, memory-intensive generative workloads that challenge traditional serving architectures. Prior literature reviews have remained fragmented across hardware, orchestration, and inference layers, leaving practitioners without a unified understanding of how these layers interact under production constraints. This paper fills that gap by providing a systematic, cross-layer synthesis that captures rapid advancements from 2024 through 2026, making it a timely reference for both academic researchers and infrastructure engineers navigating the evolving cloud LLM landscape.

## Implications
For cloud infrastructure practitioners and platform architects, this paper provides actionable guidance on designing resilient, multi-tenant LLM serving systems that balance performance, cost, and security requirements under real-world SLO constraints. The formalized Pareto trade-off framework and forward-looking roadmap toward CXL memory pooling, in-memory computing, and autonomous control planes signal concrete research directions that will shape next-generation cloud LLM infrastructure, informing both hardware procurement decisions and software orchestration strategies for organizations scaling generative AI services.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.33475v1)
