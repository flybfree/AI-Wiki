---
title: Inductive Graph Layout with Implicit Neural Fields
published: 2026-08-09T19:31:12Z
authors: Berfin Inal, Daniel Probst
url: http://arxiv.org/abs/2608.08876v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Inductive Graph Layout with Implicit Neural Fields

## Abstract
A graph layout is normally a table of $N$ free coordinates. We optimise a function with a fixed number of parameters instead. This gives a drawing a sample complexity and an extensible domain. Force-directed algorithms remain the standard tools for graph drawing. The most accurate among them minimise stress in the Kamada-Kawai formulation by directly optimising the node coordinates, at a full objective cost of $O(N^2)$ in time and space. Here, we propose Fling (Field Layout via Implicit Neural Geometry), a small neural network mapping the distances of each node to a set of landmarks, positioning it in the plane by training on the layout energy. The full spring system then becomes tractable without its distance matrix, as rest lengths follow from a landmark bound in constant time per pair while a second network learns the majorisation sums from exact anchor rows, at $O(|\mathcal{A}|N)$ per step for $|\mathcal{A}|\ll N$ anchors. Unlike neural drawers that read the graph by message passing, we represent the drawing as a function of node features. An unseen node costs one forward pass, where sparse and low-rank majorisation remain transductive. As the unknowns are weights rather than coordinates, the energy only requires a small fraction of the nodes, and a field fitted that way outperforms PivotMDS, landmark MDS, and a kernel ridge trained on the same energy and features, when the task is fitting the energy of a graph from a sample of its nodes. In addition, the same parameterisation enables a stochastic pivot stress variant, an aesthetics-optimised variant carrying a neighbour-embedding energy with node-edge clearance and crossing terms on the same field, and conditioning on the weight between two energies gives a whole layout family from one run.

## Metadata
- **Published**: 2026-08-09T19:31:12Z
- **Authors**: Berfin Inal, Daniel Probst
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08876v1)