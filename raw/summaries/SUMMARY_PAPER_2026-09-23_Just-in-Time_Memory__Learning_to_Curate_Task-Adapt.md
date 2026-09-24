---
title: Just-in-Time Memory: Learning to Curate Task-Adaptive Memory for LLM Agents
url: http://arxiv.org/abs/2609.27334v1
type: paper-summary
date: 2026-09-23
source_paper: 2026-09-23_04-14-53Z_Just_in_TimeMemory_LearningtoCurateTask_AdaptiveMe.md
generated_at: 2026-09-23 22:18
model: freedomaisvr/gemma-4-12b-it
---

## Summary
The paper introduces Just-in-Time Memory (JitMem), a novel framework for LLM agents that shifts the curation of memory from the moment of task completion to the point of retrieval. By retaining raw trajectories and synthesizing compact, task-specific payloads only when needed, this approach avoids the irreversible information loss inherent in traditional "write-time" systems that attempt to create one-size-fits-all summaries before future queries are known.

## Key Takeaways
- Traditional agentic memory systems typically curate data at "write-time," meaning they attempt to distill a task's trajectory into a fixed artifact—such as a summary, skill, or strategy—before the system knows what future queries will be asked. This approach forces the model to make permanent decisions about what is worth remembering, often leading to the loss of nuanced details that might be critical for different but related tasks, ultimately producing a query-independent summary that may not serve many downstream needs effectively.
- Training an effective write-time curator is inherently difficult due to a long-horizon credit assignment problem; it is hard to determine if a specific storage decision was correct until a relevant query arrives, which could occur many steps later in the agent's operation. By contrast, JitMem allows for training the curator based on immediate task success because the synthesized payload is consumed during the same interaction cycle, providing a much clearer and more immediate signal for optimization.
- Empirical evaluations across ALFWorld, WebShop, and $\tau^2$-bench demonstrate that JitMem consistently outperforms no-memory agents as well as existing heuristic and learned write-time methods by significant margins (up to 16.3 absolute success-rate points). Notably, even an untrained curator outperformed the baseline models, suggesting that simply moving to a task-adaptive read-time curation model provides a substantial performance boost regardless of the specific training methodology employed.

## Context
As LLM agents are increasingly deployed for complex, multi-step tasks, managing context windows and long-term memory has become a primary bottleneck in reliability and scalability. This research addresses a fundamental architectural flaw in how AI systems "remember," moving the field toward more dynamic, context-aware retrieval mechanisms that can handle the nuances of varied environments more effectively than static summaries.

## Implications
This work suggests that the architecture of "when" we curate information may be just as important as "how" we curate it, potentially simplifying the training process for developers by shortening the feedback loop for reward signals. For practitioners and researchers, this implies a shift toward systems that can dynamically synthesize context on-the-fly, allowing agents to maintain high performance without requiring perfectly optimized long-term storage summaries or complex, long-horizon credit assignment models.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2609.27334v1)
