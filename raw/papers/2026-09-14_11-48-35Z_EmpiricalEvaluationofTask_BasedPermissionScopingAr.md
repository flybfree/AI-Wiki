---
title: Empirical Evaluation of Task-Based Permission Scoping Architecture for AI Agents
published: 2026-09-14T11:48:35Z
authors: Halil Burak Noyan
url: http://arxiv.org/abs/2609.15422v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Empirical Evaluation of Task-Based Permission Scoping Architecture for AI Agents

## Abstract
AI agents are provisioned the same as employee-owned hosts in many enterprise settings with a static credential set fixed at deployment which includes all permissions the employee role might ever need. Role-based access control made this compromise for human principals because scoping access per task was infeasible. For AI agents, the compromise leaves every credential standing exposed whether or not the current task uses them. These permissions can later be utilised by a compromised or misaligned agent. Prior work (Noyan, 2026) defined this as the task-context mismatch, and proposed a three-source permission architecture which includes role-based permission ceilings, a task permission classifier and policy-based prohibitions, together eliminating the exposure preemptively. The work released a 600-prompt labelled dataset to evaluate it.   This paper presents that evaluation end to end by implementing the security gate; a fine-tuned RoBERTa-large encoder which matched few-shot trained Claude Haiku 4.5 on classification quality (macro-F1 0.881 against 0.886, precision 0.897 against 0.842, severity-weighted residual risk 0.63 against 1.12). The results show the trusted component does not need to scale with the agent it supervises, and the scalable-oversight margin for this control method is wide.   We also propose an attack-surface elimination metric which shows the role ceiling alone closes 27.9% of the severity-weighted surface and adding the task classifier closes 84.4%. The gap displays security advantages of task-granular access control over role-granular, and AI agents are the first principal type for which the task-granular access control is enforceable because their tasks arrive as machine-readable text.   The research establishes task-based access control as a measured, potentially deployable mechanism for reducing attack surface in agentic deployments.

## Metadata
- **Published**: 2026-09-14T11:48:35Z
- **Authors**: Halil Burak Noyan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.15422v1)