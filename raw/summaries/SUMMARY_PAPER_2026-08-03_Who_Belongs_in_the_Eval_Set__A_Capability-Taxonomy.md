---
title: Who Belongs in the Eval Set? A Capability-Taxonomy-Driven Pipeline for Curating Regression Eval Sets in Agent-Extensibility Platforms
url: http://arxiv.org/abs/2608.01004v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-02_05-19-25Z_WhoBelongsintheEvalSet_ACapability_Taxonomy_Driven.md
generated_at: 2026-08-03 20:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a capability‑taxonomy driven pipeline that curates regression evaluation sets for agent extensibility platforms, resolving the tension between incoming customer data and fixed platform limits. It generates per‑query decisions to admit, drop, swap, or review based on how queries exercise distinct capability signatures.

## Key Takeaways
- The classifier uses deterministic extraction combined with LLM inference to assign verdicts per query and capability, ensuring systematic mapping of queries to the taxonomy.
- An Invocation Quality rater scores each query’s thoroughness in exercising capabilities, allowing newer queries that share a signature but are higher quality to replace older ones.
- A consolidator applies rule‑based coverage checks against the existing regression set, with a conservative curator only suggesting evictions.

## Context
AI platforms increasingly rely on agent extensibility where each customer contributes unique evaluation data. Existing frameworks treat these sets as static or ignore platform constraints, leading to inefficiencies in resource allocation and evaluation throughput.

## Implications
This approach enables scalable, adaptive regression set maintenance across evolving taxonomies, supporting continuous learning without manual curation overhead. Practitioners can integrate such pipelines into their deployment workflows to maintain high‑quality tests within strict query limits.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01004v1)
