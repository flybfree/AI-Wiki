---
title: Reasoning Consensus: Structural Ensembling of LLM Reasoning via Weighted DAG Aggregation
published: 2026-07-30T07:14:50Z
authors: Amruta Parulekar, Jinu Lee, Dilek Hakkani-Tür, Hari Sundaram
url: http://arxiv.org/abs/2607.27783v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Reasoning Consensus: Structural Ensembling of LLM Reasoning via Weighted DAG Aggregation

## Abstract
Large Language Models (LLMs) explore problems through chain-of-thought, but this exploration is buried in unstructured prose. On high-stakes tasks, users cannot tell which steps are well-supported, which alternatives were seriously considered, or how the final conclusion compares to those the model discarded. We propose a framework that ensembles the reasoning structure, not just the answers, of multiple LLMs by weighted merging of Directed Acyclic Graphs (DAGs) extracted from reasoning chains. We weight each step by how many traces independently attest to it, to return "Consensus Reasoning". Across six benchmarks spanning statutory interpretation, graduate-level science, narrative multi-hop reasoning, and first-order logic, our ensemble outperforms a matched-budget majority-vote baseline, with a maximum accuracy gain of 3.1% on MuSR-MM (narrative multi-hop reasoning). On a single model, the framework matches or exceeds self-consistency at the same trace budget while additionally exposing an inspectable consensus reasoning graph. Ensemble weights correlate with LLM-judge rankings of reasoning quality at Spearman $ρ= 0.30$-$0.51$, and consensus subgraphs are preferred over alternatives leading to the majority-vote answer in 54.4-65.4% of head-to-head comparisons across five of six datasets. We observe that our framework can also be used to analyze diverse reasoning perspectives for a problem.

## Metadata
- **Published**: 2026-07-30T07:14:50Z
- **Authors**: Amruta Parulekar, Jinu Lee, Dilek Hakkani-Tür, Hari Sundaram
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27783v1)