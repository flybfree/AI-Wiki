---
title: Agentic Graph Token Reasoning
published: 2026-08-01T08:56:26Z
authors: Zhuoyi Peng, Yi Yang
url: http://arxiv.org/abs/2608.00542v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Agentic Graph Token Reasoning

## Abstract
Graphs model relational data throughout science and industry, from citation networks to product co-purchase graphs. Because the nodes of many such graphs carry rich text, a growing line of work applies large language models (LLMs) to graph analysis. The most graph-native of these methods use graph tokens: a graph encoder compresses a graph view, such as a node, its k-hop neighbourhood, or a cluster, into a short block of continuous tokens that jointly encodes node attributes and topology and is read directly by the model. Existing methods, however, use graph tokens in a static single-shot manner: they encode one predefined graph view before the model has even seen the target and never revise it, leaving the model's step-by-step reasoning ability unused. We introduce agentic graph token reasoning, which recasts graph tokenization as part of the reasoning process itself. At each step, the model chooses which graph view to encode and at what granularity; a graph encoder is invoked on demand to materialise the corresponding graph tokens; and the resulting block is spliced into the running context. The model thus reasons step by step in the graph token space, and the tokens it reads are trajectory-dependent. We realise this with a three-stage training pipeline: (i) self-supervised tasks that teach the model to read heterogeneous graph tokens, (ii) a token-robust trajectory stage with a graph-token consistency regulariser, and (iii) preference optimisation that rewards trajectories in which the graph-token evidence and the node-text evidence agree. Across evaluations spanning seven graph domains, our models outperform a broad set of baselines by a large margin and transfer zero-shot to unseen domains without any per-target fine-tuning. More broadly, this work pushes LLM-based graph analysis from static graph-token encoders towards a graph-native agent paradigm.

## Metadata
- **Published**: 2026-08-01T08:56:26Z
- **Authors**: Zhuoyi Peng, Yi Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00542v1)