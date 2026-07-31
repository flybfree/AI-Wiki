---
title: What makes prompts a graph: necessary and sufficient conditions for prompt graph engineering
published: 2026-07-30T01:42:09Z
authors: Sandeco Macedo
url: http://arxiv.org/abs/2607.27578v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# What makes prompts a graph: necessary and sufficient conditions for prompt graph engineering

## Abstract
Prompts stopped being isolated strings some time ago. In real systems, one model call feeds another, retrieval interleaves with generation, routers branch, and aggregators merge parallel results. Practice converged on a single structure to hold this together: the graph. Frameworks such as LangGraph, DSPy, and Prompt Flow expose it openly, and research systems already optimize it automatically. The vocabulary, however, lags behind. Graph names, variously, a reasoning topology inside one sampling strategy, a multi-agent conversation, or an orchestration artifact, while prompt engineering still evokes writing one good string. What is missing is a reference definition treating prompts as nodes of an explicit, executable, improvable graph. We build that definition through conceptual analysis over sources with persistent identifiers, complemented by primary grey literature. We reconstruct the genealogy of the idea, from dataflow graphs and build systems, through prompt chaining and the thought topologies (chain, tree, graph), to graphs compiled and optimized as artifacts. We then propose a constitutive definition of prompt graph engineering, state its four conditions (explicit structure, separation between structure and prompt content, executable semantics, and the graph as a first-class engineering artifact), and operationalize them as an inclusion and exclusion test. We draw the boundary against six neighboring concepts and apply the test to six real systems (LangGraph, DSPy, Prompt Flow, AutoGen, CrewAI, and Claude Code subagents); it includes and excludes consistently. We close with a research agenda organized along four design tension axes. The contribution is an operational definition and a shared vocabulary for a practice that industry already exercises daily without naming precisely.

## Metadata
- **Published**: 2026-07-30T01:42:09Z
- **Authors**: Sandeco Macedo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27578v1)