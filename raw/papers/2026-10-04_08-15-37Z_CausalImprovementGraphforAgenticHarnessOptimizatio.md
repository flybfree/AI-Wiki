---
title: Causal Improvement Graph for Agentic Harness Optimization
published: 2026-10-04T08:15:37Z
authors: Junjie Zhang, Shunyu Liu, Haoyu Wang, Ting-En Lin, Yongbin Li, Dacheng Tao
url: http://arxiv.org/abs/2610.05039v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Causal Improvement Graph for Agentic Harness Optimization

## Abstract
Agentic Harness is the runtime that constructs task context and controls execution flow, thereby shaping overall agent performance. Given a fixed model and external evaluation, automated Harness optimization seeks to improve this runtime through an iterative proposal--evaluation loop to better solve target tasks. Existing meta-harness methods mainly adopt proposer-centric discovery, in which an LLM-based proposer integrates accumulated experimental findings to determine subsequent Harness revisions. This places the burden of maintaining the evolving improvement state on the proposer as history expands and its underlying experimental logic becomes harder to discern. In this paper, we introduce the Causal Improvement Graph (CIG), a graph-governed meta-harness framework that externalizes the evolving improvement state in a persistent graph, allowing prior findings to directly govern subsequent Harness optimization through local proposer operations. CIG grows and links Evidence, Hypothesis, Intervention, and Outcome nodes to represent what was observed, how it may be explained, how to test that explanation, and what the evaluation reveals. Their structural relations preserve how the improvement state changes across iterations, allowing local proposers to build directly on relations among prior findings rather than recover them from raw history. Across various agent tasks, CIG discovers stronger Harnesses than previous meta-harness baselines and remains robust to the choice of task solver and proposer. Structural ablations further support the design of an explicit improvement state with graph-governed evolution.

## Metadata
- **Published**: 2026-10-04T08:15:37Z
- **Authors**: Junjie Zhang, Shunyu Liu, Haoyu Wang, Ting-En Lin, Yongbin Li, Dacheng Tao
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.05039v1)