---
title: ProgramDistill: From Interactive Web Apps to Verifiable Reference-Guided SWE Tasks
published: 2026-09-16T15:19:05Z
authors: Jeonghye Kim, Minseon Kim, Young Jin Kim, Matheus Pereira, Marc-Alexandre Côté, Alessandro Sordoni, Xingdi Yuan, Zhengyan Shi
url: http://arxiv.org/abs/2609.18805v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ProgramDistill: From Interactive Web Apps to Verifiable Reference-Guided SWE Tasks

## Abstract
Coding agents are typically evaluated with desired behavior specified through issues or instructions. In practical web development, however, agents may need to infer behavior from working software and implement it in an incomplete application. We introduce ProgramDistill, a benchmark evaluating coding agents on features discovered through interaction with fully functional reference applications. We build ProgramDistill by factorizing applications into features of different granularities, each associated with replayable behaviors executable via its gold patch. Our pipeline, mine-craft-patch, discovers 1,975 replay-verified behaviors across 26 applications and constructs 4,063 tasks without human intervention. Across nine frontier coding agents, GPT-6 Astra and Claude Opus 5 achieve 49.2% and 28.8% success on cumulative workflows in full-application reconstruction. In partial-application reconstruction, success falls from 100% to 64.0% and from 96% to 32% as restoration depth increases from 1 to 8. ProgramDistill thus provides a scalable benchmark with controlled difficulty for evaluating and diagnosing coding agents, and a natural basis for future curriculum-based training.

## Metadata
- **Published**: 2026-09-16T15:19:05Z
- **Authors**: Jeonghye Kim, Minseon Kim, Young Jin Kim, Matheus Pereira, Marc-Alexandre Côté, Alessandro Sordoni, Xingdi Yuan, Zhengyan Shi
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.18805v1)