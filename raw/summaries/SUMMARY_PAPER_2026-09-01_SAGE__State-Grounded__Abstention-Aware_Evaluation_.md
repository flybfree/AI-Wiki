---
title: SAGE: State-Grounded, Abstention-Aware Evaluation of Task-Oriented Dialogue Agents
url: http://arxiv.org/abs/2609.00434v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-08-31_22-14-52Z_SAGE_State_Grounded_Abstention_AwareEvaluationofTa.md
generated_at: 2026-09-01 21:27
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces SAGE (State-Grounded Abstention-Aware Evaluation) to assess task‑oriented dialogue agents by measuring whether each turn correctly updates the workflow state, a metric that conventional holistic LLM judges often overlook. By compiling a workflow specification and per‑turn state diff into atomic criteria, SAGE routes them through symbolic and encoder/NLI verifiers that abstain rather than guess, delivering a turn‑level decision with an evidence trace at zero paid LLM cost for its core version.

## Key Takeaways
- SAGE‑Core decides 81–91 % of criteria without any paid LLM calls, achieving comparable accuracy to expensive GPT‑4.1 judges while keeping costs near $0 per thousand turns.
- Human audit (n=200, κ=0.94) shows strong label fidelity on transcript‑visible failure classes; SAGE‑Core is statistically tied with the strongest LLM judge except for the weak‑salience IUV class and correctly scopes ignored‑user‑value as a state‑consistency signal.
- The two‑annotator human audit confirms that SAGE’s abstention strategy reduces unnecessary LLM calls, preserving both cost efficiency and reliability.

## Context
Current evaluation of dialogue agents often relies on holistic judgments that treat the entire conversation context as a single unit, leading to missed state‑advancement errors. Efficient, state‑grounded methods are needed to align model performance with real workflow requirements without incurring high compute costs.

## Implications
This work provides a cost‑effective evaluation framework that can be integrated into production pipelines, offering reliable metrics for state consistency while minimizing reliance on expensive LLM judges. Practitioners can adopt SAGE‑Core to validate agents quickly and accurately, supporting responsible deployment of task‑oriented systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.00434v1)
