---
title: Harmful Responses Are Jailbreak Templates: Transferring Autoregressive Jailbreaks to Diffusion Language Models
published: 2026-10-22T14:20:36Z
authors: Jinwei Gan, Zifeng Cheng, Zhiwei Jiang, Ran Sun, Shiping Ge, Qing Gu
url: http://arxiv.org/abs/2610.31331v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Harmful Responses Are Jailbreak Templates: Transferring Autoregressive Jailbreaks to Diffusion Language Models

## Abstract
Diffusion large language models (dLLMs) enable flexible masked generation through bidirectional context modeling, but this capability also introduces a distinct jailbreak attack surface. We find that a harmful response to a given query naturally serves as an effective jailbreak template: simply masking a subset of its tokens can induce a dLLM to reconstruct harmful content. Based on this observation, we propose RMT-Jailbreak, a general framework that transfers existing autoregressive (AR) jailbreak attacks to dLLMs through their induced harmful responses. RMT-Jailbreak converts an AR-generated harmful response into a high-mask-ratio template using uniform token retention, and further applies prompt-based safety filtering to mask any remaining visible harmful content. The refined template is then provided to the target dLLM for bidirectional reconstruction. Extensive experiments across multiple AR jailbreak methods and target dLLMs demonstrate the effectiveness and generality of RMT-Jailbreak, revealing strong cross-paradigm transferability of jailbreak attacks.

## Metadata
- **Published**: 2026-10-22T14:20:36Z
- **Authors**: Jinwei Gan, Zifeng Cheng, Zhiwei Jiang, Ran Sun, Shiping Ge, Qing Gu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.31331v1)