---
title: Can Graph Learning Learn Circuits?
published: 2026-08-09T07:14:13Z
authors: Chester Tan, Moritz Lampert, Courtney Maynard, Ankit Ramakrishnan, Tina Eliassi-Rad, Ingo Scholtes
url: http://arxiv.org/abs/2608.08536v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Can Graph Learning Learn Circuits?

## Abstract
Circuit localization is a mechanistic interpretability task whose goal is to identify a sparse subgraph of a transformer's computation graph sufficient to reproduce a particular behavior. Most established methods localize circuits independently for each model--task pair. We instead frame circuit localization as a graph machine learning problem in which the edges of a computation graph represent computational pathways, and graph neural networks (GNNs) model interactions among these pathways. We introduce Graph Circuit Learning (GCL), a supervised, amortized framework that trains a GNN across multiple model--task pairs and applies it to unseen cases. To provide sufficient data, we augment the InterpBench benchmark with additional cases derived from the TracrBench programs. Of the 14 evaluated GCL configurations, the highest scored a median edge AUROC of $0.902$ (interquartile interval $[0.861, 0.942]$) on the 16 original held-out InterpBench cases. This is close to the published InterpBench median of $0.910$ for EAP-IG while remaining below ACDC's $0.959$. Removing all message-passing edges reduces the median to $0.825$. We also adapt PGExplainer, a GNN explainability method, to circuit localization, obtaining a median edge AUROC of $0.858$ on the same cases. These preliminary results suggest that graph machine learning offers a natural and potentially powerful perspective on circuit localization, and we hope this perspective encourages closer exchange between the two communities.

## Metadata
- **Published**: 2026-08-09T07:14:13Z
- **Authors**: Chester Tan, Moritz Lampert, Courtney Maynard, Ankit Ramakrishnan, Tina Eliassi-Rad, Ingo Scholtes
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08536v1)