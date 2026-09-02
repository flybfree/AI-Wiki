---
title: Making Prospective Memory SLM-Shaped: Typed Intention Stores for Small-Model Agents
url: http://arxiv.org/abs/2609.01272v1
type: paper-summary
date: 2026-09-01
source_paper: 2026-09-01_14-04-27Z_MakingProspectiveMemorySLM_Shaped_TypedIntentionSt.md
generated_at: 2026-09-01 22:07
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper introduces a new architecture called Prospective Intention Store (PIS) that enables small language models to perform prospective memory by storing typed intentions and retrieving them at cue moments without fine‑tuning or extra data. On PM‑Bench the model DeepSeek‑Chat with PIS reaches 82.9% Set‑F1, far above the best published scaffold of 65.1%. The authors show that a lightweight store can outperform large models when action space is typed.

## Key Takeaways
- Prospective memory in LLMs is limited by schema‑constrained state tracking rather than open reasoning, and small models succeed when actions are typed.
- A training‑free, agentic PIS scaffold stores lifecycle logic in code while keeping model work scoped to language generation.
- On Gemma‑E2B the baseline without a store scores 4.2% Set‑F1, with seven retrospective memories only 6.6%, whereas PIS reaches 66.2% and outperforms retrospectives at 70.1%.

## Context
Prospective memory is increasingly used as a benchmark for agentic language models, yet most solutions rely on large‑scale fine‑tuned selectors or massive trajectory data. This work demonstrates that the problem can be solved with a minimal, code‑driven store, reducing reliance on compute and data.

## Implications
The findings suggest that small models can achieve state‑of‑the‑art performance on memory tasks without costly training pipelines, encouraging developers to embed lightweight lifecycle logic directly into model inference. This could lower costs for applications requiring proactive behavior in chatbots or assistants.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.01272v1)
