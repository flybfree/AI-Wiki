---
title: SWE-Residual: Evaluating Starting-State Robustness of Coding Agents
published: 2026-10-19T07:00:04Z
authors: Jinze Li, Weijie Liu, Jinfeng Xu, Shuo Yang, Xin Yang, Yang Zhang, Yijin Wang, Zifei Shan, Edith C. H. Ngai
url: http://arxiv.org/abs/2610.25899v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SWE-Residual: Evaluating Starting-State Robustness of Coding Agents

## Abstract
Software engineering (SWE) benchmarks are the primary way to measure the capabilities of coding agents: an agent is placed in a code repository or machine environment, given a request, and judged by hidden tests. These benchmarks almost always start the agent from a clean state that contains no earlier work on the task. In practice, however, agents often continue work that a developer or another agent has already done and reported as complete, with no indication of what remains incorrect or missing. We introduce SWE-Residual, a benchmark for Starting-State Robustness: the ability to maintain performance on a task when the starting state already contains earlier work on that task. SWE-Residual contains 198 Residual States drawn from 111 tasks in DeepSWE and Terminal-Bench, where the earlier work modifies a code repository or a whole machine environment. Each Residual State is the state a predecessor agent left behind after submitting its work as complete, although the hidden tests still fail. The evaluated agent receives only the original request and this state, without the predecessor's trajectory or any sign that the attempt failed; because the request and hidden tests are unchanged, the starting state is the only difference from the source benchmark. Across five frontier agents, success drops by 20.6--53.5 percentage points on DeepSWE and 20.6--34.9 points on Terminal-Bench relative to a Clean Start, and agent rankings on DeepSWE reverse. Failed continuations show a pattern we call acceptance bias: agents treat the inherited work as the definition of what remains to be done instead of checking it against the request. On DeepSWE, in 58.9--88.2% of failed runs, they submit with exactly the same tests failing, although they pass most of these tests from a Clean Start. SWE-Residual thus exposes a capability gap that clean-start evaluation does not capture.

## Metadata
- **Published**: 2026-10-19T07:00:04Z
- **Authors**: Jinze Li, Weijie Liu, Jinfeng Xu, Shuo Yang, Xin Yang, Yang Zhang, Yijin Wang, Zifei Shan, Edith C. H. Ngai
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.25899v1)