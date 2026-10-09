---
title: Harness Compilation: Which Decisions Should a Small Vision-Language Model Keep?
published: 2026-10-08T04:31:36Z
authors: Minhao Fan, Yinyi Liu, Jiayu Zhao, Zihan Teng, Song Chen, Weichen Liu
url: http://arxiv.org/abs/2610.11231v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Harness Compilation: Which Decisions Should a Small Vision-Language Model Keep?

## Abstract
Small vision-language models may be able to read external evidence yet struggle to obtain it. We introduce Harness Compilation (HC), an offline procedure that adapts the division of work between a frozen small VLM and its external harness. A large teacher uses student execution traces to revise reusable content and control, while a separate validation set selects the deployed harness. Deployment requires neither weight updates nor teacher calls. Across seven visual question-answering settings with students of at most 9B parameters, HC improves scores over bare students by 9.9-23.9 points, averaged over three independent builds per setting. Interventions on five runtime decision types (invocation, selection, argument generation, evidence integration and abstention) show why this allocation matters: requesting evidence and generating open queries can be costly, whereas bounded choices and reading supplied text can remain useful student work. Fact cards benefit all ten evaluated students, but decision policies transfer unevenly. Recompilation for a new student model helps when the transferred interface no longer fits the student. With 100 practice items, HC exceeds answer-only LoRA on three tasks. Larger training budgets can match or surpass a fixed harness, while combining the two improves SlideVQA beyond either alone. These findings support allocating work from measured student behavior rather than uniformly removing decisions.

## Metadata
- **Published**: 2026-10-08T04:31:36Z
- **Authors**: Minhao Fan, Yinyi Liu, Jiayu Zhao, Zihan Teng, Song Chen, Weichen Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.11231v1)