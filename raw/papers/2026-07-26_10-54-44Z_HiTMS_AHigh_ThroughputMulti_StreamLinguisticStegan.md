---
title: HiTMS: A High-Throughput Multi-Stream Linguistic Steganography Framework
published: 2026-07-26T10:54:44Z
authors: Ruiyi Yan, Yugo Murawaki, Zhongliang Yang
url: http://arxiv.org/abs/2607.23597v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# HiTMS: A High-Throughput Multi-Stream Linguistic Steganography Framework

## Abstract
Generative linguistic steganography conceals secret bits within the sampling randomness of large language models. Existing schemes are single-stream, conveying an entire secret through a single response to a single prompt. This convention incurs two limitations: it provides no protocol-level support for batched multi-stream inference, and naive co-batching does not conceal slot occupancy or payload completion. We propose HiTMS, which distributes a secret across multiple responses produced jointly over successive rounds of interaction. Each round embeds and extracts several streams within a single batched call, thereby amortizing the cost of model invocation and substantially improving throughput. To ensure recoverability, HiTMS wraps each response in a self-describing frame and employs a key-derived schedule that binds streams to slots and fills unused slots with decoys, guaranteeing exact recovery while concealing the number of active streams. The framework is agnostic to both the language model and the steganographic coder. Across eight dataset-model-coder settings, eight-stream HiTMS achieves up to 4.3 times higher embedding and extraction speeds than single-stream baselines, while reducing the steganalyzer AUROC from 0.681 to 0.601 on average. Additional experiments with 4 to 64 streams demonstrate sustained throughput gains as concurrency increases. GitHub repository for this work is https://github.com/ryehr/HiTMS_steganography.

## Metadata
- **Published**: 2026-07-26T10:54:44Z
- **Authors**: Ruiyi Yan, Yugo Murawaki, Zhongliang Yang
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23597v1)