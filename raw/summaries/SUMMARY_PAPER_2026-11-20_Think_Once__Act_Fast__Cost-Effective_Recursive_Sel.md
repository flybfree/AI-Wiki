---
title: Think Once, Act Fast: Cost-Effective Recursive Self-Improvement for Decision Model Harness
url: http://arxiv.org/abs/2611.22432v3
type: paper-summary
date: 2026-11-20
source_paper: 2026-11-17_09-06-14Z_ThinkOnce_ActFast_Cost_EffectiveRecursiveSelf_Impr.md
generated_at: 2026-11-20 21:52
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
The paper introduces JevRSI, a framework that bridges the gap between fast System-1 decision models and slow but powerful System-2 LLM reasoning by transforming LLM-generated insights into a transferable, modular decision harness. Through recursive self-improvement guided by environmental feedback, the system progressively reduces its reliance on expensive LLM invocations while maintaining or exceeding the decision quality of full LLM agents across multiple benchmark datasets.

## Key Takeaways
- JevRSI employs a Jev-style System-1 model for low-latency action selection paired with an asynchronous System-2 LLM that builds a modular harness integrating procedures, state memory, and world models. This harness provides decision contexts spanning past, present, and future states, enabling the fast model to act with informed reasoning without repeatedly invoking the costly LLM.
- The framework uses utility-driven retrieval to select harness modules based on both contextual relevance and demonstrated utility on previous tasks, ensuring that only the most effective reasoning components are activated during decision-making. Environmental feedback then guides targeted revisions to the harness, enabling recursive self-improvement over time.
- Experimental results across three datasets demonstrate that JevRSI consistently improves decision quality, matching or surpassing dedicated LLM agents in several settings while preserving low-latency execution. Critically, System-2 development interventions decrease as the harness matures, effectively amortizing the computational cost of LLM reasoning through continuous harness evolution rather than repeated invocation.

## Context
This work sits at the intersection of dual-process theory in cognitive science and practical deployment constraints in AI agent systems. The System-1/System-2 paradigm, popularized by Daniel Kahneman and adopted in AI research, highlights the tension between fast heuristic reasoning and slow deliberative reasoning. Prior approaches either rely entirely on fast models that fail on novel tasks or repeatedly invoke expensive LLMs for every decision, creating prohibitive latency and cost barriers. JevRSI addresses this gap by treating LLM reasoning as a one-time developmental investment that produces reusable decision infrastructure, aligning with broader trends toward distillation, tool-augmented reasoning, and self-improving agent architectures.

## Implications
For practitioners deploying autonomous agents in robotics, game-playing, or interactive decision environments, JevRSI offers a practical path to high-quality reasoning without the recurring computational overhead of full LLM inference, making it viable for latency-sensitive or resource-constrained applications. For the broader AI research community, the recursive harness improvement paradigm suggests a scalable strategy for amortizing expensive reasoning costs, potentially informing future agent architectures that learn from their own operational history rather than requiring constant external reasoning support.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2611.22432v3)
