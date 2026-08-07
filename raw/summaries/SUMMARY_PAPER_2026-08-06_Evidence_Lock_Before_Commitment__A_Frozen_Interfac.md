---
title: Evidence Lock Before Commitment: A Frozen Interface Degrades LLM-as-Judge Evaluation
url: http://arxiv.org/abs/2608.05353v1
type: paper-summary
date: 2026-08-06
source_paper: 2026-08-05_19-23-56Z_EvidenceLockBeforeCommitment_AFrozenInterfaceDegra.md
generated_at: 2026-08-06 21:34
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how language model judges extract evidence and make decisions, comparing several evaluation protocols across large datasets. It finds that locking evidence between calls reduces agreement with human preferences but increases inconsistency in answer ordering relative to structured one‑call judging.

## Key Takeaways
- Evidence locking reduces agreement with released human preferences by 4 to 6 percentage points compared to standard pairwise judging.
- Answer-order inconsistency rises by 8 to 10 points under two‑call evidence locking versus structured one‑call judging.
- Pointwise locking is also harmful, while structured evidence elicitation remains close to standard judging.

## Context
This work addresses the hidden ordering problem in LLM judges where visible field order does not reflect internal decision logic. The study demonstrates that persisting evidence across calls can compromise evaluation fidelity despite intended auditability benefits.

## Implications
For practitioners relying on automated judge systems, the findings suggest that preserving evidence should be balanced with source answer integrity to avoid systematic bias. It highlights a need for careful protocol design in LLM‑as‑judge applications.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.05353v1)
