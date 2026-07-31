---
title: Encryption-Compatible Clustered Federated Learning via Distributed Expectation-Maximization over Metadata
published: 2026-07-30T15:04:59Z
authors: Michael Ben Ali, Imen Megdiche, André Péninou, Olivier Teste
url: http://arxiv.org/abs/2607.28338v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Encryption-Compatible Clustered Federated Learning via Distributed Expectation-Maximization over Metadata

## Abstract
Clustered Federated Learning (CFL) addresses data heterogeneity in federated settings by grouping clients with similar data distributions to enable effective training. Existing methods face a trade-off between privacy preservation, communication cost, and computational efficiency. We formalize this as the CFL trilemma, according to which improving two of these dimensions comes at the expense of the third. A prominent paradigm relies on metadata (i.e., low-dimensional representations of client datasets shared with the server) to enable communication- and computation-efficient clustering. However, such approaches are not compatible with standard FL privacy-preserving mechanisms. To address this limitation, we propose FLAMECHE, which reformulates metadata-based CFL as a distributed Expectation-Maximization (EM) procedure, restricting server updates to additive operations while preserving efficiency. This design enables compatibility with practical secure FL schemes. We conducted extensive experiments on multiple datasets under various heterogeneous scenarios. Results show that FLAMECHE improves the effectiveness of client models. It enables encryption-compatible metadata-based clustering, enhancing its positioning within the CFL trilemma.

## Metadata
- **Published**: 2026-07-30T15:04:59Z
- **Authors**: Michael Ben Ali, Imen Megdiche, André Péninou, Olivier Teste
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28338v1)