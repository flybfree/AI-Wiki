---
title: HyperFL: Query-Adaptive Representation Learning for Software Fault Localization
published: 2026-08-04T00:00:46Z
authors: Shuai Shao, Yiming Zeng, Yu Zhao, Tingting Yu
url: http://arxiv.org/abs/2608.02967v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HyperFL: Query-Adaptive Representation Learning for Software Fault Localization

## Abstract
Software fault localization identifies the code locations responsible for reported issues and is a fundamental step toward automated debugging and program repair. Recent retrieval-based approaches formulate fault localization as a dense retrieval task by learning a shared embedding space between issue reports and source code. However, these methods encode all issue reports using a fixed query representation, despite the substantial diversity of real-world issue reports in length, structure, and debugging information. To address this limitation, we propose HyperFL, a query-adaptive representation learning framework for software fault localization. HyperFL employs a lightweight hypernetwork to generate query-specific LoRA parameters for the query encoder, enabling dynamic query adaptation while keeping the code encoder fixed and reusable. Experiments on a real-world issue localization benchmark demonstrate that HyperFL consistently improves retrieval performance across multiple embedding backbones, achieving up to 13.3% relative improvement in function-level MRR@10 and 16.7% relative improvement in Hit@1 over the state-of-the-art method SweRank. Further analysis shows that HyperFL learns distinct adaptation patterns for different issue characteristics, highlighting the effectiveness of query-adaptive representations for software issue localization.

## Metadata
- **Published**: 2026-08-04T00:00:46Z
- **Authors**: Shuai Shao, Yiming Zeng, Yu Zhao, Tingting Yu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.02967v1)