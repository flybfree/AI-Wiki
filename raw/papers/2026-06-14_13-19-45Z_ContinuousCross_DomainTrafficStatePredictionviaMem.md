---
title: Continuous Cross-Domain Traffic State Prediction via Memory-Augmented Graph Liquid Time-Constant Networks
published: 2026-06-14T13:19:45Z
authors: Jinrong Xiang, Ming Xu
url: http://arxiv.org/abs/2606.15807v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Continuous Cross-Domain Traffic State Prediction via Memory-Augmented Graph Liquid Time-Constant Networks

## Abstract
Traffic state prediction is a fundamental task in intelligent transportation systems. In practical applications, some regions suffer from limited traffic observations due to insufficient sensing infrastructure, making cross-domain knowledge transfer an important solution for data-scarce traffic prediction. However, existing cross-domain traffic prediction methods still face several limitations, including coarse-grained source-target adaptation, limited capability in handling unseen target-domain patterns, and insufficient modeling of continuous traffic dynamics under irregular or heterogeneous temporal conditions. To address these issues, this paper proposes a continuous cross-domain traffic prediction framework, termed Memory-Augmented Graph Liquid Time-Constant Network (MA-GLTC). Specifically, we first construct spatio-temporal units (STUs) to decompose traffic networks into transferable local units, enabling fine-grained knowledge alignment across domains. Then, a graph liquid time-constant network (GLTC) is developed to model graph-coupled traffic evolution in continuous time. Different from generic graph neural ODE-based models, GLTC introduces graph-coupled recurrent conductance into liquid time-constant dynamics, allowing node states to evolve with leakage, adaptive time constants, and neighborhood-aware feedback. Furthermore, a Memory-based Transfer Storage (MTS) mechanism is designed to preserve source-domain knowledge, retrieve matched traffic patterns, and update reliable target-domain patterns when unseen states emerge. Experiments on five public traffic datasets demonstrate that MA-GLTC consistently outperforms representative innerdomain and cross-domain baselines in both short-term and longterm prediction tasks. Compared with the second-best method, MA-GLTC reduces the average prediction errors by 3.02%, 0.33%, 8.92%, 10.09%, and 2.11%, respectively.

## Metadata
- **Published**: 2026-06-14T13:19:45Z
- **Authors**: Jinrong Xiang, Ming Xu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2606.15807v1)