---
title: MedClaw: Heuristic Agent Harness for Long-Horizon Surgical Video Reasoning
url: http://arxiv.org/abs/2608.14015v1
type: paper-summary
date: 2026-08-16
source_paper: 2026-08-14_07-03-06Z_MedClaw_HeuristicAgentHarnessforLong_HorizonSurgic.md
generated_at: 2026-08-16 21:11
model: nvidia/nemotron-3-nano-4b
---

## Summary
MedClaw introduces a heuristic agent harness that separates reasoning from perception in long‑horizon surgical videos, enabling the model to answer “before” and “after” questions by retrieving evidence across time. The approach uses a text‑only orchestrator to plan tool calls while vision‑language sub‑agents execute them on frozen models, and a gradient‑free reward‑gated distillation loop that builds reusable retrieval skills from few labeled examples. Experiments show the agent outperforms one‑shot VLMs and general video agents across both benchmark datasets.

## Key Takeaways
- The orchestrator plans which visual evidence to gather, issuing auditable tool calls rather than optimizing model weights.
- A reward‑gated distillation loop mines low‑scoring traces to retain only skills that improve validation rewards, creating reusable retrieval abilities like directed re‑look.
- The system learns from about 100 labeled examples instead of thousands needed for supervised or reinforcement fine‑tuning.

## Context
Long‑horizon reasoning in video is limited by context windows and data scarcity. Current agents either compress entire procedures, losing temporal detail, or require massive training to adapt to new domains. MedClaw’s modular design addresses both issues by decoupling planning from perception and leveraging few examples.

## Implications
Practitioners can deploy reliable surgical assistants that answer procedural questions without retraining large models for each case. The framework reduces reliance on labeled data, lowering cost and accelerating deployment in clinical settings where video evidence is abundant but labeling scarce.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.14015v1)
