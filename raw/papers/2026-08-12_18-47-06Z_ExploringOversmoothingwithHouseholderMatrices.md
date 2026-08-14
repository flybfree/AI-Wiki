---
title: Exploring Oversmoothing with Householder Matrices
published: 2026-08-12T18:47:06Z
authors: Bhaskar Karol
url: http://arxiv.org/abs/2608.12514v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Exploring Oversmoothing with Householder Matrices

## Abstract
Deep graph neural networks(GNNs) suffer from oversmoothing- a progressive collapse of node representation towards a low information subspace as network depth increases because the normalized graph propagation operator is repeatedly applied directly to the hidden representations. In this work we study Householder Graph Neural Network (HouseGNN). Rather than updating the hidden state like standard GCN, HouseGNN uses the aggregated neighbourhood message solely to estimate a reflection direction; the node embedding is then updated by a Householder reflector followed by GroupSort, yielding a piecewise orthogonal layer that preserves Euclidean norm at every node and at every depth. We prove three core properties: (i) every internal layer preserves the node-wise Euclidean norm; (ii) the Householder reflector is scale scale and sign-invariant in the message; and (iii) pairwise distance between nodes can change through mismatch between node-wise orthogonal operators.

## Metadata
- **Published**: 2026-08-12T18:47:06Z
- **Authors**: Bhaskar Karol
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12514v1)