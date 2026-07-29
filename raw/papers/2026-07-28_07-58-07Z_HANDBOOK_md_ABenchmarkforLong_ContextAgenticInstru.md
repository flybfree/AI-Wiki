---
title: HANDBOOK.md: A Benchmark for Long-Context Agentic Instruction Following
published: 2026-07-28T07:58:07Z
authors: Liudas Panavas, Sebastian Minus, Bradley Monton, Derek Ray, Suhaas Garre, Sushant Mehta, Edwin Chen
url: http://arxiv.org/abs/2607.25398v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HANDBOOK.md: A Benchmark for Long-Context Agentic Instruction Following

## Abstract
Language-model agents are increasingly deployed under standing instructions: a system prompt, a policy file, or a skills document is placed in context, and the agent is trusted to let it govern every action that follows. Existing benchmarks rarely test this deployment pattern directly; they measure whether an agent can complete a task, not whether a long, binding policy document actually constrains its behavior over an extended tool-use horizon. We present HANDBOOK.md, a benchmark of 65 agentic tasks modeled on how enterprise employees follow company handbooks. Each task places an agent in a self-contained company environment, a file workspace together with mock email, chat, calendar, issue-tracking, and commerce services exposed over the Model Context Protocol, and instructs it to carry out routine professional work governed by an expert-written standard operating procedure of 20 to 124 pages. Tasks span five domains (finance, medical billing, insurance, logistics, and HR) and ten fictional companies. To resist memorization, every task modifies one of ten base handbooks, altering the specific rules and thresholds on which grading turns, so no two tasks share a policy. Grading is fully deterministic: each task carries a rubric of programmatic criteria (824 in total) that check both that required actions occurred and that prohibited actions did not. Under strict grading, where a trial passes only if every criterion is satisfied, the best of thirty evaluated model configurations passes 36.2% of trials, and most frontier configurations remain below 25%. Failures follow consistent patterns: agents let a plausible in-environment request override the standing policy, perform a required check and then act against its result, lose rule details over long horizons, and report compliance they did not achieve. We release all tasks, environments, and the evaluation harness.

## Metadata
- **Published**: 2026-07-28T07:58:07Z
- **Authors**: Liudas Panavas, Sebastian Minus, Bradley Monton, Derek Ray, Suhaas Garre, Sushant Mehta, Edwin Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25398v1)