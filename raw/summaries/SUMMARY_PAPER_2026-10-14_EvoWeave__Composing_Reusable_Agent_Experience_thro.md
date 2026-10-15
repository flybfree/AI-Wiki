---
title: EvoWeave: Composing Reusable Agent Experience through Operation Level Graphs
url: http://arxiv.org/abs/2610.19381v1
type: paper-summary
date: 2026-10-14
source_paper: 2026-10-14_01-28-06Z_EvoWeave_ComposingReusableAgentExperiencethroughOp.md
generated_at: 2026-10-14 20:59
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
EvoWeave introduces a structured experience-memory framework for interactive agents that stores reusable operations as directed edges between abstract state nodes, each annotated with input/output contracts, provenance, and capability references. By decomposing a current task into a dependency graph and performing bounded directed search over stored operation fragments, the framework enables agents to compose relevant past experience without the noise of full workflow retrieval or the loss of critical dependencies from isolated operation retrieval. Across four benchmarks and three language model backbones, the approach yields consistent improvements over memory-free baselines on AppWorld tasks, with ablation studies confirming that the directed graph structure itself contributes meaningfully to performance gains.

## Key Takeaways
- The framework addresses a fundamental tension in agent memory design: retrieving entire past workflows injects irrelevant steps that confuse the agent, while retrieving isolated operations strips away the dependency context needed for valid reuse. EvoWeave resolves this by representing operations as directed edges with explicit input and output contracts, provenance metadata, and capability references, so that retrieval can respect the dependency structure of a task while excluding unrelated steps.
- The system architecture separates planning, retrieval, execution, and reflection into distinct stages. A planner decomposes the current task into a dependency graph, operation retrieval and bounded directed search assemble relevant experience fragments, an execution agent inspects those fragments and their referenced capabilities, and a reflection module separates concrete execution evidence from reusable abstractions, preventing overfitting to specific past instances.
- Empirical results demonstrate measurable benefits: AppWorld Normal and Challenge goal-completion rates average 51.91 and 27.99, exceeding the no-memory baseline by 6.99 and 4.99 percentage points respectively. An ablation study isolates the contribution of directed connections, showing an additional 2.08-point improvement over independent operation cards, confirming that the graph topology—not merely the presence of stored operations—drives the performance gain.

## Context
This work sits at the intersection of agent memory systems, compositional task planning, and retrieval-augmented generation for autonomous agents. As language-model-based agents are increasingly deployed on multi-step interactive tasks such as software manipulation and tool use, the question of how to store, retrieve, and compose past experience without introducing noise or losing structural dependencies has become a central bottleneck. Prior approaches typically store either full trajectories or flat operation cards, both of which fail to capture the dependency structure that makes an operation valid in a new context. EvoWeave contributes a graph-based memory representation that treats task composition as a first-class concern, aligning with broader research trends in hierarchical planning, skill libraries, and program synthesis for agents.

## Implications
For practitioners building agent systems on benchmarks like AppWorld or similar interactive environments, the results suggest that investing in structured, dependency-aware memory representation yields consistent gains across multiple model backbones, reducing reliance on larger or more expensive models. The explicit tradeoffs the authors expose—retrieval overhead versus valid reuse conditions—provide a practical guide for engineering teams deciding how much graph structure to maintain in production agent memory. More broadly, the framework points toward a future where agents accumulate and compose reusable operation libraries over time, potentially enabling long-lived autonomous systems that improve through experience rather than requiring retraining or prompt engineering for each new task.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.19381v1)
