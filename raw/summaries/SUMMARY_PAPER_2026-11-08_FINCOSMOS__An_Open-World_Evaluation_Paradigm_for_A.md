---
title: FINCOSMOS: An Open-World Evaluation Paradigm for Agents in Finance
url: http://arxiv.org/abs/2611.07464v1
type: paper-summary
date: 2026-11-08
source_paper: 2026-11-05_05-19-44Z_FINCOSMOS_AnOpen_WorldEvaluationParadigmforAgentsi.md
generated_at: 2026-11-08 21:22
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
FINCOSMOS introduces an open-world evaluation paradigm designed to assess language agents performing financial tasks under realistic conditions, where data must be sourced from the Web, strategies are hidden in the user's mind, and correctness is time-dependent. The authors demonstrate that across 150 sessions with four coding agents and a tool-less model, no session was accepted by the automated grading system, revealing that agents consistently fail silent correctness checks even when a simulated user appears satisfied. Notably, when agents were given persistent memory and FINCOSMOS feedback, they successfully learned all ten tasks, suggesting the paradigm can drive improvement.

## Key Takeaways
- The evaluation paradigm simulates a user who holds a hidden financial strategy sampled from a compositional grammar and only reveals it when explicitly asked, forcing agents to actively elicit requirements rather than assuming them. Agents raised only 54–64% of the details they were not told, exposing a critical gap in proactive clarification behavior that existing benchmarks do not measure.
- Grading is fully programmatic and reference-free: programs verify point-in-time data correctness, recompute every reported metric, check the delivered strategy against the hidden specification, and apply 15 veto checks. A run is accepted only when the simulated user is satisfied AND no veto check fails, eliminating the possibility of a convincing but incorrect report passing evaluation.
- Human experts attributed 88.33% of failures to the agents themselves rather than to the evaluation setup, validating that the paradigm captures genuine agent shortcomings. However, providing FINCOSMOS feedback combined with persistent memory enabled an agent to learn all ten tasks, demonstrating that the paradigm can serve as a training signal for improving agent behavior.

## Context
This paper addresses a fundamental gap in AI agent evaluation: existing benchmarks artificially constrain the world by fixing tasks, data sources, or timelines, thereby eliminating the very failure modes that matter most in real-world deployment. In finance specifically, silent failures—such as using future data in a backtest, delivering an unrequested strategy, or presenting unverified numbers—produce outputs indistinguishable from correct ones to a casual observer. FINCOSMOS matters because it shifts evaluation from closed-world correctness to open-world robustness, aligning benchmark design with how agents actually operate on the open Web.

## Implications
For practitioners deploying financial AI agents, this work demonstrates that current agents cannot be trusted to independently source data, respect temporal constraints, or elicit hidden user requirements without explicit prompting, which has direct consequences for compliance, risk management, and user trust in automated financial advice. For the broader AI research community, the paradigm offers a template for evaluating agents in any domain where correctness is time-sensitive, data is distributed across the open Web, and user intent is partially hidden. The finding that persistent memory plus structured feedback enables learning across tasks also suggests a practical path toward improving agent reliability in production settings.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.07464v1)
