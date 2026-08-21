---
title: Evidence-Gated Task and Motion Planning with Vision-Language Models
url: http://arxiv.org/abs/2608.20084v1
type: paper-summary
date: 2026-08-20
source_paper: 2026-08-20_14-17-52Z_Evidence_GatedTaskandMotionPlanningwithVision_Lang.md
generated_at: 2026-08-20 22:10
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper introduces Evidence Acquisition and Feasibility Gating (EAFG), a method that combines Vision‑Language Models with Task and Motion Planning to handle long‑horizon manipulation tasks under partial observability. By generating exploratory subgoals from the VLM, EAFG acquires visual evidence before planning, and then uses a feasibility gate to decide whether to proceed, gather more data, or stop. Experiments on cooking tasks show higher recipe completion rates when objects are ambiguous, while instructions for absent objects lead to correct halts instead of repeated failures.

## Key Takeaways
- The framework generates VLM‑driven subgoals that provide visual evidence before full task planning, enabling robots to discover relevant objects in ambiguous scenes.  
- A feasibility gate evaluates whether the accumulated evidence supports safe execution, allowing the system to pause or halt when the goal is unattainable.  
- In tasks where an object does not exist, EAFG correctly decides to stop rather than continue attempting manipulation of a non‑existent item.

## Context
Robots must interpret natural‑language instructions that specify both semantic actions and spatial requirements, yet real‑world scenes often lack full visibility or contain ambiguous objects. Existing approaches either rely solely on prior knowledge or fail when observations are missing, leading to unsafe or incomplete task completion. This work bridges the gap by integrating evidence‑based acquisition with formal planning.

## Implications
EAFG offers a practical pathway for deploying robots in kitchen and service environments where visual cues are uncertain. Practitioners can reduce costly retries and improve user trust by ensuring that actions are only taken when supported by concrete evidence, aligning AI systems with real‑world constraints.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.20084v1)
