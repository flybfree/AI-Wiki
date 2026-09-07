---
title: GUT: Quantifying and Optimizing the Reasoning Uncertainty of LLMs via Graph Complexity
published: 2026-09-04T15:40:12Z
authors: Shuang Liang, Xin-Yu Hu, Xiang-Jun Ou, Shao-Qun Zhang
url: http://arxiv.org/abs/2609.05284v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# GUT: Quantifying and Optimizing the Reasoning Uncertainty of LLMs via Graph Complexity

## Abstract
Recent years have witnessed great advances in the reasoning ability of Large Language Models (LLMs). However, the reasoning processes of LLMs often exhibit uncertainty, where LLMs often produce a proliferation of divergent branches at each reasoning step even when fed the same prompting inputs, and certain branches exhibit evidently incredible, even nonsensical, reasoning chains and results. In this paper, we propose the Graph-complexity-based UncerTainty (GUT) method for investigating the reasoning uncertainty of LLMs. The key idea of GUT is to characterize the potential branches of each reasoning chain with a directed acyclic graph, thereby ensuring that all potential branches are comprehensively covered within the graph space. Building upon this recognition, we further build two modules of GUT, that is, a Quantification (GUT-Q) module and an Optimization (GUT-O) module, for quantifying and reducing the reasoning uncertainty of LLMs, respectively. GUT-Q measures LLM reasoning uncertainty by approximating the reasoning space complexity with graph complexity. GUT-O implements uncertainty optimization by treating negative uncertainty as the reward function in reinforcement learning. Experimental results conducted on four LLMs and five datasets validate the effectiveness of GUT.

## Metadata
- **Published**: 2026-09-04T15:40:12Z
- **Authors**: Shuang Liang, Xin-Yu Hu, Xiang-Jun Ou, Shao-Qun Zhang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.05284v1)