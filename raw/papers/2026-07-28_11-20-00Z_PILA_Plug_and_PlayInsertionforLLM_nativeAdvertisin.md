---
title: PILA: Plug-and-Play Insertion for LLM-native Advertising
published: 2026-07-28T11:20:00Z
authors: Zhaowei Zhang, Yuhan Fu, Yihang Zhang, Xiaohan Liu, Ceyao Zhang, Xiaoyuan Zhang, Yipeng Kang, Tonghan Wang, Yaodong Yang
url: http://arxiv.org/abs/2607.25590v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PILA: Plug-and-Play Insertion for LLM-native Advertising

## Abstract
How to monetize large language models (LLMs) by naturally integrating sponsored content into their responses, known as LLM-native advertising, has recently emerged as a critical problem. However, existing solutions entangle advertising with content generation inside a single model, which is incompatible with modern API-only or workflow-based LLM applications and inevitably compromises the original response quality. To address this, we propose PILA, which reformulates ad insertion as a conditional response rewriting problem and decouples it from the upstream service as a lightweight sidecar module. PILA is model-agnostic and can be seamlessly integrated with existing LLM services without modifying the base model or its workflow. It also exposes a controllable trade-off between user-side naturalness and ad-side exposure, offering a practical interface for downstream pricing and deployment. Experiments across diverse upstream models show that \pila consistently improves ad effectiveness while preserving response quality, highlighting its promise as a practical solution for LLM-native advertising.

## Metadata
- **Published**: 2026-07-28T11:20:00Z
- **Authors**: Zhaowei Zhang, Yuhan Fu, Yihang Zhang, Xiaohan Liu, Ceyao Zhang, Xiaoyuan Zhang, Yipeng Kang, Tonghan Wang, Yaodong Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.25590v1)