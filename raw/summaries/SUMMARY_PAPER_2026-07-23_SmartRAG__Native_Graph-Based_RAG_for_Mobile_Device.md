---
title: SmartRAG: Native Graph-Based RAG for Mobile Device
url: http://arxiv.org/abs/2607.14661v2
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-16_07-28-31Z_SmartRAG_NativeGraph_BasedRAGforMobileDevice.md
generated_at: 2026-07-23 23:18
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SmartRAG, a mobile-friendly RAG system that splits intelligence into Perception, Memory, Focus, and Thinking modules and uses EvoNER for continual entity learning. It stores knowledge in MRGraph and retrieves via hybrid pipeline while limiting LLM inference to high-value tasks.

## Key Takeaways
- SmartRAG deploys a 1.7B quantized LLM on commodity smartphones achieving performance comparable to larger models, demonstrating that model size is not the only factor for mobile efficiency.
- The continual learning EvoNER expands entity labels without retraining the backbone, enabling offline adaptation to unseen entities.
- MRGraph’s three‑layer provenance graph enables fast retrieval through combined traversal, lexical and semantic search.

## Context
Mobile AI assistants must balance privacy, latency, and hardware constraints, making full large models impractical. This work shows that modular design and incremental knowledge graphs can meet these demands while preserving reasoning quality.

## Implications
The approach offers a blueprint for edge‑deployed RAG systems that can scale beyond cloud resources, encouraging developers to adopt lightweight yet powerful on‑device architectures for personal assistants.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.14661v2)
