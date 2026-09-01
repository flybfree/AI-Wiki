---
title: WebWorld: The Browser as a World Model for Self-Improving Web Code
published: 2026-08-31T10:00:12Z
authors: Jiajun Wu, Jian Yang, Yaxin Du, Wei Zhang, Haowen Wang, Junhang Cheng, Yuxuan Zhang, Tuney Zheng, Xianglong Liu, Ming Zhou
url: http://arxiv.org/abs/2608.30530v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# WebWorld: The Browser as a World Model for Self-Improving Web Code

## Abstract
VLM-driven self-improvement of web code has a structural flaw: the model that proposes the repair is the model that judges it, and visual plausibility under that judge is a poor proxy for whether the page actually works. What the loop is missing is a counterparty the VLM cannot fool, and the browser already is that counterparty: a deterministic, executable simulator of how an HTML artifact behaves under user actions, and in everything but name a world model for web code. We present WebWorld, the interface that lets a VLM prior interact with this browser-as-world-model autonomously and decides which interactions become supervision. Each round, the VLM emits a critique that the planner compiles into a typed interaction contract; the browser re-executes the candidate and issues an acceptance certificate only when both target progress and preservation of every previously verified capability hold; certified transitions accumulate as a quality ratchet that is the only thing the SFT export ever sees. Under matched training, WebWorld-27B improves Raw-27B by 5.3 points on HTMLBench-400 and 14.9 points on MiniAppBench-Val, and reaches the level of strong frontier systems such as Kimi-K2.6 and GPT-5.4 on interactive HTML generation. Equal-size ablations show that browser-backed admission carries the gain: without the certificate, the matched 9B lift nearly disappears.

## Metadata
- **Published**: 2026-08-31T10:00:12Z
- **Authors**: Jiajun Wu, Jian Yang, Yaxin Du, Wei Zhang, Haowen Wang, Junhang Cheng, Yuxuan Zhang, Tuney Zheng, Xianglong Liu, Ming Zhou
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.30530v1)