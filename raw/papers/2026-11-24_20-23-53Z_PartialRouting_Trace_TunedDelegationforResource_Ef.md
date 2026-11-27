---
title: Partial Routing: Trace-Tuned Delegation for Resource-Efficient Agentic Workflows
published: 2026-11-24T20:23:53Z
authors: Siddharth Arya, Kshitij Jain
url: http://arxiv.org/abs/2611.33402v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Partial Routing: Trace-Tuned Delegation for Resource-Efficient Agentic Workflows

## Abstract
AI models vary enormously in capability and price. Model routing exploits this by sending easier tasks to cheaper models. However, a single agentic task often combines easy and difficult subtasks, making one model choice for the entire task inefficient. We introduce partial routing, which guides a frontier lead model to delegate suitable subtasks to a cheaper worker model. From both models' past runs, we identify recurring subtasks and measure each model's quality and cost on them. These measurements produce delegation guidance, with a parameter, $δ$, controlling how much is delegated. The lead decides when and what to delegate during execution, without training either model. On held-out tasks from ViBench and Terminal-Bench 4.0, partial routing achieves higher mean task performance than the lead alone and task-level routing. With $δ= 0.75$, it raises the lead's ViBench score from 70.2 to 78.5 at 19% lower cost, and its Terminal-Bench pass rate from 54% to 61% at similar cost. Giving the lead only the subtask breakdown, without a worker, also reduces cost on both benchmarks and raises the Terminal-Bench pass rate. These results show that analysis of past runs can support more efficient planning and more effective delegation, with little cost and implementation overhead.

## Metadata
- **Published**: 2026-11-24T20:23:53Z
- **Authors**: Siddharth Arya, Kshitij Jain
- **Source**: [ArXiv Link](http://arxiv.org/abs/2611.33402v1)