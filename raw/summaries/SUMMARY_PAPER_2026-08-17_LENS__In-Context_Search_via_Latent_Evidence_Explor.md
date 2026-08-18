---
title: LENS: In-Context Search via Latent Evidence Exploration over Dynamic Raw Documents
url: http://arxiv.org/abs/2608.16185v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_07-04-25Z_LENS_In_ContextSearchviaLatentEvidenceExplorationo.md
generated_at: 2026-08-17 21:13
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces LENS, a framework for in‑context search over dynamic raw documents that avoids pre‑materializing evidence. It achieves strong performance with exact match and evidence recall scores while requiring no persistent indexing. The method is query‑ready after corpus changes.

## Key Takeaways
- LENS avoids pre‑materializing evidence by maintaining a query‑conditioned belief over candidate units.
- The framework iteratively selects candidates via lexical, local and exploratory policies updating belief with an LLM relevance oracle within a budget.
- On evaluation it achieves 62.4% exact match and 84.8% evidence recall versus 50.4% for ReAct.

## Context
This work addresses the challenge of dynamic document collections where preprocessing may lag behind query needs, a common bottleneck in retrieval‑augmented LLM systems. By operating index‑free and grounding answers to source regions, it moves toward more flexible and up‑to‑date reasoning pipelines.

## Implications
For practitioners this means they can deploy models that adapt instantly when new files are added without costly reindexing. The approach also improves factual grounding by consistently linking answers to retrieved evidence across queries.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16185v1)
