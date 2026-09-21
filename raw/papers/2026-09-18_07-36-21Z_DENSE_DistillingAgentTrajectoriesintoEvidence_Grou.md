---
title: DENSE: Distilling Agent Trajectories into Evidence-Grounded Shortcut Trees for Self-Refinement
published: 2026-09-18T07:36:21Z
authors: Siyuan Liu, Fan Yu, Dongyu Ru, Yizhu Liu, Yifan Yang, Xuezhi Cao, Xunliang Cai, Yixin Cao
url: http://arxiv.org/abs/2609.21423v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DENSE: Distilling Agent Trajectories into Evidence-Grounded Shortcut Trees for Self-Refinement

## Abstract
Online agent deployments produce abundant execution traces, while task-specific verification and expert annotation are costly to scale. We study how to distill these traces into reusable feedback without post-hoc outcome labels, drawing on their evidence of local progress, recovery, and unfinished requirements. We introduce DENSE (Distilling Evidence from Nested Subtask Executions), which organizes this evidence into evidence-grounded nested shortcut trees. DENSE compresses redundant attempts, reconciles issues across levels using recovery evidence, and summarizes completed branches while expanding unresolved ones, linking reusable progress to remaining obligations. We introduce REFIT, a source-paired protocol comparing feedback from shared initial trajectories under post-hoc outcome blindness, with environments and model contexts reset for fresh attempts at the same tasks. On Terminal-Bench 2.1, DENSE achieves the highest strict pass rate among tested non-privileged feedback methods across four recipient models. Relative to initial executions, strict pass rate improves by 7.12-15.64 pp, with 19.0-43.6% fewer observed recipient tokens in reruns. GPT-5.5 ablations support combining nested subtask analysis with shortcut construction and issue reconciliation. These findings point toward agent self-refinement through evidence-grounded trajectory reuse with less reliance on external supervision.

## Metadata
- **Published**: 2026-09-18T07:36:21Z
- **Authors**: Siyuan Liu, Fan Yu, Dongyu Ru, Yizhu Liu, Yifan Yang, Xuezhi Cao, Xunliang Cai, Yixin Cao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.21423v1)