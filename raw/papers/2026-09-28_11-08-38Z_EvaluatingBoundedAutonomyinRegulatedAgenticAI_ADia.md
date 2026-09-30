---
title: Evaluating Bounded Autonomy in Regulated Agentic AI: A Diagnostic Harness with Constitutional Rewards, Escalation Labels, and Runtime Governance
published: 2026-09-28T11:08:38Z
authors: Dipankar Sarkar
url: http://arxiv.org/abs/2609.37501v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evaluating Bounded Autonomy in Regulated Agentic AI: A Diagnostic Harness with Constitutional Rewards, Escalation Labels, and Runtime Governance

## Abstract
We propose RegLLM, a diagnostic harness for bounded autonomy in regulated agentic workflows. It instruments six trustworthiness signals: citation validity, source grounding, schema compliance, escalation correctness, constitutional alignment, and unsafe-action rate. Signals are distinguished by their source of supervision: programmatic verifiers, task-level escalation labels, or AI-judge scores. A deterministic runtime supervisor blocks ungrounded answers and forces escalation, logging interventions. The same domain constitution informs evaluation, training rewards, and serving guardrails. Task-level should-escalate labels make the act-versus-defer decision a measurable training signal. We demonstrate the harness at smoke scale. An offline reference run (n=12) lifts escalation recall from 0 to 0.67 and reduces unsafe-action rate from 0.33 to 0.08 when governance is enabled. Two single-GPU Qwen2.5-3B LoRA/DPO pilots (n=8, same seed and evaluation split) expose substantial variation: nominally identical RL-base configurations yield task success of 0.25 versus 0.12 and escalation recall of 1.0 versus 0.5. An answer-quality adapter changes recall from 1.0 to 0.5 in Run A, but from 0.5 to 1.0 in Run B. An escalation-aware variant produces no measurable change in Run B. These small pilots do not establish reliable adapter effects or production readiness. Their contribution is diagnostic: configuration variance can overwhelm apparent tuning effects on bounded-autonomy metrics, motivating larger evaluation sets and repeated runs.

## Metadata
- **Published**: 2026-09-28T11:08:38Z
- **Authors**: Dipankar Sarkar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.37501v1)