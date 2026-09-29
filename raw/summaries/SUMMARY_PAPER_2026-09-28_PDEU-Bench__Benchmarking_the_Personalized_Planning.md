---
title: PDEU-Bench: Benchmarking the Personalized Planning Lifecycle of Tool-Calling LLM Agents
url: http://arxiv.org/abs/2609.34930v1
type: paper-summary
date: 2026-09-28
source_paper: 2026-09-28_11-27-17Z_PDEU_Bench_BenchmarkingthePersonalizedPlanningLife.md
generated_at: 2026-09-28 22:50
model: qwen3.6-35b-a3b
---

## Summary
This paper introduces PDEU-Bench, a comprehensive benchmark designed to evaluate how well large language model agents maintain user preferences while navigating the full planning lifecycle across long-horizon interactions. Through rigorous testing of fifteen prominent models, the authors demonstrate that current systems excel at executing isolated tool calls aligned with stated preferences but consistently struggle to dynamically define and update coherent multi-step plans. The study concludes that existing personalization techniques fail to sustain preference propagation over time, highlighting an urgent need for advanced memory-augmented architectures in agent design.

## Key Takeaways
- PDEU-Bench establishes a standardized evaluation framework featuring 214 long-horizon tasks spanning twelve everyday domains and ninety-four tools, specifically structured to measure preference adherence and plan quality across distinct stages of definition, execution, and update.
- Extensive model evaluations reveal a critical capability gap: while LLMs can successfully instantiate user preferences in single tool invocations, they frequently fail to construct or revise coherent long-term plans that preserve those preferences throughout extended interactions.
- Mainstream personalization and memory-augmentation methods only yield marginal, stage-specific improvements; none reliably propagate preferences across the entire planning lifecycle, with fine-grained error analysis confirming persistent preference omissions and internal conflicts during dynamic updates.

## Context
As AI agents transition from reactive command executors to proactive, goal-driven assistants, benchmarking their ability to maintain context and personalize interactions over time has become a critical research frontier. Traditional evaluation metrics fall short by focusing on isolated tool invocations rather than sustained, multi-step reasoning processes that mirror real-world user workflows. This work addresses that limitation by establishing a standardized protocol for assessing dynamic planning and preference retention in complex, long-horizon environments.

## Implications
The findings suggest that developers building production-grade AI agents must prioritize robust memory architectures and preference-aware retrieval mechanisms rather than relying solely on prompt engineering or isolated tool-calling optimizations. For the broader AI community, this benchmark provides a necessary diagnostic tool to track progress toward truly autonomous, personalized agents capable of long-horizon task completion without degrading user alignment over time.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.34930v1)
