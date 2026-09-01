---
title: EvoGenUI-Bench: Evaluating LLMs as Multi-Turn Generative UI Assistants
url: http://arxiv.org/abs/2608.29387v1
type: paper-summary
date: 2026-08-31
source_paper: 2026-08-29_17-54-02Z_EvoGenUI_Bench_EvaluatingLLMsasMulti_TurnGenerativ.md
generated_at: 2026-08-31 20:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces EvoGenUI-Bench, a benchmark that tests large language models' ability to generate and maintain executable web interfaces across multi-turn interactions. It evaluates eight models on 150 five‑turn tasks spanning information presentation, interactive actions, and tool‑grounded state changes using screenshots, DOM traces, actor logs, and runtime execution.

## Key Takeaways
- Turn pass rates are low even for top models: the strongest model achieves only 37.3% episode completion while passing 74.9% of turns, indicating frequent breakdowns in later turns.
- Adjacent Pass Retention drops sharply on tool‑grounded tasks to 52.4%, showing that maintaining external state is harder than internal UI logic.
- Diagnostic analysis reveals presentation failures stem from poor information architecture, interaction failures from broken derived‑state propagation and affordance binding, and tool‑grounded issues from grounding problems and requirement decomposition.

## Context
Generative UI assistants are a growing research area where models must produce code that runs in browsers while preserving state across conversation turns. Existing benchmarks often focus on single‑turn outputs or limited multi‑step tasks, overlooking the cumulative challenges of external dependencies and derived states.

## Implications
These results highlight that evaluating generative UI must consider not just final artifact correctness but also ongoing behavior consistency and alignment with user expectations. Practitioners should incorporate cross‑turn retention metrics into model testing to avoid deceptive performance on complex, multi‑modal tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.29387v1)
