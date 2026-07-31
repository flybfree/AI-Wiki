---
title: Building a User Foundation Model for the Open Web
published: 2026-07-30T11:07:54Z
authors: Solal Vernier, Ivan Can Arisoy, Merwan Barlier, Blaž Škrlj
url: http://arxiv.org/abs/2607.28019v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Building a User Foundation Model for the Open Web

## Abstract
User foundation models have demonstrated strong results in e-commerce and social recommendation, but most industrial deployments assume environments where user identity is stable and persistent. Open-web real-time bidding (RTB) operates on a structurally different data distribution: user identity is fragmented and non-persistent across browsing sessions, and the availability of browsing history depends on user privacy choices. Consequently, a significant portion of traffic carries no historical data, and available records often consist of relatively short, disjointed sessions. As a result, historical signals in this domain are typically represented as aggregated counters and recency buckets, leaving the sequential structure unexploited. To address this limitation, we present a user foundation model that applies self-supervised learning on user browsing histories and show that the learned representation improves multiple downstream production tasks, demonstrating the viability of this approach on the open web. We pre-train a Transformer encoder with masked language modeling and a sequence-level contrastive objective, then fine-tune it on the click prediction task. We optimize the encoder's pre-training pipeline with an LLM-in-the-loop search over a curated catalog of reviewable, code-level edits (lifters), instantiating the LLM-as-optimizer paradigm in an industrial setting. The same encoder representation yields +1.197% RIG on the production bid win-rate model and +1.354% RIG on the production CTR ranker; a 7-day live A/B test confirms +2.13% CTR, -1.13% eCPC (80% CI excluding zero on both metrics).

## Metadata
- **Published**: 2026-07-30T11:07:54Z
- **Authors**: Solal Vernier, Ivan Can Arisoy, Merwan Barlier, Blaž Škrlj
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.28019v1)