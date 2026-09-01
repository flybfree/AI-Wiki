---
title: Review Before Trust: Source-Grounded Integrity Gates for AI-Assisted Personal Health Records
published: 2026-08-30T18:51:43Z
authors: Nora Girda, Adrian Groza
url: http://arxiv.org/abs/2608.29965v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Review Before Trust: Source-Grounded Integrity Gates for AI-Assisted Personal Health Records

## Abstract
Large language models can convert medical documents into structured data, but plausible output may still be unsupported by the source. Persisting such output in a longitudinal health record, a record that accumulates patient information over time, therefore creates an integrity risk: unverified data may influence later summaries, trends, or preventive-care computations. We introduce an evidence-gated trust-promotion model that keeps generated data provisional until a deterministic monitor verifies it against the source document. The monitor admits a candidate for a specified downstream use only when the source contains a unique supporting quotation, the relevant fields occur within the same laboratory row, and the required provenance is preserved. The generator cannot approve its own output, missing or ambiguous evidence causes refusal, and refused candidates remain available for human review rather than being silently discarded. We implement the model in Medical DataCloud, a personal health-record application, and evaluate it through automated tests and a replay of saved extraction outputs. All 22 conformance and mutation tests pass. The replay covers nine historical laboratory PDF reports containing 102 manually labelled rows. The reports produce 97 numeric candidates: schema validation accepts all 97, an earlier packet-level evidence check accepts 94, and the hardened quotation- and row-level policy admits 72 while retaining 25 for review. The study evaluates system integrity rather than clinical correctness or clinical safety. The results demonstrate the technical feasibility of an enforceable boundary that prevents generated claims from authorizing their own reuse in a longitudinal health record.

## Metadata
- **Published**: 2026-08-30T18:51:43Z
- **Authors**: Nora Girda, Adrian Groza
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29965v1)