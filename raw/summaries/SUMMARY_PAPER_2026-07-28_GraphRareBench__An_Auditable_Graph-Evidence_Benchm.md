---
title: GraphRareBench: An Auditable Graph-Evidence Benchmark for Phenotype-Driven Rare-Disease Diagnosis
url: http://arxiv.org/abs/2607.24878v1
type: paper-summary
date: 2026-07-28
source_paper: 2026-07-27_07-58-29Z_GraphRareBench_AnAuditableGraph_EvidenceBenchmarkf.md
generated_at: 2026-07-28 20:12
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces GraphRareBench, a provenance‑preserving benchmark for phenotype‑driven rare disease diagnosis that includes 2,365 ontology‑derived cases and 18,093 target‑confounder pairs. The study evaluates supervised rankers on a gene‑component‑disjoint test split, achieving MRRs of 0.64 to 0.74 and high accuracy for target‑over‑confounder predictions. It also reports that two large language models, Agents‑A1 and DeepSeek‑V4‑Flash, have comparable performance but differ in evidence coverage.

## Key Takeaways
- The benchmark reveals which plausible alternatives are ranked above the reference disease and shows how model tools access evidence before deciding.
- Full‑pool retrieval, discrimination of hard confounders, and evidence access each capture distinct aspects of diagnostic behavior.
- Despite similar MRRs, the two models differ in target‑evidence coverage by 0.561, highlighting complementary strengths.

## Context
GraphRareBench addresses a gap in AI medical evaluation where many benchmarks only report reference disease rank without exposing alternative candidates or evidence pathways. By preserving provenance and linking evidence to graph‑defined confounders, the benchmark enables transparent assessment of phenotype‑driven diagnostic systems.

## Implications
For researchers, GraphRareBench provides a rigorous framework to compare model behavior beyond simple ranking scores. Practitioners can use it to design more evidence‑aware diagnostic tools that better handle real‑world disease complexity and reduce false positives.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.24878v1)
