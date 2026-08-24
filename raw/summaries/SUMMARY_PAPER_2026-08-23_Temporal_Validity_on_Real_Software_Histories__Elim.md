---
title: Temporal Validity on Real Software Histories: Eliminating Stale-Fact Errors in Code-Assistant Memory over GitHub Fixes
url: http://arxiv.org/abs/2608.20685v1
type: paper-summary
date: 2026-08-23
source_paper: 2026-08-21_02-48-36Z_TemporalValidityonRealSoftwareHistories_Eliminatin.md
generated_at: 2026-08-23 22:02
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper addresses the problem of stale‑fact errors in retrieval‑augmented generation when models answer questions about real software histories that have been updated on GitHub. By extracting clean atomic state transitions from 130 fixes, it demonstrates that a deterministic supersession memory can eliminate the failure to serve the current value, achieving higher accuracy than standard RAG approaches.

## Key Takeaways
- MemStrata reaches 0.91 answer accuracy on real fix data, while vanilla RAG performs only 0.57‑0.59, showing that a dedicated supersession memory can dramatically improve factual correctness.  
- The model serves the superseded value in about 36‑38% of cases under standard retrieval, and this rate drops to near zero when MemStrata is used, indicating that deterministic tracking resolves the stale‑fact issue.  
- Retrieval latency for MemStrata is only ~2.1 seconds compared with ~18 seconds for a reranker, highlighting both accuracy gains and efficiency benefits.

## Context
Retrieval‑augmented generation remains a dominant approach for grounding language models in external data, yet it lacks temporal awareness, leading to outdated answers when software evolves. This work shows that integrating a deterministic supersession memory can mitigate this limitation on real code histories, advancing the reliability of AI tools used in software engineering.

## Implications
Developers and engineers can rely more confidently on AI assistants for code‑related queries, reducing the risk of deploying buggy fixes caused by stale information. The approach also offers a scalable mechanism that can be embedded into existing RAG pipelines without sacrificing performance, supporting safer automation in CI/CD workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20685v1)
