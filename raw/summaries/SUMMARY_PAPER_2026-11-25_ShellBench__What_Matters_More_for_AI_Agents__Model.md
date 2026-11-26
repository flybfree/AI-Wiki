---
title: ShellBench: What Matters More for AI Agents, Models, or Harness for Everyday Tasks
url: http://arxiv.org/abs/2611.32946v1
type: paper-summary
date: 2026-11-25
source_paper: 2026-11-24_16-48-06Z_ShellBench_WhatMattersMoreforAIAgents_Models_orHar.md
generated_at: 2026-11-25 21:53
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
ShellBench introduces a benchmark of 100 realistic day-to-day tasks derived from over 10 million user requests, designed to evaluate AI agent configurations across models, harnesses, and reasoning levels. The study conducted 53,100 rollouts across 12 models and 5 agent harnesses, finding that model selection has a significantly greater impact on performance than harness selection, though the top three models differ by only 1.1 percentage points in pass rate.

## Key Takeaways
- Model choice dominates performance outcomes: GPT-6 Astra achieved the highest pass rate at 62.5%, while GPT-6.1 Sol reached 61.4% at approximately one-sixth the estimated token cost per attempt, demonstrating a meaningful cost-performance tradeoff that practitioners should weigh carefully when selecting configurations for personal or organizational use.
- Agent harness selection has negligible effect on both performance and safety: all five tested harnesses scored within a narrow band of 42.9% (Claude Code) to 45.2% (OpenClaw) for pass@1, suggesting that the surrounding tooling and orchestration layer contributes far less to task success than the underlying model itself.
- The benchmark emphasizes realistic, messy work environments with competing data sources and grades agents on both correctness and safety, reflecting the actual conditions under which everyday users deploy AI agents rather than clean, synthetic evaluation scenarios.

## Context
As AI agents move from research demonstrations into daily personal and professional workflows in 2026, users face a growing array of model and tooling choices without clear guidance on which combinations deliver the best outcomes. ShellBench addresses this gap by grounding evaluation in real user request patterns and realistic workspace conditions, providing a practical decision framework rather than abstract capability scores. The finding that harness differences are marginal while model differences, though small among top performers, still dominate reshapes how the community should prioritize investment in agent infrastructure versus model development.

## Implications
For practitioners and consumers choosing AI agent configurations, the results suggest that selecting the right model is the primary lever for performance, while switching between popular harnesses offers little practical benefit. The near-parity among the top three models (a 1.1 percentage-point spread) also implies that cost efficiency and safety considerations should drive selection rather than chasing marginal accuracy gains. For the broader field, the benchmark's emphasis on safety alongside correctness signals a maturing evaluation standard that industry deployments will need to adopt as agent use scales to hundreds of millions of everyday users.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.32946v1)
