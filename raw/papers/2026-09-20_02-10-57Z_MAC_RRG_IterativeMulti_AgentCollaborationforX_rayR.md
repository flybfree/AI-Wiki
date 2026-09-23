---
title: MAC-RRG: Iterative Multi-Agent Collaboration for X-ray Radiology Report Generation
published: 2026-09-20T02:10:57Z
authors: Futian Wang, Yuhan Qiao, Xiao Wang, Dan Xu, Yuehang Li, Zhixiang Guo, Yaowei Wang, Jin Tang
url: http://arxiv.org/abs/2609.26124v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# MAC-RRG: Iterative Multi-Agent Collaboration for X-ray Radiology Report Generation

## Abstract
Despite the remarkable progress of LLM-based and knowledge graph-augmented Radiology Report Generation (RRG) methods, existing techniques still suffer from inherent defects. Conventional LLM-only models lack structured medical prior knowledge, resulting in frequent medical hallucinations and low diagnostic interpretability. Current knowledge graph-enhanced schemes adopt static one-round knowledge fusion with single-source knowledge, incapable of dynamic knowledge updating according to generation feedback. This paper proposes a novel Multi-Agent Collaborative iterative framework for X-ray Radiology Report Generation, termed MAC-RRG. Inspired by multi-agent technology, our framework constructs a closed-loop optimization paradigm based on task decoupling and collaborative reasoning. Specifically, the framework first generates a preliminary radiology report from input X-ray images via a vision encoder and a basic LLM. Subsequently, a multimodal knowledge graph (MM-KG) agent mines structured disease correlation and anatomical knowledge from medical knowledge graphs, while an auxiliary knowledge agent extracts unstructured domain knowledge from public medical databases. The multi-source knowledge acquired by dual agents is fused and embedded to guide the LLM in iteratively refining the initial report. Extensive quantitative and qualitative experiments on mainstream X-ray RRG datasets, including IU X-ray, MIMIC, and CheXpert Plus, fully verify the superiority of our proposed method. The source code and pre-trained models have been released on https://github.com/Event-AHU/Medical_Image_Analysis

## Metadata
- **Published**: 2026-09-20T02:10:57Z
- **Authors**: Futian Wang, Yuhan Qiao, Xiao Wang, Dan Xu, Yuehang Li, Zhixiang Guo, Yaowei Wang, Jin Tang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.26124v1)