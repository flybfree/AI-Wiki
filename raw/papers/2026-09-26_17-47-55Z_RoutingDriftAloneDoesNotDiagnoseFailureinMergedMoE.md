---
title: Routing Drift Alone Does Not Diagnose Failure in Merged MoE LLMs
published: 2026-09-26T17:47:55Z
authors: Yuanyi Wang, Yanggan Gu, Su Lu, Guanghao Zhu, Pengkai Wang, Yifan Yang, Congkai Xie, Zhaoyi Yan, Jianmin Wu, Hongxia Yang
url: http://arxiv.org/abs/2609.32821v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Routing Drift Alone Does Not Diagnose Failure in Merged MoE LLMs

## Abstract
Model merging efficiently combines specialized large language models (LLMs) without joint retraining, but can substantially alter expert routing in Mixture-of-Experts (MoE) models. Such \emph{routing drift} is often interpreted as routing failure, raising a fundamental question that remains unclear: \emph{does routing drift after MoE merging actually indicate routing failure, and what evidence should justify repair?} We investigate these questions across DeepSeekMoE, OLMoE, and Qwen3-MoE proposing a routing analysis toolkit for controlled counterfactual interventions and token-level analysis. By crossing source and merged router inputs and parameters, we attribute most expert reassignments to input shifts rather than parameter changes at the same layer. However, source-relative routing differences poorly predict next-token likelihood gains from source-route restoration, and different expert selections can produce directionally similar mixture outputs. We therefore operationalize routing failure as \textit{task loss recoverable under a specified routing intervention, with non-routing parameters fixed.} These tests detect recoverable loss under deliberate router corruption, whereas source-route restoration does not establish reliable task benefits in the evaluated merged models. Motivated by these, we propose \emph{Selective Router Repair (SRR)} as a case study, and find that source-specialist token-likelihood advantages do not reliably identify beneficial local corrections. Together, these findings show that \textbf{routing drift alone is insufficient evidence of routing failure}: source-informed corrections must be judged by their task-level intervention effects. The analysis toolkit and SRR code are released.

## Metadata
- **Published**: 2026-09-26T17:47:55Z
- **Authors**: Yuanyi Wang, Yanggan Gu, Su Lu, Guanghao Zhu, Pengkai Wang, Yifan Yang, Congkai Xie, Zhaoyi Yan, Jianmin Wu, Hongxia Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.32821v1)