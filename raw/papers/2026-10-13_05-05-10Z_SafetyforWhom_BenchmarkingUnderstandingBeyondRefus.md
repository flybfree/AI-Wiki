---
title: Safety for Whom? Benchmarking Understanding Beyond Refusal in Egocentric Multimodal Assistants
published: 2026-10-13T05:05:10Z
authors: Yewon Han, Jisu Jeon, Suhyun Choi, Juan Yeo, Minsoo Jo, Gihoon Kim, Hyunggyu Lim, Taesup Kim
url: http://arxiv.org/abs/2610.17728v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# Safety for Whom? Benchmarking Understanding Beyond Refusal in Egocentric Multimodal Assistants

## Abstract
Egocentric multimodal assistants see through the user's eyes and guide what the user does next, so their outputs directly shape physical actions, including those that affect bystanders. Yet existing safety evaluations do not distinguish whom a response would harm, and score only whether a model refuses. Pooling all harms into one refusal rate hides two failures: a model may protect one target but not another, and it may refuse without understanding the risk, or understand it and comply anyway. We present STOU, a benchmark of 2,902 egocentric video-audio and video-text queries whose potential harm targets the user (Self), co-present individuals (The Others), or society at large (Others). Our evaluation decouples safety understanding from refusal behavior: beyond refusal, we score whether the model recognizes the user's intent, the presence and target of harm, and its downstream consequences. Across 10 open and closed source omnimodal and multimodal LLMs, we find that refusal varies systematically with the harm target, and that models often recognize a harm yet still assist with it. These results show that refusal rates alone cannot certify an assistant as safe, and that safety alignment must account for who would be harmed. Project page: https://onedayoneyeah.github.io/safety-for-whom

## Metadata
- **Published**: 2026-10-13T05:05:10Z
- **Authors**: Yewon Han, Jisu Jeon, Suhyun Choi, Juan Yeo, Minsoo Jo, Gihoon Kim, Hyunggyu Lim, Taesup Kim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2610.17728v1)