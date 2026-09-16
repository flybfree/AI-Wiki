---
title: State of Thought Enables Endogenous Reasoning
published: 2026-09-13T05:55:03Z
authors: Zhiren Gong, Yikun Hou, Zihao Zeng, Ming Xiao, Chau Yuen, Wei Yang Bryan Lim
url: http://arxiv.org/abs/2609.16055v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# State of Thought Enables Endogenous Reasoning

## Abstract
Test-time compute has emerged as a major approach to improving the capabilities of Large Language Models (LLMs). However, existing test-time reasoning paradigms rely heavily on externally imposed control, either through fixed reasoning programs or through costly expansion in constrained search spaces, limiting both generalization and efficiency. We propose State of Thought (SoT), a new reasoning paradigm that enables endogenous reasoning in LLMs, with the model's internal reasoning state governing how reasoning unfolds. Concretely, SoT extracts a compact dynamics-geometric state from the model's internal information transfer and uses a 582-parameter controller on frozen backbones to selectively activate historical reasoning support useful under the current reasoning state, framing reasoning as a state-conditioned process over evidence rather than an externally prescribed token chain. Across quantitative (1.34x), general (1.62x), symbolic-and-code (1.76x), and long-context (2.51x) reasoning on 3 LLMs and 16 datasets, SoT consistently improves mean-baseline accuracy while reducing generated tokens by 62.6% and end-to-end latency by 44.6%. Across 2 VLM scales and 3 reasoning tasks, it improves mean accuracy by 3.8 points over reasoning baselines, with 74.9% fewer completion tokens and 73.5% lower latency than search-based methods. Under constrained access, SoT retains 38.2%/36.5% mean accuracy gains in training-free/embedding-only settings, while trajectory-only judging reaches 84.1% agreement across 3 API models. Together, endogenous state-driven reasoning provides a generalizable and efficient alternative.

## Metadata
- **Published**: 2026-09-13T05:55:03Z
- **Authors**: Zhiren Gong, Yikun Hou, Zihao Zeng, Ming Xiao, Chau Yuen, Wei Yang Bryan Lim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.16055v1)