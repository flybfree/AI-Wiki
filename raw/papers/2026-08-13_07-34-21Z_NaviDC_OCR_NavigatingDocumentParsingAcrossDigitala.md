---
title: NaviDC-OCR: Navigating Document Parsing Across Digital and Camera-Captured Documents
published: 2026-08-13T07:34:21Z
authors: Peng Cai, Zhaofan Zou, Shifa Liu, Yikun Wang, Jiawei Tang, Kaicheng Yang, Meng Tong, Zhongjiang He, Hao Sun
url: http://arxiv.org/abs/2608.12898v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# NaviDC-OCR: Navigating Document Parsing Across Digital and Camera-Captured Documents

## Abstract
Document parsing aims to transform unstructured documents into structured and machine-readable representations. Recent advances in Vision-Language Models (VLMs) have significantly advanced document parsing. However, existing approaches still face two major challenges. First, decoupled VLM-based methods heavily rely on accurate layout analysis, where geometric distortions in camera-captured documents can introduce cascading errors. Second, although end-to-end VLM-based methods alleviate the dependence on explicit layout detection, they often suffer from redundant generation, hallucinations, and insufficient structural reasoning in high-resolution scenarios. To address these challenges, we propose NaviDC-OCR, a unified framework for document parsing. NaviDC-OCR introduces deformation-aware learning to incorporate geometric perception into VLMs and proposes an adaptive sampling mechanism for complex layout representation. Furthermore, a content-structure decoupled learning strategy is developed to explicitly model formula grammars and table structures, enabling more effective structured representation learning. Extensive experiments demonstrate that NaviDC-OCR achieves state-of-the-art performance across diverse document parsing benchmarks. It obtains overall scores of 96.87, 88.53 and 78.41 on OmniDocBench v1.6, Wild-OmniDocBench, and PureDocBench, respectively, and ranks first in the ICDAR 2026 Sci-ImageMiner Challenge. These results validate the effectiveness and generalization capability of NaviDC-OCR in complex document parsing scenarios.

## Metadata
- **Published**: 2026-08-13T07:34:21Z
- **Authors**: Peng Cai, Zhaofan Zou, Shifa Liu, Yikun Wang, Jiawei Tang, Kaicheng Yang, Meng Tong, Zhongjiang He, Hao Sun
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12898v1)