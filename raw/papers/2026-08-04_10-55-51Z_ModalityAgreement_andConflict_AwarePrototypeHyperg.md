---
title: Modality Agreement- and Conflict-Aware Prototype Hypergraph Learning for Multimodal Intent Understanding
published: 2026-08-04T10:55:51Z
authors: Mohnish Raj, Suraj Kumar, Soumi Chattopadhayay, Chandranath Adak, Ayan Dutta
url: http://arxiv.org/abs/2608.04054v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Modality Agreement- and Conflict-Aware Prototype Hypergraph Learning for Multimodal Intent Understanding

## Abstract
Multimodal intent recognition requires understanding not only what textual, acoustic, and visual signals share, but also how they disagree. Such disagreement is frequently class-informative; for example, lexical positivity accompanied by incongruent vocal or facial behavior may indicate sarcasm or taunting, yet most fusion methods either encourage modality alignment or treat inconsistency as uncertainty to be suppressed. We propose MACH (Modality Agreement- and Conflict-aware prototype Hypergraph), a hierarchical prototype-hypergraph framework that represents multimodal agreement and conflict as distinct, recurring relational structures. MACH progressively composes unimodal representations into bimodal and trimodal abstractions. At each applicable level, modality-composition anchors activate sparse agreement prototype hypergraphs that capture reusable consensus patterns, while a separate conflict pathway maps cross-modal discrepancies to dedicated conflict prototype hypergraphs. The two pathways are combined through a feature-wise, sample-adaptive arbitration mechanism, enabling the model to preserve informative disagreement while suppressing incidental modality noise. A progressive optimization strategy stabilizes the interdependent hierarchy before joint agreement-conflict learning. Experiments on benchmark datasets demonstrate the effectiveness of the proposed formulation, while component and robustness analyses validate the distinct roles of hierarchical composition, prototype-mediated semantic refinement, and agreement-conflict arbitration.

## Metadata
- **Published**: 2026-08-04T10:55:51Z
- **Authors**: Mohnish Raj, Suraj Kumar, Soumi Chattopadhayay, Chandranath Adak, Ayan Dutta
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.04054v1)