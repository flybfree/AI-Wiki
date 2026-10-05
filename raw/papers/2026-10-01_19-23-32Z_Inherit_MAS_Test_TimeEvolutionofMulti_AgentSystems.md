---
title: Inherit-MAS: Test-Time Evolution of Multi-Agent Systems through Workflow and Execution Inheritance
published: 2026-10-01T19:23:32Z
authors: Songtao Wei, Yi Li, Zhichun Guo, Bingzhe Li
url: http://arxiv.org/abs/2610.02396v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Inherit-MAS: Test-Time Evolution of Multi-Agent Systems through Workflow and Execution Inheritance

## Abstract
Multi-agent systems (MAS) built from large language models coordinate specialized agents to tackle complex tasks, but effective workflows are difficult to design in advance. Test-time evolution refines workflows using execution feedback, yet broad revisions can disturb useful components, while re-executing unchanged requests can incur redundant computation. Inspired by the interplay of inheritance and selection in biological evolution, we introduce Inherit-MAS, which makes inheritance explicit at the workflow and execution levels. A meta-model first synthesizes a workflow of worker agents with declared roles, communication inputs, and tool permissions, and a separately prompted judge scores each executed candidate and diagnoses its deficiencies. In ordinary refinement rounds, \emph{workflow inheritance} starts from the latest completed candidate, may discard removable nodes judged unhelpful, and applies a validated edit to address the diagnosed deficiency. When the new candidate executes, \emph{execution inheritance} inherits eligible stored results only if the complete resolved request and execution context match, avoiding redundant model and tool calls. With GPT-4o-mini workers, Inherit-MAS achieves 55.4\% completion on WorkBench and 49.7\% joint F1 on HotpotQA FullWiki, outperforming EvoAgent, EvoMAS, and TacoMAS. With Qwen3-32B workers, it also exceeds these evolving-MAS baselines on both benchmarks. Compared with rerunning the same controller with execution inheritance disabled, execution inheritance reduces worker-token usage by 29.1\% on WorkBench and 34.6\% on HotpotQA, and total token usage by 5.3\% and 18.1\%.

## Metadata
- **Published**: 2026-10-01T19:23:32Z
- **Authors**: Songtao Wei, Yi Li, Zhichun Guo, Bingzhe Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.02396v1)