---
title: ExRole: From Team Trajectories to Executable Roles in Multi-Agent Language Models
published: 2026-08-12T11:35:31Z
authors: Zhou Liu, Chaoyang Han, Zewei Pan, Zeli Su, Wentao Zhang
url: http://arxiv.org/abs/2608.11949v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ExRole: From Team Trajectories to Executable Roles in Multi-Agent Language Models

## Abstract
Roles provide an interpretable interface for organizing language-model agents, yet most multi-agent systems treat them as hand-written prompt labels disconnected from learned behavior and parameter updates. We argue that a useful role should instead be an executable control variable: it should summarize behavior predictive of future utility, guide subsequent interaction, and identify the trainable capacity responsible for that behavior. We introduce ExRole, a trajectory-to-role framework that learns future-aware role prototypes from prefix-local team traces, resolves them into readable instructions and token-aligned role markers, and optionally routes shared LoRA rank slots with turn-aligned credit. Across MuSiQue and 2WikiMultiHopQA, ExRole improves over single-agent search by 15.0/14.4 and 13.5/16.1 EM/F1 points, respectively. Against the strongest non-ExRole controls, the corresponding gains remain 11.5/11.6 and 7.7/9.7 points. Across both benchmarks, the controlled results consistently favor trajectory-induced role conditioning over role-free, manual, random, and shuffled alternatives. Role-Agent-Turn interventions further show that the induced roles capture transferable behavioral specialization beyond fixed agent identities or turn positions.

## Metadata
- **Published**: 2026-08-12T11:35:31Z
- **Authors**: Zhou Liu, Chaoyang Han, Zewei Pan, Zeli Su, Wentao Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.11949v1)