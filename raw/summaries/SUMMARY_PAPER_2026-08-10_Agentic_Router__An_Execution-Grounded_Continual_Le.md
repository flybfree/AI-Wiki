---
title: Agentic Router: An Execution-Grounded Continual Learning Approach With Memory
url: http://arxiv.org/abs/2608.09184v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_06-53-24Z_AgenticRouter_AnExecution_GroundedContinualLearnin.md
generated_at: 2026-08-10 22:04
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces an execution-grounded dual-path consequence-aware agent for CLI-based SONiC operations that jointly improves candidate coverage and action selection by generating multiple actions, predicting their consequences, and selecting via utility and risk‑aware reranking. Experiments show improved feasible-action coverage and top‑1 success across multi‑turn sessions with various Qwen3 proposal models.

## Key Takeaways
- The framework generates multiple complete CLI actions and predicts their execution consequences before final selection.
- A side‑path abstracts reusable operational lessons into retrievable guidance to boost feasible‑action coverage without altering the proposal LLM.
- Another side‑path adapts the consequence predictor using session‑level LoRA updates from real SSH feedback, enhancing conditional selection quality.

## Context
Continual learning for language agents remains limited to static model updates, whereas real‑world interaction provides dynamic feedback that can be leveraged. This work bridges that gap by integrating execution outcomes into agent design, offering a more responsive and reliable interface for command‑line tasks.

## Implications
Practitioners can deploy agents that continuously improve from live operations, reducing errors in automated network workflows. The approach demonstrates how memory‑based adaptation can yield tangible gains in reliability without retraining large models, encouraging broader adoption of continual learning in AI assistants.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09184v1)
