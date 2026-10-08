---
title: Coding-Agent Benchmarks Should Match Their Users' Task Flows
published: 2026-10-07T08:08:39Z
authors: Igor Slinko, Yaroslav Golubev, Sergey Titov
url: http://arxiv.org/abs/2610.09633v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Coding-Agent Benchmarks Should Match Their Users' Task Flows

## Abstract
The evaluation of coding agents generally strives to be as realistic as possible. In our study, we collect 4,782 agent sessions of real software engineers in JetBrains IDEs, which we call Production Sessions. Since our subject is interactive agents, we study the sessions with at least three user messages (33% of the sample). These long sessions differ from issue-derived benchmark tasks in two ways: (i) user requests span a far wider mix of task types - questions about the project's code, planning, review, refactoring, execution - and (ii) users switch between types throughout a session. Long-session samples from three public interaction corpora exhibit markedly different Task Flows (the distributions of session lengths, task types, and type-to-type transitions), so no single interaction distribution is universally realistic: benchmarks should name a target use case and calibrate to measurements from it. We present SWE-TaskFlow, an approach for transforming any issue-derived benchmark: it preserves the verified tasks and tests while steering the interaction toward a target Task Flow through prompt splitting and verifiable repository QA, with a TaskFlow Alignment Score (TFAS) for selecting among generated trajectories. In a pilot on 700 SWE-Bench Pro tasks, solving the task sequentially in several steps approximately doubles agent cost without a stable change in resolve rate: the interaction protocol itself is an important dimension of evaluation.

## Metadata
- **Published**: 2026-10-07T08:08:39Z
- **Authors**: Igor Slinko, Yaroslav Golubev, Sergey Titov
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.09633v1)