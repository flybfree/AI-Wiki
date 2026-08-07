---
title: Project2Task: Graph-Guided Project-Level Planning for Autonomous Research
published: 2026-08-05T11:39:29Z
authors: Huirui Xu, Runtao Xu, Shuo Ren, Jiajun Zhang
url: http://arxiv.org/abs/2608.05225v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Project2Task: Graph-Guided Project-Level Planning for Autonomous Research

## Abstract
Research agents can increasingly search literature, propose hypotheses, generate code, run experiments, and draft manuscripts from a single topic. However, a research project is not merely a larger task: it is a long-horizon agenda that must be advanced through multiple bounded tasks with distinct but related objectives, parallel alternatives, and dependency-aware sequences. Existing single-task systems often treat the project as one oversized task, produce a flat set of vague or overlapping tasks, or leave task boundaries and execution order to manual coordination. We introduce Project2Task, a graph-guided project-level planning layer for autonomous research. Given a project brief, it represents candidate contributions as innovation atoms and organizes them in a directed lineage graph. A lightweight Bernoulli block-model objective selects among horizontal, vertical, and hybrid portfolio decompositions. Project2Task then generates bounded tasks with explicit contribution ownership, repairs overlaps and missing execution fields, and emits dependency-aware task contracts that specify objectives, inputs, expected artifacts, evaluation requirements, boundary constraints, dependencies, and execution order. The contracts are independent of any particular downstream research executor and support integration of task outputs into a coherent project-level result. On a benchmark of ten project briefs yielding roughly 30 tasks, manuscript-based portfolio evaluation gives Project2Task an average quality score of 7.15, compared with 4.58 for the Brief Baseline and 5.31 for the Topic-only Setting. Integrating its contracts with AutoResearchClaw increases average downstream task accuracy from 0.536 to 0.759. These results demonstrate the value of explicit project-to-task planning for producing coherent, non-redundant, and executable research-task portfolios.

## Metadata
- **Published**: 2026-08-05T11:39:29Z
- **Authors**: Huirui Xu, Runtao Xu, Shuo Ren, Jiajun Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.05225v1)