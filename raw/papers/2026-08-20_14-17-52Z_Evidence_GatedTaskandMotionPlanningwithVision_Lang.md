---
title: Evidence-Gated Task and Motion Planning with Vision-Language Models
published: 2026-08-20T14:17:52Z
authors: Tsunehiko Tanaka, Matthew Stephenson, Alistair Macvicar, Edgar Simo-Serra
url: http://arxiv.org/abs/2608.20084v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evidence-Gated Task and Motion Planning with Vision-Language Models

## Abstract
Robots executing long-horizon manipulation tasks from natural-language instructions must reason about both semantic task structure and geometric feasibility. However, under partial observability, the availability of goal-relevant objects may be uncertain. In such cases, approaches that combine Vision-Language Models (VLMs) with Task and Motion Planning (TAMP) may generate subgoals that rely on the VLM's prior knowledge without observational support, leading to execution failures or unintended outcomes. We propose Evidence Acquisition and Feasibility Gating (EAFG), a framework that acquires visual evidence through VLM-generated exploratory subgoals and TAMP-based execution. EAFG then applies a feasibility gate to decide whether to proceed with task planning, acquire further evidence, or halt. Our experiments show that, in cooking tasks with ambiguous object use, EAFG improves recipe completion by discovering task-relevant objects before planning. For instructions requiring an absent object, EAFG promotes appropriate halt decisions and reduces repeated attempts to manipulate that object.

## Metadata
- **Published**: 2026-08-20T14:17:52Z
- **Authors**: Tsunehiko Tanaka, Matthew Stephenson, Alistair Macvicar, Edgar Simo-Serra
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.20084v1)