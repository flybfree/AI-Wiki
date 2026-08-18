---
title: AeroCopilotBench: A Two-Tier Benchmark for Evaluating LLM Agents as Aviation Copilots in an Interactive Virtual Cockpit Environment
published: 2026-08-17T09:53:52Z
authors: Yuchen Yuan, Zhenghuang Wu, Yuangan Li, Liang Ma, Ke Li
url: http://arxiv.org/abs/2608.16349v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# AeroCopilotBench: A Two-Tier Benchmark for Evaluating LLM Agents as Aviation Copilots in an Interactive Virtual Cockpit Environment

## Abstract
Large language model (LLM) agents may assist flight crews with complex decisions and task execution, but existing aviation evaluations centered on static knowledge do not support systematic testing of procedural execution and safety compliance in interactive environments. This paper presents the AeroCopilot Operational Environment (ACOE), a reproducible interactive virtual-cockpit test environment, and AeroCopilotBench, a two-tier aviation agent evaluation benchmark. Tier-1 evaluates aviation knowledge using 1,200 multiple-choice questions, while Tier-2 comprises 73 emergency and abnormal tasks derived from the manufacturers' Pilot's Operating Handbooks (POHs) and instantiated in ACOE. ACOE converts natural-language procedures into executable state transitions, final-state goal conditions, and hard safety constraints, enabling models to interpret cockpit state, diagnose faults, and operate aircraft systems through standardized tool interfaces. We establish a safety-gated evaluation framework in which a trajectory succeeds only when all task goals are achieved without violating any hard safety constraint, while safe goal progress and trajectory safety are measured separately. Across 12 models, the highest Tier-2 success rate is 72.6%, while static knowledge performance does not consistently translate into procedural execution. Analysis of 451 failed episodes from 3 representative models identifies recurring failures in procedural completeness, use of state feedback, and long-horizon execution management. These findings motivate state-aware agent orchestration, joint assessment of task completion and trajectory safety, and repeated regression testing. ACOE and AeroCopilotBench provide a reproducible foundation for testing knowledge application, interactive execution, and operational safety in aviation agents.

## Metadata
- **Published**: 2026-08-17T09:53:52Z
- **Authors**: Yuchen Yuan, Zhenghuang Wu, Yuangan Li, Liang Ma, Ke Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16349v1)