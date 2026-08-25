---
title: Physical Agentic AI: An Architecture for Orchestrating a Robot Crew with LLMs
published: 2026-08-23T23:35:31Z
authors: Xinyuan Liu, Eren Sadikoglu, Riana Chatterjee, Ransalu Senanayake
url: http://arxiv.org/abs/2608.22657v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Physical Agentic AI: An Architecture for Orchestrating a Robot Crew with LLMs

## Abstract
Agentic AI frameworks interpret open-ended task goals and decompose them into multi-step plans. Richer information about embodiment-specific capabilities, physical preconditions, and cross-robot coordination improves grounding, but does not eliminate infeasible, mistimed, or unsafe physical actions. Physical robot crews therefore require an explicit architectural interface between semantic planning and execution, where every planned action is verified against robot capabilities, system state, and workflow constraints before actuation. This paper introduces Physical Agentic AI, a framework for skill-grounded robot agent orchestration, in which each robot exposes a typed library of executable skills while a foundation model planner decomposes a task into phases and assigns each phase to a robot-skill pair. A Robot Orchestration layer exposes the skill library, robot state, named locations, and workflow contracts to a non-actuating Mission Planner, while a deterministic Robot Orchestrator validates and authorizes one skill at a time. We evaluate on a drone-UGV search-and-dispatch mission, where every mission in every condition is executed live in Gazebo, and on a humanoid-quadruped transportation task using hardware-equivalent skill interfaces plus two physical trials on a Unitree G1 and Go2. Varying planner knowledge and runtime enforcement independently, we find that retrieval raises skill grounding from 51% to 96% yet leaves informed planners dispatching 23-29% of faulted steps. Per-dispatch enforcement reduces false dispatch to 0% with no false blocks, and a held-plan ablation confirms that the gate, not plan variation, is responsible. Live execution makes the difference physical: without enforcement all eight injected faults crossed the orchestration boundary and six produced robot motion; with enforcement all eight were refused before motion.

## Metadata
- **Published**: 2026-08-23T23:35:31Z
- **Authors**: Xinyuan Liu, Eren Sadikoglu, Riana Chatterjee, Ransalu Senanayake
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22657v1)