---
title: A Trust Layer for Agent Evaluation
published: 2026-10-05T19:15:37Z
authors: Mohammadreza Sediqin, Shivali Dalmia, Srinivasa Karthikeya Reddy Kovvuri, Abhishek Mukherji
url: http://arxiv.org/abs/2610.07274v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# A Trust Layer for Agent Evaluation

## Abstract
Deterministic benchmark scores show that an agent received credit, but not whether that credit was earned, reported honestly, or would hold on a second run. We introduce a Trust Layer for Agent Evaluation, an additive post-hoc framework that reports, beside each recorded score, whether it should be believed. It verifies four properties: whether the result is supported by the benchmark's own grading logic, whether a passing answer was earned through traceable computation, whether the agent's completion claim matches what occurred, and whether the result is stable under repeated execution. The first three use only saved artifacts; the fourth re-runs the agent. Model judgments only label evidence under majority voting; all verdicts follow deterministic rules and never modify the recorded score. Applied to five agent configurations on 108 tasks from Agents' Last Exam, every model shows passing runs with no traceable computation (at rates varying tenfold), confirmed false completion claims, and unstable results: 18-46% of tasks do not stay in one score band over five runs. Only 22.6% of recorded passes clear all four checks (95% CI 15.0-32.6, n=84). Measuring what an agent can do and verifying that it did it are different problems, and current benchmarks address only the first.

## Metadata
- **Published**: 2026-10-05T19:15:37Z
- **Authors**: Mohammadreza Sediqin, Shivali Dalmia, Srinivasa Karthikeya Reddy Kovvuri, Abhishek Mukherji
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.07274v1)