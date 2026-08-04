---
title: Constructing Executable Analytical Knowledge Representations for Meta-Analysis Synthesis Using an Agentic Harness
url: http://arxiv.org/abs/2608.01711v1
type: paper-summary
date: 2026-08-03
source_paper: 2026-08-03_05-19-05Z_ConstructingExecutableAnalyticalKnowledgeRepresent.md
generated_at: 2026-08-03 23:21
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Executable Analytical Knowledge Representation (EAKR), a structured format that captures the analytical decisions needed to turn meta‑analysis evidence into executable code, and demonstrates it with MetaSynDec, an agentic harness using large language models. Across 58 synthesis units, MetaSynDec generated EAKRs, with 57 proceeding to statistical execution; most achieved high fidelity in reference analysis objects (67.9%) and exact evidence‑set agreement (75.0%), yielding a mean Jaccard similarity of 0.909.

## Key Takeaways
- The EAKR captures all necessary analytical decisions—evidence assignment, contrasts, alignment, effect‑size formulation, and methodological admissibility—in a machine‑actionable way rather than embedding them in code or workflow traces.
- MetaSynDec achieved near‑perfect agreement with human reference analyses: 38 of 56 units matched the exact evidence set (75.0%) and 42 out of 56 had complete object fidelity (67.9%), while confidence intervals overlapped in 98.2% of cases.
- The approach outperformed direct LLM generation, achieving 57/58 correct reference‑synthesis structures versus only 23/58 with standard methods.

## Context
The work addresses a longstanding gap in AI‑driven meta‑analysis: automated tools often produce code or summaries that hide the underlying analytical logic. By formalising this knowledge as EAKR, researchers can ensure traceability and reproducibility, aligning with broader goals of verifiable, auditable scientific reasoning.

## Implications
EAKR provides a framework for integrating human expertise into AI pipelines, enabling rigorous validation and execution of meta‑analysis without sacrificing interpretability. Practitioners can leverage this to produce trustworthy statistical outputs, fostering confidence in automated scientific synthesis.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.01711v1)
