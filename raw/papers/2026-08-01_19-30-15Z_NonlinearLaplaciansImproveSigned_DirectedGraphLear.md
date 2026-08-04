---
title: Nonlinear Laplacians Improve Signed-Directed Graph Learning
published: 2026-08-01T19:30:15Z
authors: Ali Parviz, Yuichi Yoshida
url: http://arxiv.org/abs/2608.00836v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Nonlinear Laplacians Improve Signed-Directed Graph Learning

## Abstract
While signed-directed graphs have been studied using linear Laplacians in the design of graph neural networks, relatively little research has focused on developing non-linear Laplacian operators for such networks. We introduce a non-linear Laplacian operator specific to signed and directed networks (NLSD). This non-linear operator extends the concepts of the signed Laplacian for signed graphs and the Laplacian for directed graphs. The NLSD calculates node-specific potentials based on features More precisely, if the potential discrepancy is not aligned with the edge direction, we ignore it (and vice versa) leveraging message-passing techniques only across edges where potential discrepancies align with the edge's direction. Utilizing this novel operator, we propose an efficient spectral GNN framework (NLSD-GNN). We conducted comprehensive evaluations focusing on node classification and link prediction, examining scenarios involving signed, directional, or both types of information. Our findings reveal that this spectral GNN framework not only integrates signed and directional data effectively but also achieves superior performance across diverse datasets.

## Metadata
- **Published**: 2026-08-01T19:30:15Z
- **Authors**: Ali Parviz, Yuichi Yoshida
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.00836v1)