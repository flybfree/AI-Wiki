---
title: Mahalanobis-Based Multi-Head Attention for Complex State Propagation
published: 2026-08-25T12:13:28Z
authors: Xiaohe Li
url: http://arxiv.org/abs/2608.24462v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Mahalanobis-Based Multi-Head Attention for Complex State Propagation

## Abstract
In this paper, we propose \textbf{Mahalanobis-Based Multi-Head Attention} (MHA-CSP), a novel attention mechanism that replaces the standard dot-product with a \textbf{Mahalanobis distance-based RBF kernel}, which effectively computes attention in an infinite-dimensional feature space without increasing the parameter count. Crucially, the positive definiteness of the Mahalanobis distance enables a \textbf{direct construction of Tree Attention}: attention scores are built directly from accumulated distances, with a LogSumExp correction that rectifies the raw distance by subtracting the log-sum of edge exponentials. Moreover, the multi-head Mahalanobis distance matrices are themselves repurposed to construct an \textbf{attention meshing mechanism}, enabling cross-head kernel collaboration that simultaneously boosts accuracy and training efficiency.   Extensive experiments demonstrate that MHA-CSP, with only 119K parameters and \textbf{teacher forcing applied exclusively at the final hidden state}, consistently outperforms Transformer and GCN baselines trained from scratch under identical conditions on long-sequence state tracking tasks. While these baselines rely on dense attention or graph propagation, MHA-CSP achieves robust structured reasoning via synthetic distance rectification---powered by Mahalanobis-based attention---and efficient information bypass inherited from the CSP backbone.   This result highlights the effectiveness of complex-valued state propagation with collaborative multi-head rectification in capturing symbolic structures, establishing a new efficiency-performance trade-off for structured reasoning.

## Metadata
- **Published**: 2026-08-25T12:13:28Z
- **Authors**: Xiaohe Li
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24462v1)