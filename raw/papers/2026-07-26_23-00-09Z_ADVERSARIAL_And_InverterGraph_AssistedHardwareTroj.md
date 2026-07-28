---
title: ADVERSARIAL: And-Inverter Graph-Assisted Hardware Trojan Detection At Scale
published: 2026-07-26T23:00:09Z
authors: Yaroslav Popryho, Debjit Pal, Inna Partin-Vaisband
url: http://arxiv.org/abs/2607.23882v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# ADVERSARIAL: And-Inverter Graph-Assisted Hardware Trojan Detection At Scale

## Abstract
Modern System-on-Chip (SoCs) often contain hundreds of millions to tens of billions of gates, making existing Hardware Trojan (HT) detection methods impractical due to their immense scale. The proposed approach incorporates symbolically enabled learning by modeling flattened gate-level netlists as Boolean networks represented as And-Inverter Graphs (AIGs), where all internal nodes are 2-input AND gates and inversions reside on the edges. Each directed connection is expressed as a triple within a Knowledge Graph Embedding (KGE) framework, producing compact, constant-size per-node representations that retain multi-hop structural context. The AIG's bounded fan-in and uniform semantics ensure training and inference complexity scale linearly with edge count, addressing major scalability bottlenecks in HT detection. Symbolically enabled learning across deep datapaths enables the model to differentiate circuit structures from rare and functionally inconsistent connections that signify potential Trojan triggers and payloads. Experiments on large-scale SoC benchmarks demonstrate clear geometric separation between Trojan and benign nodes and practical scalability.

## Metadata
- **Published**: 2026-07-26T23:00:09Z
- **Authors**: Yaroslav Popryho, Debjit Pal, Inna Partin-Vaisband
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23882v1)