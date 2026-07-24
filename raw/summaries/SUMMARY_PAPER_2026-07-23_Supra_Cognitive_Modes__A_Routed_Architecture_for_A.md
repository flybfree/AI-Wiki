---
title: Supra Cognitive Modes: A Routed Architecture for Agent Memory
url: http://arxiv.org/abs/2607.19096v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-21_13-37-17Z_SupraCognitiveModes_ARoutedArchitectureforAgentMem.md
generated_at: 2026-07-23 23:01
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Supra Cognitive Modes (SCM), a routing architecture that assigns query types to retrieval and synthesis tasks over a shared memory substrate. It reports benchmark results showing improved performance compared with baselines, particularly in long-term conversational memory tasks.

## Key Takeaways
- The fused lexical‑dense lookup combined with graph or iterative multi‑hop handling enables flexible query dispatch based on per‑query modes.
- Benchmark scores reach 84.87 % on LoCoMo factoid categories and 61.49 % on MemoryAgentBench, indicating substantial gains from routing.
- The shared substrate stores multi‑granular embeddings, triples, and metadata, allowing asynchronous enrichments to support long‑form synthesis.

## Context
Current AI systems struggle to unify short‑term retrieval with deep reasoning over extensive histories. Routing architectures aim to allocate computational resources efficiently without sacrificing memory fidelity. This work exemplifies a step toward modular yet unified agent memory designs.

## Implications
Practitioners can adopt SCM’s per‑query mode selection to boost factual accuracy and reduce abstention errors in conversational agents. The design also offers diagnostic pathways for failure analysis, supporting more robust deployment of long‑term memory systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.19096v1)
