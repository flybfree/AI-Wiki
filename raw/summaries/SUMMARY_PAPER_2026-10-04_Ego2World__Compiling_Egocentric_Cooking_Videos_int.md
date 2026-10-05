---
title: Ego2World: Compiling Egocentric Cooking Videos into Executable Worlds for Belief-State Planning
url: http://arxiv.org/abs/2610.02715v1
type: paper-summary
date: 2026-10-04
source_paper: 2026-10-02_02-51-03Z_Ego2World_CompilingEgocentricCookingVideosintoExec.md
generated_at: 2026-10-04 21:36
model: qwen3.8-flash-next-iq3_xxs
---

## Summary
Ego2World introduces a benchmark that converts annotated egocentric cooking videos into executable planning environments operating under partial observation, enabling researchers to test agents by executing their proposed actions and verifying outcomes against persistent world states. The paper evaluates six planners across 105 tasks, finding that accepted operations frequently fail to achieve task goals, and demonstrates in a paired Qwen-Plus study that maintaining persistent belief improves action validity by 4.15 percentage points while reducing visual-query attempts by over 90%, though without yielding detected completion gains.

## Key Takeaways
- Ego2World's compiler links source video steps and objects to symbolic action rules, persistent world states, and explicit task conditions, creating a structured executable environment where an agent's proposed actions can be run and their consequences checked, separating world state from agent belief to enable controlled studies of planning and information reuse across continuing tasks.
- Evaluation of six planners on 105 cooking tasks reveals that operations accepted by the system often leave task goals unmet, and the benchmark's execution traces and condition checks can distinguish between interrupted runs, partial attainment, and completed execution that still fails to achieve the goal, exposing a critical gap between action validity and task success.
- In a separate paired study using Qwen-Plus, persistent belief-state maintenance improves action validity by 4.15 percentage points and reduces visual-query attempts by 90.27%, but at the cost of higher token consumption and with no detected improvement in task completion, highlighting a trade-off between memory efficiency and planning effectiveness.

## Context
This work sits at the intersection of egocentric video understanding, symbolic planning, and belief-state reasoning—three areas that have largely developed in isolation. Egocentric video datasets such as EPIC-KITCHENS have provided rich recordings of human activity, but converting those recordings into environments where an agent can plan, act, and be evaluated under partial observability has remained an open challenge. Ego2World addresses this gap by providing a compiler pipeline that bridges recorded human demonstrations to executable, stateful planning tasks, enabling rigorous evaluation of interactive agents rather than passive recognition systems.

## Implications
For the AI research community, Ego2World offers a reusable testbed that connects recorded human activity to the development and evaluation of interactive agents, allowing practitioners to trace how specific planning and memory design choices affect execution validity, observation demand, and task attainment. For industry applications in robotics, assistive technology, and embodied AI, the finding that action validity does not guarantee goal attainment underscores the need for agents that reason about task completion rather than merely executing locally valid operations. The demonstrated trade-off between persistent belief and token cost also informs practical deployment decisions for large language model-based planners operating under resource constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2610.02715v1)
