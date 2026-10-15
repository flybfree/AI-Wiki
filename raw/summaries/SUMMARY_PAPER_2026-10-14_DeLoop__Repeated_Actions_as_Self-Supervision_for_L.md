---
title: DeLoop: Repeated Actions as Self-Supervision for Long-Horizon Agents
url: http://arxiv.org/abs/2610.19376v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_01-23-00Z_DeLoop_RepeatedActionsasSelf_SupervisionforLong_Ho.md
generated_at: 2026-10-14 20:59
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
DeLoop is a self-supervised training method designed to reduce redundant, looping actions in long-horizon language-model agents that re-issue previously executed tool calls and receive identical observations. The method leverages the agent's own rollout trajectories to construct preference pairs—treating a looping action as negative and the subsequent non-looping action as positive—and trains via direct preference optimization without requiring task rewards, gold answers, or LLM judges. On CodeGym benchmarks under context compression, DeLoop dramatically reduces loop occurrence (from 57.3% to 6.1% of tasks for Qwen3-8B) and cuts step counts by roughly two-thirds while maintaining or improving task success rates.

## Key Takeaways
- Loops are a native failure mode across major open and proprietary model families (Qwen, Llama, Gemini) and become significantly more prevalent when an agent's conversation history is compressed to fit within its context window, indicating that context management strategies directly exacerbate redundant behavior rather than merely exposing it.
- DeLoop's supervision signal is entirely self-generated: it identifies a looping action within a rollout as a negative example and the first subsequent non-looping action in the same trajectory as a positive example, then applies direct preference optimization (DPO) to learn to avoid the loop. This eliminates the need for external reward signals, ground-truth answers, or auxiliary LLM judges, making the method scalable and annotation-free.
- Quantitative results demonstrate substantial efficiency gains: Qwen3-8B loop-containing tasks drop from 57.3% to 6.1% with approximately one-third the steps per task at comparable success, while Qwen3-32B sees loops and steps reduced alongside a task success improvement from 37.7% to 44.8%, showing the method scales across model sizes.

## Context
Long-horizon agentic systems are increasingly deployed for software engineering, research automation, and multi-step tool-use tasks, where context-window limitations force aggressive history compression that inadvertently amplifies repetitive behavior. Prior mitigation strategies have relied on external reward models, curated datasets, or prompt-engineering heuristics, none of which scale cleanly across model families or task domains. DeLoop addresses this gap by turning the agent's own failure patterns into training signal, aligning with the broader trend toward self-supervised and preference-based fine-tuning that reduces dependence on human annotation.

## Implications
For practitioners building production agent pipelines, DeLoop offers a lightweight fine-tuning recipe that can be applied to existing model checkpoints without collecting new labeled data, potentially reducing inference costs by cutting redundant tool calls and token generation. For the research community, the finding that context compression itself is a primary driver of loops suggests that agent training and context-management strategies must be co-designed rather than treated as independent concerns, opening a new axis for improving agentic reliability in resource-constrained deployments.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19376v1)
