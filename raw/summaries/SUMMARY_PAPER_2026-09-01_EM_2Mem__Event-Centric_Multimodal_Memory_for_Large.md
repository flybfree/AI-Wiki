---
title: EM^2Mem: Event-Centric Multimodal Memory for Large Language Models
url: http://arxiv.org/abs/2609.00551v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_01-38-41Z_EM_2Mem_Event_CentricMultimodalMemoryforLargeLangu.md
generated_at: 2026-09-01 22:25
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces EM^2Mem, an event-centric multimodal memory system that binds heterogeneous evidence to event anchors for long-video question answering. It demonstrates that grounding events improves accuracy and reduces inference cost compared with fragment-based baselines.

## Key Takeaways
- EM^2Mem constructs memory cells indexed by events rather than isolated modality fragments, allowing retrieval of aligned multimodal records, temporal context, graph facts, and provenance.
- The framework achieves higher event-level Top‑5 evidence recall (7.0 points) across three long‑video QA benchmarks compared with the strongest baseline.
- Inference latency is reduced 4.67 times and total inference tokens are cut by 63.66%, indicating a more efficient use of language model resources.

## Context
Current multimodal memory approaches treat each modality separately, leading to fragmented evidence that must be reconstructed at query time. This limits performance on tasks requiring cross‑modal temporal alignment in long videos.

## Implications
The event‑centric design offers a scalable solution for real‑world video analytics and LLM applications where precise grounding is essential. Practitioners can adopt EM^2Mem to lower latency, improve recall, and reduce token usage without sacrificing accuracy.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00551v1)
