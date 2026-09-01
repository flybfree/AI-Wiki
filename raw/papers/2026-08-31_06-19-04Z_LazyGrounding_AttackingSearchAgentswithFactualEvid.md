---
title: Lazy Grounding: Attacking Search Agents with Factual Evidence
published: 2026-08-31T06:19:04Z
authors: Yulin Zhang, Yukun Huang, Sanxing Chen, Tianyi Lin, Ziang Yang, Xunjian Yin, Bhuwan Dhingra
url: http://arxiv.org/abs/2608.30303v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Lazy Grounding: Attacking Search Agents with Factual Evidence

## Abstract
Search agents reduce hallucination by grounding answers in retrieved web evidence. Yet reliance on retrieval also creates an attack surface: poisoned corpora with false or malicious documents can cause agents to reproduce misinformation. We show that falsehood is not necessary -- a search agent can be misled by factual evidence for a nearby question, adopting that nearby answer even when it does not answer the current question. We call this failure lazy grounding. We expose lazy grounding using nearby evidence from answer-changing rewrites of benchmark questions. Each document truthfully supports a neighboring rewritten question, but is surfaced for the original question. Across 12 model-benchmark pairs, nearby evidence reduces accuracy by 5.9 points on average and by up to 17.3 points, while inducing nearby-answer adoption in every setting. The effect is stronger when nearby evidence appears later or is more answer-shaped. Our results show that robust search agents must defend against not only misinformation but also the misapplication of factual evidence. The code is publicly available at https://github.com/frankyzha/lazy-grounding.

## Metadata
- **Published**: 2026-08-31T06:19:04Z
- **Authors**: Yulin Zhang, Yukun Huang, Sanxing Chen, Tianyi Lin, Ziang Yang, Xunjian Yin, Bhuwan Dhingra
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30303v1)