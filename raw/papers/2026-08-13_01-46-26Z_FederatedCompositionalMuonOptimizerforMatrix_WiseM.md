---
title: Federated Compositional Muon Optimizer for Matrix-Wise Models
published: 2026-08-13T01:46:26Z
authors: Wang Yan, Feihu Huang
url: http://arxiv.org/abs/2608.12710v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Federated Compositional Muon Optimizer for Matrix-Wise Models

## Abstract
Muon, a more recently developed optimizer, is useful for matrix-wise models in AI areas. Although many works have studied Muon and its variants, these methods are still not particularly well-suited for hierarchical structured problems. To fill this gap, we propose an effective federated compositional Muon (FedCoMuon) optimizer to solve distributed matrix-wise compositional optimization problems. Specifically, our FedCoMuon optimizer builds on compositional gradient tracking and orthogonalized momentum. Moreover, we propose a variance reduced variant of FedCoMuon (FedCoMuon-VR) based on a momentum-based variance reduced technique. In theory, we analyze the convergence properties of our algorithms under the non-i.i.d. and non-convex settings. In particular, we prove that our FedCoMuon-VR obtains a lower sample complexity of $O(ε^{-3})$ for finding an $ε$-stationary solution than the existing FedMuon algorithms. Extensive numerical experiments on robust federated learning and task-distributed risk-sensitive meta learning show that our proposed methods are competitive with existing compositional baselines and achieve the best reported accuracy in several settings.

## Metadata
- **Published**: 2026-08-13T01:46:26Z
- **Authors**: Wang Yan, Feihu Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12710v1)