---
title: KAP: Bridging the Knowledge Selection-Runtime Consumption Gap in LLM Systems
url: http://arxiv.org/abs/2607.24260v1
type: paper-summary
date: 2026-07-27
source_paper: 2026-07-27_10-51-38Z_KAP_BridgingtheKnowledgeSelection_RuntimeConsumpti.md
generated_at: 2026-07-27 21:24
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces Knowledge Access Planning (KAP) to address the KSRC gap between knowledge selection and runtime consumption in LLM serving. It demonstrates that structured priors can be compiled into a plan that drastically reduces KV access while preserving answer quality.

## Key Takeaways
- The KSRC gap causes dense full‑prompt KV consumption, increasing latency and throughput loss even when only part of the context is needed.
- KAP creates a runtime access plan that decouples physical KV usage from prompt length, enabling selective knowledge retrieval.
- Experiments show proposal‑time KV access drops to 5.5% of source state at 128K context while maintaining quality.

## Context
LLM serving struggles with long contexts because memory and compute scale linearly with token count, making dense consumption inefficient. This work offers a method to separate these costs from the logical prompt structure.

## Implications
For practitioners, KAP enables more efficient deployment of knowledge‑rich models without redesigning hardware or training pipelines, opening new possibilities for scalable long‑context applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24260v1)
