---
title: What the Specification Did Not Say: Specification-Oracle Gaps in Test-Graded Coding-Agent Benchmarks
published: 2026-10-22T02:56:44Z
authors: Fei Ding
url: http://arxiv.org/abs/2610.30635v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What the Specification Did Not Say: Specification-Oracle Gaps in Test-Graded Coding-Agent Benchmarks

## Abstract
Coding-agent benchmarks often describe a task in natural language but grade it with tests taken from the upstream project. Passing those tests can require information the description never states: a constant's name, a module path, an exact message. We call this a specification-oracle gap: where it exists, a benchmark also measures whether an agent reproduces upstream implementation details. We formalise the gap, including the inconsistencies that chains of dependent tasks add, and build a static audit for five languages that classifies every name-, path- and literal-level dependency of every scored test (held-out precision 89.2%, recall 92.9%). On SWE-Milestone (98 graded milestones, 35 published runs), 25 milestones contain a test that depends on an unstated, non-inferable name or path. Build units with such a dependency fail in 80.6% of runs, against 48.4% for comparable units without one, and withholding a single hidden name from the reference stops its unit's tests from compiling in 126 of 128 cases. The leaderboard's ranking is robust to removing the affected tests, but they shift scores within repositories and favour agents that reproduce upstream names. Across four further benchmarks, prevalence appears to follow construction: a third or more of the tasks are affected where specifications are release notes or LLM summaries, almost none where tasks are screened or written for their tests; how much a gap costs depends on how the harness grades. We release the audit, corrected filter lists and specification addenda.

## Metadata
- **Published**: 2026-10-22T02:56:44Z
- **Authors**: Fei Ding
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.30635v1)