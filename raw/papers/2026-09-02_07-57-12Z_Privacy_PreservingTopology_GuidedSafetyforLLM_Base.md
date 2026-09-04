---
title: Privacy-Preserving Topology-Guided Safety for LLM-Based Multi-Agent Systems via Federated Graph Learning
published: 2026-09-02T07:57:12Z
authors: Jinxi Yu, Eric Hanchen Jiang, Levina Li, Dong Liu, Zhi Zhang, Wenxiao Zhao, Yanxuan Yu, Kai-Wei Chang, Ying Nian Wu
url: http://arxiv.org/abs/2609.02967v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Privacy-Preserving Topology-Guided Safety for LLM-Based Multi-Agent Systems via Federated Graph Learning

## Abstract
Topology-guided safeguards for LLM-based multi-agent systems (MAS) train a GNN over the inter-agent communication graph to localize risky agents and intervene on the topology---but they assume one operator can pool all labeled traces. Across organizations that assumption breaks: episodes contain private prompts, tool outputs, and proprietary workflows, and no silo alone sees the full attack distribution. We cast privacy-preserving MAS safeguarding as graph federated learning and instantiate FGLGuard: each operator fits an edge-featured graph attention detector on its own judge-labeled episode graphs and shares only model updates. The method couples a proximal local objective for non-IID clients, domain-balanced aggregation, over-refusal-constrained threshold calibration, corroborated upstream scoring, and a guarded rewrite for blocked answers. Federation is not optional: off-the-shelf transfer collapses under distribution shift (AUROC 0.51 to 0.70 only after in-domain retraining), so a deployable guard must adapt on each site's private traces. On Agent-SafetyBench, R-Judge, and AgentDojo, federated FGLGuard exceeds the in-domain centralized ceiling on all three benchmarks without pooling any data---where unsupervised anomaly guards and local-only training fail. One guard federated across four different-domain operators comes within 0.03 AUROC of multi-domain centralization, while any single-domain guard collapses on the others. Live FGLGuard cuts AgentDojo's ground-truth attack-success rate by 43% at near-unguarded utility, zero API cost, and negligible capability loss.

## Metadata
- **Published**: 2026-09-02T07:57:12Z
- **Authors**: Jinxi Yu, Eric Hanchen Jiang, Levina Li, Dong Liu, Zhi Zhang, Wenxiao Zhao, Yanxuan Yu, Kai-Wei Chang, Ying Nian Wu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.02967v1)