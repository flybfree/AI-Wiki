---
title: WorkWorlds: An Infrastructure for Evaluating AI Agents on Workplace Tasks
published: 2026-09-20T18:50:13Z
authors: Yining Hua, Levi Lian
url: http://arxiv.org/abs/2609.23806v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WorkWorlds: An Infrastructure for Evaluating AI Agents on Workplace Tasks

## Abstract
Many knowledge-work benchmarks are constructed around individual tasks, with the context needed for each task selected together with or after the task has been specified. This design measures performance on workplace-like tasks in an environment assembled for the task. When task specification guides which context is selected, the evaluation can encode task information into the environment and pre-complete part of the information-localization work that workplace performance normally requires. We introduce WorkWorlds, an evaluation infrastructure that separates organizational state from task specification. A world first fixes a revision, date, and employee seat and materializes the organizational state that employee can access; tasks are introduced only afterward. We implement WorkWorlds in a primary synthetic pharmaceutical company with 8 measured tasks across 6 employee seats, and construct additional organizational worlds. Across 192 matched evaluations, moving from task-curated context to the full role-visible workplace reduced evidence access from 90.4% to 74.5% and criterion pass from 79.4% to 68.2%, while pass conditional on evidence access remained nearly unchanged; most of the measured difference occurred before the agent reached sufficient evidence.

## Metadata
- **Published**: 2026-09-20T18:50:13Z
- **Authors**: Yining Hua, Levi Lian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.23806v1)