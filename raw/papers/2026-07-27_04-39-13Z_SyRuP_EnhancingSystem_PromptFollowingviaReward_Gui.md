---
title: SyRuP: Enhancing System-Prompt Following via Reward-Guided Prediction in LLM Decoding
published: 2026-07-27T04:39:13Z
authors: Seoyeon Kim, Minjae Kang, Jaehyung Kim
url: http://arxiv.org/abs/2607.23991v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# SyRuP: Enhancing System-Prompt Following via Reward-Guided Prediction in LLM Decoding

## Abstract
Large Language Models (LLMs) are increasingly controlled through system prompts that specify roles, styles, formats, and safety requirements. However, models follow these prompts only implicitly through in-context learning, which can be insufficient for complex or compositional prompts. Existing approaches often require model tuning or response-level reranking, limiting their practicality for lightweight inference-time control. We introduce SyRuP, a decoding-time framework for improving system-prompt adherence while keeping the base LM frozen. SyRuP trains a cross-attention reward head from system-prompt-conditioned preference pairs, treating the system prompt as a separate memory to produce token-level adherence scores. At inference, SyRuP reranks the base LM's top-k candidates by combining base logits with the learned reward signal and an optional contrastive signal capturing system-induced logit shifts. Experiments on system-prompt following benchmarks show that SyRuP consistently outperforms prompting and decoding-time baselines with moderate inference overhead. These results suggest that explicit token-level guidance is an effective and practical mechanism for reliable system-prompt following.

## Metadata
- **Published**: 2026-07-27T04:39:13Z
- **Authors**: Seoyeon Kim, Minjae Kang, Jaehyung Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.23991v1)