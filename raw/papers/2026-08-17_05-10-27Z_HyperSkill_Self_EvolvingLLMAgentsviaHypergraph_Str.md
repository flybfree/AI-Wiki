---
title: HyperSkill: Self-Evolving LLM Agents via Hypergraph-Structured Skill Memory
published: 2026-08-17T05:10:27Z
authors: Ruiyao Xu, Tiankai Yang, Wei-Chieh Huang
url: http://arxiv.org/abs/2608.16114v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HyperSkill: Self-Evolving LLM Agents via Hypergraph-Structured Skill Memory

## Abstract
As agentic tasks grow in complexity, LLM agents increasingly rely on experiential memory to reuse procedural knowledge across tasks. Effective memory design must jointly address what to store, how memory is structured and retrieved, and how memory evolves. Existing systems tackle each only partially: they store trajectories, insights, or workflows as isolated entries, discarding compositional relationships among subtasks and reusable skills; retrieve by flat embedding similarity that ignores relational signals; and maintain memory without leveraging its relational structure. We propose HyperSkill, a hypergraph-based memory framework that jointly improves all three. HyperSkill represents memory as a hypergraph with two node types, subtask steps and reusable skills, where each hyperedge links the subtasks and skills from a single trajectory. Dual-path retrieval queries both subtask and trajectory levels, ranking skills by co-occurrence across retrieved trajectories. Periodic structure-informed maintenance prunes low-utility nodes and merges redundant skills via quality-weighted propagation. Across xBench, GAIA, and WebWalkerQA with GPT-4o and Qwen3-30B-A3B, HyperSkill outperforms ten memory baselines, yielding gains of up to +11.51 on GAIA and +11.18 on WebWalkerQA.

## Metadata
- **Published**: 2026-08-17T05:10:27Z
- **Authors**: Ruiyao Xu, Tiankai Yang, Wei-Chieh Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.16114v1)