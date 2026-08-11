---
title: MoRSE: Task-Oriented Multi-Agent System with Mixture of Role-Subtask Experts
url: http://arxiv.org/abs/2608.09251v1
type: paper-summary
date: 2026-08-10
source_paper: 2026-08-10_08-11-24Z_MoRSE_Task_OrientedMulti_AgentSystemwithMixtureofR.md
generated_at: 2026-08-10 22:06
model: nvidia/nemotron-3-nano-4b
---

## Summary
This paper presents MoRSE, a task‑oriented multi‑agent system that enables agents to specialize both at the structural level (role and subtask) and at the parameter level using LoRA adapters. The authors demonstrate that this dual specialization improves whole‑task and step‑wise performance on code‑generation benchmarks across three backbones, with gains generalizing to unseen task categories.  

## Key Takeaways
- Agents are distinguished by (role, subtask)-conditional specialization at both the task structure and parameter levels.  
- A dynamic mixture of role‑subtask LoRA experts is augmented by a prototype‑based semantic router for cost‑effective adaptation.  
- Hierarchical group‑relative policy optimization with two‑layer credit assignment isolates expert updates from routing variance, stabilizing learning under sparse rewards.  

## Context
Multi‑agent systems based on large language models often rely on coarse prompt‑level differentiation, limiting the ability to create heterogeneous agents that can handle complex subtasks efficiently. This work moves beyond such simplistic approaches by embedding specialization directly into the model’s parameters and task architecture.  

## Implications
The method offers a scalable framework for deploying specialized LLM agents in industry settings where fine‑tuning each agent is costly. By decoupling expert updates from routing decisions, it reduces variance and improves robustness, making it valuable for applications that require reliable, long‑horizon collaboration across diverse tasks.

## Original Paper Reference
- **Source**: [Original Paper](http://arxiv.org/abs/2608.09251v1)
