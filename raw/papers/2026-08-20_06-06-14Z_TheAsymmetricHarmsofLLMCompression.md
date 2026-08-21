---
title: The Asymmetric Harms of LLM Compression
published: 2026-08-20T06:06:14Z
authors: Yuan Wu, Mairui Li, Lesia Semenova, Chudi Zhong
url: http://arxiv.org/abs/2608.19670v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# The Asymmetric Harms of LLM Compression

## Abstract
Large language models (LLMs) compression reduces deployment costs, but standard aggregate metrics like perplexity and accuracy often mask underlying behavioral shifts. In this work, we systematically evaluate 3 LLMs across 11 compression methods to investigate the effects of compression on knowledge retention, model confidence, and social bias. We find that compression disproportionately reduces the relative retention of head knowledge compared to tail knowledge. Furthermore, compressed models often remain substantially confident in their incorrect answers on newly lost knowledge. Finally, we demonstrate that stable aggregate bias scores can conceal substantial, opposing shifts in stereotypical preferences across demographic subgroups. Together, these findings reveal asymmetric behavioral changes that aggregate performance measures fail to capture, highlighting the need for granular evaluation of compressed models before deployment.

## Metadata
- **Published**: 2026-08-20T06:06:14Z
- **Authors**: Yuan Wu, Mairui Li, Lesia Semenova, Chudi Zhong
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.19670v1)