---
title: Dissecting Sensitivity to Training Language in Self-Supervised Speech Learning Using Neural Audio Codec Tokens
published: 2026-07-28T23:46:37Z
authors: Daigo Takizawa, Tomohiko Nakamura, Samuele Cornell, William Chen, Satoru Fukayama, Shinji Watanabe
url: http://arxiv.org/abs/2607.26350v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Dissecting Sensitivity to Training Language in Self-Supervised Speech Learning Using Neural Audio Codec Tokens

## Abstract
Neural audio codecs (NACs) have become popular for obtaining speech representations as discrete tokens. Beyond compression, discrete tokens can be used to train self-supervised learning (SSL) models. Such models, referred to as codec-based SSL models, reduce data storage and computational cost, enabling scalable SSL pre-training. However, their language sensitivity remains unclear. When the language changes, codec-based SSL models may require retraining, which undermines their efficiency. In this paper, we present a systematic analysis of language sensitivity by varying either the NAC training language or the SSL pre-training language while keeping the other fixed. Experimental results show that downstream performance is insensitive to the NAC training language but strongly dependent on the SSL pre-training language. These findings suggest that a single NAC can be reused across languages, while aligning the SSL pre-training language with the target language is crucial.

## Metadata
- **Published**: 2026-07-28T23:46:37Z
- **Authors**: Daigo Takizawa, Tomohiko Nakamura, Samuele Cornell, William Chen, Satoru Fukayama, Shinji Watanabe
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.26350v1)