---
title: Neurosymbolic Discovery of Algebraic Graph Constructions
published: 2026-08-08T13:07:51Z
authors: David Seka, Stefan Szeider
url: http://arxiv.org/abs/2608.08118v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Neurosymbolic Discovery of Algebraic Graph Constructions

## Abstract
There are several methods for searching for graphs with prescribed properties, such as SAT solvers and specialized generators. These methods return the result as raw data: an adjacency matrix or a string encoding. The raw data certifies that the graph exists, but it does not reveal any structural properties of the graph. We ask whether one can automatically discover a short algebraic description if only this raw data is provided. We look for a description such as a Cayley graph $\mathrm{Cay}(Γ, S)$ or a lexicographic product $C_5[K_3]$.   We address this question with a neurosymbolic approach. We propose an agent that runs on a general-purpose large language model with no fine-tuning or per-target training. The model interleaves reasoning with calls to the computer algebra system SageMath: it analyzes the target graph, proposes and tests candidate constructions, and revises them until the output matches the target. The agent communicates with SageMath through a Model Context Protocol (MCP) server, which we release as a general-purpose bridge. Whether a construction matches the target is checked by a single exact isomorphism test, and therefore rests on the symbolic side and not on the model. We test the approach on a benchmark of 100 highly symmetric graphs, namely two-orbit graphs on up to 25 vertices; the benchmark was fixed in advance. Our agent could find verified algebraic constructions for all of them, without falling back to raw encodings. A strong template-enumeration baseline reaches only about $20\%$, and a catalog lookup could not identify any of these graphs. However, construction quality declines when symmetry is removed.   As a concrete application, we identify the smallest known counterexample to the Bernhart-Kainen dispersability conjecture, a $16$-vertex graph that enumeration found as raw data. For this graph, our agent found an explicit algebraic construction.

## Metadata
- **Published**: 2026-08-08T13:07:51Z
- **Authors**: David Seka, Stefan Szeider
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08118v1)