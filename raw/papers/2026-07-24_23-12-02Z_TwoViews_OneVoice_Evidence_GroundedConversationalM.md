---
title: Two Views, One Voice: Evidence-Grounded Conversational Music Recommendation
published: 2026-07-24T23:12:02Z
authors: Sungwook Yoo, Sewook Yoo
url: http://arxiv.org/abs/2607.24846v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Two Views, One Voice: Evidence-Grounded Conversational Music Recommendation

## Abstract
Traditional conversational recommenders entangle retrieval and response generation within a single text interface, so exact entity cues fade as the dialogue's intent evolves, which compromises explanation credibility. We address this within the ACM RecSys Challenge 2026, which mandates both top-20 ranking and evidence-grounded response generation. This paper presents the third-place solution by team "swyoo" for the Blind-B industry track. We decouple retrieval and response into separate pipelines connected strictly via ranked tracks and metadata. Retrieval combines a hybrid lexical-dense pool for exact matching with a task-adapted pool driven by fine-tuned Qwen 8B adapters. Candidates are calibrated via LightGBM, then routed to an evidence-grounded propose-assign-select (PAS) framework to structure responses. This system also ranked second on the explanation-quality leaderboard in the final blind evaluation. Our findings demonstrate that: (i) isolating retrieval and response preserves both catalog cues and fluid intent; (ii) structuring generation via explicit evidence assignment is key to this near-best-in-class explanation reliability.

## Metadata
- **Published**: 2026-07-24T23:12:02Z
- **Authors**: Sungwook Yoo, Sewook Yoo
- **Source**: [ArXiv Link](http://arxiv.org/abs/2607.24846v1)