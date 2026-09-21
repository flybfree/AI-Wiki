---
title: Verify, Don't Trust: Agentic Model Development for Video Discovery Retrieval at Scale
published: 2026-09-18T03:04:28Z
authors: Hao Fu, Baiting Zhu, Minglei Chen, Yinjie Huang, Shuai Ding
url: http://arxiv.org/abs/2609.21257v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Verify, Don't Trust: Agentic Model Development for Video Discovery Retrieval at Scale

## Abstract
Large language model (LLM) agents can propose, implement, and evaluate model changes. Autoresearch loops demonstrate this capability through minutes-scale iterations on a self-contained program. Online autoresearch instead spans asynchronous systems, hours-long variants, and weeks-long campaigns that can influence a product. A completed run can still support an invalid conclusion when a code change is a no-op, data windows leak, evaluator semantics drift, or the two arms traverse different serving funnels. We present EvoPilot, a human-gated method for long-horizon online autoresearch. Role-specific agents execute each round through a versioned domain skill and typed adapter. Durable records preserve experiments and failures; deterministic checks enforce recorded lessons.   We study a 37-day campaign for the retrieval system that powers Video Deep Dive (VDD), an online experience for discovering follow-on videos after a user opens a seed video. The campaign covered seven directions and used an hourly refreshed index of hundreds of millions of videos. Earlier manual experiments had not established a benefit from an interaction head. A primitive autoresearch attempt revisited the direction but incorrectly attributed an offline hit-rate decline of 22 percentage points to the head. We then introduced EvoPilot. Its human-gated verification traced the drop to a pre-existing evaluation defect that produced output depths of 3,000 and 600. After repair, a matched comparison measured an offline improvement of 3.20 percentage points. Post-study replay and mutation tests rejected invalid comparisons while admitting valid counterparts. Durable state recovered an interrupted round, and artifact reuse avoided approximately five GPU-hours. Separately, a seven-day randomized online evaluation estimated a 0.66% relative increase in the VDD slice of Good Search Result Rate for Retention (GSRR).

## Metadata
- **Published**: 2026-09-18T03:04:28Z
- **Authors**: Hao Fu, Baiting Zhu, Minglei Chen, Yinjie Huang, Shuai Ding
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.21257v1)