---
title: SG-Layout: Structured Scene Graph-Guided Layout Generation with LLMs
published: 2026-08-02T09:11:38Z
authors: Junsheng Wang, Chao Chen, Mengying Xie, Mingyan Li, Fuqiang Gu
url: http://arxiv.org/abs/2608.01106v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SG-Layout: Structured Scene Graph-Guided Layout Generation with LLMs

## Abstract
Understanding and generating spatially coherent layouts from natural language remains a fundamental yet challenging task for large language models (LLMs). Existing LLMs often struggle to capture explicit geometric relationships and structural dependencies between objects. To address this issue, we propose SG-Layout, a graph-guided layout generation framework that explicitly incorporates structured spatial knowledge into LLMs. SG-Layout follows a two-stage training paradigm: (1) a graph-language feature alignment stage, where a relational graph encoder and a projector are trained to map scene-graph embeddings into the LLM's linguistic space; and (2) an instruction tuning stage, where LoRA-based adapters enable efficient fine-tuning for instruction-driven layout generation while keeping the backbone frozen. We evaluate SG-Layout on image layout generation, indoor scene synthesis and robotic object rearrangement tasks. Experimental results show that SG-Layout improves spatial reasoning accuracy and geometric consistency over the compact open-source backbone, with particularly clear advantages in relation-dense and compositionally complex scenes. These results highlight the effectiveness of graph-structured feature alignment for enhancing controllable layout generation.

## Metadata
- **Published**: 2026-08-02T09:11:38Z
- **Authors**: Junsheng Wang, Chao Chen, Mengying Xie, Mingyan Li, Fuqiang Gu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.01106v1)