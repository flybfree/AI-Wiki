---
title: PropUQ-MAS: Propagation-Aware Uncertainty Quantification for LLM Multi-Agent Systems
published: 2026-08-22T23:07:39Z
authors: Yaokun Liu, Yifan Liu, Daniel Yue Zhang, Ruichen Yao, Zelin Li, Dong Wang
url: http://arxiv.org/abs/2608.22130v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# PropUQ-MAS: Propagation-Aware Uncertainty Quantification for LLM Multi-Agent Systems

## Abstract
LLM-based multi-agent systems (MAS) solve complex tasks through communication among role-specialized agents. However, inter-agent dependencies introduce reliability risks beyond isolated agent failures. For instance, errors in intermediate messages could be inherited and amplified by downstream agents. Existing uncertainty quantification (UQ) methods mainly target isolated responses or single-agent reasoning, and therefore fail to capture uncertainty propagation in MAS. To this end, we propose PropUQ-MAS, an error propagation-aware UQ framework that represents MAS execution as a communication-structured graph and estimates each step's reliability by combining local uncertainty with uncertainty inherited from upstream messages. Extensive experiments demonstrate that PropUQ-MAS consistently improves UQ in MAS, with average relative gains of +6.10% in AUROC and +47.58% in PRR.

## Metadata
- **Published**: 2026-08-22T23:07:39Z
- **Authors**: Yaokun Liu, Yifan Liu, Daniel Yue Zhang, Ruichen Yao, Zelin Li, Dong Wang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22130v1)