---
title: EconSkills: Studying Skill Transfer and Retrieval for Web Agents on Live Economic Data
published: 2026-09-17T00:29:46Z
authors: Yinzhu Quan, Zefang Liu
url: http://arxiv.org/abs/2609.19523v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EconSkills: Studying Skill Transfer and Retrieval for Web Agents on Live Economic Data

## Abstract
Web agents often revisit the same sites, yet most evaluations discard the procedures learned in earlier successful interactions. We introduce EconSkills, a skill library and evaluation framework that distills verified EconWebArena trajectories into parameterized standard operating procedures for retrieving live economic data. Each skill records its scope, navigation procedure, site-specific guidance, verification checks, and recovery steps while replacing source-instance values with placeholders. EconSkills separates two questions: whether a known relevant procedure transfers to a held-out task, and whether an agent can retain that benefit when selecting from a library. In controlled transfer, matched skills improve success over no-skill prompting and require fewer steps on paired successes, while abstraction is substantially more effective than replaying raw trajectories. At library scale, retrieval is competitive with the no-skill baseline overall and performs best on directly covered tasks; coverage-stratified outcomes show that approximate matches on uncovered tasks offset these gains. Browser trajectories further identify when procedural guidance shortens portal-specific navigation and when semantic verification remains necessary. These results establish that reusable economic web procedures can transfer across task instances and provide a concrete design target for coverage-aware selection and context delivery.

## Metadata
- **Published**: 2026-09-17T00:29:46Z
- **Authors**: Yinzhu Quan, Zefang Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.19523v1)