---
title: PaletteID: Prototype-Composed Semantic Identifiers for Multimodal CTR Prediction
published: 2026-07-31T03:54:38Z
authors: Huanyu Liu, Baining Chen, Hui Liu, Zengyang Li, Ziyi Huang
url: http://arxiv.org/abs/2607.29000v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PaletteID: Prototype-Composed Semantic Identifiers for Multimodal CTR Prediction

## Abstract
Multimodal information can improve the accuracy of click-through rate (CTR) prediction and effectively alleviate item cold-start and long-tail problems. Recent studies commonly discretize pretrained multimodal embeddings into semantic identifiers (SIDs), allowing the model to learn task-specific semantic representations for recommendation. However, existing methods still provide limited gains due to two major limitations. First, codebook assignment fails to preserve semantic relevance and discards fine-grained continuous signals in the original embedding space. Second, the residual code paths are highly dependent on prefix codes, which limits the effective representational scalability of hierarchical identifiers. To address these issues, we propose PaletteID (PID), a prototype-based semantic identifier. Inspired by palette-based color composition, PID uses a compact set of representative prototype items as semantic anchors to bridge pretrained multimodal content space and recommendation models. Specifically, we first construct a prototype palette with Semantic Quality-Aware Determinantal Point Process (SQ-DPP), which jointly considers local content density and global semantic diversity. Then, for each target item, PID retrieves a sequence of semantically related prototypes and aggregates them into an informative PID representation, enabling rich and complementary semantic modeling. Extensive experiments on two public datasets demonstrate that PID consistently improves CTR prediction and yields larger gains for long-tail items. PID also produces more robust identifier assignments and provides more interpretable token semantics than existing residual SID methods.

## Metadata
- **Published**: 2026-07-31T03:54:38Z
- **Authors**: Huanyu Liu, Baining Chen, Hui Liu, Zengyang Li, Ziyi Huang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29000v1)