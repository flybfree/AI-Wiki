---
title: Skill Issue: Lessons from Optimizing Repository SKILLs for Coding Agents
published: 2026-09-11T11:41:29Z
authors: Mykhailo Kozyrev, Andrei Kozyrev, Anton Podkopaev
url: http://arxiv.org/abs/2609.12742v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Skill Issue: Lessons from Optimizing Repository SKILLs for Coding Agents

## Abstract
Coding agents increasingly read repository knowledge from SKILLs --- plain \texttt{.md} files versioned alongside the code. Recent work synthesizes these files automatically, by optimizing the document against a benchmark. A bare repository comes with no benchmark, and the synthetic tasks prior work builds are small enough that a capable agent saturates them with no document at all. We mine harder tasks --- merged pull requests of the repository, reverted at a single frozen base commit; and score a candidate document by whether the same agent does better with it than without it. On three Kotlin repositories, the documents GEPA finds raise this score by $4.9$pp on average, and the ones SkillOpt finds leave it where it started, $0.1$pp above the seed. The GEPA gain matches what prior work reports with the same optimizer, and at the dataset size a single repository supplies it cannot be separated from the agent's run-to-run variance; settling that would take more tasks than one repository's history yields. The documents themselves read better than the score: a maintainer of one repository found in them knowledge one only gets by working in the project.

## Metadata
- **Published**: 2026-09-11T11:41:29Z
- **Authors**: Mykhailo Kozyrev, Andrei Kozyrev, Anton Podkopaev
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.12742v1)