---
title: Teacher-Student Gaps Are Not Enough: Outcome-Guided On-Policy Distillation for Multi-Turn Autonomous Agents
published: 2026-09-28T14:49:13Z
authors: Tong Zhang, Zhou Liu, Yihao Liu, Jiahua Bao, Xuchen Li, Honglin Lin, Tao Cheng, Zhihan Yu, Kai Tang, Xiaoxi Jiang, Guanjun Jiang
url: http://arxiv.org/abs/2609.35319v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Teacher-Student Gaps Are Not Enough: Outcome-Guided On-Policy Distillation for Multi-Turn Autonomous Agents

## Abstract
On-policy distillation (OPD) trains a student on its own trajectories with dense teacher supervision. Recent work on OPD for multi-turn autonomous agents often treats large teacher-student token-level distributional gaps as promising intervention points, linking larger gaps to a greater need for correction. Yet, our empirical analysis reveals a supervision-benefit mismatch: large gaps can be benign, while small gaps can be outcome-critical. Teacher-student gaps capture differences at the current turn, whereas the benefit of teacher guidance depends on how the current student interacts with the environment afterward. The student may still succeed despite choosing an action that differs from the teacher's, while a teacher-preferred action may lead to a state from which the student cannot complete the task. Local gaps alone are therefore not enough to determine whether teacher guidance benefits the current student. Effective supervision should instead emphasize guidance that the current student can translate into better final task outcomes. Accordingly, we propose Outcome-Guided On-Policy Distillation (OG-OPD), which applies trajectory-relative weighting to teacher supervision and calibrates these weights using final task outcomes from paired student continuations. This calibration selectively strengthens supervision on the student's original trajectories at turns where teacher guidance benefits the current student. Across ALFWorld, ScienceWorld, and WebShop, OG-OPD consistently outperforms baselines under diverse settings. It improves task success rates by 3.6-17.7 percentage points over vanilla OPD and by up to 7.0 percentage points over the strongest baseline.

## Metadata
- **Published**: 2026-09-28T14:49:13Z
- **Authors**: Tong Zhang, Zhou Liu, Yihao Liu, Jiahua Bao, Xuchen Li, Honglin Lin, Tao Cheng, Zhihan Yu, Kai Tang, Xiaoxi Jiang, Guanjun Jiang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.35319v1)