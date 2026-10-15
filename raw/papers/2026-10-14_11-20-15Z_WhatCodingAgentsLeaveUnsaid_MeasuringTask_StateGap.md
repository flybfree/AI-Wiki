---
title: What Coding Agents Leave Unsaid: Measuring Task-State Gaps Between Execution and Reports
published: 2026-10-14T11:20:15Z
authors: Guoyang Xu, Rui Zhang, Xiuyu Wu, Hao Chen
url: http://arxiv.org/abs/2610.20003v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What Coding Agents Leave Unsaid: Measuring Task-State Gaps Between Execution and Reports

## Abstract
Human supervisors rely on coding agents' reports to assess progress, verify repairs, and decide when to intervene. But a supervisor cannot investigate a failure they were never told occurred. Failed attempts, workarounds, and unresolved risks may disappear from routine reports, leaving supervisors unaware of issues that warrant scrutiny. We conduct CTXGAP, a measurement study quantifying the gap in task-state recoverability between agents' accumulated user-facing reports and their full recorded execution contexts. Across 37 coding tasks and 4,799 valid probes, agents answer 93.6% of task-state questions on demand; full-context readers recover 92.7%, while report-only readers recover 52.0%, a 40.7-point gap. At the final checkpoints of 30 verified fixes, the gap remains 34.8 points. Human annotation identifies states mentioned without enough supporting detail as the largest category of unrecovered information, and model-assessed supervision-relevant states retain substantial gaps. Full terminal scrollback improves recovery to 73.6% but still trails full context. Under matched report lengths, context-informed rewrites improve recovery by about eight points, without a detectable targeted-over-natural advantage. Positive gaps persist across harnesses and independent DeepSeek execution and measurement. CTXGAP establishes report-based task-state recoverability as a complementary evaluation dimension.

## Metadata
- **Published**: 2026-10-14T11:20:15Z
- **Authors**: Guoyang Xu, Rui Zhang, Xiuyu Wu, Hao Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.20003v1)