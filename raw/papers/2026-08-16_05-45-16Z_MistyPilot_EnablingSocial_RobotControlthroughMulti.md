---
title: MistyPilot: Enabling Social-Robot Control through Multi-Agent LLM Skill Orchestration
published: 2026-08-16T05:45:16Z
authors: Xiao Wang, Lu Dong, Ifeoma Nwogu, Srirangaraj Setlur, Venu Govindaraju
url: http://arxiv.org/abs/2608.15549v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MistyPilot: Enabling Social-Robot Control through Multi-Agent LLM Skill Orchestration

## Abstract
Programming small social robots from natural-language instructions requires more than invoking isolated APIs. Interactive tasks combine reactive physical behaviors with stateful social behaviors, while existing interfaces often require developers to manually compose APIs into skills, configure their parameters, bind sensor events to skills, and manage task states at runtime. We present MistyPilot, a multi-agent LLM framework that interprets high-level natural-language instructions and orchestrates the corresponding skills on the Misty social robot. A Task Router dispatches each instruction to one of two specialized agents: a Physically Interactive Agent for sensor-triggered robot control and direct skill invocation, and a Social Interaction Agent for dialogue-oriented task-state management and context-dependent multimodal response generation. To improve efficiency, the Social Interaction Agent reuses previously generated results when applicable and invokes full generation otherwise. We evaluate MistyPilot on five component-level suites, with sensor bindings and skill invocations executed on the physical Misty robot, and a preliminary user study with 12 participants. MistyPilot attains high accuracy on routing, sensor-skill binding, task-state parsing, result reuse, and skill extension up to 100 skills, and lower variance than an otherwise identical single-agent baseline, while participants report positive perceptions of usability and interaction quality. The code will be made publicly available via the project page.

## Metadata
- **Published**: 2026-08-16T05:45:16Z
- **Authors**: Xiao Wang, Lu Dong, Ifeoma Nwogu, Srirangaraj Setlur, Venu Govindaraju
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15549v1)