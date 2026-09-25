---
title: Where Cyber Agents Struggle: Bottleneck Analysis of Multi-Stage LLM Agents
published: 2026-09-23T11:58:25Z
authors: Saeedeh Lohrasbi, Mohammad Mamun, Ahmed Yehia, Scott Buffett, Sherif Saad
url: http://arxiv.org/abs/2609.28572v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Where Cyber Agents Struggle: Bottleneck Analysis of Multi-Stage LLM Agents

## Abstract
Multi-stage LLM-based cyber agents may complete attack workflows while remaining brittle, costly, or reliant on incorrect interpretations of execution evidence. Success rates alone obscure inefficiency, adaptation through retries, and recognition of success or failure. We present an end-to-end diagnostic study of an Autonomous Adversary system with orchestrator, executor, and validator LLMs in enterprise-like lateral-movement scenarios. Six frontier models are evaluated across two scenarios and three modes: expert-defined, self-scaffolded, and fully autonomous. We assess validator consistency and evidence grounding; introduce a subtask-conditioned, cost-aware score for abnormal token use, retries, and runtime; and use comparative LLM-as-a-Judge analysis to identify planning deficiencies, including tool misalignment, plan similarity, over-specification, inadequate probing, and weak recovery. Validators are generally relevant and evidence-grounded but often nonspecific and overly optimistic. Bottlenecks cluster in credential and lateral-movement tasks, spread with scenario complexity, and vary more under full autonomy. Reliable evaluation must assess outcomes, evidence interpretation, resource use, and adaptation after failure.

## Metadata
- **Published**: 2026-09-23T11:58:25Z
- **Authors**: Saeedeh Lohrasbi, Mohammad Mamun, Ahmed Yehia, Scott Buffett, Sherif Saad
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.28572v1)