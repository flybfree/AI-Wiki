---
title: Time as Structure: Temporal Dependency Graphs for Verifiable Deadline Computation over Legal Documents
published: 2026-08-15T15:14:46Z
authors: Maryia Zhyrko, Lifeng Han, Suzan Verberne
url: http://arxiv.org/abs/2608.15270v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Time as Structure: Temporal Dependency Graphs for Verifiable Deadline Computation over Legal Documents

## Abstract
Miss a filing deadline by one day and the claim is barred, however strong the case. Computing that deadline is rarely simple: the period runs from a triggering event, is counted by a statutory convention, and may be suspended by a mandatory conciliation window. We ask whether a language model should answer such questions directly, or read the document and leave the arithmetic to code. We extract dated facts and their dependencies into a temporal dependency graph and compute deadlines from it with a calendar-correct engine. On UK Employment Appeal Tribunal judgments the engine reproduces six of seven timeliness rulings, and matches the judges' own dates to the day. The strongest of four language models, asked the same cases, gets the arithmetic right and the answer wrong: in six of twenty-one responses its stated verdict contradicts its own thinking, and every contradiction runs the same way, calling a late claim timely. To test the systems at scale we move the dismissal date across the statutory boundary, generating 427 cases whose answers are computed rather than annotated. On the cases both systems answer, the pipeline is right 90.2% of the time against 61.2% for direct answering. The limit is extraction: on contracts the errors are almost never in the arithmetic, but in choosing which event the period starts from.

## Metadata
- **Published**: 2026-08-15T15:14:46Z
- **Authors**: Maryia Zhyrko, Lifeng Han, Suzan Verberne
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15270v1)