---
title: More Memory, Worse Agents: Error Reproduction and Anti-Persistence in LLM Agents
url: http://arxiv.org/abs/2610.27406v1
type: paper-summary
date: 2026-10-20
source_paper: 2026-10-19_23-58-46Z_MoreMemory_WorseAgents_ErrorReproductionandAnti_Pe.md
generated_at: 2026-10-20 22:01
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper investigates a critical failure mode in memory-based self-improving LLM agents: the propagation and regeneration of errors through stored abstractions. The authors identify a feedback loop they term "error reproduction," where faulty rules or summaries stored in memory influence subsequent agent behavior, which in turn generates new trajectories that reinforce the original errors. To address this, they propose Anti-Persistence, a memory architecture that retains raw trajectories and outcomes but synthesizes task-specific guidance only on demand, discarding it after execution. Across multiple benchmarks and model backbones, Anti-Persistence achieves the highest held-out success rates and the lowest average LLM-call cost among the evaluated memory designs.

## Key Takeaways
- Error reproduction is a novel feedback mechanism distinct from simple reuse of faulty knowledge: errors cycle through abstraction, execution, and re-abstraction, meaning a single stored error can regenerate itself across many future tasks even without being directly retrieved again. This makes the problem fundamentally harder than one-shot retrieval errors and demands architectural solutions rather than simple filtering.
- Anti-Persistence separates experience accumulation from abstraction persistence. The agent stores trajectories and outcomes as ground truth but uses an adaptive selector to decide whether and how to synthesize guidance for a given task. That synthesized guidance is discarded after execution, preventing it from becoming a stored object that future retrievals could pull. Indirect feedback through retained trajectories remains, but the direct propagation channel is severed.
- Empirically, Anti-Persistence outperforms memory designs that persistently store rules, summaries, and skills across diverse benchmarks and backbone models, while simultaneously reducing the average number of LLM calls needed per task. This suggests that reconstructing context on demand is both more accurate and more efficient than maintaining a growing library of abstractions.

## Context
As LLM agents increasingly rely on external memory systems to improve performance across sequential tasks without fine-tuning model weights, the design of what gets stored and how it is retrieved has become a central engineering question. Prior work has largely assumed that richer stored abstractions—rules, skills, summaries—yield better agent performance. This paper challenges that assumption by demonstrating that persistent abstractions introduce a self-reinforcing error channel that degrades long-term reliability. It contributes to the growing literature on agent memory architectures, retrieval-augmented generation, and self-improving AI systems by providing a concrete mechanism (error reproduction) and a principled countermeasure (Anti-Persistence).

## Implications
For practitioners building autonomous agents that learn from their own execution history, this work suggests that storing raw trajectories and reconstructing guidance on demand is preferable to maintaining a persistent library of distilled rules or skills, both for accuracy and for cost efficiency. For the broader field, the identification of error reproduction as a structural failure mode in abstraction-based memory systems highlights a design principle: separating what an agent records from what it synthesizes can prevent compounding errors in long-running agent deployments. Industry teams deploying agents in production should reconsider whether their memory pipelines inadvertently create feedback loops that amplify early mistakes into persistent behavioral biases.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.27406v1)
