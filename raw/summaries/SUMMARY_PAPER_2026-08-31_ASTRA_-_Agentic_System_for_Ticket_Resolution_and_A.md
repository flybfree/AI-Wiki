---
title: ASTRA - Agentic System for Ticket Resolution and Analysis
url: http://arxiv.org/abs/2608.28790v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-28_18-50-17Z_ASTRA_AgenticSystemforTicketResolutionandAnalysis.md
generated_at: 2026-08-31 21:05
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces ASTRA, an agentic system that coordinates three specialist agents to generate evidence‑backed troubleshooting reports for telecom fault tickets. Evaluated on 987 real‑world tickets across seven product lines, ASTRA achieves a mean quality score of 4.13/5.0 with high relevance and clarity scores.

## Key Takeaways
- The system models evidence provenance by linking each claim to a verbatim source passage and assigning a support level while preventing cross‑attribution.
- A judge‑orchestrator loop refines the report iteratively, converting low scores into targeted follow‑up queries for bounded refinement.
- Hardware fault diagnosis remains substantially harder than software or configuration faults, as shown by Cohen’s d=0.80.

## Context
ASTRA addresses a key challenge in AI‑driven technical support: producing interpretable, provenance‑aware reports from heterogeneous data sources such as ticket text, logs, and documentation. By integrating dense retrieval, deterministic filtering, and constrained LLM analysis, the approach demonstrates how multi‑agent orchestration can improve reliability.

## Implications
For practitioners, ASTRA offers a framework to automate evidence‑driven troubleshooting while maintaining auditability, reducing the risk of fabricated technical details. In industry, it could streamline incident resolution across telecom and other sectors where fault diagnosis is critical.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.28790v1)
