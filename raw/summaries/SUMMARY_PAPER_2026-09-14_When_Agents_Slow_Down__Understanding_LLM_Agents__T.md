---
title: When Agents Slow Down: Understanding LLM Agents' Test-Time Strategies via Elo-per-token Analysis
url: http://arxiv.org/abs/2609.15309v1
type: paper-summary
date: 2026-09-14
source_paper: 2026-09-14_09-57-49Z_WhenAgentsSlowDown_UnderstandingLLMAgents_Test_Tim.md
generated_at: 2026-09-14 22:19
model: timtimtimtimtim/qwen3.6-35b-a3b
---

## Summary
This paper introduces Elo-per-token analysis, a novel framework for evaluating how large language model agents adaptively allocate test-time compute across open-ended tasks. By tracking the best solution discovered at each token budget and aggregating performance using a Bradley-Terry model, the authors demonstrate that while LLM agents initially convert tokens into performance gains faster than independent sampling, their marginal returns quickly diminish and eventually fall below baseline references. The study identifies a scaling inflection point where parallelizing compute across multiple shorter sessions yields significantly higher Elo improvements compared to single extended trajectories.

## Key Takeaways
- The proposed Elo-per-token analysis leverages continuous scoring on open-ended benchmarks to track solution quality against token budgets, using a Bradley-Terry model to standardize performance across diverse tasks with varying score scales.
- LLM agents exhibit rapid initial performance gains that quickly plateau and underperform independent sampling baselines, whereas historical human contestants demonstrate superlinear improvement over time, indicating substantial untapped potential for continual learning in agent architectures.
- Defining a scaling inflection point allows researchers to optimize compute allocation; splitting a 100M-token budget into ten parallel sessions on the FrontierCS Polyomino Packing benchmark yielded +355 Elo gains compared to only +264 Elo from a single long session, highlighting the benefits of parallelized test-time compute.

## Context
As LLM agents increasingly rely on extended reasoning and tool-use during inference, understanding how they utilize test-time compute has become critical for scaling AI capabilities. Traditional evaluation metrics often fail to capture adaptive strategies or intermediate progress, making it difficult to benchmark long-horizon agent behaviors fairly. This work addresses a growing gap in the literature by introducing a standardized, continuous scoring framework that aligns with real-world agent workflows and open-ended problem-solving environments.

## Implications
The findings suggest that practitioners should favor parallelized, shorter inference sessions over monolithic long-context runs to maximize performance per token when working with current LLM agents. By identifying the scaling inflection point, developers can optimize resource allocation in production systems, reducing latency and computational costs while maintaining or improving output quality. Furthermore, the observed performance gap between AI agents and human contestants underscores the need for architectures that support iterative refinement and continual learning during test-time reasoning.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.15309v1)
