---
title: ATLAS: Dual-Horizon Diagnostic Evaluation for Industrial Tool-Use Agents
url: http://arxiv.org/abs/2608.30685v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-31_12-25-24Z_ATLAS_Dual_HorizonDiagnosticEvaluationforIndustria.md
generated_at: 2026-08-31 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces ATLAS, a dual‑horizon diagnostic evaluation framework for industrial LLM agents that use tools iteratively under dynamic business conditions. The authors demonstrate ATLAS on Meituan Xiaotuan production traffic and show that it uncovers execution deficiencies and maintains service alignment across user interactions.

## Key Takeaways
- ATLAS provides trajectory‑wise diagnostic signals at the request horizon, linking capability issues to specific execution locations within a single request.
- It also generates interaction‑wise signals at the user horizon, assessing whether the agent’s behavior stays consistent when users continue interacting over time.
- The framework uses high‑confidence references from real business logs to calibrate LLM judges and distills their decisions into efficient diagnostic models for low‑latency evaluation.

## Context
Industrial AI agents must balance rapid response with long‑term consistency, yet existing evaluation methods often focus only on final outcomes or single request traces. ATLAS addresses this gap by separating short‑term execution diagnostics from ongoing user engagement, offering a more holistic view of agent performance.

## Implications
Practitioners can use ATLAS to refine policy decisions that affect both immediate task success and sustained service quality. By providing structured diagnostic evidence, the framework supports cost‑effective optimization in real‑time production environments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.30685v1)
