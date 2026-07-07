---
title: Graph Classification via Network Usable Information: From Representation Evaluation to Structure Selection
published: 2026-07-03T20:11:34Z
authors: Abdullah Shaik, Anwar Said
url: http://arxiv.org/abs/2607.03587v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Graph Classification via Network Usable Information: From Representation Evaluation to Structure Selection

## Abstract
We propose NetinfoGC, a framework for graph classification that extends the Network Usable Information (NUI) paradigm to graph-level learning. Unlike conventional graph neural network approaches that rely on end-to-end training of black-box embeddings, NetinfoGC constructs a family of permutation-invariant graph representations derived from propagation-based mechanisms and classical structural descriptors, including graph centrality measures.   To evaluate representation quality, we introduce a training-free NUI estimation procedure based on clustering consistency with ground-truth labels, providing a proxy for task-relevant information without supervised learning. We further exploit the same representations using sparse-group LASSO regularization, enabling automatic selection of informative structural descriptors while suppressing redundant ones.   Experiments on benchmark datasets show that classical centrality measures are highly competitive with learned propagation-based representations, and in several cases yield superior performance. Moreover, we observe a strong correlation between estimated NUI and downstream classification accuracy, validating NUI as an effective measure of representation utility.   Overall, NetinfoGC provides a unified and interpretable framework for evaluating and exploiting graph representations without requiring end-to-end neural training.

## Metadata
- **Published**: 2026-07-03T20:11:34Z
- **Authors**: Abdullah Shaik, Anwar Said
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.03587v1)