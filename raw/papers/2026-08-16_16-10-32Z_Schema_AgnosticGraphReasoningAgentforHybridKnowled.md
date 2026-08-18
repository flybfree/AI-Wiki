---
title: Schema-Agnostic Graph Reasoning Agent for Hybrid Knowledge Graphs
published: 2026-08-16T16:10:32Z
authors: Marius Dragic, Ruben Ifrah, Alexandre Rio
url: http://arxiv.org/abs/2608.15834v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Schema-Agnostic Graph Reasoning Agent for Hybrid Knowledge Graphs

## Abstract
Tool-calling LLM agents navigate unfamiliar codebases with a handful of generic primitives for listing, reading and searching files (ls, cat, grep). A knowledge graph admits the same interface: listing neighbours, reading node content and searching descriptions are the same operations on a different substrate. Building on this correspondence, we present GRA, a Graph Reasoning Agent that explores hybrid knowledge graphs, whose nodes are either textual concepts or relational tables, with seven generic tools, discovering everything domain-specific at run time. On UFK-M (Unified Factory Knowledge Model), an industrial benchmark of 258 analytical questions whose gold answers are produced by executing validated SQL programs, GRA beats a full-context agent by 5.1 pp (88.4% vs. 83.3%), while reading under a third of its input tokens. A graph-free control shows the gain comes chiefly from selective agentic access rather than graph topology, and that the effect depends on a model able to drive tools reliably. Seeing less, the agent answers better: selective navigation over a structured substrate beats exhaustive context.

## Metadata
- **Published**: 2026-08-16T16:10:32Z
- **Authors**: Marius Dragic, Ruben Ifrah, Alexandre Rio
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15834v1)