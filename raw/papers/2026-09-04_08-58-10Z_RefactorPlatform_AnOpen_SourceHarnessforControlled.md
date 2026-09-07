---
title: RefactorPlatform: An Open-Source Harness for Controlled Evaluation of Repository-Scale Refactoring Agents
published: 2026-09-04T08:58:10Z
authors: Aziz Ben Amor, Drish Mali, Mann Acharya, Vijayasri Iyer, Sébastien Bratières
url: http://arxiv.org/abs/2609.04898v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# RefactorPlatform: An Open-Source Harness for Controlled Evaluation of Repository-Scale Refactoring Agents

## Abstract
Repository-scale refactoring requires coding agents to propagate a single change across many interdependent files without altering program behavior, yet to our knowledge no existing harness isolates the design choices that determine agent success on this task. We present RefactorPlatform, an open-source evaluation harness that holds the environment fixed and varies each design axis explicitly: model backbone (via OpenRouter and GitHub Copilot CLI), execution regime (baseline, retrieval-augmented, and multi-agent), and prompt specificity. Each run executes in an isolated workspace with live terminal streaming, per-task logging of tokens, diffs, and transcripts, AST-based verification, and exportable telemetry for audit and reproduction. Demonstrating the platform on 100 multi-file RefactorBench tasks across four model families, we illustrate the analyses it supports: AST-aware chunking outperforms naive token-window chunking by 25-30% across prompt modes, whereas naive retrieval falls below the retrieval-free baseline; a lean retrieval-augmented single agent (86%) beats the sub-agent configuration we evaluated (66%) on matched tasks with no task passing under delegation that fails under retrieval; and retrieval's accuracy gains absorb its token overhead, leaving cost per successful refactoring unchanged. RefactorPlatform is open-sourced to make refactoring-agent evaluation reproducible and auditable.

## Metadata
- **Published**: 2026-09-04T08:58:10Z
- **Authors**: Aziz Ben Amor, Drish Mali, Mann Acharya, Vijayasri Iyer, Sébastien Bratières
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.04898v1)