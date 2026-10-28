---
title: From Interaction to Capability: Task Advancement as State and Supervision for GUI Agents
url: http://arxiv.org/abs/2610.37482v1
type: paper-summary
date: 2026-10-27
source_paper: 2026-10-27_16-09-25Z_FromInteractiontoCapability_TaskAdvancementasState.md
generated_at: 2026-10-27 22:04
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
This paper introduces Task Advancement Memory (TAM), a framework for GUI agents that reframes memory management around verified task progress rather than raw interaction logs. TAM operates through two mechanisms: Task Advancement State, which tracks how verified progress reshapes remaining goals across applications during execution, and advancement supervision, which abstracts reusable operations from interactions that produced verified local results. The approach yields substantial improvements, raising success rates from 12.0% to 28.2% on MobileWorld tasks with state tracking alone, and achieving a 17.6% relative gain over the strongest baseline when the full TAM system is applied.

## Key Takeaways
- Task Advancement State redefines agent memory as a representation of verified task progress that dynamically updates remaining goals, enabling agents to build on earlier achievements across different applications rather than starting fresh in each context. This mechanism alone nearly doubles task success on MobileWorld GUI-only benchmarks, from 12.0% to 28.2%, demonstrating that tracking what has been verified as completed is more valuable than storing raw interaction history.
- Advancement supervision extracts and abstracts reusable operations from interactions that produced verified local results, preserving the relationship between required inputs, expected outcomes, and verification conditions. Critically, this learning process operates on both successful and failed tasks, meaning locally successful operations embedded within otherwise failed attempts are not discarded, which addresses a major limitation in long-horizon workflows where useful operations are interleaved with failures.
- Full TAM achieves a 17.6% relative improvement in task success over the strongest evaluated baseline while simultaneously reducing lifecycle tokens per solved task by 38.7%, indicating that structured task advancement memory improves both effectiveness and efficiency. On SPA-Bench, TAM reaches state-of-the-art performance in the single-app English Level 3 setting, validating the approach across different benchmark environments.

## Context
GUI agents operating in long-horizon, multi-application workflows face a fundamental challenge: they must retain useful information across applications while distinguishing productive operations from failed attempts. Existing memory approaches typically store raw interaction sequences, which become noisy and unhelpful as task complexity grows. This paper addresses a core bottleneck in the broader field of autonomous agents, where the inability to build incrementally on verified progress prevents agents from handling complex, multi-step tasks that span different software environments. By formalizing task advancement as a supervisable signal, TAM bridges the gap between interaction-level learning and capability-level generalization.

## Implications
For practitioners building autonomous GUI agents for productivity automation, TAM offers a practical path toward agents that genuinely learn from experience rather than merely replaying past interactions, with a nearly 40% reduction in token costs per solved task making deployment more economically viable. For the research community, the separation of advancement state from advancement supervision provides a principled framework for studying how agents can develop reusable skills from noisy interaction data, potentially informing future work in continual learning, tool-use agents, and multi-application automation systems.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.37482v1)
