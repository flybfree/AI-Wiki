---
title: Dynamic Multi-Byte Prediction With Hierarchical Language Models
published: 2026-08-16T00:11:11Z
authors: Abraham Toluwase Owodunni, Chibuzor Okocha, Christan Grant, Tomasz Limisiewicz, Sachin Kumar
url: http://arxiv.org/abs/2608.15454v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dynamic Multi-Byte Prediction With Hierarchical Language Models

## Abstract
Byte-level hierarchical language models (LMs) have recently emerged as a robust alternative to their popular counterparts that use subword tokenization. However, generating one byte at a time remains a bottleneck for inference speed. To address this, we introduce multi-byte prediction (MBP), which generates multiple bytes in parallel, speeding up inference with minimal performance impact and no additional parameters. MBP builds on the popular multi-token prediction (MTP) paradigm with two crucial innovations. First, we introduce a variable-length prediction window that aligns with the latent tokens, or segments, of a hierarchical LM. Second, we implement a novel attention-masking scheme that enables parallel byte prediction without violating causality. We show that multi-byte prediction strikes a Pareto-optimal trade-off across multiple generative tasks, instruction following, question answering, summarization, and machine translation, achieving the best trade-off between performance and inference throughput.

## Metadata
- **Published**: 2026-08-16T00:11:11Z
- **Authors**: Abraham Toluwase Owodunni, Chibuzor Okocha, Christan Grant, Tomasz Limisiewicz, Sachin Kumar
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.15454v1)