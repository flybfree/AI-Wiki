---
title: NodeJEPA: Structure-Conditioned Latent Prediction for Node-Level Graph Self-Supervised Learning
published: 2026-08-05T02:39:28Z
authors: Tinghe Zhang, Jian Xu, Jiaheng Chen, Jiaxing Li, Yucheng Xiao, Qiang Wang
url: http://arxiv.org/abs/2608.04381v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NodeJEPA: Structure-Conditioned Latent Prediction for Node-Level Graph Self-Supervised Learning

## Abstract
Self-supervised learning on graphs is largely shaped by contrastive methods that depend on carefully designed augmentations, and by generative methods that reconstruct node attributes in the input space. Both paradigms can entangle representations with low-level input statistics rather than with relational structure. Joint-embedding predictive architectures (JEPA) instead learn by predicting latent targets rather than reconstructing inputs. Recent work has explored this idea for graph-level representation learning, but how to design JEPA-style objectives for node-level tasks, and which structural signals the predictor should condition on, remains less clear. We present NodeJEPA, a joint-embedding predictive architecture for node-level graph self-supervised learning. NodeJEPA masks structure-aware k-hop ego-subgraphs and trains a context encoder to predict the latent representations of the masked nodes. These targets come from an EMA-updated target encoder with stop-gradient. A structure-conditioned predictor integrates spectral and centrality descriptors through cross-attention. Variance, covariance, and Laplacian spectral regularizers help stabilize the embedding geometry, and an optional curriculum gradually increases masking difficulty during training. Because prediction occurs in latent space, NodeJEPA does not rely on input reconstruction or hand-crafted graph augmentations. We evaluate NodeJEPA on standard node classification benchmarks under linear probing and fine-tuning protocols, and conduct ablations on masking, prediction, and regularization design choices. Our study offers a practical recipe for node-level JEPA-style latent prediction on graphs, and clarifies when structural conditioning helps representation learning. Code, configurations, and evaluation scripts are publicly available at https://github.com/OliverZ-dot/Node-Jepa.

## Metadata
- **Published**: 2026-08-05T02:39:28Z
- **Authors**: Tinghe Zhang, Jian Xu, Jiaheng Chen, Jiaxing Li, Yucheng Xiao, Qiang Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04381v1)