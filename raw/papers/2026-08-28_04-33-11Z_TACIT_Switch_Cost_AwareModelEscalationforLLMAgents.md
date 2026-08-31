---
title: TACIT-Switch: Cost-Aware Model Escalation for LLM Agents from Censored Supervision
published: 2026-08-28T04:33:11Z
authors: Ji'an Lei, Jian Huang
url: http://arxiv.org/abs/2608.27911v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# TACIT-Switch: Cost-Aware Model Escalation for LLM Agents from Censored Supervision

## Abstract
Agents with smaller language-model backbones are less expensive but can drift into persistent failure modes, whereas those with larger backbones are generally more reliable but more costly. This reliability-cost trade-off motivates routing methods that decide when to invoke an agent with a larger backbone: before execution, after a fixed trajectory prefix, or locally at individual steps. Our method, TACIT-SWITCH, learns permanent handoff policies from accumulated trajectory evidence and Teacher-Annotated Censored Intervention Times (TACIT). It represents each annotation as an interval-censored observation on a cumulative-risk scale. The resulting mixture-cure threshold model estimates the probability that the paired Strong rollout succeeds and, conditional on success, the handoff threshold; no teacher is required at deployment. In a mechanism-based multi-step simulation, TACIT-SWITCH improves success by 7.4-11.1 percentage points over task-level, step-level, and fixed-prefix routing baselines at comparable cost. Within that controlled simulation, ablations show that task features and cumulative trajectory risk provide complementary information. With operating points selected on development data, TACIT-SWITCH achieves the highest held-out success among learned policies on both ALFWorld (48.5% with 4B Cheap; 45.5% with 9B Cheap) and DABench (73.1%).

## Metadata
- **Published**: 2026-08-28T04:33:11Z
- **Authors**: Ji'an Lei, Jian Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.27911v1)