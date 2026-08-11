---
title: Evidence-Grounded Forensic Reasoning for Detecting and Grounding Multi-Modal Media Manipulation
published: 2026-08-08T08:41:26Z
authors: Yichun Yeh, Yiheng Li, Xiaobo Hu, Zhen Lei, Yang Yang
url: http://arxiv.org/abs/2608.08009v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Evidence-Grounded Forensic Reasoning for Detecting and Grounding Multi-Modal Media Manipulation

## Abstract
Fake news increasingly relies on cross-modal image-text forgeries, making transparent and verifiable reasoning chains an urgent need for Detecting and Grounding Multi-Modal Media Manipulation (DGM4). Existing methods produce black-box detection results without any decision rationale, limiting their reliability in forensic practice. Multi-modal Large Language Models (MLLMs) offer a natural path toward explainability, but applying them to DGM4 raises two difficulties. First, models tend to generate explanations disconnected from predicted evidence locations, producing unverified attribution. Second, enforcing evidence-conclusion consistency requires active optimization, yet uniform training signals fail to distinguish localization tokens from classification tokens, making multi-head joint training unreliable. We propose a multi-modal manipulation detector based on an Evidence-Grounded Forensic Reasoning (EFR) framework. EFR introduces an Anchor-and-Verify reasoning chain that enforces modality-isolated perception before cross-modal comparison, with conclusion coordinates as explicit anchors to which downstream evidence must spatially correspond. A verifiable reward system then enforces evidence-conclusion consistency during training, while a Modality-Decoupled Advantage (MDA) routing mechanism mitigats credit misassignment across prediction tasks. Experiments show that EFR achieves state-of-the-art performance while producing structured forensic reasoning records that explicitly bind explanations to evidence.

## Metadata
- **Published**: 2026-08-08T08:41:26Z
- **Authors**: Yichun Yeh, Yiheng Li, Xiaobo Hu, Zhen Lei, Yang Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.08009v1)