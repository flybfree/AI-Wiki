---
title: Coverage Is Not Containment: A Fundamental Limit of Admission-Time Defenses Against Coordinated Poisoning of Vector Retrieval
url: http://arxiv.org/abs/2608.16044v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-17_03-18-51Z_CoverageIsNotContainment_AFundamentalLimitofAdmiss.md
generated_at: 2026-08-17 22:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates why ingestion‑time defenses fail against coordinated poisoning of vector retrieval in RAG systems. It demonstrates that a small set of individually benign documents can dominate the top‑k passages for a target query, causing the generator to output the attacker’s claim with high frequency. Moreover, any classifier trained only on document and query statistics cannot reliably distinguish these attacks from legitimate niche uploads.

## Key Takeaways
- Ingestion‑time filters cannot stop a coordinated poisoning attack because the injected documents form a geometrically identical cone to normal niche uploads, making any classifier based only on document and query statistics fail at near chance performance.
- The attack succeeds by surrounding a single target query with a small set of unremarkable documents that together capture the top‑k passages in retrieval, causing the generator to emit the attacker’s claim in 88 % of cases.
- A retrieval‑time detector that observes the query’s demand can catch all attacks at the same low false‑positive rate, proving that coverage is not containment.

## Context
RAG systems rely on trusted retrieval to ground generation, but any vulnerability in document ingestion can be exploited by adversaries. This work demonstrates a fundamental limitation of admission‑time defenses against coordinated poisoning attacks.

## Implications
For practitioners, this means robust security must look beyond static filters and incorporate real‑time query analysis. The paper urges a shift toward defense mechanisms that monitor the intent behind retrieval rather than only the documents themselves.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.16044v1)
