---
title: KNOWPLAN: Knowledge-Driven AI Agents for Smart Degree Pathway Planning
url: http://arxiv.org/abs/2608.06530v1
type: paper-summary
date: 2026-08-09
source_paper: 2026-08-06_19-24-01Z_KNOWPLAN_Knowledge_DrivenAIAgentsforSmartDegreePat.md
generated_at: 2026-08-09 22:08
model: nvidia/nemotron-3-nano-4b
---

## Summary
KnowPlan introduces a knowledge‑driven framework for designing AI agents that plan university degree pathways from unstructured institutional sources. The system separates extraction and optimization, achieving high recall and feasibility while using far fewer source accesses than exhaustive crawlers.

## Key Takeaways
- CatalogBrowse extracts curriculum facts by scoring actions on expected marginal gain per unit of access, producing a closure certificate over index, schema, provenance, and reference completeness rather than relying on reward thresholds.  
- DegreeMap builds a typed requirement hypergraph from the extracted JSON documents and solves a lexicographic optimization problem with CP‑SAT to maximize personalized utility while maintaining hard feasibility.  
- The full pipeline attains 96.2% inventory recall, 88.7% masked‑source recovery at 47% less source access than an exhaustive crawler, and certifies 99.5% of requests with a utility gap of only 0.015 to the gold graph.

## Context
This work advances AI planning by treating data extraction as a distinct, verifiable stage rather than assuming seamless integration, highlighting the need for robust interface metrics in knowledge‑intensive pipelines. It aligns with broader efforts to make large‑scale curriculum crawling more efficient and reliable.

## Implications
For universities seeking scalable degree advising tools, KnowPlan offers a certifiable, low‑cost approach that reduces manual effort and improves personalization. Practitioners can adopt the extraction‑first boundary to build trustworthy AI agents that respect source constraints while delivering optimal pathways.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.06530v1)
