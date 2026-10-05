---
title: DeReAct: Decomposed Reasoning and Acting for Reliable AI Agents
published: 2026-10-01T18:25:07Z
authors: Ajay Vohra, Tao Chen, Neeti Narayan, Caron Zhang
url: http://arxiv.org/abs/2610.02351v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DeReAct: Decomposed Reasoning and Acting for Reliable AI Agents

## Abstract
ReAct-based agents typically rely on a single LLM policy to propose actions, interact with the environment, and decide when a task is complete. This coupling makes action authorization and completion control difficult to enforce independently, allowing errors to propagate and unsupported completion claims to terminate execution. We introduce DeReAct, a modular agent architecture that externalizes two gating policies: a Critic that validates proposed actions before execution, and a Context Manager that reconstructs an environment-supported \textsc{State} and certifies task completion.   Across GAIA and SWE-bench Verified, DeReAct improves Pass@1 most for weaker Brain models, with gains of 6.5--7.0 points for Qwen3-Coder-480B and 4.2--5.2 points for Claude Sonnet~4.5; gains diminish as Brain capability increases. Trajectory and ablation analyses show that external gating is effective when targeted failures are sufficiently prevalent and the gating policy is itself sufficient. With Claude Opus~4.5, Pass@1 remains comparable to ReAct, while DeReAct produces more evidence-complete and constraint-satisfying trajectories, indicating that completion control can trade earlier termination for stronger grounding. Overall, DeReAct improves weaker agents while retaining grounding benefits as models strengthen.

## Metadata
- **Published**: 2026-10-01T18:25:07Z
- **Authors**: Ajay Vohra, Tao Chen, Neeti Narayan, Caron Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.02351v1)