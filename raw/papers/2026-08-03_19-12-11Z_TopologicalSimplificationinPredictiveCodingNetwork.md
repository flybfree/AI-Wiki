---
title: Topological Simplification in Predictive Coding Networks
published: 2026-08-03T19:12:11Z
authors: Adam Shaw, Jiayu Li, Michael Sperling, Michael Kim, Alvin Jin
url: http://arxiv.org/abs/2608.02816v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Topological Simplification in Predictive Coding Networks

## Abstract
We study the topology of learned representations in predictive coding networks (PCNs), a neuro-inspired bidirectional architecture, using a quantitative layer-wise persistent homology analysis. We train well-performing PCNs on a synthetic classification dataset ($\geq 99.9\%$ test accuracy) and on MNIST ($\geq 95\%$ test accuracy), and measure how topological features change across layers for different architectures and activation functions. We find that smaller PCNs collapse connected components across layers earlier than larger models (Spearman $\unicode{x1D70C} \in [0.72, 0.79]$ across activations), with model size measured as the sum of hidden-layer widths. We also observe a strong negative correlation ($\unicode{x1D70C} = -0.58$) between the depth at which simplification occurs and reconstruction error; i.e., architectures that simplify later reconstruct better. Finally, a seed-level bootstrap comparison across architectures and activations shows that PCNs consistently collapse connected components later than matched MLPs, with an average difference of $3.6$ layers. These results suggest that persistent homology offers a useful quantitative lens on the compression--reconstruction tradeoff in PCNs, and that both model capacity and the recurrent, bidirectional dynamics of predictive coding inference shape when this tradeoff is resolved across layers.

## Metadata
- **Published**: 2026-08-03T19:12:11Z
- **Authors**: Adam Shaw, Jiayu Li, Michael Sperling, Michael Kim, Alvin Jin
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02816v1)