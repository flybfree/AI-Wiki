---
title: GADR: Gathering Architecture Decision Records from Meeting Transcriptions
url: http://arxiv.org/abs/2608.17694v1
type: paper-summary
date: 2026-08-18
source_paper: 2026-08-18_12-11-42Z_GADR_GatheringArchitectureDecisionRecordsfromMeeti.md
generated_at: 2026-08-18 21:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces GADR, a multi‑agent workflow that extracts architectural decisions from raw meeting transcripts and creates Nygard‑formatted ADR drafts. Feasibility testing with five real meetings shows the system captures most expert‑identified decisions and produces clear drafts, outperforming zero‑shot and few‑shot baselines in stability.

## Key Takeaways
- The assumption that input is already reasonably structured is false; raw meeting transcripts are noisy and require multi‑agent processing. 
- GADR’s agentic workflow improves decision capture and draft clarity compared to simple prompting methods.
- The trade‑off between enriching ADRs with RAG and preserving transcript fidelity remains an open research question.

## Context
Architectural Decision Records are essential for software teams, yet current LLM methods rely on structured inputs that rarely exist in practice. This work bridges the gap by handling unstructured meeting data directly, offering a more realistic path to automated documentation.

## Implications
Automated ADR generation can reduce manual effort and ensure consistency across projects. Understanding the fidelity‑depth trade‑off is crucial for trustworthy AI tools in engineering workflows.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.17694v1)
