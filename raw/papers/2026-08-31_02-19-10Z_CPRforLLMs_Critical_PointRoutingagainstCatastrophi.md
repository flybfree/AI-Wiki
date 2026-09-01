---
title: CPR for LLMs: Critical-Point Routing against Catastrophic Forgetting in Domain Adaptation
published: 2026-08-31T02:19:10Z
authors: Kwangmin Ki, Yunhun Nam, Jongheon Jeong, Jaehyung Kim
url: http://arxiv.org/abs/2608.30158v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# CPR for LLMs: Critical-Point Routing against Catastrophic Forgetting in Domain Adaptation

## Abstract
Supervised fine-tuning (SFT) is the de facto standard for adapting large language models (LLMs) to target domains, but it often degrades the model's general capabilities, a phenomenon known as catastrophic forgetting. Existing approaches typically modify the SFT loss to mitigate forgetting, but they inevitably operate along a domain-generality trade-off. In this work, we step outside this trade-off by decoupling the two capabilities at the model level: we keep the original base model for general capability, and selectively invoke the SFT expert only when domain-specific knowledge is required. Specifically, we propose CPR (Critical-Point Routing), a token-level routing framework between a base model and its expert derivative, based on critical tokens where the base model fails but the expert succeeds. We train a lightweight hierarchical router that estimates the expert-call probability per token, and pair it with a tailored inference procedure that combines momentum smoothing and threshold gating. Across diverse model-domain configurations, CPR achieves state-of-the-art across all settings, surpassing SFT expert by 1.4-5.5% in domain performance while recovering its general-capability drop from 3.4-14.5% to at most 0.5%, with minimal overhead from invoking the expert on only one-third of tokens.

## Metadata
- **Published**: 2026-08-31T02:19:10Z
- **Authors**: Kwangmin Ki, Yunhun Nam, Jongheon Jeong, Jaehyung Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30158v1)