---
title: Can Agents Design Libraries for Agents?
published: 2026-09-29T05:04:44Z
authors: Gabriel Orlanski, Alex L. Zhang, Avi Trost, Vincent Sunn Chen, Frederic Sala, Aws Albarghouthi, Ludwig Schmidt
url: http://arxiv.org/abs/2609.36730v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can Agents Design Libraries for Agents?

## Abstract
Agents increasingly build on code written by other agents, and they reimplement rather than reuse, growing the codebases later agents must work in. To measure how well agents design libraries for other agents, we introduce LibraryDesignBench, a two-phase benchmark in which an agent implements a full-featured library from a specification that defines required capabilities and potential use cases without prescribing the design. We evaluate the library through the correctness and simplicity of programs written by three user agents from different model families. The benchmark spans 242 expert-validated programming problems across 15 library-design tasks in four languages. On eleven of the fifteen tasks, agent designers reproduce the abstractions of the human-written production library. Downstream agents adopt agent- and human-written libraries alike but underuse them, reimplementing capabilities the library already provides. Our failure analysis finds that downstream agents write extra code mainly because agent-written libraries are rigid or hard to use, not because capabilities are missing. We also experiment with giving designers more prescriptive, agent-first guidance and having them test their library with subagents; this improves downstream scores and yields simpler programs. LibraryDesignBench provides both a testbed for evaluating library-design practices for agent users and an initial design baseline that improves downstream reuse.

## Metadata
- **Published**: 2026-09-29T05:04:44Z
- **Authors**: Gabriel Orlanski, Alex L. Zhang, Avi Trost, Vincent Sunn Chen, Frederic Sala, Aws Albarghouthi, Ludwig Schmidt
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.36730v1)