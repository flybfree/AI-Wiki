---
title: Enrich-Retrieve-Rank: Scaling Capability Discovery Beyond In-Context Routing
url: http://arxiv.org/abs/2608.22695v1
type: paper-summary
date: 2026-08-24
source_paper: 2026-08-24_01-21-05Z_Enrich_Retrieve_Rank_ScalingCapabilityDiscoveryBey.md
generated_at: 2026-08-24 21:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper proposes a new capability discovery pipeline that separates offline enrichment of sparse metadata into searchable profiles from an online retrieve‑then‑rank process. Experiments show that as the number of registered capabilities grows from 10 to 7278, in‑context routing accuracy drops sharply while retrieve‑then‑rank degrades more gently. The pipeline outperforms two full‑in‑context baselines by six point five percentage points on Match@1 and reduces cost by seventy times.

## Key Takeaways
- In‑context routing’s top‑one accuracy collapses from 0.85 to 0.12 when scaling to thousands of capabilities, indicating severe performance loss.
- Retrieve‑then‑rank maintains higher accuracy (0.39) because its reranker often ranks the correct capability first after retrieval finds it.
- The pipeline cuts cost by a factor of seventy compared with Full‑Ctx while still delivering better accuracy.

## Context
Current agent ecosystems rely on in‑context routing, which becomes inefficient as registries expand and metadata is sparse. This work introduces an offline enrichment step to convert that metadata into searchable profiles, addressing the scalability bottleneck.

## Implications
The approach enables large‑scale multi‑agent platforms to discover capabilities efficiently without overwhelming LLMs with full registry prompts. Practitioners can adopt this pipeline to improve accuracy and reduce computational expense in real‑world deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.22695v1)
