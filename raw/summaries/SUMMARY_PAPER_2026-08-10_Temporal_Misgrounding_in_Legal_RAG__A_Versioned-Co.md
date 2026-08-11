---
title: Temporal Misgrounding in Legal RAG: A Versioned-Corpus Benchmark for French Tax Law
url: http://arxiv.org/abs/2608.09393v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_10-20-13Z_TemporalMisgroundinginLegalRAG_AVersioned_CorpusBe.md
generated_at: 2026-08-10 22:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces FiscalQA Pro, a benchmark for French tax law that highlights temporal misgrounding in legal retrieval. It demonstrates that standard RAG systems retrieve outdated or future versions of articles with high confidence, leading to incorrect answers. The study shows that even advanced models achieve only 3% mean strict accuracy on versioned questions.

## Key Takeaways
- Legal question answering is a temporally-indexed problem and static corpora ignore version changes, causing systematic retrieval errors.
- All evaluated models failed to retrieve the date-applicable article closed-book, with only one exception due to missing gold values.
- Retrieval over a multi-version index reaches 98.3% mean strict accuracy without an oracle, indicating the bottleneck is in first-stage recall.

## Context
Legal RAG systems assume a fixed legal text, but real-world law evolves annually. This work underscores that ignoring temporal dynamics degrades performance and can produce legally inaccurate answers. The release of a version-aware dataset provides a resource for future research on dynamic knowledge retrieval.

## Implications
Practitioners must design pipelines that track article versions and apply temporal filters to ensure citations are current. Ignoring this leads to misinformation in automated legal advice, eroding trust in AI systems. The benchmark encourages industry adoption of versioned indexing strategies across legal domains.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09393v1)
