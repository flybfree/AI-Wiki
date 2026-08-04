---
title: RH-RAG: Trustworthy Long-Form Generation for Privacy-Constrained Settings
published: 2026-08-02T15:27:00Z
authors: Raj Shekhar Singh
url: http://arxiv.org/abs/2608.01311v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RH-RAG: Trustworthy Long-Form Generation for Privacy-Constrained Settings

## Abstract
Generating long-form content from extensive internal reports remains challenging for organizations operating under strict privacy and security constraints, where proprietary cloud-based LLM APIs are often not viable. While locally deployed open-weight models offer a privacy-preserving alternative, existing retrieval-augmented generation (RAG) approaches on smaller models frequently lack effective global planning and accumulate factual inconsistencies over long outputs. To address these limitations, we present RH-RAG, a multi-agent framework for secure and trustworthy long form generation using local language models. RH-RAG decomposes generation into three coordinated stages: a Planner Agent that constructs a global document outline from high-level semantic summaries, a Writer Agent that incrementally generates coherent section-wise content using bounded coherence memory, and a Checker Agent that mitigates hallucinations through natural language inference-based factual verification and an attestation-driven revision loop. The framework further employs a dual-level retrieval index that supports efficient planning and fine-grained contextual generation on consumer-grade hardware. Evaluations across literary, financial, and legal domains demonstrate that RH-RAG consistently improves factual grounding, semantic coherence, and document-level alignment compared to standard and hierarchical RAG baselines, while achieving reliability competitive with proprietary cloud-based systems without compromising data privacy.

## Metadata
- **Published**: 2026-08-02T15:27:00Z
- **Authors**: Raj Shekhar Singh
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01311v1)