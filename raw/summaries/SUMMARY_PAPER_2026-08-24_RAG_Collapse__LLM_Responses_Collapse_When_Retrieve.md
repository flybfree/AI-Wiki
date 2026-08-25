---
title: RAG Collapse: LLM Responses Collapse When Retrieved Documents Are Self-Authored
url: http://arxiv.org/abs/2608.22118v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-22_22-06-44Z_RAGCollapse_LLMResponsesCollapseWhenRetrievedDocum.md
generated_at: 2026-08-24 21:29
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates RAG collapse, a phenomenon where large language models retrieve references they themselves authored and experience reduced response diversity that eventually leads to model collapse. Experiments across three model families with over one million API calls show that 79.6% of simulations end in collapse despite attempts to control for reference quality.

## Key Takeaways
- A single self‑authored reference can trigger collapse because the LLM disproportionately cites its own content.
- Collapse occurs even after controlling for reference quality, indicating a systematic bias rather than merely poor references.
- The phenomenon is observed across three model families and over one million API calls.

## Context
This research extends classic model collapse concepts to retrieval‑augmented generation pipelines. It highlights how AI systems that generate their own answers may unintentionally degrade performance through self‑referential feedback loops, a risk not previously considered in RAG literature.

## Implications
Practitioners must design safeguards against self‑citation in RAG workflows, such as limiting self‑generated references or monitoring citation bias. The finding underscores the need for robust evaluation beyond reference quality to detect emergent model collapse.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22118v1)
