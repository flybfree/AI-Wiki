---
title: "Summary: Contrastive-Collapsed Loss for Flexible and Geometrically Optimal Embeddings and Faster Convergence"
date: "2026-07-14"
type: "paper-summary"
source_url: "http://arxiv.org/abs/2607.12916v1"
tags: ["summary", "paper-summary", "arxiv"]
authors: "Blanca Cano-Camarero, \u00c1ngela Fern\u00e1ndez-Pascual, Jos\u00e9 R. Dorronsoro"
---
# Summary: Contrastive-Collapsed Loss for Flexible and Geometrically Optimal Embeddings and Faster Convergence

**Source**: [Original Paper](http://arxiv.org/abs/2607.12916v1)

## Summary

In this work, we introduce CoCo, a loss function aimed at learning normalized and well-structured representations. The proposed loss encourages intra-class collapse and inter-class contrast while preserving sufficient flexibility for neural networks to approximate geometrically optimal embeddings with large angular separation between classes. We provide a theoretical analysis positioning CoCo with respect to related objectives such as dot regression and cross-entropy, showing that the new proposed loss benefits from closer initialization to the optimal configuration, more informative gradients, and stronger incentives for class-wise representation collapse. Extensive experiments on diverse tabular datasets from the OpenML-CC18 benchmark show that CoCo achieves competitive performance with state-of-the-art methods, including kernel SVM, Random Forest, dot regression, and cross-entropy-based neural networks. In addition, both theoretical arguments and empirical analyses demonstrate that the proposal promotes tighter class clustering and faster convergence. These results highlight CoCo loss as an effective objective for learning discriminative representations while maintaining competitive predictive performance.
