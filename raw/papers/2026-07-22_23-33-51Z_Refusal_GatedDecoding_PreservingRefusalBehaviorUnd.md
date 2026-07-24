---
title: Refusal-Gated Decoding: Preserving Refusal Behavior Under High-Temperature Sampling
published: 2026-07-22T23:33:51Z
authors: Phillip Howard, Xin Su, Allen Roush, Manikandan Ravikiran, Amir Abdullah
url: http://arxiv.org/abs/2607.20791v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Refusal-Gated Decoding: Preserving Refusal Behavior Under High-Temperature Sampling

## Abstract
High-temperature sampling is one of the primary mechanisms for increasing diversity in LLMs. Recent advances in truncation-based sampling techniques have helped mitigate drawbacks of high-temperature sampling such as neural text degeneration, thereby enabling greater diversity in LLM outputs without sacrificing coherence. However, increasing the entropy of the token probability distribution via high temperatures has also been shown to weaken model guardrails by reducing the model's refusal response in the presence of harmful prompts. Despite the potential benefits of high-temperature sampling and the importance of maintaining model safety, there is a lack of existing solutions for maintaining the refusal behavior of LLMs under a higher entropy regime. To address this gap, we systematically study how temperature influences refusal behavior in LLMs and propose an efficient sequential decoding approach which preserves a model's greedy decoding refusal response at high temperatures while incurring minimal additional latency. Through extensive experiments, we show that our approach preserves 91-99% of the greedy decoding refusal behavior across three benchmark datasets without compromising the model's high-temperature response for safe prompts. Our work demonstrates how refusal behavior can be maintained in an efficient manner for applications which require high-temperature sampling.

## Metadata
- **Published**: 2026-07-22T23:33:51Z
- **Authors**: Phillip Howard, Xin Su, Allen Roush, Manikandan Ravikiran, Amir Abdullah
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.20791v1)