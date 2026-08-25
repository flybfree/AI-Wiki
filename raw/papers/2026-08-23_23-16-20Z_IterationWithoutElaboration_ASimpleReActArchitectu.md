---
title: Iteration Without Elaboration: A Simple ReAct Architecture Suffices for Text-to-SQL Generation
published: 2026-08-23T23:16:20Z
authors: Jian Lu, Haiwei Yu, Raymond M Xiong, Anru Zhang, Danyang Zhuo
url: http://arxiv.org/abs/2608.22651v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Iteration Without Elaboration: A Simple ReAct Architecture Suffices for Text-to-SQL Generation

## Abstract
Modern text-to-SQL systems have become increasingly elaborate, relying on schema-linking modules, retrieval-augmented prompting, candidate generation, and multi-stage refinement pipelines. While effective, these additions introduce substantial latency and engineering overhead. To this end, we present \textbf{ReAct-SQL}, a simple yet effective zero-shot ReAct-style framework built solely on iterative reasoning and a constrained action space defined by a typed Domain-Specific Language (DSL) of 15 relational operations, rather than free-form SQL generation. The model incrementally issues DSL calls, observes compiled-SQL execution feedback, and revises its reasoning through interaction. On corrected BIRD mini-dev and EHR-SQL, ReAct-SQL achieves \textbf{84.5\%} and \textbf{73.9\%} accuracy, respectively, matching substantially more elaborate baselines while running up to $8\times$ faster. Incremental ablations further show that iteration primarily improves grounding, while the DSL improves compositional reliability.

## Metadata
- **Published**: 2026-08-23T23:16:20Z
- **Authors**: Jian Lu, Haiwei Yu, Raymond M Xiong, Anru Zhang, Danyang Zhuo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22651v1)