---
title: DualStake: Dual-Path Confidence Calibration in Deep Research Agents
published: 2026-09-01T08:56:01Z
authors: Yinuo Xu, Yuwei Liang, Jianjie Cheng, Meng Wang, Yongcan Yu, Shuo Lu, Jian Liang
url: http://arxiv.org/abs/2609.00935v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# DualStake: Dual-Path Confidence Calibration in Deep Research Agents

## Abstract
Deep Research agents tackle knowledge-intensive tasks through multi-round retrieval and decision-oriented generation. However, these agents suffer from severe overconfidence, making their expressed confidence unreliable for user trust and downstream abstention. To address this, we augment the Deep Research pipeline with step confidence elicitation after each retrieval, building on the commonly used post-answer verbalized confidence. Interestingly, we find that Evidence Confidence (E-Conf), elicited after the final retrieval step, provides a stronger uncertainty signal than Answer Confidence (A-Conf), elicited after answer generation, and that A-Conf is largely shaped by E-Conf. Based on these findings, we propose DualStake, a dual-path calibration method that applies margin-clipped, confidence-dependent stake rewards to jointly align E-Conf and A-Conf with answer correctness while limiting extreme confidence optimization. Experiments on Qwen2.5-7B, Qwen2.5-7B-Instruct, and Qwen3-4B across 8 QA benchmarks demonstrate that DualStake consistently improves calibration without sacrificing answer accuracy. The code is available at https://github.com/FloXXXt/DualStake.

## Metadata
- **Published**: 2026-09-01T08:56:01Z
- **Authors**: Yinuo Xu, Yuwei Liang, Jianjie Cheng, Meng Wang, Yongcan Yu, Shuo Lu, Jian Liang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.00935v1)