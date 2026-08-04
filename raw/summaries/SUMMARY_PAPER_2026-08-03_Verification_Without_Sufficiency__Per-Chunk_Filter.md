---
title: Verification Without Sufficiency: Per-Chunk Filtering Fails on Multi-Hop RAG, and Decomposition Repairs It
url: http://arxiv.org/abs/2608.00585v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-01_10-52-56Z_VerificationWithoutSufficiency_Per_ChunkFilteringF.md
generated_at: 2026-08-03 21:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why per‑chunk verification fails for multi‑hop retrieval‑augmented generation and proposes a decomposition‑based repair that conditions verification on sub‑questions. It demonstrates that standard entailment scoring yields low performance, while conditioning on decomposed hops restores high scores across multiple datasets.

## Key Takeaways
- Per‑chunk filtering assumes each retrieved chunk is sufficient for the answer, which breaks down when answers require linking information from several chunks.
- Entailment scores drop dramatically (0.643 AUC) compared to single‑hop SQuAD (0.951), showing that simple gating harms retrieval quality.
- Conditioning verification on a decomposed sub‑question lifts scores to 0.840 with a lift of +0.355, outperforming the original question’s baseline.

## Context
Multi‑hop QA systems rely on aggregating information across many retrieved paragraphs, yet current verification pipelines treat each chunk independently, ignoring the logical dependencies between hops. This mismatch leads to unnecessary discarding of useful evidence and degraded generation quality.

## Implications
Practitioners must redesign verification to respect hierarchical reasoning rather than applying flat filters, which will improve retrieval relevance and reduce hallucinations in large language models. The approach also offers a template for integrating decomposition into iterative retrieval pipelines without sacrificing performance.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.00585v1)
