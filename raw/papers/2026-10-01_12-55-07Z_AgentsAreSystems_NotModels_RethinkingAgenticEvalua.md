---
title: Agents Are Systems, Not Models: Rethinking Agentic Evaluation
published: 2026-10-01T12:55:07Z
authors: Luis Wiedmann, Leander Girrbach, Cordelia Schmid, Zeynep Akata
url: http://arxiv.org/abs/2610.01618v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agents Are Systems, Not Models: Rethinking Agentic Evaluation

## Abstract
Agent evaluations increasingly go beyond a single success rate, reporting metrics such as cost, consistency, and robustness. Yet they typically treat the agent itself as fixed. In practice, an agent is a configurable system: users decide what to tell it, how long to let it run, and which model to use, and each of these choices can change how well and how consistently it performs. We study these choices on a new benchmark of four scientific tasks, where a coding agent must find and correctly operate a published specialist model. We investigate five parts of the agent's configuration: task information, reasoning, self-verification, time budget, and backbone model. We find substantial run-to-run variability, with approximately 54% of the outcome variance coming from repeating the same configuration rather than changing it. Across configurations, the information provided to the agent has the largest effect, exceeding both time budget and model size, while also reducing cost and improving calibration. Configuration choices also interact: additional time helps only when the agent has sufficient information or a capable enough model to use it. Finally, a trajectory-based taxonomy of agent behavior reveals that prompting an agent to verify its answer has little effect on its verification behavior, whereas providing a dedicated verification tool changes that behavior substantially. These results suggest that agents should be evaluated as configurable systems themselves, and that some desired behaviors are more effectively implemented in the system than requested through prompting. We release the benchmark and more than 18,000 agent trajectories.

## Metadata
- **Published**: 2026-10-01T12:55:07Z
- **Authors**: Luis Wiedmann, Leander Girrbach, Cordelia Schmid, Zeynep Akata
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.01618v1)