---
title: Your Prompt Is Not the Only Prompt: How Much Do LLMs Weight Structured-Output Schema Descriptions?
url: http://arxiv.org/abs/2608.08254v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-08_17-27-22Z_YourPromptIsNottheOnlyPrompt_HowMuchDoLLMsWeightSt.md
generated_at: 2026-08-10 22:15
model: nvidia/nemotron-3-nano-4b
---

## Summary
The paper investigates how structured-output schemas affect LLM performance when definitions are placed in system prompts, user prompts, or schema descriptions. It tests classification tasks with ten model configurations and finds that schema instructions can override prompt instructions, causing accuracy drops ranging from 5 to 45 points. Adding a reasoning field before the label improves schema‑only accuracy by 15–24 points, sometimes exceeding system‑prompt performance.

## Key Takeaways
- Schema descriptions do not consistently outperform prompt‑based placement; for GPT‑4.1 and GPT‑5.4 without reasoning they underperformed system prompts by 11–13 percentage points.
- Incorrect schema instructions can cause accuracy drops of 5–45 points, as seen in Claude Haiku 4.5 dropping from 52.5% to 7% when schemas conflicted with prompts.
- Adding an intermediate reasoning field before the label boosts schema‑only accuracy by 15–24 points and can surpass system‑prompt performance even for models like Claude Sonnet 4.6.

## Context
Structured output is now a standard method for data labeling, but its instruction channel is split between prompts and schemas. This paper highlights that the way information is encoded in field descriptions interacts with model behavior, affecting accuracy more than where definitions are placed. The findings underscore the need to treat schema design as an active lever rather than passive metadata.

## Implications
For practitioners, maintaining a single source of truth between prompts and schemas is essential to avoid drift that degrades performance. Schema design may be a stronger control knob than instruction placement, so empirical validation of both aspects should be prioritized in model deployment pipelines across the industry.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.08254v1)
