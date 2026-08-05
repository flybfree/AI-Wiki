---
title: DocTrace: Towards Traceable Long Document VQA via Hierarchical Evidence Graph Reasoning
url: http://arxiv.org/abs/2608.03292v1
type: paper-summary
date: 2026-08-05
source_paper: 2026-08-04_08-04-59Z_DocTrace_TowardsTraceableLongDocumentVQAviaHierarc.md
generated_at: 2026-08-05 01:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces DocTrace, a hierarchical framework for traceable long document visual question answering that treats evidence localization and reasoning as explicit graph operations. The authors report substantial gains over existing models on three benchmark datasets, achieving 14.4, 11.3, and 11.7 point improvements relative to the Qwen3-VL-8B-Instruct baseline.

## Key Takeaways
- DocTrace casts LongDocVQA as an evidence graph reasoning problem rather than implicit prediction, enabling explicit provenance tracking of each piece of evidence used in a response.
- The two‑stage training combines joint supervised fine‑tuning to initialize localization and graph reasoning with task‑specific group relative policy optimization that refines these abilities.
- Experimental results show DocTrace consistently outperforms both open‑source baselines and proprietary MLLMs, demonstrating higher accuracy and fully traceable evidence graphs.

## Context
Long document understanding remains a challenge for multimodal large language models due to the need to integrate heterogeneous elements across pages. Current systems often lack mechanisms to verify how evidence is assembled, limiting transparency and reliability in downstream applications.

## Implications
For researchers, DocTrace provides a template for building explainable reasoning pipelines that can be adapted to other long‑form tasks such as document summarization or legal analysis. Practitioners can leverage its traceability feature to meet regulatory requirements for auditability in enterprise AI systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.03292v1)
