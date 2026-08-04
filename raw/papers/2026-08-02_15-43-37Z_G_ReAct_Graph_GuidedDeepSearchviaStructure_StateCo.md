---
title: G-ReAct: Graph-Guided Deep Search via Structure-State Co-Evolution
published: 2026-08-02T15:43:37Z
authors: Shaoxiong Yang, Mengyuan Zhang, Shaojun Lin, Chao Li, Wei Liu, Kun Shao, Jian Luan
url: http://arxiv.org/abs/2608.01324v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# G-ReAct: Graph-Guided Deep Search via Structure-State Co-Evolution

## Abstract
Deep search has become a fundamental capability of large language models (LLMs) for solving open-domain complex tasks. However, existing approaches typically rely on linear sequential reasoning for both trajectory generation and inference, making it difficult to consistently preserve intermediate states and constraints throughout long-horizon multi-hop search. Consequently, they often suffer from context forgetting, search drift, and inefficient exploration. To address these limitations, we propose $\textbf{G-ReAct}$, a reasoning framework for deep search that organizes reasoning as $\textbf{state evolution over a fixed-topology query graph}$. The evolving graph state explicitly tracks search progress and guides subsequent decisions, transforming exploratory search driven by textual history into graph-guided reasoning under explicit constraints. G-ReAct supports both training and inference: it generates high-quality deep-search trajectories for supervised fine-tuning and provides structured guidance for inference-time search without additional fine-tuning. Experiments demonstrate that with only 1.9K generated trajectories for fine-tuning, Qwen3-30B-A3B-Thinking-2507 achieves $52.6\%$ accuracy on BrowseComp-ZH and $79.0\%$ on XBench, outperforming comparable open-source methods trained on substantially larger datasets, including RL-enhanced methods. Furthermore, when applied at inference time, G-ReAct consistently improves the performance of existing strong LLMs on deep-search tasks. We will publicly release all code and model weights.

## Metadata
- **Published**: 2026-08-02T15:43:37Z
- **Authors**: Shaoxiong Yang, Mengyuan Zhang, Shaojun Lin, Chao Li, Wei Liu, Kun Shao, Jian Luan
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01324v1)