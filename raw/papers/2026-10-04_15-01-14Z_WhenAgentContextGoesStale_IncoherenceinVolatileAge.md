---
title: When Agent Context Goes Stale: Incoherence in Volatile Agent Context
published: 2026-10-04T15:01:14Z
authors: Yingying Liu, Junzhou Fang, Chenxiong Qian
url: http://arxiv.org/abs/2610.05281v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# When Agent Context Goes Stale: Incoherence in Volatile Agent Context

## Abstract
Modern agents increasingly ground their reasoning in observations returned by tools, such as file contents read from a workspace. However, the data sources underlying these observations may later be modified by users, other agents, or external tools, while the model retains only the stale content in its context window. Existing agent runtimes provide little support for notifying the model that a previously observed fact has become stale, causing agents to reuse outdated observations and make incorrect claims about the current workspace state. We propose Concord, a context coherence framework that maintains the consistency between tool observation in agent context and the mutable sources from which they were derived. Concord links each observation to its source, detects source changes, and uses configurable handling policies to update, annotate, or suppress stale context before reuse. Concord is applicable across different agent runtimes and external resources, and can be easily extended to new runtime-resource settings. We implement Concord as a general framework, and instantiate a concrete use case to assess its effectiveness. We construct ConcordBench, where previously observed file contents become stale after subsequent edits. Across three evaluated frontier models, Concord produces answers consistent with the restored workspace state in all evaluated cases under these constructed conditions, matching the oracle on recover count for this benchmark, while using 46.4% fewer tokens than the strongest non-oracle baseline.

## Metadata
- **Published**: 2026-10-04T15:01:14Z
- **Authors**: Yingying Liu, Junzhou Fang, Chenxiong Qian
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.05281v1)