---
title: StageWell: A Process-Aligned Chinese Corpus for Positive-Psychology Support Dialogue
published: 2026-08-29T15:13:11Z
authors: Yuxiong Wang, Ziwei Lin, Bo Wang, Yu Zhang, Shiguang Ni
url: http://arxiv.org/abs/2608.29326v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# StageWell: A Process-Aligned Chinese Corpus for Positive-Psychology Support Dialogue

## Abstract
Positive psychology dialogue aims to support emotional distress and positive resource building, requiring models to produce not only empathetic replies but also coherent progression through a multi-turn support process. Existing resources often reduce supervision to turn-level strategies or holistic preference labels, leaving process position, support function, and local repair targets implicit. We introduce StageWell, a process-aligned Chinese corpus for positive psychology dialogue, together with HQS, a structured protocol for data construction and evaluation. StageWell organizes support into a six-stage support process and uses a multi-agent whole-dialogue rewriting workflow to construct 12,445 SFT instances, 1,849 DPO preference pairs, and a GroundTruth subset of 120 expert-revised dialogues and 977 QA pairs. Guided by HQS, DPO pairs are built as process-localized repairs: flawed model outputs are used as rejected responses, and targeted rewrites under the same context and stage constraint are used as chosen responses. Across four 9B-14B open-source LLMs, this supervision yields robust gains in process control, response quality, and safety. Averaged across models, BERTScore improves by 0.037, Q-Overall increases by 1.32 points, S-exact increases by 0.236, and the H-critical rate decreases by 0.167. These results highlight the value of modeling supportive dialogue as a structured multi-turn support process rather than as single-turn response generation.

## Metadata
- **Published**: 2026-08-29T15:13:11Z
- **Authors**: Yuxiong Wang, Ziwei Lin, Bo Wang, Yu Zhang, Shiguang Ni
- **Source**: [ArXiv Link](http://arxiv.org/abs/2608.29326v1)