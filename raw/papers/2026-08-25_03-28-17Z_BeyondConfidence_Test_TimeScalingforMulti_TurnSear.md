---
title: Beyond Confidence: Test-Time Scaling for Multi-Turn Search Agents via Retrieval Grounding
published: 2026-08-25T03:28:17Z
authors: Hyunho Kook, Junhyuk So, Tianyu Fu, Haizhong Zheng, Beidi Chen
url: http://arxiv.org/abs/2608.24024v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Beyond Confidence: Test-Time Scaling for Multi-Turn Search Agents via Retrieval Grounding

## Abstract
Confidence-based voting aggregates parallel LLM rollouts by weighting each with internal signals such as token log probabilities, and has been actively studied for single-turn reasoning. However, modern LLMs increasingly act as multi-turn search agents that retrieve and condition on external documents. In this paper, we show that confidence-based voting transfers poorly to this multi-turn setting, and identify the underlying failure reason as copy inflation: when retrieved documents are appended to an agent's context, tokens copied from those documents receive systematically inflated log probabilities. This flattens confidence scores within each question and weakens the resulting weighted vote. To address this issue, we propose Retrieval-Grounded Voting (RGV), which scores each rollout by the lexical overlap between its final answer and the documents it retrieved. By computing the signal outside the contaminated context, RGV sidesteps both token log probabilities and additional LLM calls. Across four search-agent benchmarks and five LLMs, RGV consistently outperforms confidence-based voting, with gains of up to +5.4% accuracy and +35% on minority-correct questions, where the correct answer appears in only 1-2 of 8 rollouts.

## Metadata
- **Published**: 2026-08-25T03:28:17Z
- **Authors**: Hyunho Kook, Junhyuk So, Tianyu Fu, Haizhong Zheng, Beidi Chen
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.24024v1)