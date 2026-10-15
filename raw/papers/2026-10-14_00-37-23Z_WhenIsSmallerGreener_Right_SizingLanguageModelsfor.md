---
title: When Is Smaller Greener? Right-Sizing Language Models for Agentic AI
published: 2026-10-14T00:37:23Z
authors: Sajid Siraj, Maria Barbati
url: http://arxiv.org/abs/2610.19345v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Is Smaller Greener? Right-Sizing Language Models for Agentic AI

## Abstract
AI agents use large language models (LLMs) to plan and act over multiple steps, yet models are usually compared per call rather than per completed task. This paper asks: which model should an agent use to complete tasks reliably while minimising energy, cost and time? We show that per-call comparisons can be misleading for agentic AI. Because a task succeeds only if all required steps succeed, small differences in per-step reliability can produce large differences in overall task success. Failed attempts also consume resources. We therefore evaluate models using energy, cost and time per successfully completed task, treating the completed task as the functional unit. On this basis, we develop a decision model for choosing LLMs in agentic workflows. The model applies to tasks with binary or graded outcomes and to settings with or without retries. We show that each resource has a crossover task length at which a smaller, less reliable model ceases to be the greener, cheaper or faster option. These crossovers divide tasks into three regimes: for short tasks smaller models are preferred, for long tasks larger models are preferred, and only between these extremes do preferences among objectives matter. We embed these results in a two-stage framework that separates efficiency from preference. A Pareto screen first removes models that are never competitive; a weighted decision is required only when a genuine trade-off remains. A pilot study of 15 open-weight models from five developers, ranging from 0.6B to 27B parameters, on two multi-step agent tasks with measured GPU energy supports the predicted structure. The model with the lowest energy per completed task changes with task length and task type, and observed crossover points generally match those predicted from per-step measurements. These findings provide a practical framework for right-sizing language models in agentic AI.

## Metadata
- **Published**: 2026-10-14T00:37:23Z
- **Authors**: Sajid Siraj, Maria Barbati
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19345v1)