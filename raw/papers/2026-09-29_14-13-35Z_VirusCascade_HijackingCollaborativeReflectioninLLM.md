---
title: VirusCascade: Hijacking Collaborative Reflection in LLM-Powered Recommender Agents
published: 2026-09-29T14:13:35Z
authors: Yurong Hao, Wen Zhou, Guowei Guan, Tiantong Wu, Fuyao Zhang, Wei Yang Bryan Lim
url: http://arxiv.org/abs/2609.38270v1
type: paper-summary
tags: [paper-summary, arxiv]
---

# VirusCascade: Hijacking Collaborative Reflection in LLM-Powered Recommender Agents

## Abstract
Advancing beyond traditional static scoring models, LLM-powered agentic recommender systems (LLM-ARS) instantiate users and items as autonomous agents, whose semantic states are dynamically refined through a recurrent process known as collaborative reflection. While this mechanism improves recommendation quality, it simultaneously introduces a systemic vulnerability: adversarial evidence injected into a single agent can be rationalised into a legitimate preference narrative, written back into memory, and propagated to other agents through interaction contexts. We term the local rationalisation process reflection laundering, and its system-wide escalation through collaborative reflection collaborative-reflection hijacking. Existing attacks on recommender systems, whether based on interaction-level data poisoning or text-level adversarial perturbations, assume static pipelines and thus cannot exploit this recurrent, multi-agent amplification pathway. To bridge this gap, we first conduct a controlled vulnerability analysis that establishes two exploitable properties underlying collaborative-reflection hijacking: reflective persistence and cross-agent propagation. Then building on these findings, we propose VirusCascade, the first black-box targeted promotion attack that jointly shapes semantic and structural attack surfaces: the former ensures the target item is naturally rationalised as satisfying broad user preferences, the latter positions it for system-wide propagation. Extensive experiments on four real-world datasets across diverse LLM-ARS architectures demonstrate that VirusCascade consistently achieves state-of-the-art targeted exposure under evaluated stealth constraints, reaching a mean E@20 of 0.384 and surpassing the strongest baseline by an absolute margin of +0.185.

## Metadata
- **Published**: 2026-09-29T14:13:35Z
- **Authors**: Yurong Hao, Wen Zhou, Guowei Guan, Tiantong Wu, Fuyao Zhang, Wei Yang Bryan Lim
- **Source**: [ArXiv Link](http://arxiv.org/abs/2609.38270v1)