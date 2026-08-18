---
title: Time as Structure: Temporal Dependency Graphs for Verifiable Deadline Computation over Legal Documents
url: http://arxiv.org/abs/2608.15270v1
type: paper-summary
date: 2026-08-17
source_paper: 2026-08-15_15-14-46Z_TimeasStructure_TemporalDependencyGraphsforVerifia.md
generated_at: 2026-08-17 21:37
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a temporal dependency graph model to compute filing deadlines from legal documents, contrasting direct language‑model answers with code‑driven computation. On UK Employment Appeal Tribunal judgments the graph engine matches judge dates and outperforms the best language model in both correctness and consistency. The study also shows that errors arise mainly from extracting which event starts the statutory period.

## Key Takeaways
- The temporal dependency graph captures dated facts and their dependencies, enabling a calendar‑correct deadline engine that reproduces six of seven timeliness rulings on UK EAT judgments.
- Direct language models often produce contradictory verdicts: in 6 out of 21 cases they claim a late claim is timely despite the correct arithmetic being late.
- Error rates improve when deadlines are computed rather than annotated, with a pipeline accuracy of 90.2% versus 61.2% for direct answering.

## Context
Legal AI systems must handle complex statutory timelines that involve triggering events, counting conventions, and suspension windows. Traditional approaches rely on rule‑based parsing or simple arithmetic, which can misinterpret the start date or ignore conciliation periods. This work demonstrates a hybrid extraction‑computation pipeline as a more reliable alternative.

## Implications
For legal practitioners, automated deadline calculators reduce manual errors and speed up case preparation. For AI developers, the study highlights that accurate event identification is crucial; without it, even correct arithmetic leads to wrong outcomes. The findings suggest that future legal LLMs should be paired with structured temporal graphs rather than answering directly.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.15270v1)
