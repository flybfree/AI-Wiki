---
title: Unveiling the Depth-Performance Dilemma in Split-Federated Fine-tuning of LLMs
published: 2026-08-23T02:53:20Z
authors: Hariharan Ramesh, Someshwaran Murugaiyan, Jyotikrishna Dass
url: http://arxiv.org/abs/2608.22188v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Unveiling the Depth-Performance Dilemma in Split-Federated Fine-tuning of LLMs

## Abstract
Split Federated Fine-tuning (SFF) is a promising paradigm for scaling Large Language Models (LLMs) by partitioning model depth between resource-constrained clients and a centralized server. While system incentives for throughput and privacy favor deep partitions, the impact of such configurations on model utility remains poorly understood. In this work, we identify and characterize the Depth-Performance Dilemma: the regime that maximizes system efficiency is precisely where fine-tuning quality collapses. Through a comprehensive audit across four model scales (GPT-2 to Llama-3-8B) and diverse benchmarks, we demonstrate that deeper partitions provide monotonic gains in throughput and privacy at the cost of catastrophic performance plateaus. We evaluate a suite of state-of-the-art federated adapter aggregation methods including AVG, STACK, SVD, and FREEZE, revealing that while these techniques are effective in standard Federated Learning, they fail to mitigate the artifacts unique to split architectures. Finally, we provide a mechanistic diagnosis for this failure, tracing the collapse to the near-isometric topology of Transformers, which allows aggregation noise to propagate without attenuation until it triggers Attention Collapse in the server partition. Our findings challenge the prevailing assumption that partition depth is a utility-neutral tuning knob and provide a structural foundation for stable distributed LLM fine-tuning.

## Metadata
- **Published**: 2026-08-23T02:53:20Z
- **Authors**: Hariharan Ramesh, Someshwaran Murugaiyan, Jyotikrishna Dass
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.22188v1)