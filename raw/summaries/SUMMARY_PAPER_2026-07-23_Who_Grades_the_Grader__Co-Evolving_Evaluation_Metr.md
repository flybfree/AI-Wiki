---
title: Who Grades the Grader? Co-Evolving Evaluation Metrics and Skills for Self-Improving LLM Agents
url: http://arxiv.org/abs/2607.12790v1
type: paper-summary
date: 2026-07-23
source_paper: 2026-07-14_14-02-50Z_WhoGradestheGrader_Co_EvolvingEvaluationMetricsand.md
generated_at: 2026-07-23 23:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper proposes a framework for self-improving LLM agents where evaluation metrics are co-evolved with the skill loop to replace reliance on ground truth. It demonstrates that evolving metrics can maintain high performance across tasks without external rubrics and that safety mechanisms prevent abuse. The results show metric retention of 88–110% lift compared to baseline.

## Key Takeaways
- Metric evolution uses a full lifecycle with detectors, consensus regularization, and an out‑of‑sample anchor for transparent inspection.
- Double Ratchet recovers the performance of ground‑truth driven loops by co‑evolving metrics, achieving 88–110% of held‑out lift in code generation, text‑to‑SQL, and report tasks.
- Safety is ensured by keeping anchors active; removing them collapses detection, while removing the lifecycle leaves a functional system.

## Context
Self‑improving agents require reliable verification but most real applications lack such verifiers. This work addresses that gap by showing metrics can be built from scratch through evolutionary processes. The approach aligns with trends toward autonomous systems and continual learning in AI research.

## Implications
Practitioners can deploy self‑evolving LLM pipelines without waiting for human‑crafted rubrics, reducing reliance on costly annotation efforts. The framework also offers a safety net that catches gamed outputs, supporting trustworthy deployment of autonomous agents.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2607.12790v1)
