---
title: You Know What I Mean: A Benchmark for Agentic Conversational Reference Grounding
published: 2026-08-30T15:06:51Z
authors: Karen Fuchs, Uri Katz, Yoav Goldberg
url: http://arxiv.org/abs/2608.29834v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# You Know What I Mean: A Benchmark for Agentic Conversational Reference Grounding

## Abstract
Collaborative conversations frequently contain references whose targets are indirect rather than named: resolving "this looks like the fix discussed yesterday" requires combining conversational context with evidence from the surrounding workspace which is accessible through APIs or user interfaces. We formalize this problem as Conversational Reference Grounding (CoRG): using a given set of tools to resolve a reference in conversation to the unique external item intended by the speaker. CoRG is challenging because it combines lexical, semantic, and temporal cues distributed across the conversation and the external workspace. Agents must translate these heterogeneous signals into effective tool use: formulating strategies, discovering plausible candidates, inspecting their metadata and content, and ruling out close alternatives. We study CoRG through RepoRef, a benchmark of 400 developer-chat segments grounded in GitHub issues, pull requests, and commits across 92 repositories. Unlike single-shot retrieval tasks, RepoRef often requires multi-step tool use. Our results show that CoRG remains challenging for current agents, even the best agent reaches only 67.0% success rate, leaving one third of references unresolved. These findings position CoRG as a concrete benchmark for studying how agents search, inspect, and verify information in realistic multi-tool environments.

## Metadata
- **Published**: 2026-08-30T15:06:51Z
- **Authors**: Karen Fuchs, Uri Katz, Yoav Goldberg
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29834v1)