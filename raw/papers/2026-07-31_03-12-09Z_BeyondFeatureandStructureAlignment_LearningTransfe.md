---
title: Beyond Feature and Structure Alignment: Learning Transferable Propagation Knowledge for Graph Foundation Models
published: 2026-07-31T03:12:09Z
authors: Yi Wang, Jitao Zhao, Di Jin, Dongxiao He
url: http://arxiv.org/abs/2607.28980v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Feature and Structure Alignment: Learning Transferable Propagation Knowledge for Graph Foundation Models

## Abstract
Graph Foundation Models (GFMs) have recently emerged as a promising paradigm for enabling knowledge transfer across diverse domains. Unlike traditional graph learning methods that are typically designed for in-domain settings, GFMs aim to learn transferable knowledge that can generalize to unseen graph domains. However, unlike language or visual data, graphs lack intrinsic and unified representation units, such as tokens in language and patches in vision, making it challenging to identify transferable knowledge units for building graph foundation models. Existing graph foundation models mainly focus on mitigating domain discrepancies through feature alignment and structure alignment, while overlooking the exploration of transferable knowledge units underlying graph data. Moreover, these methods generally rely on fixed propagation mechanisms during message passing, overlooking the heterogeneity in propagation patterns, as different edges may exhibit distinct propagation patterns for different feature dimensions. To address these limitations, we propose a Propagation-aware Graph Foundation Model (ProGFM), which regards the propagation relationships between edges and feature dimensions as transferable knowledge units. Through a propagation relationship prototype bank, ProGFM learns cross-domain transferable propagation knowledge, enabling adaptive information aggregation in unseen graph domains. Extensive experiments across various cross-domain transfer scenarios demonstrate that ProGFM possesses strong cross-domain knowledge transfer capability and exhibits superior generalization performance compared with existing methods.

## Metadata
- **Published**: 2026-07-31T03:12:09Z
- **Authors**: Yi Wang, Jitao Zhao, Di Jin, Dongxiao He
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28980v1)