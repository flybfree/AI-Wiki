---
title: "Summary: Meta-Harness: End-to-End Optimization of Model Harnesses"
date: 2026-03-30
status: draft
tags: [summary, agents, harness, paper]
url: "https://arxiv.org/abs/2603.28052"
---

# Summary: Meta-Harness: End-to-End Optimization of Model Harnesses

**Source**: [Meta-Harness: End-to-End Optimization of Model Harnesses](https://arxiv.org/abs/2603.28052)

## Summary
Meta-Harness treats the harness as an optimization target. Instead of hand-tuning the orchestration code around a language model, it searches over harness code using an agentic proposer that can inspect source code, scores, and execution traces of prior candidates.

## Key Takeaways
- Harness quality is a first-class driver of LLM system performance, not just a detail around the edges.
- Better access to prior traces and execution history can enable automated harness engineering.
- The method improves online text classification, retrieval-augmented math reasoning, and agentic coding benchmarks with the same general pattern: search over the harness, not only the model.

## Context
The paper is a direct answer to the question of why so many agent systems plateau: the surrounding code is often more important than the prompt alone, but that code is usually tuned by hand and poorly instrumented. Meta-Harness makes the harness itself the thing being optimized.

## Implications
For agent builders, this suggests that better systems may come from treating orchestration logic as searchable and testable infrastructure. The model is still central, but the control layer is where many gains now live.

## Semantic links
- [[concepts/ai-agents/harness-engineering-hub.md|Harness Engineering Hub]]
- [[concepts/ai-agents/ai-agents-lesson-02-harness-implementing-an-agent.md|AI Agents Lesson 2: The Harness: Implementing an Agent]]
- [[concepts/ai-agents/agentic-workflows-hub.md|Agentic Workflows Hub]]
