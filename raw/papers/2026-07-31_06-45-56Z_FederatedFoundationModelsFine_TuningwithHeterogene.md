---
title: Federated Foundation Models Fine-Tuning with Heterogeneous Compressed Clients
published: 2026-07-31T06:45:56Z
authors: Shengkun Zhu, Jinshan Zeng, Zhihua Allen-Zhao, Mayi Xu, Quanqing Xu, Wei Ren, Qiang Yang, Yang Liu
url: http://arxiv.org/abs/2607.29071v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Federated Foundation Models Fine-Tuning with Heterogeneous Compressed Clients

## Abstract
Federated learning of foundation models faces a fundamental resource-asymmetry challenge: the institutions holding the most valuable domain-specific data cannot host billion-parameter models. Existing heterogeneous federated approaches attempt to bridge this gap through parameter-efficient tuning, model pruning, or knowledge distillation, yet each trades away a critical property, whether full-model memory reduction, architectural self-containedness, or representational fidelity, leaving the core tension unresolved. We propose FedSLM, a parameter-centric framework for federated fine-tuning with heterogeneous compressed clients. FedSLM uses SVD-based decomposition to produce self-contained client models, whose low-rank subspaces form nested manifolds that are structurally compatible for aggregation. It then applies a two-stage protocol that synchronizes lightweight adapters within compression groups and fuses full-rank reconstructions across groups via structural alignment. Finally, a weak-to-strong elicitation step with auxiliary confidence loss transfers the aggregated knowledge to the full-scale server, while an explicit bias--variance trade-off mitigates compression artifacts. We provide theoretical guarantees for adapter-level aggregation, subspace-alignment bounds for cross-group fusion, and a characterization of how the confidence loss mitigates weak-supervision noise. Experiments on natural language and vision--language benchmarks show that FedSLM outperforms existing federated baselines under both IID and non-IID partitions, while client models operate at roughly 50% of the GPU memory required by the full model.

## Metadata
- **Published**: 2026-07-31T06:45:56Z
- **Authors**: Shengkun Zhu, Jinshan Zeng, Zhihua Allen-Zhao, Mayi Xu, Quanqing Xu, Wei Ren, Qiang Yang, Yang Liu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29071v1)