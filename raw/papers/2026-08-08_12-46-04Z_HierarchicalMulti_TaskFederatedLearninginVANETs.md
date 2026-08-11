---
title: Hierarchical Multi-Task Federated Learning in VANETs
published: 2026-08-08T12:46:04Z
authors: M. Saeid HaghighiFard, Sinem Coleri
url: http://arxiv.org/abs/2608.08111v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Hierarchical Multi-Task Federated Learning in VANETs

## Abstract
Vehicular Ad hoc Networks (VANETs) increasingly rely on federated learning (FL) to enable collaborative intelligence without sharing raw sensory data. However, most existing vehicular FL frameworks assume that all vehicles train a single global model for a common task, which limits their applicability in practical vehicular environments where vehicles may perform heterogeneous learning tasks under non-independent and identically distributed (non-IID) data, intermittent connectivity, and high mobility. To address these challenges, this paper proposes an AutoEncoder-based Reliability-Optimized Hierarchical Multi-Task Federated Learning (AERO-HMTFL) framework for dynamic multi-hop clustered VANETs. The proposed framework introduces a tri-weighted clustering metric that jointly considers vehicular mobility, shared-model similarity, and task affinity to produce mobility-stable, semantically aligned clusters. Each vehicle employs a split-model architecture comprising a shared autoencoder-based representation module and multiple task-specific heads, with only the shared autoencoder parameters exchanged while the task heads remain local. To improve robustness, cluster heads perform reliability-aware aggregation based on historical validation performance and participation frequency, while the Evolved Packet Core (EPC) conducts global shared-autoencoder fusion across clusters. Extensive simulations demonstrate that, compared with the multi-task federated learning benchmarks, AERO-HMTFL achieves up to 13% higher sustained EPC-level accuracy, exhibits more stable learning dynamics, and reduces EPC-level packet transmissions by approximately 87-97%. Under short-range connectivity, it also requires approximately 13-29% fewer communication rounds to converge.

## Metadata
- **Published**: 2026-08-08T12:46:04Z
- **Authors**: M. Saeid HaghighiFard, Sinem Coleri
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08111v1)