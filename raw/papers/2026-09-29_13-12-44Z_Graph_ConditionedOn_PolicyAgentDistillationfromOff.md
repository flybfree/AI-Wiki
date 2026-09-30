---
title: Graph-Conditioned On-Policy Agent Distillation from Off-the-Shelf Teachers
published: 2026-09-29T13:12:44Z
authors: Xiaohan Yi, Wen Luo, Yani Huang, Junfeng Zhan, Asher Qin, Peilin Zhao, Xi Xiao
url: http://arxiv.org/abs/2609.37522v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Graph-Conditioned On-Policy Agent Distillation from Off-the-Shelf Teachers

## Abstract
On-policy distillation (OPD) trains compact language agents with teacher feedback on student-generated trajectories. In multi-turn tasks, compounding errors can move students beyond the teacher's effective supervision. We introduce Graph-Conditioned On-Policy Agent Distillation (GC-OPD), which enriches an off-the-shelf teacher's scoring context with execution evidence. A graph indexes repeated teacher executions by shared states while preserving complete successful and failed histories. After each student episode, GC-OPD retrieves current-state references or historical alternatives and combines them with student hindsight to score the original thought-action tokens. Using the same original teachers, GC-OPD improves mean success over vanilla OPD from 24.70% to 48.78% on ScienceWorld (4B student), from 53.36% to 85.26% on ALFWorld Unseen, and from 29.10% to 37.65% on WebShop. At matched student sizes, it also achieves higher mean success than every evaluated OPD baseline using GRPO-trained teachers on ScienceWorld and ALFWorld; the strongest such ScienceWorld 4B baseline reaches 46.66%. GC-OPD requires no task-specific teacher optimization.

## Metadata
- **Published**: 2026-09-29T13:12:44Z
- **Authors**: Xiaohan Yi, Wen Luo, Yani Huang, Junfeng Zhan, Asher Qin, Peilin Zhao, Xi Xiao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.37522v1)