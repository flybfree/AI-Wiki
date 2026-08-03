---
title: Data Turnstile: A Scalable Open Framework for Function-Calling Data Generation
published: 2026-07-31T10:21:36Z
authors: Goutham Ramakrishnan, Megha Sharma
url: http://arxiv.org/abs/2607.29250v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Data Turnstile: A Scalable Open Framework for Function-Calling Data Generation

## Abstract
Small language models (SLMs) are attractive for agentic deployment due to low latency, reduced cost, and on-device privacy, yet they struggle with tool-use tasks where training data is scarce and noisy. Unlike larger models, SLMs cannot compensate for low-quality supervision through sheer capacity, making data quality the critical bottleneck. We present Data Turnstile, an open-source framework that takes user-defined API specifications and generates high-quality synthetic training data for function calling. Turnstile decomposes multi-turn tool-use interactions into constrained, stepwise generation with validation and error-feedback loops, providing fine-grained control over API diversity, conversation complexity, and output correctness. We demonstrate effectiveness of domain adaptation with Turnstile data on two challenging function calling benchmarks. On the BFCL single-turn benchmark, a Qwen3-0.6B fine-tuned on Turnstile data without chain-of-thought achieves 75.9% overall accuracy (versus 67.4% for the base model with thinking enabled), closing the gap with thinking-enabled Qwen3-1.7B (78.4%) and Qwen3-4B (79.9%) despite being 3$\times$ and 7$\times$ smaller respectively. On $τ^2$-bench, a multi-turn agentic benchmark, Turnstile-trained Qwen3-1.7B achieves 31.1% pass^1 on the Telecom domain, improving 4.7$\times$ over its 6.6% base and surpassing Qwen2.5-32B-Instruct (27.4%), a model 19$\times$ larger. Turnstile-trained Qwen3-0.6B achieves 24.6%, improving 7$\times$ over its 3.5% base and approaching the 32B model (53$\times$ larger). We release Data Turnstile along with a dataset spanning 1,000+ APIs and 100K+ multi-turn interactions.

## Metadata
- **Published**: 2026-07-31T10:21:36Z
- **Authors**: Goutham Ramakrishnan, Megha Sharma
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.29250v1)