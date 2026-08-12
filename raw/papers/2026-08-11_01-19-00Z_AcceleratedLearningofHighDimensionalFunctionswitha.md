---
title: Accelerated Learning of High Dimensional Functions with a Tensor-Featured Training Network
published: 2026-08-11T01:19:00Z
authors: Karl Pierce, Yuehaw Khoo, Haizhao Yang
url: http://arxiv.org/abs/2608.10351v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Accelerated Learning of High Dimensional Functions with a Tensor-Featured Training Network

## Abstract
In this work we present a method to accelerate the optimization of learning high dimensional functions using deep neural network (DNN). This optimization procedure introduces contextual features into the first layer of a DNN. The parameters of DNN are optimized via standard gradient descent while keeping the input-feature basis fixed. After optimization of the DNN parameters, the feature layer is provided a chance to update and change before DNN optimization resumes. The feature layer has two types of functions: those that can be evaluated quickly in a matrix-free way on the domain (i.e. rank-1 features) and more complex features that must first be decomposed using tensor network (TN) decomposition strategies (tensor features). In particular, we study the effect of adding features which distill pretrained DNN into TNs using a discretize and decompose strategy. To efficiently decompose high-dimensional functions constructed from discretized DNN, we leverage a randomized tensor decomposition strategy. Using randomization, we are able to reduce the storage cost of decomposing high dimensional functions by at least 8 orders of magnitude. Using this approach, we are able to efficiently train models between 5 and 40 dimensions.

## Metadata
- **Published**: 2026-08-11T01:19:00Z
- **Authors**: Karl Pierce, Yuehaw Khoo, Haizhao Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.10351v1)