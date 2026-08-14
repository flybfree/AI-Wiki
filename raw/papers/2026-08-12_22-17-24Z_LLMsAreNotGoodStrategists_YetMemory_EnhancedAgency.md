---
title: LLMs Are Not Good Strategists, Yet Memory-Enhanced Agency Boosts Reasoning
published: 2026-08-12T22:17:24Z
authors: Yi Wu, Zhimin Hu
url: http://arxiv.org/abs/2608.12626v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# LLMs Are Not Good Strategists, Yet Memory-Enhanced Agency Boosts Reasoning

## Abstract
Strategic reasoning in Large Language Models (LLMs) within long-horizon environments is often limited by inconsistent subgoals. In these settings, finite attention resources prevent the model from maintaining strategic coherence over thousands of steps. This limitation leads to strategic drift, where localized decisions fail to sustain a coherent trajectory across reasoning. To address this, we introduce EpicStar, a framework that enables agents to learn memory as policy to tackle long-horizon reasoning. Specifically, the agent maintains a bank of successful past episodes as a heuristic alongside a working memory to track short-term environmental changes. During inference, a dynamic gating mechanism determines whether to execute a retrieved action directly or to perform new reasoning through a contextual fusion of the retrieved episodes and current working memory. Utilizing StarCraft II as the testbed, we evaluated EpicStar against diverse opponent styles. It significantly outperforms baseline methods, achieving higher win rates while consuming an order of magnitude fewer tokens, and it maintains this advantage consistently across difficulty levels and opponent strategies. Our findings provide compelling evidence that structured cross-episode memory is essential for enabling LLM agents to perform robust, long-term strategic execution in dynamic, autonomous settings.

## Metadata
- **Published**: 2026-08-12T22:17:24Z
- **Authors**: Yi Wu, Zhimin Hu
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.12626v1)