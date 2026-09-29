---
title: AgentHabit: Characterizing Distinct Behaviors of Agents on Everyday Tasks
published: 2026-09-26T17:09:58Z
authors: Woojung Song, Hoyeol Yang, Jeonghoon Shim, Sungjib Lim, Jonggeun Lee, Yunho Choi, Yohan Jo
url: http://arxiv.org/abs/2609.32795v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AgentHabit: Characterizing Distinct Behaviors of Agents on Everyday Tasks

## Abstract
Large language model (LLM) agents assist users with everyday tasks that can be completed in many reasonable ways. Even when their answers are useful, how agents carry out these tasks may not match users' preferences and needs. For example, agents differ in whether they ask clarifying questions or search the web. We introduce HABIT, a taxonomy of 23 behavioral axes in five categories, which three authors and three LLMs derive bottom-up from 408 agent trajectories across 17 domains. On held-out tasks, HABIT distinguishes models more clearly than existing taxonomies of human values and agent actions while supporting comparably consistent annotation. Building on HABIT, we construct AgentHABIT, a benchmark that profiles each agent's behavioral tendencies from its trajectories on 86 everyday tasks. Profiling 18 models with AgentHABIT reveals a range of distinctive tendencies. For example, most GPT and Claude models state their assumptions and offer alternatives when requirements conflict, whereas Qwen and Google's models more often leave assumptions or changes to requirements unstated. These profiles remain recognizable even when built from entirely different sets of tasks, indicating that they reflect general tendencies rather than task-specific behavior. Prompting agents to adopt specific behaviors shifts some axes readily but barely changes others, while fine-tuning on another model's trajectories changes only part of a model's profile and leaves much of it intact. Overall, HABIT and AgentHABIT provide a systematic framework for characterizing how agents carry out everyday tasks beyond task success, offering insights to guide the development of agents whose behavior better fits users' needs.

## Metadata
- **Published**: 2026-09-26T17:09:58Z
- **Authors**: Woojung Song, Hoyeol Yang, Jeonghoon Shim, Sungjib Lim, Jonggeun Lee, Yunho Choi, Yohan Jo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32795v1)