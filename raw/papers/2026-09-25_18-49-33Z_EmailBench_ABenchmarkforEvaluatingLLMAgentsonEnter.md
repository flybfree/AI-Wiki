---
title: EmailBench: A Benchmark for Evaluating LLM Agents on Enterprise Email and Productivity Tasks
published: 2026-09-25T18:49:33Z
authors: Mukul Singh, Mansi Uniyal, Devin Devlin, Wen Xie, Big Thadawasin, Ritam Dutt, Vivian Lai, Hyeonsu B. Kang
url: http://arxiv.org/abs/2609.31906v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# EmailBench: A Benchmark for Evaluating LLM Agents on Enterprise Email and Productivity Tasks

## Abstract
Enterprise email agents must combine information retrieval, structured state changes, temporal reasoning, and multi-step coordination. Recent agent benchmarks include productivity tasks, but few center on typed email workflows in a self-contained environment. We introduce EmailBench, a benchmark of 206 email and productivity scenarios across 16 task categories. The benchmark couples a typed email API specification with provider-neutral naming, a deterministic synthetic Enron-inspired corpus, and a scenario suite whose topic selection was informed by aggregate task-intent telemetry from an interactive prototype. Its hybrid evaluation protocol combines 258 executable static assertions with 211 LLM rubrics. We evaluate eight LM configurations on a fixed single-user corpus. The best-performing configuration passes only 33.5% of scenarios despite 99.7% of its tool calls completing without an observed API failure, with pass rates varying substantially across task categories. This gap shows that valid tool execution is not equivalent to task completion. EmailBench provides a self-contained environment for end-to-end email-agent evaluation, with broader tool coverage, multi-persona testing, and repeated-run evaluation as future work areas.

## Metadata
- **Published**: 2026-09-25T18:49:33Z
- **Authors**: Mukul Singh, Mansi Uniyal, Devin Devlin, Wen Xie, Big Thadawasin, Ritam Dutt, Vivian Lai, Hyeonsu B. Kang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.31906v1)