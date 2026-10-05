---
title: Ego2World: Compiling Egocentric Cooking Videos into Executable Worlds for Belief-State Planning
published: 2026-10-02T02:51:03Z
authors: Qinchuan Cheng, Zhantao Gong, Pengzhan Sun, Angela Yao, Shijie Li
url: http://arxiv.org/abs/2610.02715v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Ego2World: Compiling Egocentric Cooking Videos into Executable Worlds for Belief-State Planning

## Abstract
Egocentric videos capture how people carry out everyday activities, yet testing an agent requires evaluating the consequences of actions it chooses itself. We introduce Ego2World, a benchmark that turns annotated cooking activities into executable planning environments under partial observation. Its compiler links source steps and objects to symbolic action rules, persistent world states, and explicit task conditions, so researchers can execute an agent's proposed actions and check their outcomes. World state and agent belief are maintained separately, enabling controlled studies of planning and information reuse across continuing tasks. Evaluating six planners on 105 tasks shows that accepted operations often leave task goals unmet. Execution traces and condition checks distinguish interrupted runs, partial attainment, and completed execution without goal attainment. In a separate paired Qwen-Plus study, persistent belief improves action validity by 4.15 percentage points and reduces visual-query attempts by 90.27%, with higher token use and no detected completion gain. Ego2World provides a reusable testbed for tracing how planning and memory choices affect execution, observation demand, and task attainment, connecting recorded human activity to the development and evaluation of interactive agents.

## Metadata
- **Published**: 2026-10-02T02:51:03Z
- **Authors**: Qinchuan Cheng, Zhantao Gong, Pengzhan Sun, Angela Yao, Shijie Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.02715v1)