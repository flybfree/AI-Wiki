---
title: DeltaReplay: Task-Relative Memory Reuse for Mobile GUI Agents
published: 2026-10-08T11:12:57Z
authors: Yudong Bai, Yihong Chen, Quanming Yao, Yaqing Wang
url: http://arxiv.org/abs/2610.11707v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DeltaReplay: Task-Relative Memory Reuse for Mobile GUI Agents

## Abstract
Memory-augmented mobile GUI agents store successful execution trajectories and reuse them in later tasks, but a stored trajectory rarely matches a new task exactly. The new task may use different parameters, share only some of its steps with a stored trajectory, or have no relevant record in memory. Forcing the agent to use irrelevant memory can mislead it, whereas discarding memory that may still be useful deprives it of guidance from past experience. To address this dilemma, we propose DeltaReplay, a step-level memory reuse framework that decides how to use existing memory without modifying it. We observe that the reusable part of a stored record is determined not by the record itself but by its relation to the new task, mainly through two factors: page-level consistency and action-level generality. We therefore store execution trajectories as paths in a transition graph, whose nodes (pages) and edges (actions between pages) capture these two factors. At reuse time, the action on each edge is split into a task-independent operation and task-specific parameters. DeltaReplay then compares each recorded step with the new task and the current screen, and decides whether to follow it, execute it after replacing its parameters, or leave it to the base agent. On AndroidWorld and SPA-Bench, DeltaReplay improves the task success rate over a base agent with the same backbone by up to 10.3 and 25.0 percentage points, respectively. These results indicate that deciding at each step how to use retrieved memory lets agents benefit even from partially matching trajectories.

## Metadata
- **Published**: 2026-10-08T11:12:57Z
- **Authors**: Yudong Bai, Yihong Chen, Quanming Yao, Yaqing Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.11707v1)