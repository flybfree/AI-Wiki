---
title: Agentic Self-Awareness: Aligning Knowing, Acting, and Holding
published: 2026-10-13T21:44:39Z
authors: Qinglin Chen, Hiroaki Hayashi, Jiaxin Zhang, Chien-Sheng Wu
url: http://arxiv.org/abs/2610.19226v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agentic Self-Awareness: Aligning Knowing, Acting, and Holding

## Abstract
Frontier AI agents increasingly act in environments where seemingly solvable tasks may lack prerequisites, contain conflicting requirements, or reveal blockers only during execution. We formulate agentic self-awareness (ASA) as the alignment of task-grounded feasibility judgments (know), warranted behavior (act), and responses to reconsideration (hold), distinguishing what a task permits from what an agent can solve. We build paired feasible and blocked tasks in Terminal-Bench 2.1 and retail $τ^2$-bench and introduce an authorship-aware M0-M3 rubric that separates recognizing a blocker from taking the certified deferral action for the correct reason. Separate probes assess stated feasibility beliefs and responses to a single challenge. In a Terminal-Bench protocol baseline, blocker recognition reaches 84.4%, but strict self-awareness (SA) reaches only 40.6%. Harness search without model-weight updates increases strict SA from 45.3% to 93.8% on reused Terminal-Bench search tasks; selection for abstention alone, however, can reduce success on feasible tasks. Independently initialized joint-objective searches improve both blocked-task SA and feasible-task solve on their own search sets. Retail held-out gains remain limited, and Terminal-Bench blocked-task transfer is not measured. This evaluation pipeline makes the recognition-action gap measurable and sets a two-sided target for improving agent decisions under changing task evidence.

## Metadata
- **Published**: 2026-10-13T21:44:39Z
- **Authors**: Qinglin Chen, Hiroaki Hayashi, Jiaxin Zhang, Chien-Sheng Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.19226v1)