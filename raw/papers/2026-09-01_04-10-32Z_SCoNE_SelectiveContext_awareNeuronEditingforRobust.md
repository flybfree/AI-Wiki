---
title: SCoNE: Selective Context-aware Neuron Editing for Robust Retrieval-Augmented Generation
published: 2026-09-01T04:10:32Z
authors: Chaewon Kim, Seo Yeon Park
url: http://arxiv.org/abs/2609.00689v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SCoNE: Selective Context-aware Neuron Editing for Robust Retrieval-Augmented Generation

## Abstract
Retrieval-Augmented Generation (RAG) is highly sensitive to retrieval noise: when retrieved documents mix informative and irrelevant context, LLMs are easily distracted, leading to hallucinations. To overcome this, we propose SCoNE (Selective Context-aware Neuron Editing), a training-free model editing approach that improves retrieval noise robustness by selectively strengthening context-aware FFN neurons that are identified by both high attribution and high cross-input variability. SCoNE requires only a small number of mining samples, no fine-tuning, and no inference-time overhead. Across various knowledge-intensive question-answering benchmarks and two LLM backbones, SCoNE consistently outperforms competitive baseline methods. Our code is available at https://github.com/HYU-ARK-Lab/SCoNE.

## Metadata
- **Published**: 2026-09-01T04:10:32Z
- **Authors**: Chaewon Kim, Seo Yeon Park
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00689v1)