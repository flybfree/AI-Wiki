---
title: BrainLinear: A Linear Model for Brain Network Analysis in Sparse Tangent Subspaces
published: 2026-08-15T14:57:48Z
authors: Sijing Wu, Dongyuan Li, Miaoting Huang, Weiwei Ye, Ying Zhang, Feng Xia, Renhe Jiang
url: http://arxiv.org/abs/2608.15266v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# BrainLinear: A Linear Model for Brain Network Analysis in Sparse Tangent Subspaces

## Abstract
Functional connectome analysis examines brain-region interactions to understand and identify disorders such as autism spectrum disorder and Alzheimer's disease. Existing methods typically use GNNs and Transformers to model the full functional connectivity matrix. However, processing tens of thousands of connections introduces redundancy and noise, increases computational cost, and limits connection-level interpretability. This raises a central question: do we really need complex interaction modeling, or is identifying a small set of disease-relevant connectivity patterns sufficient? To answer this question, we propose BrainLinear, a lightweight geometry-aware framework for mining disease-discriminative connectome patterns. BrainLinear first maps each functional connectivity matrix to a shared tangent space centered at the Fréchet mean of the training set, capturing subject-specific deviations while respecting matrix geometry. It then scores each ROI-pair tangent direction by its classification contribution and disease--control difference, retaining Top-$K$ directions as a compact representation. Finally, a shallow multilayer perceptron performs classification on the selected representation. Experiments on ABIDE and ADNI show that BrainLinear matches or exceeds strong GNN and Transformer baselines at a fraction of their cost: it improves AUC and ACC over the best baseline for each metric by up to $3.54$ and $1.39$ percentage points, while reducing runtime and peak GPU memory by $84.0\%$ and $68.4\%$ relative to the closest baseline in AUC. The selected directions are directionally consistent with between-group displacements and organized across major functional systems, supporting connection-level interpretation.

## Metadata
- **Published**: 2026-08-15T14:57:48Z
- **Authors**: Sijing Wu, Dongyuan Li, Miaoting Huang, Weiwei Ye, Ying Zhang, Feng Xia, Renhe Jiang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15266v1)