---
title: IFHierBench: Hierarchical Instruction Following for Large Language Models
published: 2026-07-30T09:26:06Z
authors: Yuetian Mao, Chunyang Chen
url: http://arxiv.org/abs/2607.27912v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# IFHierBench: Hierarchical Instruction Following for Large Language Models

## Abstract
Instruction-following ability is critical for deploying large language models in real-world applications, where downstream components depend on the output satisfying specific constraints. Modern deployments increasingly handle the full task in a single LLM call, with one prompt specifying a layered output whose overall artifact, structural sections, and nested fields must each satisfy concrete constraints. Existing instruction-following benchmarks treat the constraint set as a flat list applied uniformly to the response, so they cannot scope a check to a particular section of the output. We introduce IFHierBench, a hierarchical instruction-following benchmark of 600 prompts stratified across four constraint-tree depths and 35 distinct constraints, each prompt paired with a deterministic checker that verifies satisfaction at every scope. Evaluating seven leading proprietary and open-weight models, we find that even the strongest model only marginally exceeds 50% prompt-level accuracy and that accuracy degrades sharply as constraint depth grows. Reliably following nested constraints remains a substantial gap for current LLMs, motivating future training methods that consider constraint adherence at finer granularity to achieve better instruction-following ability.

## Metadata
- **Published**: 2026-07-30T09:26:06Z
- **Authors**: Yuetian Mao, Chunyang Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.27912v1)