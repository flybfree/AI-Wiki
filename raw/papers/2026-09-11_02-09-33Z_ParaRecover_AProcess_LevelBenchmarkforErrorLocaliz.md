---
title: ParaRecover: A Process-Level Benchmark for Error Localization and Recovery in Parallel Tool-Use Agents
published: 2026-09-11T02:09:33Z
authors: Bowen Guan, Zhentao Yin, Yanming Shen
url: http://arxiv.org/abs/2609.12345v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ParaRecover: A Process-Level Benchmark for Error Localization and Recovery in Parallel Tool-Use Agents

## Abstract
Existing agent benchmarks mainly evaluate final task success or tool-call correctness, providing limited insight into whether agents can reliably diagnose and recover from intermediate execution failures. This limitation becomes particularly critical in multi-turn parallel tool-use scenarios, where errors may propagate across dependent branches and trigger cascading failures. We introduce ParaRecover, a process-level benchmark for evaluating error localization and recovery in multi-turn parallel tool-use agents. Built upon a fine-grained taxonomy of 14 error types covering planning dependencies, tool selection, and argument matching, the benchmark comprises 10,626 instances spanning two difficulty levels. To enable finegrained, process-oriented evaluation, we further propose the SDE rubric, which measures structural integrity, diagnostic reasoning, and evolutionary strategy during agent execution.Experiments across more than ten mainstream LLMs reveal that even state-of-the-art models still struggle with multi-turn error propagation,implicit tool-use failures, and precise replanning. Moreover, we demonstrate that the SDE rubric provides effective supervision signals for improving agents' reflective recovery capabilities. Our data and code are available at https://github.com/gbw206/ParaRecover.

## Metadata
- **Published**: 2026-09-11T02:09:33Z
- **Authors**: Bowen Guan, Zhentao Yin, Yanming Shen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.12345v1)