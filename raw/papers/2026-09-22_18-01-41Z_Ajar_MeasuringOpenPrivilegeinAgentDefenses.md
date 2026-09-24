---
title: Ajar: Measuring Open Privilege in Agent Defenses
published: 2026-09-22T18:01:41Z
authors: Reshabh K Sharma, Linxi Jiang, Shuo Chen, Zhiqiang Lin
url: http://arxiv.org/abs/2609.26900v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Ajar: Measuring Open Privilege in Agent Defenses

## Abstract
A language model agent acts through the tools it is given. The data it reads while working on a task can redirect what it does with those tools. A growing set of techniques for safe and secure agent execution therefore sits between the agent and its tools, aiming to enforce access control, information flow or isolation at that boundary. Today these techniques are evaluated on agent-security benchmarks built around indirect prompt injection. Those benchmarks judge a defense by how far it brings the number of successful attacks down while preserving the agent's utility. A defense is judged only on the agent's execution. It can score well on both metrics while holding open a transfer, a deletion or a broad read that no task needed. Ajar measures that open privilege directly using the existing benchmarks. It attaches to an agent-security benchmark that already exists and reuses the tasks, tool schemas, reference solutions and goal states that benchmark uses to grade its own runs. For each benign task it builds candidate tool calls the task does not need, so allowing one is privilege left open. These calls are presented to the defense at every point where the agent could act. We evaluate Ajar by attaching it to AgentDojo, where open privilege becomes a third axis beside the existing attack success and benign utility. We run it on five defenses: Progent, CaMeL, AC4A, Permission Assistant, and Claude Code's Auto mode. We observed that they leave widely different amounts of privilege open. Two defenses leak by almost the same amount yet differ widely in the benign tasks they finish, and one defense buys part of its tightness by refusing calls its tasks were entitled to make. This open privilege cannot be derived from the measured attack success or benign utility. The source code of Ajar is available at https://github.com/reSHARMA/Ajar.

## Metadata
- **Published**: 2026-09-22T18:01:41Z
- **Authors**: Reshabh K Sharma, Linxi Jiang, Shuo Chen, Zhiqiang Lin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.26900v1)