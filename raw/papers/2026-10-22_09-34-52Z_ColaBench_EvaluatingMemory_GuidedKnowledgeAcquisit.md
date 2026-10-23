---
title: ColaBench: Evaluating Memory-Guided Knowledge Acquisition in Personal Agents
published: 2026-10-22T09:34:52Z
authors: Wenjie Zhang, Zhichao Shi, Xuhui Jiang, Xiaojun Wu, Cehao Yang, Chengjin Xu, Xiaoning Song
url: http://arxiv.org/abs/2610.30989v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ColaBench: Evaluating Memory-Guided Knowledge Acquisition in Personal Agents

## Abstract
Personal agents need to draw on long-term interaction history to retrieve and apply external knowledge suited to a user's current request. Even an answer grounded in relevant documents can be unsuitable when it overlooks the user's circumstances. This creates two connected challenges: using historical conditions to identify the knowledge needed for a new request, and applying that knowledge to the user's situation. Existing benchmarks advance memory recall, personalized retrieval, and memory-guided action, while the joint evaluation of these two challenges remains underexplored. We introduce ColaBench, a synthetic benchmark in health and daily living, with 349 tasks across 10 Profiles and a knowledge base of 13,033 documents. Its Evidence Graph connects personal conditions to their disclosures across public interaction sessions, records prior document exposure, and links answer requirements to personal and newly acquired document evidence. We also introduce MemKB, which uses state summaries to inform queries and rule application, and memory-document links to retrieve knowledge associated with the user's history. MemKB achieves 86.25% Accuracy with an average of 4.07 interaction rounds per task. Task-level analysis finds larger gains on tasks integrating information across multiple historical Facts; error analysis further identifies unsupported personal assumptions and rule misapplication as obstacles to using retrieved evidence. ColaBench provides traceable tasks and an evaluation framework for studying how memory guides knowledge acquisition and rule application.

## Metadata
- **Published**: 2026-10-22T09:34:52Z
- **Authors**: Wenjie Zhang, Zhichao Shi, Xuhui Jiang, Xiaojun Wu, Cehao Yang, Chengjin Xu, Xiaoning Song
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.30989v1)